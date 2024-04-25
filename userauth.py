from flask import Blueprint,jsonify
from flask import request
from db_connector import DbConnector
import hashlib
import secrets


auth = Blueprint('user_auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    register_data = request.json
    k = DbConnector.get_instance()
    k.insert_data(collection_name='dc_userpool', request_data=register_data)
    # todo: Store the data in mongoDB after validation.
    return "Added successfully"

def generate_salt():
    return secrets.token_hex(16)

def hash_string(string, salt):
    salted_string = string.encode() + salt.encode()
    hashed_string = hashlib.sha256(salted_string).hexdigest()
    return hashed_string

def store_salted_string(email, k):
    salt = generate_salt()
    hashed_string = hash_string(email, salt)
    try:
        if k.get_records('session', {"email" : email}) is not None:
            k.update_record('session',  {"email":email}, {'email': email, 'salt': salt, 'hashed_string': hashed_string})
    except:
        k.insert_data('session', {'email': email, 'salt': salt, 'hashed_string': hashed_string})
    
    return {
        'email': email,
        'salt': salt,
        'hashed_string': hashed_string
    }

def verify_string(email, salt, hashed_string):
    if hash_string(email, salt) == hashed_string:
        return True
    else:
        return False

@auth.route('/login', methods=['POST'])
def login():
    login_data = request.json
    k = DbConnector.get_instance()
    data = k.get_records('dc_userpool', {"email" : login_data.get("email")})
    if (data is not None):
        return store_salted_string(email=login_data.get('email'),k=k)
    else:
        return {"error":"Invalid User"}

@auth.route('/update',methods=['POST'])
def update():
    update_ref = request.json
    filter_query = {"username":update_ref.get('username')}
    k = DbConnector.get_instance()
    k.update_record(collection_name='dc_userpool',filter_query=filter_query,request_data=update_ref)
    return "Updated successfully"

@auth.route('/delete',methods=['DELETE'])
def delete():
    print(request.json)
    delete_data=request.json
    k=DbConnector.get_instance()
    k.delete_record(collection_name='dc_userpool',request_data=delete_data)
    return "Deleted Successfully"


@auth.route('/get_records',methods=['GET'])
def get_records():
    query_params = request.args
    pass