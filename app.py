from flask import Flask, make_response, request
from model.event import Event
from flask_cors import CORS

app = Flask(__name__)
# TODO: setup cors with proper resources matching frontend
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'webserver is working fine'

@app.route('/api/getEvents', methods=['GET', 'OPTIONS'])
def getEvent():
    if request.method == 'GET':
        events = Event()
        res = make_response(events.get_all_events())
        return res

if __name__ == '__main__':
    app.run(debug=True)


