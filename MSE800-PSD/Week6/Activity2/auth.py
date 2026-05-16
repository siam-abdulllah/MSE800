# Simple in-memory admin session for the Zoo Application demo.
# Default admin credentials are used only for this coursework example.

ADMIN_CREDENTIALS = {
    "admin": "zoo2026",
}

_current_admin = None


def admin_login(username: str, password: str) -> bool:
    """Validate admin credentials and start a session."""
    global _current_admin

    stored_password = ADMIN_CREDENTIALS.get(username)
    if stored_password is None or stored_password != password:
        print("Login failed: Invalid username or password.")
        return False

    _current_admin = username
    print(f"Welcome, {username}! You are now logged in as Zoo Admin.")
    return True


def admin_logout() -> None:
    """End the current admin session."""
    global _current_admin

    if _current_admin is None:
        print("No admin is currently logged in.")
        return

    print(f"Goodbye, {_current_admin}. You have been logged out.")
    _current_admin = None


def is_admin_logged_in() -> bool:
    """Return True when an admin session is active."""
    return _current_admin is not None


def get_current_admin() -> str | None:
    """Return the username of the logged-in admin, or None."""
    return _current_admin
