"""Login, signup, profile, and forgot-password logic."""

import getpass
import hashlib
import secrets
from datetime import date
from typing import Dict, Optional, Tuple

import storage


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return f"{salt}${digest.hex()}"


def check_password(password: str, stored: str) -> bool:
    try:
        salt, expected = stored.split("$", 1)
    except ValueError:
        return False
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return secrets.compare_digest(digest.hex(), expected)


def validate_dob(dob_str: str) -> Tuple[Optional[date], Optional[str]]:
    try:
        dob = date.fromisoformat(dob_str)
    except ValueError:
        return None, "Invalid date. Use YYYY-MM-DD."

    today = date.today()
    if dob > today:
        return None, "Date of birth cannot be in the future."

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 13:
        return None, "You must be at least 13 years old."
    return dob, None


def signup() -> Optional[Dict]:
    print("\n--- Sign Up ---")
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    full_name = input("Full Name: ").strip()
    dob_str = input("Date of Birth (YYYY-MM-DD): ").strip()
    password = getpass.getpass("Password: ")
    confirm = getpass.getpass("Confirm Password: ")

    if len(username) < 3:
        print("Error: Username must be at least 3 characters.")
        return None
    if storage.username_exists(username):
        print("Error: Username already taken.")
        return None
    if storage.email_exists(email):
        print("Error: Email already registered.")
        return None
    if not full_name:
        print("Error: Full name is required.")
        return None
    if password != confirm:
        print("Error: Passwords do not match.")
        return None
    if len(password) < 8:
        print("Error: Password must be at least 8 characters.")
        return None

    dob, err = validate_dob(dob_str)
    if err:
        print(f"Error: {err}")
        return None

    storage.create_user(username, email, hash_password(password), full_name, dob)
    print("Account created successfully!")
    return storage.get_user_by_username(username)


def login() -> Optional[Dict]:
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    user = storage.get_user_by_username(username)
    if not user or not check_password(password, user["password_hash"]):
        print("Error: Invalid username or password.")
        return None

    print(f"Welcome back, {user['full_name']}!")
    return user


def forgot_password() -> None:
    print("\n--- Forgot Password ---")
    email = input("Enter your email: ").strip()
    user = storage.get_user_by_email(email)

    if not user:
        print("If that email exists, a reset code has been sent.")
        return

    code = secrets.token_hex(3).upper()
    print(f"\nReset code for {user['email']}: {code}")
    print("(In a real app this would be emailed to you.)\n")

    entered = input("Enter reset code: ").strip().upper()
    if entered != code:
        print("Error: Invalid reset code.")
        return

    new_password = getpass.getpass("New password: ")
    confirm = getpass.getpass("Confirm new password: ")
    if new_password != confirm:
        print("Error: Passwords do not match.")
        return
    if len(new_password) < 8:
        print("Error: Password must be at least 8 characters.")
        return

    storage.update_password(user["id"], hash_password(new_password))
    print("Password updated successfully!")


def view_profile(user: dict) -> None:
    dob = date.fromisoformat(user["date_of_birth"])
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    print("\n--- Your Profile ---")
    print(f"Username:      {user['username']}")
    print(f"Full Name:     {user['full_name']}")
    print(f"Email:         {user['email']}")
    print(f"Date of Birth: {dob.strftime('%d %B %Y')}")
    print(f"Age:           {age}")


def edit_profile(user: dict) -> Dict:
    print("\n--- Edit Profile ---")
    print("Press Enter to keep the current value.\n")

    full_name = input(f"Full Name [{user['full_name']}]: ").strip() or user["full_name"]
    dob_str = input(f"Date of Birth [{user['date_of_birth']}]: ").strip() or user["date_of_birth"]
    email = input(f"Email [{user['email']}]: ").strip() or user["email"]

    dob, err = validate_dob(dob_str)
    if err:
        print(f"Error: {err}")
        return user

    if email.lower() != user["email"].lower():
        if storage.email_exists(email):
            print("Error: Email already in use.")
            return user

    storage.update_user(user["id"], full_name, dob, email)
    print("Profile updated!")
    return storage.get_user_by_username(user["username"])
