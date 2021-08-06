class event:
    def __init__(self, db):
        self.collection=db.event


    def insert(self, title, description, images, date):
        record = {
            'title': title,
            'description': description,
            'images': images,
            'date': date
        }

        self.collection.insert_one(record)
