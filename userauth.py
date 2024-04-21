from flask import Blueprint,jsonify
from flask import request
from db_connector import DbConnector
import pymongo


auth = Blueprint('user_auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    register_data = request.json
    k = DbConnector.get_instance()
    k.insert_data(collection_name='my_collection', request_data=register_data)
    # todo: Store the data in mongoDB after validation.
    return "Added successfully"

@auth.route('/login', methods=['POST'])
def login():
    login_data = request.data
    # todo: Validate from db and create a session using a salted string and maintain them in the mongoDb

@auth.route('/update',methods=['POST'])
def update():
    update_ref = request.json
    filter_query = {"username":update_ref.get('username')}
    k = DbConnector.get_instance()
    k.update_record(collection_name='my_collection',filter_query=filter_query,request_data=update_ref)
    # todo: Store the data in mongoDB after validation.
    return "Updated successfully"

@auth.route('/delete',methods=['DELETE'])
def delete():
    print(request.json)
    delete_data=request.json
    k=DbConnector.get_instance()
    k.delete_record(collection_name='my_collection',request_data=delete_data)
    return "Deleted Successfully"


@auth.route('/get_records',methods=['GET'])
def get_records():
    query_params = request.args
    


# @auth.route('/get-user',methods=['GET'])
# def get_user():
#     k=DbConnector.get_instance()
#     return k.get_record(collection_name='my_collection',param=request.args.get('username'))
    

# @auth.route('/get-records', methods=['GET'])
# def get_records():
#     # Get query parameters from the request
#     query_param = request.json
#     # print(param)
#     # Get an instance of DbConnector
#     k = DbConnector.get_instance()

#     # Retrieve records from the MongoDB collection based on the query parameters
#     # This function should return a list of records in JSON format
#     records = k.get_records(collection_name='my_collection', query_params=query_param)
    
#     # Return the records as JSON response
#     return jsonify(records), 200

