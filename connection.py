# # # # from pymongo.mongo_client import MongoClient
# # # # # Replace the placeholder with your Atlas connection string
# # # # uri ="mongodb+srv://harinikesh1020:QwertyuioP@cluster0.owzcw25.mongodb.net/"
# # # # # uri = "mongodb+srv://harinikesh1020:QwertyuioP@cluster0.owzcw25.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# # # # # Create a new client and connect to the server
# # # # client = MongoClient(uri)
# # # # # Send a ping to confirm a successful connection
# # # # try:
# # # #     client.admin.command('ping')
# # # #     print("Pinged your deployment. You successfully connected to MongoDB!")
# # # # except Exception as e:
# # # #     print(e)


from pymongo import MongoClient

# Replace this connection string with your MongoDB Atlas connection string
atlas_connection_uri ="mongodb+srv://indhuma1220:c3jdN4OhcG8RpEYS@cluster0.hhjdngr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish connection to MongoDB Atlas
client = MongoClient(atlas_connection_uri)

# Access/Create database
mydb = client["my_database"] 
print("connected")
#  # Replace "mydatabase" with your desired database name

# # # (Optional) Create collection
# # mycollection = mydb["my_collection"]  # Replace "mycollection" with your desired collection name

# # # (Optional) Insert a document into the collection
data = {"name": "india", "age": 72, "city": "newyork nagaram","address":"nhdcaoin"}
mydb.my_collection.insert_one(data)

print("Database and collection created successfully!")

# # from pymongo import MongoClient

# # # Replace this connection string with your MongoDB Atlas connection string
# # atlas_connection_uri ="mongodb+srv://harinikesh1020:QwertyuioP@cluster0.owzcw25.mongodb.net/"

# # # Establish connection to MongoDB Atlas
# # client = MongoClient(atlas_connection_uri)
# # db = client["mydatabase"]
# # collection = db["mycollection"]

# # db.collection.update({},{set :{name :"FirstName"}},{multi:true})
# # # }, { $set: { existingField: "new value" } }, { multi: true }

# # mydb.my_collection.update_one({"name": "John"}, {"$set": {"age": 90}})

# # mydb.my_collection.update_many({"name": "John"},{"$set": {"city","name":"Magizh"}})
# # print("Update done")

# # print("First print")
# # demo = mydb.my_collection.find()

# # # Iterate over the cursor to access each document
# # for document in demo:
# #     print(document)

# # # data = [{"name": "John", "age": 30, "city": "New York","address":"awsedrftgw"},{"name":"king","age":45,"city":"USA","address":"gemebmob"}]
# # # mydb.my_collection.insert_many(data)
# # # print("Created many data , successfully")

# # mydb.my_collection.delete_one({"name": "abd"})
# # print("Document deleted successfully!")

# # print("Second print")
# # demo = mydb.my_collection.find()

# # # Iterate over the cursor to access each document
# # for document in demo:
# #     print(document)

# print("First print")
# demo = mydb.my_collection.find()

# # Iterate over the cursor to access each document
# for document in demo:
#     print(document)

# # data = [{"name": "John", "age": 30, "city": "New York","address":"awsedrftgw"},{"name":"king","age":45,"city":"USA","address":"gemebmob"}]
# # mydb.my_collection.insert_many(data)
# # print("Created many data , successfully")

# mydb.my_collection.delete_one({"name": "Deck"})
# print("Document deleted successfully!")

# print("Second print")
# demo = mydb.my_collection.find()

# # Iterate over the cursor to access each document
# for document in demo:
#     print(document)