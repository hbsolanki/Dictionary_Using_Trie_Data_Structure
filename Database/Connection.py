import pymongo

if __name__=="__main__":
    print("Connect To DB")
    client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    print(client)
    db=client["Dictionary"]
    collection=db["word"]
    
