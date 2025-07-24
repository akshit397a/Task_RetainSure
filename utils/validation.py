def is_valid_username(username: str) -> bool:
    return username.isalnum() and len(username) >= 3

def is_valid_password(password: str) -> bool:
    return len(password) >= 6
