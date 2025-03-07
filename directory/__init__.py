from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from directory.config import Development
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/directory_rest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.config["SECRET_KEY"] = "MY SECRET KEY"
app.config["JWT_SECRET_KEY"] = "your-strong-secret-key-here"  # Replace with a secure key

migrate = Migrate(app, db)
jwtManager = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return {"message":"hello world"}
from directory.apps.users_app import users
app.register_blueprint(users)