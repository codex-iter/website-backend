from flask import Flask, render_template, request, Response, jsonify, make_response, redirect
from flask_cors import CORS
from controller import membersDatabase, messagesDatabase, eventsDatabase, auth

app = Flask(__name__, static_folder='static')
# TODO: setup cors with proper resources matching frontend
CORS(app)

#Event routes
@app.route('/api/getEvents', methods=['GET'])
def getEvent():
    return jsonify(eventsDatabase.getAllEvents())

@app.route('/api/addEvent', methods=['POST'])
def addEvent():
    if auth.checkLogin(request.cookies.get('token')):
        files=request.files.getlist('images')
        file_urls, file_names=eventsDatabase.file_handler(files)

        if eventsDatabase.uploadEvent(request.form, file_urls, file_names):
            return Response(status=200)
        else:
            return Response(status=400)
    
    return Response(status=401)

@app.route('/api/delEvent', methods=['POST'])
def delEvent():
    if auth.checkLogin(request.cookies.get('token')):
        if eventsDatabase.deleteEvent(request.json):
            return Response(status=200)
        else:
            return Response(status=400)

    return Response(status=401)

#contact-us routes
@app.route('/api/getMessage', methods=['GET'])
def getMessage():
    if auth.checkLogin(request.cookies.get('token')):
        return jsonify(messagesDatabase.getAllMessage())

    return Response(status=401)

@app.route('/api/addMessage', methods=['POST'])
def addMessage():
    if messagesDatabase.addMessage(request.json):
        return Response(status=200)

    return Response(status=400)

@app.route('/api/delMessage', methods=['POST'])
def delMessage():
    if auth.checkLogin(request.cookies.get('token')):
        if messagesDatabase.deleteMessage(request.json):
            return Response(status=200)

        else:
            return Response(status=400)

    return Response(status=401)

#login route
@app.route('/api/login', methods=['POST'])
def backend_login():
    data = auth.login_email(request.form)
    if data is None:
        return Response(status=400)
    return jsonify(data)

@app.route('/api/loginCookie', methods=['POST'])
def backend_login_cookie():
    data = auth.login_email(request.json)
    if data is None:
        return Response(status=400)
    
    if data['success']:
        res = make_response('login successful')
        res.set_cookie('token', data['token'])
        return res

    return Response(status=401)

#member details routes
@app.route('/api/getAlumni', methods=['GET'])
def getAlumni():
    return jsonify(membersDatabase.getAlumni())

@app.route('/api/getMember', methods=['GET'])
def getMember():
    return jsonify(membersDatabase.getMembers())

@app.route('/api/addMember', methods=['POST'])
def addMember():
    if auth.checkLogin(request.cookies.get('token')):
        if membersDatabase.addMembers(request.json):
            return Response(status=200)
        else:
            return Response(status=400)

    return Response(status=401)

@app.route('/api/delMember', methods=['POST'])
def delMember():
    if auth.checkLogin(request.cookies.get('token')):
        if membersDatabase.delMember(request.json):
            return Response(status=200)
        else:
            return Response(status=400)

    return Response(status=401)

#user login apis
@app.route('/api/checkUser', methods=['POST'])
def checkUser():
    return ''

@app.route('/api/addUser', methods=['POST'])
def addUser():
    return ''

@app.route('/api/delUser', methods=['POST'])
def delUser():
    return ''


# login routes with ui
@app.route('/')
def login_ui():
    return render_template('login.html')

@app.route('/members')
def members_ui():
    if auth.checkLogin(request.cookies.get('token')):
        return render_template('members.html')
    else:
        res = make_response(redirect('/'))
        res.set_cookie('token', '', expires=0)
        return res

@app.route('/events')
def events_ui():
    if auth.checkLogin(request.cookies.get('token')):
        return render_template('events.html')
    else:
        res = make_response(redirect('/'))
        res.set_cookie('token', '', expires=0)
        return res

@app.route('/contact')
def contact_ui():
    if auth.checkLogin(request.cookies.get('token')):
        return render_template('contactus.html')
    else:
        res = make_response(redirect('/'))
        res.set_cookie('token', '', expires=0)
        return res


if __name__ == '__main__':
    app.run(debug=True)


