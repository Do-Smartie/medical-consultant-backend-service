from flask import Blueprint
from flask import request
from db_connector import DbConnector
import pymongo


auth = Blueprint('user_auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    register_data = request.json
    k = DbConnector()
    k.insert_data(collection_name='my_collection', request_data=register_data)
    # todo: Store the data in mongoDB after validation.
    return "Added successfully"

@auth.route('/login', methods=['POST'])
def login():
    login_data = request.data
    # todo: Validate from db and create a session using a salted string and maintain them in the mongoDb


    
    
    