from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from directory.config import Development
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/directory_rest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.config["SECRET_KEY"] = "MY SECRET KEY"
migrate = Migrate(app, db)


@app.route('/')
def home():
    return {"message":"hello world"}
from directory.apps.users_app import users
app.register_blueprint(users)