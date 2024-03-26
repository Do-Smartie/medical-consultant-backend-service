from flask import Flask
import chatbot
app = Flask(__name__)
app.register_blueprint(chatbot.chatbot)

@app.route('/')
def index():
    return "This is example"


