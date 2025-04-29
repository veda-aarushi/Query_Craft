# backend/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    schema = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    hint = db.Column(db.Text, nullable=True)
