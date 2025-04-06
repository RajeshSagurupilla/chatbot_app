from flask import Flask, request, jsonify, render_template
import openai
import requests
from configuration import config

app = Flask(__name__)

# Set your API keys here
OPENAI_API_KEY = config.OPENAI_API_KEY
MIXTRAL_API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mixtral-8x7B-Instruct-v0.1/v1/chat/completions"
MIXTRAL_API_KEY = config.MIXTRAL_API_KEY

openai.api_key = OPENAI_API_KEY

def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def call_mixtral(prompt):
    headers = {
        "Authorization": f"Bearer {MIXTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(MIXTRAL_API_URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt")
    model = data.get("model")

    if model == "openai":
        result = call_openai(prompt)
    elif model == "mixtral":
        result = call_mixtral(prompt)
    else:
        result = "Invalid model selected."

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)