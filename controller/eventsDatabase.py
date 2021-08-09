from model.Event import Event
from controller import firebaseOperations
import hashlib
from bson import ObjectId

def file_handler(files):
    file_url_arr=[]
    filename_arr=[]
    for file in files:
        tmp_filename='temp'
        file.save(tmp_filename)

        upload_filename=hash_file(tmp_filename)+'.'+str(file.filename).split('.')[-1]

        file_url_arr.append(firebaseOperations.upload(tmp_filename, upload_filename))
        filename_arr.append(upload_filename)

    return file_url_arr, filename_arr

def uploadEvent(data, file_urls, file_names):
    if 'title' and 'description' and 'organizers' in data:
        e = Event(
            title=data['title'],
            description=data['description'],
            organizers=str(data['organizers']).split(';'),
            images=file_urls,
            imagesNames=file_names
        )

        e.insert()
        return True

    return False

def hash_file(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

    return str(h.hexdigest())

def getAllEvents():
    return Event.query()

def deleteEvent(data):
    if 'id' in data:
        qry={
            '_id': ObjectId(data['id'])
        }
        rec=Event.query(qry)[0]

        for f_name in rec['imagesNames']:
            firebaseOperations.delete(f_name)

        Event.delete(qry)
        
        return True
    return False