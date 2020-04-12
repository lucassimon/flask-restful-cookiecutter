# Python
from functools import wraps

# Third
from flask_jwt_extended import get_jwt_identity

# Apps
from apps.users.repositories import UserRepo
from apps.messages import Messages
from apps.responses import Response


def check_user(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        jwt_user = get_jwt_identity() or None
        if jwt_user:
            response = Response("Permissions")
            repo = UserRepo()
            user = repo.get_user_by_email(jwt_user)
            if not user.is_active():
                return response.notallowed_user(Messages.USER_INACTIVE.value)

            kwargs["user_id"] = f"{user.id}"
            kwargs["user_name"] = f"{user.name}"
            kwargs["active"] = user.is_active()
            kwargs["jwt_user"] = jwt_user
            return f(*args, **kwargs)

    return wrap
