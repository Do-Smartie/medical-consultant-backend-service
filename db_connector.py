from pymongo import MongoClient
class DbConnector:
    def create_collection(self, name):
        self.mydb.create_collection(name=name)

    def insert_data(self, collection_name, request_data):
        collection = self.mydb.get_collection(collection_name)
        collection.insert_one(request_data)

    def __init__(self):
        atlas_connection_uri ="mongodb+srv://harinikesh1020:QwertyuioP@cluster0.owzcw25.mongodb.net/"
        client = MongoClient(atlas_connection_uri)
        self.mydb = client["my_database"]
