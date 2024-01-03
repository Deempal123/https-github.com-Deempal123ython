#create database
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['zibacar']
print("Database is created !!")

#connection
myclient = MongoClient("mongodb://localhost:27017/")

#database
db = myclient["zibacar"]

#table
collection = db["Student"]
record = { "_id": 5,
		"name": "Raju",
		"Roll No": "1005",
		"Branch": "CSE"}

rec_id1 = collection.insert_one(record)