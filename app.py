from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, ma
from config import Config

app = Flask(__name__)

def create_app():
    #app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    from routes import api_route
    app.register_blueprint(api_route, url_prefix='/api')

    with app.app_context():
        # Create tables for our models
        # from models.base import BaseModel
        db.create_all()
        return app
