from pymongo import MongoClient
from flask import jsonify

class DbConnector:
    _instance = None
    
    def create_collection(self, name):
        self.mydb.create_collection(name=name)

    def insert_data(self, collection_name, request_data):
        collection = self.mydb.get_collection(collection_name)
        collection.insert_one(request_data)

    def update_record(self, collection_name, filter_query, request_data):
        collection = self.mydb.get_collection(collection_name)
    # Filter query and update data
        update_statement = {'$set': request_data.get('data')}
    # Update the document
        collection.update_one(filter_query, update_statement)

    def delete_record(self,collection_name,request_data):
        collection = self.mydb.get_collection(collection_name)
        collection.delete_one(filter=request_data)
    
    def get_records(self,collection_name,query):
        collection= self.mydb.get_collection(collection_name)
        records = collection.find(query)
        return list(records)

    # def get_record(self,collection_name,param):
    #     query = {'username': param} # Replace 'field' and 'value' with your query parameters}
    #     collection = self.mydb.get_collection(collection_name)
    #     data = collection.find_one(query)
    #     return jsonify(data)
    #     # print(collection.find_one(query))
    #     # return jsonify(collection.find_one(query))

    # def get_records(self, collection_name, query_params=None):
    # # Get the MongoDB collection
    #      collection = self.mydb.get_collection(collection_name)
    
    # # Perform the query using the query parameters
    # # If query_params is not provided, find all records in the collection
    #      if query_params is None:
    #         records = collection.find()
    #      else:
    #         records = collection.find(query_params)
    #      records_list = []
    #      for record in records:
    #     # Convert `ObjectId` fields to strings
    #          for key, value in record.items():
    #             if isinstance(value, ObjectId):
    #                 record[key] = str(value)
    #          records_list.append(record)

    #      return records_list
    # # Convert the records to a list of dictionaries
    #     #  records_list = list(records)
    #     #  return records_list

        
    @classmethod
    def get_instance(cls):
        # Create a single instance of DbConnector if it doesn't already exist
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    

    def __init__(self):
        atlas_connection_uri ="mongodb+srv://doctorconsultant:l1WCjZWSQxxku56j@cluster0.dtruqtx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(atlas_connection_uri)
        self.mydb = client["doctor_consultant"]


