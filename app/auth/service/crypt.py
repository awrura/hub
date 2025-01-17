import bcrypt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid_pswrd(pswrd: str, hashed_pswrd: bytes) -> bool:
    return bcrypt.checkpw(pswrd.encode('utf-8'), hashed_pswrd)
