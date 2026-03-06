from flask import Flask, render_template, Response, request, redirect, url_for, session
from proctor import generate_frames
from questions import questions

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session

# Temporary storage (replace with DB later)
users = {}

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

    return render_template("dashboard.html")


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

    for i, q in enumerate(questions):
        selected = request.form.get(f"q{i}")
        if selected:
            if selected == q["answer"]:
                score += 4
            else:
                score -= 1

    return render_template("result.html", score=score, total=len(questions)*4)


# ---------------- CAMERA ----------------
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)