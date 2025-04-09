from flask import Blueprint, request, render_template, jsonify
from models.model import Chat
from services.service import call_openai,call_mixtral


chat_bp = Blueprint('chat',__name__)

@chat_bp.route("/")
def index():
    return render_template("index.html")

@chat_bp.route("/chat", methods=["POST"])
def chat(chat=Chat):
    data = request.get_json()
    input_validation = chat(**data)

    if input_validation.prompt == "openai":
        result = call_openai(input_validation.prompt)
    elif input_validation.model == "mixtral":
        result = call_mixtral(input_validation.prompt)
    else:
        result = "Invalid model selected."

    return jsonify({"response": result})