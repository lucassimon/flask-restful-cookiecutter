# -*- coding: utf-8 -*-

# Python
from os.path import dirname, isfile, join

import pytest
from dotenv import load_dotenv
import flask_caching as fsc

_ENV_FILE = join(dirname(__file__), "../.env")

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


@pytest.fixture(scope="session")
def client():
    from apps import create_app

    flask_app = create_app("testing")
    flask_app.testing = True
    flask_app.config["CACHE_TYPE"] = "simple"

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def cache(client):
    return fsc.Cache(client)


@pytest.fixture(scope="session")
def auth(cache):
    # from flask_jwt_extended import create_access_token, create_refresh_token

    return client
