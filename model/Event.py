from controller.mongodbOperations import addRecord, searchRecord, deleteRecord

class Event:
    def __init__(self, title, description, organizers, images, imagesNames):
        self.title=title
        self.description=description
        self.organizers=organizers
        self.images=images
        self.imagesNames=imagesNames
        
    def insert(self):
        data ={
            'title': self.title,
            'description': self.description,
            'organizers': self.organizers,
            'images': self.images,
            'imagesNames': self.imagesNames
        }

        return addRecord('event', data)

    def query(q={}):
        return searchRecord('event', q)

    def delete(q):
        return deleteRecord('event', q)