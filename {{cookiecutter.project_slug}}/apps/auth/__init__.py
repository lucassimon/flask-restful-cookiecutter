# Third
from bcrypt import gensalt, hashpw


def generate_password(password: str):
    return hashpw(password.encode(), gensalt(12))
