from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# TODO: setup cors with proper resources matching frontend
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'webserver is working fine'

if __name__ == '__main__':
    app.run(debug=True)