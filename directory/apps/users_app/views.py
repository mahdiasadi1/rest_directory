from flask import jsonify, request, abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity
from directory import db
from . import users
from .models import User
from directory.utils.request import json_only
# from werkzeug.security import  check_password_hash , generate_password_hash


@users.route('/', methods=['POST'])
@json_only
def create_user():
    args = request.get_json()

    try:
        new_user = User()
        new_user.username = args.get('username')
        new_user.password = args.get('password')
        db.session.add(new_user)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return {'error': f'{e}'}, 400
    except IntegrityError:
        db.session.rollback()
        # TODO Add status 400
        return {'error': 'Username is duplicated.'} , 400

    return {'message': 'Account created successfully'}, 201
@users.route('/auth/', methods=['POST'])
@json_only
def login():
   
    
    args = request.get_json()

    username = args.get('username')
    password = args.get('password')

    user = User.query.filter(User.username.ilike(username)).first()
    if not user:
        return {'error': 'Username does not match.'}, 403
    password = password.strip() if password else password

    if not user.check_password(password):
        return {'error': 'Password does not match.'}, 403

    access_token = create_access_token(identity=user.username, fresh=True, )
    refresh_token = create_refresh_token(identity=user.username)

    return {'access_token': access_token, 'refresh_token': refresh_token}, 200
@users.route('/',methods=["GET"])
@jwt_required()  # Remove the parentheses
def get_user():
    identitiy= get_jwt_identity()
    user= User.query.filter(User.username.ilike(identitiy)).first()
    return{ "username": user.username}
@users.route('/auth/',methods=["PUT"])
@jwt_required(refresh=True)
def get_new_access_token():
     identity = get_jwt_identity()
     return {'access_token': create_access_token(identity=identity)}