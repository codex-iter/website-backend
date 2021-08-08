from creds.config import mongoDB_URI
import os
os.environ['DB_URI']=mongoDB_URI

from app import app

if __name__ == '__main__':
    app.run(debug=True)