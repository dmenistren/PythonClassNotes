import bcrypt


def generate_secret(val: str) -> str:
    return bcrypt.hashpw(val.encode(),  bcrypt.gensalt()).decode()


def decode_secret(password: str, hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hash.encode("utf-8")
    )
