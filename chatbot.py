from flask import Blueprint
from flask import request
import pymongo

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chatbot',  methods=['POST'])
def promptInput():
    return request.json 
