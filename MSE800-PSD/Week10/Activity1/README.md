# Login & Signup System (Terminal)

A simple plain-Python account system with signup, login, profile management, and forgot password.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Menu and program entry point |
| `auth.py` | Signup, login, profile, forgot password |
| `storage.py` | SQLite database for user accounts |

## Run

```bash
python main.py
```

## Features

- **Sign Up** — username, email, password, full name, date of birth
- **Login** — username and password
- **Forgot Password** — reset via email code (printed to terminal for demo)
- **Profile** — view and edit full name, date of birth, email

User data is stored in `users.db` (created automatically on first run).
