import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = client["Deempal"]
mycol = mydb["Record"]
result = mycol.delete_many({'name':'Prajakta'})
print(result.deleted_count,"row Deleted")