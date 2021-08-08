from model.Message import Message
from bson import ObjectId

def addMessage(data):
    if 'name' and 'email' and 'message' not in data:
        return False

    m = Message(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )

    m.insert()
    return True

def getAllMessage():
    return Message.query()

def deleteMessage(data):
    if 'id' not in data:
        return False

    Message.delete({
        '_id': ObjectId(data['id'])
    })
    return True