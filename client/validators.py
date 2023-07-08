import re


EMAIL_PATTERN = re.compile(r"\w{2,}@\w{2,}\.[\w]{2,}")


def validate_username(username: str) -> bool:
    return len(username) >= 5


def validate_password(password: str) -> bool:
    return len(password) >= 5


def validate_email(email: str) -> bool:
    print(EMAIL_PATTERN.fullmatch(email))
    return bool(EMAIL_PATTERN.fullmatch(email))
