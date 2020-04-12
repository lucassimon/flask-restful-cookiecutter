# -*- coding: utf-8 -*-


# Third
from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean

# Apps
from apps.messages import Messages


class UserSchema(Schema):
    id = Str(dump_only=True)
    name = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    email = Email(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    active = Boolean()
