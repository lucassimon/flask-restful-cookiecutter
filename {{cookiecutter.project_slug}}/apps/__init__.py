# -*- coding: utf-8 -*-

from flask import Flask, jsonify

# Third
from config import config
from flask_cors import CORS

# Apps
from apps.messages import Messages

# Local
from .db import db
from .jwt import configure_jwt
from .api import configure_api
from .cache import configure_cache


def create_app(config_name):
    app = Flask(f"{{cookiecutter.project_slug}}-{config_name}")

    app.config.from_object(config[config_name])

    @app.after_request
    def apply_caching(response):
        response.headers["X-DEV"] = "Created with love."
        return response

    @app.errorhandler(404)
    def page_not_found(err):
        resp = jsonify({"status": 404, "message": Messages.RESOURCE_NOT_FOUND.value})
        resp.status_code = 404
        return resp

    @app.errorhandler(422)
    def handle_error(err):
        if "messages" in err.data:
            messages = err.data.get("messages")
        else:
            messages = Messages.RESOURCE_BAD_REQUEST.value

        resp = jsonify({"status": err.code, "message": messages})
        resp.status_code = err.code
        return resp

    CORS(app, resources={r"/*": {"origins": "*"}})

    # Configure MongoEngine
    db.init_app(app)

    # Configure Cache
    configure_cache(app)

    # Configure JWT
    configure_jwt(app)

    configure_api(app)

    return app
