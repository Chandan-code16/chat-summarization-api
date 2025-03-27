# 🚀 Chat Summarization API

![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-blue?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge)

A high-performance **Chat Summarization API** built with **FastAPI**, **MongoDB**, and **OpenAI GPT-4**. 🚀 This API enables chat storage, retrieval, and summarization for real-time conversations.

## 🌟 Features

✅ **Store & Retrieve Chats** (MongoDB Atlas)

✅ **Summarize Conversations** using OpenAI GPT-4

✅ **Asynchronous & Optimized Queries** for Performance

✅ **Dockerized for Seamless Deployment**

✅ **Deployed on Railway.app**

## 📂 Project Structure
```
chat_summarization_api/
│-- app/
│   ├── main.py             # Main FastAPI application
│   ├── models.py           # Pydantic models
│   ├── database.py         # MongoDB connection
│   ├── services.py         # Business logic
│-- .env                    # Environment variables
│-- requirements.txt        # Dependencies
│-- Dockerfile              # Docker container setup
│-- README.md               # Documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/Chandan-code16/chat-summarization-api.git
 cd chat-summarization-api
```

### 2️⃣ Create and Activate Virtual Environment
```sh
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```
MONGO_URI=your_mongodb_connection_string
OPENAI_API_KEY=your_openai_api_key
```

### 5️⃣ Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```
Access API docs at 👉 **http://127.0.0.1:8000/docs**

---

## 🛠 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/chats` | Store a chat message |
| `GET` | `/chats/{conversation_id}` | Retrieve a conversation |
| `POST` | `/chats/summarize` | Summarize a chat conversation |
| `DELETE` | `/chats/{conversation_id}` | Delete a conversation |

---

## 🐳 Docker Setup

### 1️⃣ Build the Docker Image
```sh
docker build -t chat-api .
```

### 2️⃣ Run the Container
```sh
docker run -d -p 8000:8000 --name chat_container chat-api
```

### 3️⃣ Access the API Docs
Visit **http://localhost:8000/docs** 📜

### 4️⃣ Stop & Remove Container
```sh
docker stop chat_container
docker rm chat_container
```

---

## 🚀 Deployment on Railway.app

### 1️⃣ Install Railway CLI
```sh
npm install -g @railway/cli
```

### 2️⃣ Login & Connect Project
```sh
railway login
railway init
```

### 3️⃣ Deploy the App
```sh
railway up
```

---

## 📝 License

This project is **MIT licensed**. Feel free to use and improve! 😊

💙 **Star the repo if you like it!** ⭐
