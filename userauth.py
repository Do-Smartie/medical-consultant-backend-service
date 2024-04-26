from flask import Blueprint,jsonify
from flask import request
from db_connector import DbConnector
import hashlib
import secrets
import traceback



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


def store_salted_string(email, k):
    salt = generate_salt()
    try:
        if len(k.get_records('session', {"email" : email} )) > 0:
            print("Update called")
            k.delete_record('session', {"email":email})
            k.insert_data('session', {'email': email, 'salt': salt})
        else:
            print("Insert called")
            k.insert_data('session', {'email': email, 'salt': salt})
    except:
        traceback.print_exc()
        print("Insert called")
        k.insert_data('session', {'email': email, 'salt': salt})
    return {
        'email': email,
        'salt': salt
    }

def validate_from_database(email, salt, hash_string):
    k = DbConnector.get_instance()
    data = k.get_records('session', {'email' : email})
    try:
        if(data[0].get('email') == str(email) and data[0].get('salt') == salt):
            print(email)
            return True
        else:
            return False
    except:
        return False

@auth.route('/login', methods=['POST'])
def login():
    login_data = request.json
    k = DbConnector.get_instance()
    print("email" + str(login_data.get("email")))
    data = k.get_records('dc_userpool', {"email" : login_data.get("email")})
    print(data)
    if (len(data)>0 and (data[0]["password"] == login_data.get("password"))):
        return store_salted_string(email=login_data.get('email'),k=k)
    else:
        print("Invalid User")
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

@auth.route('/logout', methods=['GET'])
def logout():
    email = request.headers.get('email')
    k = DbConnector.get_instance()
    k.delete_record(collection_name='session', request_data= {"email": email})
    return {
        "result":"Session cleared",
        "success":True
    }


@auth.route('/get_records',methods=['GET'])
def get_records():
    query_params = request.args
    pass