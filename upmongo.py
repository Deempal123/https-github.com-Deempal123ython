import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = client["Deempal"]
mycol = mydb["Record"]
result = mycol.replace_one({'name':"Mantasha"},{'name':"Prajakta",'age':"22",'class':"MBA"})
print(result.matched_count,"row Updated")
