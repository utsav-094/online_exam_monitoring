from flask import Flask, render_template, Response
from proctor import generate_frames

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/exam')
def exam():
    return render_template("exam.html")

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)