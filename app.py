from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from models import db

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

CORS(app)

app.config.from_object("config.Config")

@app.route('/')
def home():
    return 'Hello, DGS!'

# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)