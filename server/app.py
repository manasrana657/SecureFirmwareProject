from flask import Flask, request, jsonify
from models import db, Firmware
import os
from datetime import datetime

app = Flask(__name__)

def log_event(event):
    with open("audit.log", "a") as f:
        f.write(f"{datetime.now()} - {event}\n")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///firmware.db"
app.config["UPLOAD_FOLDER"] = "uploads"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Secure Firmware Update Server Running"

@app.route("/upload", methods=["POST"])
def upload():

    version = request.form.get("version")
    file = request.files["firmware"]

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(path)

    firmware = Firmware(
        version=version,
        filename=file.filename
    )

    db.session.add(firmware)
    db.session.commit()

    log_event(f"Firmware Uploaded Version {version}")

    return jsonify({
        "status": "uploaded",
        "version": version
    })

if __name__ == "__main__":
    app.run(debug=True)
