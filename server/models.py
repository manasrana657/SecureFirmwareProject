from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Firmware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(20), unique=True)
    filename = db.Column(db.String(200))
