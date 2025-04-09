from flask import Flask
import openai
from configuration import config
from controllers.controller import chat_bp
from configuration.config import OPENAI_API_KEY

app = Flask(__name__)


openai.api_key = OPENAI_API_KEY

app.register_blueprint(chat_bp)



if __name__ == "__main__":
    app.run(debug=True)