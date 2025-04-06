from dotenv import load_dotenv
load_dotenv()  # Ensure this is before anything else is imported

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.qa_engine import ask_question

import os
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("question", "")
    if not query:
        return jsonify({"error": "Question is required"}), 400

    result = ask_question(query)
    return jsonify({
        "answer": result["result"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
