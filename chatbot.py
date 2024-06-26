from flask import Blueprint
from flask import request
import userauth
from model_processor import MedicalModel

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chatbot',  methods=['POST'])
def promptInput():
    argument = request.headers
    if userauth.validate_from_database(argument.get("email"), argument.get("salt"), argument.get("hash_string")):
        model = MedicalModel(dict(request.json).get("message"))
        return model.give_tips()
    else:
        return {"error":"Invalid User"}


