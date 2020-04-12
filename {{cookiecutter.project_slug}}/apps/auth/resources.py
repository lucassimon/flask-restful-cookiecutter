# Python

# Flask
from flask import request
from flask.wrappers import Response

# Third
from bcrypt import checkpw
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
)
from flask_restful import Resource


# Apps
from apps.decorators import check_user


# Local


class AuthResource(Resource):
    def post(self):
        raise NotImplementedError()


class RefreshTokenResource(Resource):
    @jwt_refresh_token_required
    def post(self, *args, **kwargs):
        raise NotImplementedError()


class SignUp(Resource):
    def post(self, *args, **kwargs):
        raise NotImplementedError()


class Profile(Resource):
    @jwt_required
    @check_user
    def get(self, *args, **kwargs):
        raise NotImplementedError()


class ChangePassword(Resource):
    @jwt_required
    @check_user
    def post(self, *args, **kwargs):
        raise NotImplementedError()
