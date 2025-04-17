from flask import Blueprint, request, jsonify
from src.gen.chat_service import start_chat_session, send_user_message, end_chat_session

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/start_session", methods=["POST"])
def start_session():
    session_id = start_chat_session()
    return jsonify({"session_id": session_id})

@chat_bp.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    session_id = data.get("session_id")
    message = data.get("message")

    response = send_user_message(session_id, message)
    if isinstance(response, dict) and response.get("error"):
        return jsonify(response), 404

    return jsonify({"response": response})

@chat_bp.route("/end_session", methods=["POST"])
def end_session():
    data = request.get_json()
    session_id = data.get("session_id")
    result = end_chat_session(session_id)
    return jsonify(result)
