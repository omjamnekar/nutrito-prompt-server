import os
import time
import uuid
import google.generativeai as genai
from src.util.session_store import sessions, session_timestamps

# Init Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

MODEL = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.4,
        "top_p": 0.2,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
)

def start_chat_session():
    session_id = str(uuid.uuid4())
    chat_session = MODEL.start_chat(history=[])
    sessions[session_id] = chat_session
    session_timestamps[session_id] = time.time()
    return session_id

def send_user_message(session_id, message):
    if session_id not in sessions:
        return {"error": "Session expired or not found"}

    chat = sessions[session_id]
    session_timestamps[session_id] = time.time()
    try:
        response = chat.send_message(message)
        return response.text
    except Exception as e:
        return {"error": str(e)}

def end_chat_session(session_id):
    if session_id in sessions:
        del sessions[session_id]
        del session_timestamps[session_id]
        return {"message": "Session ended"}
    return {"error": "Session not found"}
