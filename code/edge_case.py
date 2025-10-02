

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def get_user(user: dict):
    user_id = user.get("id")
    if not user_id:
        return None
    name = user.get("name", "")
    return f"{user_id} {name}"
