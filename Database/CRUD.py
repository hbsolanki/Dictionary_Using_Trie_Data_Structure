import pymongo

print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["Dictionary"]
collection=db["word"]

def insertInDB(word):
    collection.insert_one({'key':word})

def getWordFromDB():
    return collection.find()
