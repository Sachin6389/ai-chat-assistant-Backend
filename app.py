import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# Create Flask App
app = Flask(__name__)
CORS(app)

# Store chat history (temporary, in memory)
chat_history = [
    {
        "role": "system",
        "content": "You are a helpful AI Assistant."
    }
]


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "AI Chat Assistant API Running 🚀"
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:

        # Save user message
        chat_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Send to Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_history,
            temperature=0.7,
            max_tokens=1024,
        )

        ai_reply = response.choices[0].message.content

        # Save assistant response
        chat_history.append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

        return jsonify({
            "success": True,
            "reply": ai_reply
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():
    return jsonify(chat_history)


@app.route("/clear", methods=["DELETE"])
def clear():

    global chat_history

    chat_history = [
        {
            "role": "system",
            "content": "You are a helpful AI Assistant."
        }
    ]

    return jsonify({
        "message": "Chat history cleared."
    })


if __name__ == "__main__":
    app.run(debug=True)