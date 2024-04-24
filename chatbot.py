from flask import Blueprint
from flask import request
from model_processor import MedicalModel

chatbot = Blueprint('chatbot', __name__)



@chatbot.route('/chatbot',  methods=['POST'])
def promptInput():
    model = MedicalModel(dict(request.json).get("message"))
    return model.give_tips()


