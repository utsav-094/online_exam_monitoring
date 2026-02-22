# Phase 5 - Flask Compatible Proctor Engine (Stabilized Version)

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

# -----------------------------
# Create Evidence Folder
# -----------------------------
if not os.path.exists("evidence"):
    os.makedirs("evidence")

# -----------------------------
# Save Evidence Function
# -----------------------------
def save_evidence(frame, reason):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"evidence/{reason}_{timestamp}.jpg"
    cv2.imwrite(filename, frame)

    with open("log.txt", "a") as file:
        file.write(f"{timestamp} - {reason}\n")


# -----------------------------
# Flask Streaming Function
# -----------------------------
def generate_frames():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    warning_count = 0
    last_warning_time = 0
    no_face_start_time = None
    multi_face_start_time = None
    exam_start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # ✅ Flip frame for natural left-right movement
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # ✅ Improved face detection (more stable)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=7,
            minSize=(120, 120)
        )

        current_time = time.time()

        # -------------------------
        # 1️⃣ No Face Detection
        # -------------------------
        if len(faces) == 0:
            if no_face_start_time is None:
                no_face_start_time = current_time

            if current_time - no_face_start_time > NO_FACE_THRESHOLD:
                if current_time - last_warning_time > WARNING_COOLDOWN:
                    warning_count += 1
                    save_evidence(frame, "No_Face")
                    last_warning_time = current_time
                no_face_start_time = None
        else:
            no_face_start_time = None

        # -------------------------
        # 2️⃣ Multiple Face Detection
        # -------------------------
        if len(faces) > 1:
            cv2.putText(frame, "Multiple Faces Detected!",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 0, 255),
                        2)

            if multi_face_start_time is None:
                multi_face_start_time = current_time

            if current_time - multi_face_start_time > MULTI_FACE_THRESHOLD:
                if current_time - last_warning_time > WARNING_COOLDOWN:
                    warning_count += 1
                    save_evidence(frame, "Multiple_Faces")
                    last_warning_time = current_time
                multi_face_start_time = None
        else:
            multi_face_start_time = None

        # -------------------------
        # 3️⃣ Face Position Check (Balanced)
        # -------------------------
        if len(faces) == 1:
            (x, y, w, h) = faces[0]

            cv2.rectangle(frame,
                          (x, y),
                          (x + w, y + h),
                          (0, 255, 0),
                          2)

            frame_center_x = frame.shape[1] // 2
            face_center_x = x + w // 2

            difference = face_center_x - frame_center_x

            # ✅ Increased tolerance (natural sitting allowed)
            if difference > 100:
                cv2.putText(frame,
                            "Looking Right!",
                            (50, 90),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2)

            elif difference < -100:
                cv2.putText(frame,
                            "Looking Left!",
                            (50, 90),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2)

        # -------------------------
        # 4️⃣ Exam Timer
        # -------------------------
        elapsed_exam = current_time - exam_start_time
        remaining = int(EXAM_DURATION - elapsed_exam)

        cv2.putText(frame,
                    f"Time Left: {max(0, remaining)}s",
                    (400, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 0, 0),
                    2)

        if remaining <= 0:
            break

        # -------------------------
        # 5️⃣ Warning Display
        # -------------------------
        cv2.putText(frame,
                    f"Warnings: {warning_count}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2)

        # -------------------------
        # Encode frame for browser
        # -------------------------
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()