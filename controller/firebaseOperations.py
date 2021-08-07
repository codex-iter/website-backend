import pyrebase
from creds.config import firebaseConfig, firebaseConfigAuth

storage = pyrebase.initialize_app(firebaseConfig).storage()
storageAuth = pyrebase.initialize_app(firebaseConfigAuth).storage()

'''
uploads the file onto firebase storage service
@param fileName: path of file to be uploaded relative to app.py in the home directory of the project
@param uploadName: name/path with which the file needs to be uploaded on the firebase storage
@return the static hotlinkable download link to file
'''


def upload(fileName, uploadName):
    global storage
    uploadInfo = storage.child(uploadName).put(fileName)

    encodedUploadName = uploadName.replace('/', '%2F')
    return f"https://firebasestorage.googleapis.com/v0/b/{uploadInfo['bucket']}/o/{encodedUploadName}?alt=media&token={uploadInfo['downloadTokens']}"


'''
deletes the file from firebase storage
@param cloudFileName: path of file which needs to be delete in the firebase storage
'''


def delete(cloudFileName):
    global storageAuth

    storageAuth.delete(cloudFileName)


def getFileList():
    global storageAuth
    return storageAuth.list_files()
