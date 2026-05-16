from datetime import datetime
from functools import wraps

from auth import is_admin_logged_in


def require_admin(func):
    """Decorator that blocks zoo admin actions unless an admin is logged in."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_admin_logged_in():
            print("Access denied: Please log in as an admin first.")
            return None

        return func(*args, **kwargs)

    return wrapper


def log_admin_activity(func):
    """Decorator that logs when an admin function runs and when it finishes."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("-----------------------------------")
        print(f"Admin action: {func.__name__}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Action started...")

        result = func(*args, **kwargs)

        print("Action completed.")
        print("-----------------------------------\n")

        return result

    return wrapper
