from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json["image"]

    img_data = base64.b64decode(data.split(",")[1])
    np_img = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    return jsonify({"faces": len(faces)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
