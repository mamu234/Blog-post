from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from app import views
from app import auth

from os import path 


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
 app = Flask(__name__)
 app.config['SECRET_KEY'] = "helloworld"
 app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
 db.init_app(app)

 app.register_blueprint(views, url_prefix="/")
 app.register_blueprint(auth, url_prefix="/")


# bootstrap = Bootstrap()

 return app 