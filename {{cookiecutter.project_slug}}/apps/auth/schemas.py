# -*- coding: utf-8 -*-


# Third
from marshmallow import Schema, post_load
from marshmallow.fields import Email, Str

# Apps
from apps.messages import Messages


class LoginSchema(Schema):
    email = Email(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )


class UserRegistrationSchema(Schema):
    email = Email(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    name = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    confirm_password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )

    @post_load
    def lowerstrip_email(self, item, **kwargs):
        item["email"] = item["email"].lower().strip()
        return item


class ChangePasswordSchema(Schema):
    old_password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    confirm_password = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
