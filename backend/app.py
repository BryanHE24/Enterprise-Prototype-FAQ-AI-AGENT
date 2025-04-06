from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable cross-origin requests
from backend.qa_engine import ask_question  # Import question answering function

import os
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # Debug: Ensure API key is loaded

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (different origin)

@app.route("/ask", methods=["POST"])
def ask():
    # Get JSON payload
    data = request.json
    query = data.get("question", "")
    
    # Validate input
    if not query:
        return jsonify({"error": "Question is required"}), 400

    # Process question through QA chain
    result = ask_question(query)
    
    # Return answer to frontend
    return jsonify({
        "answer": result["result"]
    })

if __name__ == "__main__":
    # Run app locally
    app.run(host="0.0.0.0", port=5000)
