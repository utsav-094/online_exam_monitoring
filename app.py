from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
from proctor import generate_frames, get_warning_count, increment_warning
from questions import questions

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session

# Temporary storage (replace with DB later)
users = {}
exam_results = {}  # stores last score + warnings per user

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route('/register', methods=["POST"])
def register():
    role = request.form["role"]
    fullname = request.form["fullname"]
    email = request.form["email"]
    userid = request.form["userid"]
    password = request.form["password"]

    if userid in users:
        return "User already exists!"

    users[userid] = {
        "role": role,
        "fullname": fullname,
        "email": email,
        "password": password
    }

    return redirect(url_for("home"))


# ---------------- LOGIN ----------------
@app.route('/login', methods=["POST"])
def login():
    role = request.form["role"]
    userid = request.form["userid"]
    password = request.form["password"]

    user = users.get(userid)

    if user and user["password"] == password and user["role"] == role:
        session["user"] = userid
        session["role"] = role
        return redirect(url_for("dashboard"))
    else:
        return "Invalid Credentials"


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))

    userid = session["user"]
    fullname = users[userid]["fullname"]
    result = exam_results.get(userid, None)

    return render_template("dashboard.html", fullname=fullname, result=result)


# ---------------- EXAM ----------------
@app.route('/exam')
def exam():
    if "user" not in session:
        return redirect(url_for("home"))

    return render_template("exam.html", questions=questions)


# ---------------- SUBMIT EXAM ----------------
@app.route('/submit', methods=["POST"])
def submit():
    if "user" not in session:
        return redirect(url_for("home"))

    score = 0
    total_questions = 0

    for subject, subject_questions in questions.items():
        for i, q in enumerate(subject_questions):
            selected = request.form.get(f"{subject}_{i}")
            total_questions += 1
            if selected:
                if selected == q["answer"]:
                    score += 4
                else:
                    score -= 1

    # Save result for dashboard
    exam_results[session["user"]] = {
        "score": score,
        "total": total_questions * 4,
        "warnings": get_warning_count()
    }

    return render_template("result.html", score=score, total=total_questions * 4)


# ---------------- TAB SWITCH ----------------
@app.route('/tab_switch', methods=["POST"])
def tab_switch():
    from proctor import increment_warning
    increment_warning("Tab_Switch")
    return jsonify({"status": "ok"})


# ---------------- WARNING STATUS ----------------
@app.route('/warning_status')
def warning_status():
    return jsonify({"warning_count": get_warning_count()})


# ---------------- CAMERA ----------------
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)