from pymongo import MongoClient
from os import environ

client = MongoClient(environ['DB_URI'])

db=client['codex_website']

def addRecord(tableName, data):
    table = db[tableName]
    return table.insert_one(data)