# 🤖 AI Chat Assistant Backend

A Flask-based AI Chat Assistant backend powered by the **Groq API** and the **Llama 3.3 70B Versatile** language model. This application provides REST APIs for chatting with an AI assistant, viewing chat history, and clearing previous conversations. It is designed to be used with a React frontend or any client capable of making HTTP requests.

---

# 📌 Project Description

The AI Chat Assistant Backend is a RESTful API built using **Flask** that connects to the **Groq LLM API** to generate intelligent responses. It stores conversation history in memory, allowing the AI to respond based on previous messages during the application's runtime.

This project demonstrates:

* REST API development using Flask
* Integration with the Groq LLM API
* Environment variable management using python-dotenv
* Cross-Origin Resource Sharing (CORS)
* Basic conversation memory
* JSON-based communication between frontend and backend

---

# ✨ Features

* 🤖 AI-powered chatbot using Groq API
* 💬 Maintains conversation history
* 📜 Retrieve chat history
* 🗑️ Clear chat history
* 🌐 RESTful API endpoints
* 🔒 Secure API key management using `.env`
* ⚡ Fast responses powered by Groq
* 🔗 Ready for React or other frontend frameworks

---

# 🛠 Technologies Used

### Backend

* Python 
* Flask
* Flask-CORS
* python-dotenv
* Groq Python SDK

### AI Model

* Llama-3.3-70B-Versatile

### Development Tools

* VS Code
* Git
* GitHub

---

# 📁 Project Structure

```text
ai-chat-assistant-backend/
│
├── app.py                 # Main Flask application
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore
└── venv/                  # Virtual environment 
```

---

# ⚙ Installation Instructions

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-chat-assistant-backend.git
```

## 2. Navigate into the project

```bash
cd ai-chat-assistant-backend
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Instructions

## Step 1: Create a `.env` file

```env
GROQ_API_KEY=""
```

## Step 2: Run the application

```bash
python app.py
```

The Flask server starts at

```
http://127.0.0.1:5000
```

---

# 🚀 Usage Guide

## Home Endpoint

### GET /

Returns API status.

Example Response

```json
{
  "status": "success",
  "message": "AI Chat Assistant API Running 🚀"
}
```

---

## Chat Endpoint

### POST /chat

Request

```json
{
  "message": "Hello"
}
```

Response

```json
{
  "success": true,
  "reply": "Hello! How can I assist you today?"
}
```

---

## Chat History

### GET /history

Returns the current conversation history.

Example

```json
[
  {
    "role": "system",
    "content": "You are a helpful AI Assistant."
  },
  {
    "role": "user",
    "content": "Hello"
  },
  {
    "role": "assistant",
    "content": "Hi! How can I help you?"
  }
]
```

---

## Clear History

### DELETE /clear

Response

```json
{
  "message": "Chat history cleared."
}
```

---

# 📡 API Endpoints

| Method | Endpoint   | Description           |
| ------ | ---------- | --------------------- |
| GET    | `/`        | API Status            |
| POST   | `/chat`    | Send a message to AI  |
| GET    | `/history` | Retrieve chat history |
| DELETE | `/clear`   | Clear chat history    |

---

# 🧪 Example Outputs

### User

```text
Explain Artificial Intelligence.
```

### AI

```text
Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think, learn, reason, and solve problems.
```

---






