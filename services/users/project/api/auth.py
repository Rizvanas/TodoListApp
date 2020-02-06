# /services/users/project/api/auth.py

from flask import Blueprint, request
from project.api.models import User
from project.api.schemas import UserSchema
from project import bcrypt, blacklist
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt,
    jwt_refresh_token_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity
)


user_exists_message = "User with email:{0} already exists."
user_does_not_exist_message = "User does not exist."
user_created_message = "User was successfully created."
wrong_password_or_email_message = "Entered username or password is incorrect."
successfully_logged_out_message = "Successfully logged out."

auth_blueprint = Blueprint('auth', __name__)
user_schema = UserSchema()


@auth_blueprint.route('/auth/register', methods=['POST'])
def register_user():
    '''Add new user'''
    errors = user_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 422

    user_request = user_schema.load(request.get_json())
    username = user_request.username
    email = user_request.email

    if User.find_existing_user(username, email):
        return {'message': user_exists_message.format(email)}, 409

    user_request.save()
    return {'message': user_created_message}, 201


@auth_blueprint.route('/auth/login', methods=['POST'])
def login_user():
    '''Authenticate existing user'''
    password = request.get_json()['password']
    user_request = user_schema.load(
        request.get_json(),
        partial=('email',)
    )
    user = User.find_by_username(user_request.username)

    if not user:
        return {'message': user_does_not_exist_message}, 404

    if not bcrypt.check_password_hash(user.password, password):
        return {'message': wrong_password_or_email_message}, 401

    access_token = create_access_token(identity=user.id, fresh=True)
    refresh_token = create_refresh_token(identity=user.id)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }, 201


@auth_blueprint.route('/auth/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    '''Get fresh token'''
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id, fresh=False)
    return {'access_token': access_token}, 200


@auth_blueprint.route('/auth/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return {'message': successfully_logged_out_message}
