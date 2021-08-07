from flask import Flask, make_response, request
from model.event import Event

app = Flask(__name__)
# TODO: setup cors with proper resources matching frontend
app.config['CORS_HEADERS'] = 'Content-Type'


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/', methods=['GET'])
def index():
    return 'webserver is working fine'


@app.route('/api/getEvents', methods=['GET', 'OPTIONS'])
def event():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    if request.method == 'GET':
        events = Event()
        res = make_response(events.get_all_events())
        res.headers["Access-Control-Allow-Origin"] = "*"
        return res


if __name__ == '__main__':
    app.run(debug=True)


