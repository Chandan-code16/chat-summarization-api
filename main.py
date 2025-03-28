import os
import uvicorn
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import openai
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API Keys
if not MONGO_URI or not OPENAI_API_KEY:
    raise RuntimeError("MONGO_URI and OPENAI_API_KEY must be set in .env file")

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGO_URI)
db = client["chat_database"]
collection = db["chats"]

# Ensure MongoDB connection closes on shutdown
@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

# Pydantic model
class ChatMessage(BaseModel):
    user_id: str
    message: str

@app.post("/chats")
async def store_chat(chat: ChatMessage):
    """Stores a chat message in MongoDB."""
    chat_data = {"user_id": chat.user_id, "message": chat.message}
    result = await collection.insert_one(chat_data)
    return {"message": "Chat stored", "chat_id": str(result.inserted_id)}

@app.get("/chats/{conversation_id}")
async def get_chat(conversation_id: str):
    """Retrieves a chat message from MongoDB."""
    try:
        chat = await collection.find_one({"_id": ObjectId(conversation_id)})
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")
        chat["_id"] = str(chat["_id"])
        return chat
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid conversation ID")

# Request model for summarization
class ChatSummaryRequest(BaseModel):
    user_id: str

@app.post("/chats/summarize")
async def summarize_chat(request: ChatSummaryRequest):
    """Summarizes a chat using OpenAI's API."""
    chat_messages_cursor = collection.find({"user_id": request.user_id}, {"_id": 0, "message": 1})

    messages = [chat["message"] async for chat in chat_messages_cursor]

    if not messages:
        raise HTTPException(status_code=404, detail="No chat messages found for this conversation")

    prompt = "Summarize this conversation:\n" + "\n".join(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response["choices"][0]["message"]["content"]
        return {"user_id": request.user_id, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/chats/{conversation_id}")
async def delete_chat(conversation_id: str):
    """Deletes a chat conversation."""
    try:
        result = await collection.delete_one({"_id": ObjectId(conversation_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Chat not found")
        return {"message": "Chat deleted successfully"}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid conversation ID")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
