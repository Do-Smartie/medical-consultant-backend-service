from flask import Flask
import chatbot
import userauth
app = Flask(__name__)
app.register_blueprint(chatbot.chatbot)
app.register_blueprint(userauth.auth)

@app.route('/')
def index():
    return "This is example"


