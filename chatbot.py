from flask import Blueprint

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/prompt')
def promptInput():
    return "Starting prompting"