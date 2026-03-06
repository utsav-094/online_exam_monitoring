# Phase 5 - Flask Compatible Proctor Engine (Production Ready)

import cv2
import time
import os
from datetime import datetime


# -----------------------------
# Configuration
# -----------------------------
MAX_WARNINGS = 5
WARNING_COOLDOWN = 5
NO_FACE_THRESHOLD = 2.5
MULTI_FACE_THRESHOLD = 2
EXAM_DURATION = 120  # seconds
FRAME_DELAY = 0.02   # reduces CPU usage


# -----------------------------
# Paths Setup
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EVIDENCE_FOLDER = os.path.join(BASE_DIR, "evidence")
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

os.makedirs(EVIDENCE_FOLDER, exist_ok=True)


# -----------------------------
# Save Evidence
# -----------------------------
def save_evidence(frame, reason):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(EVIDENCE_FOLDER, f"{reason}_{timestamp}.jpg")

        cv2.imwrite(filename, frame)

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {reason}\n")

    except Exception as e:
        print("Evidence save error:", e)


# -----------------------------
# Camera Initialization
# -----------------------------
def initialize_camera():
    # Windows stability
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Fallback if CAP_DSHOW fails
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Webcam could not be accessed.")

    return cap


# -----------------------------
# Load Haar Cascade Safely
# -----------------------------
def load_face_detector():
    try:
        haar_path = cv2.data.haarcascades
    except AttributeError:
        haar_path = os.path.join(
            os.path.dirname(cv2.__file__),
            "data",
            "haarcascades"
        )

    cascade_file = os.path.join(
        haar_path,
        "haarcascade_frontalface_default.xml"
    )

    if not os.path.exists(cascade_file):
        raise RuntimeError("Haarcascade file not found.")

    detector = cv2.CascadeClassifier(cascade_file)

    if detector.empty():
        raise RuntimeError("Failed to load Haarcascade classifier.")

    return detector


# -----------------------------
# Flask Streaming Generator
# -----------------------------
def generate_frames():

    cap = initialize_camera()
    face_cascade = load_face_detector()

    warning_count = 0
    last_warning_time = 0
    no_face_start = None
    multi_face_start = None
    exam_start = time.time()

    try:
        while True:

            success, frame = cap.read()
            if not success:
                print("Frame capture failed.")
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=7,
                minSize=(120, 120)
            )

            current_time = time.time()

            # -------------------------
            # No Face Detection
            # -------------------------
            if len(faces) == 0:
                if no_face_start is None:
                    no_face_start = current_time
                elif current_time - no_face_start > NO_FACE_THRESHOLD:
                    if current_time - last_warning_time > WARNING_COOLDOWN:
                        if warning_count < MAX_WARNINGS:
                            warning_count += 1
                            save_evidence(frame, "No_Face")
                        last_warning_time = current_time
                    no_face_start = None
            else:
                no_face_start = None

            # -------------------------
            # Multiple Face Detection
            # -------------------------
            if len(faces) > 1:
                cv2.putText(frame, "Multiple Faces Detected!",
                            (40, 60),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,
                            (0, 0, 255),
                            2)

                if multi_face_start is None:
                    multi_face_start = current_time
                elif current_time - multi_face_start > MULTI_FACE_THRESHOLD:
                    if current_time - last_warning_time > WARNING_COOLDOWN:
                        if warning_count < MAX_WARNINGS:
                            warning_count += 1
                            save_evidence(frame, "Multiple_Faces")
                        last_warning_time = current_time
                    multi_face_start = None
            else:
                multi_face_start = None

            # -------------------------
            # Face Drawing + Position Check
            # -------------------------
            if len(faces) == 1:
                (x, y, w, h) = faces[0]

                cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (0, 255, 0),
                              2)

                frame_center = frame.shape[1] // 2
                face_center = x + w // 2
                offset = face_center - frame_center

                if offset > 100:
                    cv2.putText(frame, "Looking Right",
                                (40, 100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 0, 255),
                                2)
                elif offset < -100:
                    cv2.putText(frame, "Looking Left",
                                (40, 100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 0, 255),
                                2)

            # -------------------------
            # Timer
            # -------------------------
            elapsed = current_time - exam_start
            remaining = int(EXAM_DURATION - elapsed)

            cv2.putText(frame,
                        f"Time Left: {max(0, remaining)}s",
                        (350, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 0, 0),
                        2)

            cv2.putText(frame,
                        f"Warnings: {warning_count}/{MAX_WARNINGS}",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2)

            if remaining <= 0:
                cv2.putText(frame,
                            "Exam Completed",
                            (200, 220),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            3)
                break

            if warning_count >= MAX_WARNINGS:
                cv2.putText(frame,
                            "Exam Terminated!",
                            (180, 220),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            3)
                break

            # -------------------------
            # Encode for Streaming
            # -------------------------
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   frame_bytes +
                   b'\r\n')

            time.sleep(FRAME_DELAY)

    except Exception as e:
        print("Streaming error:", e)

    finally:
        cap.release()
        cv2.destroyAllWindows()