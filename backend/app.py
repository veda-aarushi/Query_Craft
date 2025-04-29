# backend/app.py
from flask import Flask, request, jsonify
from validate_query import run_user_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin for frontend

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    user_query = data.get("query", "")
    result = run_user_query(user_query)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
