from flask import Blueprint
from flask import request
import userauth
from model_processor import MedicalModel

chatbot = Blueprint('chatbot', __name__)



@chatbot.route('/chatbot',  methods=['POST'])
def promptInput():
    argument = request.args
    if userauth.verify_string(argument.get("email"), argument.get("salt"), argument.get("hash_string")):
        model = MedicalModel(dict(request.json).get("message"))
        return model.give_tips()
    else:
        return {"error":"Invalid User"}


