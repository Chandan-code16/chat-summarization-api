# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" /> Chat Summarization API

![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-blue?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge)

![Render](https://img.shields.io/badge/Deployed%20on-Render-blue)

A high-performance **Chat Summarization API** built with **FastAPI**, **MongoDB**, and **OpenAI GPT-4**. 🚀 This API enables chat storage, retrieval, and summarization for real-time conversations.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Globe%20with%20Meridians.png" alt="Globe with Meridians" width="25" height="25" /> Live API
- **Base URL:** [Chat Summarization API](https://chat-summarization-api.onrender.com)
- **Swagger UI (API Docs):** [Swagger Docs](https://chat-summarization-api.onrender.com/docs)
- **Redoc:** [Redoc Docs](https://chat-summarization-api.onrender.com/redoc)

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" /> Features

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check Mark Button" width="25" height="25" /> **Store & Retrieve Chats** (MongoDB Atlas)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check Mark Button" width="25" height="25" /> **Summarize Conversations** using OpenAI GPT-4

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check Mark Button" width="25" height="25" /> **Asynchronous & Optimized Queries** for Performance

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check Mark Button" width="25" height="25" /> **Dockerized for Seamless Deployment**

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check Mark Button" width="25" height="25" /> **Deployed on Render**

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Open%20File%20Folder.png" alt="Open File Folder" width="25" height="25" /> Project Structure
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

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Wrench.png" alt="Wrench" width="25" height="25" /> Installation & Setup

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20One.png" alt="Keycap Digit One" width="25" height="25" /> Clone the Repository
```sh
 git clone https://github.com/Chandan-code16/chat-summarization-api.git
 cd chat-summarization-api
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Two.png" alt="Keycap Digit Two" width="25" height="25" /> Create and Activate Virtual Environment
```sh
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Three.png" alt="Keycap Digit Three" width="25" height="25" /> Install Dependencies
```sh
pip install -r requirements.txt
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Four.png" alt="Keycap Digit Four" width="25" height="25" /> Configure Environment Variables
Create a `.env` file in the root directory:
```
MONGO_URI=your_mongodb_connection_string
OPENAI_API_KEY=your_openai_api_key
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Five.png" alt="Keycap Digit Five" width="25" height="25" /> Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```
Access API docs at <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Right%20Medium-Light%20Skin%20Tone.png" alt="Backhand Index Pointing Right Medium-Light Skin Tone" width="25" height="25" /> **http://127.0.0.1:8000/docs**

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" alt="Hammer and Wrench" width="25" height="25" /> API Endpoints

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" alt="Pushpin" width="25" height="25" /> Store a Chat Message
**POST** `/chats`
```json
{
  "user_id": "user123",
  "message": "Hello, how are you?"
}
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" alt="Pushpin" width="25" height="25" /> Get a Chat Message
**GET** `/chats/{conversation_id}`

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" alt="Pushpin" width="25" height="25" /> Summarize Chat
**POST** `/chats/summarize`
```json
{
  "user_id": "user123"
}
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" alt="Pushpin" width="25" height="25" /> Delete a Chat Message
**DELETE** `/chats/{conversation_id}`

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/chats` | Store a chat message |
| `GET` | `/chats/{conversation_id}` | Retrieve a conversation |
| `POST` | `/chats/summarize` | Summarize a chat conversation |
| `DELETE` | `/chats/{conversation_id}` | Delete a conversation |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Spouting%20Whale.png" alt="Spouting Whale" width="25" height="25" /> Docker Setup

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20One.png" alt="Keycap Digit One" width="25" height="25" /> Build the Docker Image
```sh
docker build -t chat-api .
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Two.png" alt="Keycap Digit Two" width="25" height="25" /> Run the Container
```sh
docker run -d -p 8000:8000 --name chat_container chat-api
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Three.png" alt="Keycap Digit Three" width="25" height="25" /> Access the API Docs
Visit **http://localhost:8000/docs** 📜

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Keycap%20Digit%20Four.png" alt="Keycap Digit Four" width="25" height="25" /> Stop & Remove Container
```sh
docker stop chat_container
docker rm chat_container
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" /> Deployment on Render
1. Push code to GitHub.
2. Create a new service on **Render.com**.
3. Select "FastAPI" and connect your GitHub repository.
4. Set environment variables (`MONGO_URI`, `OPENAI_API_KEY`).
5. Deploy the service and use the provided URL!

---
## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People%20with%20professions/Man%20Technologist%20Light%20Skin%20Tone.png" alt="Man Technologist Light Skin Tone" width="25" height="25" /> Project Owner <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Hamsa.png" alt="Hamsa" width="25" height="25" />
### **Chandan Mishra**  
<a href="https://www.linkedin.com/in/chandan-mishra-b2110a247" target="blank">
<img src=https://ziadoua.github.io/m3-Markdown-Badges/badges/LinkedIn/linkedin2.svg /></a>

<a href="https://github.com/Chandan-code16" target="blank">
<img src=https://ziadoua.github.io/m3-Markdown-Badges/badges/Github/github3.svg /></a>

<a href="mailto:er.chandanmishra03@gmail.com" target="blank">
<img src=https://ziadoua.github.io/m3-Markdown-Badges/badges/Gmail/gmail1.svg /></a>


## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" alt="Memo" width="25" height="25" /> License

This project is **MIT licensed**. Feel free to use and improve! <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face.png" alt="Smiling Face" width="25" height="25" />

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Blue%20Heart.png" alt="Blue Heart" width="25" height="25" /> **Star the repo if you like it!** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Star.png" alt="Star" width="25" height="25" />
