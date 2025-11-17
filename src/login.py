def login(username: str, password: str) -> bool:
    """Simple login function for demo purposes."""
    if username == "admin" and password == "secret":
        return True
    return False
