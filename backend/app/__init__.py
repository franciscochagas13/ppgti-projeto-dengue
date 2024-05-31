from flask import Flask
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(app.config['MONGODB_URI'])
db = client.get_default_database()

from app.routes import bp as routes_bp
app.register_blueprint(routes_bp)

from app.scheduler import start_scheduler
start_scheduler(app)