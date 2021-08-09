from pymongo import MongoClient
from os import environ

client = MongoClient(environ['DB_URI'])

db=client['codex_website']

def addRecord(tableName, data):
    table = db[tableName]
    return table.insert_one(data)

def searchRecord(tableName, q):
    curr = db[tableName].find(q)
    arr=[]

    for tmp in curr:
        tmp['_id']=str(tmp['_id'])
        arr.append(tmp)
    
    return arr

def deleteRecord(tableName, q):
    return db[tableName].delete_one(q)