import bcrypt


def generate_secret(val: str) -> str:
    return bcrypt.hashpw(val.encode(),  bcrypt.gensalt())
