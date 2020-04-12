# Python
from http import HTTPStatus

from flask import jsonify

# Third
from flask_jwt_extended import JWTManager

# Apps
from apps.messages import Messages

# Flask


def configure_jwt(app):
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback():
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 42,
                "message": Messages.TOKEN_EXPIRED.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.unauthorized_loader
    def my_unauthorized_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 1,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.claims_verification_loader
    def my_claims_verification_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 2,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.invalid_token_loader
    def my_invalid_token_loader_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 3,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.needs_fresh_token_loader
    def my_needs_fresh_token_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 4,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.revoked_token_loader
    def my_revoked_token_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 5,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.user_loader_callback_loader
    def my_user_loader_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 6,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.user_loader_error_loader
    def my_user_loader_error_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 7,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.token_in_blacklist_loader
    def my_token_in_blacklist_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 8,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp

    @jwt.claims_verification_failed_loader
    def my_claims_verification_failed_callback(e):
        resp = jsonify(
            {
                "status": HTTPStatus.UNAUTHORIZED,
                "sub_status": 9,
                "description": e,
                "message": Messages.INVALID_CREDENTIALS.value,
            }
        )

        resp.status_code = HTTPStatus.UNAUTHORIZED

        return resp
