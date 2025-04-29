from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from validate_query import run_user_query

# Init
app = Flask(__name__)
CORS(app)

# Configure SQLite DB path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'problems.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    schema = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    hint = db.Column(db.Text, nullable=True)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/problems", methods=["GET"])
def get_problems():
    problems = Problem.query.all()
    return jsonify([{
        "id": p.id,
        "title": p.title,
        "prompt": p.prompt,
        "schema": p.schema,
        "solution": p.solution,
        "hint": p.hint
    } for p in problems])

@app.route("/problems/random")
def get_random_problem():
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, prompt, schema, solution, hint FROM problems ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({
            "title": row[0],
            "prompt": row[1],
            "schema": row[2],
            "solution": row[3],
            "hint": row[4]
        })
    else:
        return jsonify({"error": "No problems found"}), 404

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    user_query = data.get("query", "")
    result = run_user_query(user_query)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
