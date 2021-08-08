from controller.mongodbOperations import addRecord, searchRecord, deleteRecord
import datetime

class Message:
    def __init__(self, name, email, message):
        self.name=name
        self.email=email
        self.message=message
        self.time=datetime.datetime.now()
        
    def insert(self):
        data ={
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'time': self.time
        }

        return addRecord('message', data)

    def query(q={}):
        return searchRecord('message', q)

    def delete(q):
        deleteRecord('message', q)