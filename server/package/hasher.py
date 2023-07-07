from passlib.hash import bcrypt_sha256


def hash_password(psw: str) -> str:
    return bcrypt_sha256.hash(psw)


def verify_password(psw: str, hash_) -> bool:
    return bcrypt_sha256.verify(psw, hash_)

