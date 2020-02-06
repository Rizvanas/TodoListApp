# services/users/project/api/users.py

from flask import Blueprint
from flask_restful import Resource, Api
from project.api.models import User
from project.api.schemas import UserSchema
from flask_jwt_extended import (
    jwt_required,
)

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


user_schema = UserSchema()
users_list_schema = UserSchema(many=True)

user_exists_message = "User with email:{0} already exists."
user_created_message = "User was successfully created."
users_not_found_message = "No users were found."
user_not_found_message = "User you were looking for was not found."
user_found_message = "User was successfully found."


class UsersPing(Resource):
    @classmethod
    def get(cls):
        return {
            'status': 'success',
            'message': 'pong!'
        }


class UsersList(Resource):
    @classmethod
    def get(cls):
        '''Get full list of users'''
        users = users_list_schema.dump(User.get_all())
        if not users:
            return {'message': users_not_found_message}, 404

        return {'users': users}, 200


class Users(Resource):
    '''Get user by id'''

    @classmethod
    @jwt_required
    def get(cls, user_id: int):
        user = User.find_by_id(user_id)

        if not user:
            return {'message': user_not_found_message}, 404

        return (
            {
                'message': user_found_message,
                'user': user_schema.dump(user)
            },
            200)


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<int:user_id>')
