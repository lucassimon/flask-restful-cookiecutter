# Python
from datetime import datetime

# Third
from mongoengine import BooleanField, DateTimeField, EmailField, StringField

# Apps
from apps.db import db


class UserAbstract:
    """
    Default implementation for User fields
    """

    meta = {"abstract": True, "ordering": ["email"]}

    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

    created = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)

    def is_active(self):
        return self.active


class User(db.Document, UserAbstract):
    meta = {"collection": "users"}
