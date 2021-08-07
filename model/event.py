import os
import datetime

try:
    from flask import jsonify
    from constants import EventMongoDB
    import controller.firebaseOperations as firebase
    from pymongo import MongoClient
    from creds.config import mongodbConfigs  # TODO: Comment this, after adding env variables
except ImportError:
    print("Fulfil requirements....")


def valid_extension() -> list:
    return [".png", ".jpg", ".jpeg", ".webp"]


def select_images(images_path: list) -> list:
    images_uri = []
    for path in images_path:
        image_name, extension = os.path.splitext(os.path.basename(path))  # for getting file name and extension
        print(image_name, extension)
        if extension in valid_extension():
            uri = firebase.upload(path, image_name)
            images_uri.append(uri)
    return images_uri


class Event:
    def __init__(self):

        """
        TODO: Things to be changed, after changing mongodb account :
        1. cluster = MongoClient(f"mongodb+srv://{os.environ['username']}:{os.environ['password']}@iamsimp.twewe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        2. You can change "database name" and "collection name" from "model/constants.py".
        """

        self.cluster = MongoClient(
            f"mongodb+srv://{mongodbConfigs['username']}:{mongodbConfigs['password']}@iamsimp.twewe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.cluster[EventMongoDB.db_name.value]
        self.collection = self.db[EventMongoDB.collection.value]

    def set_event(self, title: str, description: str, date: str, organizers: list, images_path: list):
        # checking already a record present or not, of same title
        document = self.collection.find_one({
            "title": title
        })
        if document is None:
            images_uri = []
            if len(images_path) != 0:
                try:
                    images_uri = select_images(images_path)
                except FileNotFoundError:
                    print("Not valid image path")

                record = {                  # random '_id' will generated
                    'title': title,
                    'description': description,
                    'images': images_uri,
                    'date': date,
                    'organizers': organizers
                }
                self.collection.insert_one(record)
                return {"status": "0", "comment": "success"}
        else:
            return {"status": "1", "comment": "record already exists of same title"}

    def get_all_events(self):
        docs = []
        cursors = self.collection.find({})
        for doc in cursors:
            docs.append(doc)
        return docs


# Testing

cats = ['../testingAssets/cat 1.jpeg']
ev = Event()
_title = "Event ross"
_des = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum hendrerit consectetur. Aliquam tincidunt nisi in metus sodales cursus. Etiam sed dui feugiat, volutpat mauris sit amet, auctor nulla. Vivamus iaculis metus lobortis tortor viverra, sed venenatis metus sodales. Proin bibendum auctor aliquam. Integer blandit dolor lectus, ut aliquet diam sagittis eu. Donec sodales, justo nec sollicitudin pharetra, sem eros finibus sapien, in sollicitudin urna neque id arcu. Phasellus malesuada lectus felis, at dictum neque feugiat eu. Duis ut aliquam nibh, a porttitor justo. "
_images = cats
_date = str(datetime.datetime.now().date())
_organizers = ["joey", "chandler", "rachel", "ross"]
print(ev.set_event(_title, _des, _date, _organizers, _images))
# print(ev.get_all_events())