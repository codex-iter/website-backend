from flask import Flask, make_response, request, Response, jsonify
from flask_cors import CORS
from controller import membersDatabase, auth

app = Flask(__name__)
# TODO: setup cors with proper resources matching frontend
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'webserver is working fine'

#Event routes
@app.route('/api/getEvents', methods=['GET'])
def getEvent():
    return ''

@app.route('/api/addEvent', methods=['POST'])
def addEvent():
    return ''

@app.route('/api/delEvent', methods=['POST'])
def delEvent():
    return ''

#contact-us routes
@app.route('/api/getMessage', methods=['GET'])
def getMessage():
    return ''

@app.route('/api/addMessage', methods=['POST'])
def addMessage():
    return ''

@app.route('/api/delMessage', methods=['POST'])
def delMessage():
    return ''

#member details routes
@app.route('/api/getAlumni', methods=['GET'])
def getAlumni():
    return jsonify(membersDatabase.getAlumni())

@app.route('/api/getMember', methods=['GET'])
def getMember():
    return jsonify(membersDatabase.getMembers())

@app.route('/api/addMember', methods=['POST'])
def addMember():
    if auth.checkLogin():
        if membersDatabase.addMembers(request.json):
            return Response(status=200)
        else:
            return Response(status=400)

    return Response(status=401)

@app.route('/api/delMember', methods=['POST'])
def delMember():
    if auth.checkLogin():
        if membersDatabase.delMember(request.json):
            return Response(status=200)
        else:
            return Response(status=400)

    return Response(status=401)

if __name__ == '__main__':
    app.run(debug=True)


