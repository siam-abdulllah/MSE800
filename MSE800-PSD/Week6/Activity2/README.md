# Zoo Application – Admin Login System

A small Python demo of a **Zoo Application** with an **admin login system**. Protected admin tasks only run after a successful login. Activity logging is handled with decorators so the business logic stays clean.

## Project structure

```
Activity2/
├── auth.py          # Admin credentials, login, logout, session state
├── decorators.py    # @require_admin and @log_admin_activity decorators
├── zoo_admin.py     # Protected admin operations (animals, reports, schedules)
├── main.py          # Demo script showing login flow and blocked access
└── README.md        # This file
```

| File | Role |
|------|------|
| `auth.py` | Stores the active admin session and validates username/password |
| `decorators.py` | Wraps functions to enforce login and log admin actions |
| `zoo_admin.py` | Admin-only zoo management functions |
| `main.py` | Interactive login prompts and admin menu after verification |

## Functionality

1. **Interactive login** – The program prompts for username and password, then verifies them with `admin_login()`.
2. **Verification** – Invalid credentials are rejected; you get up to 3 login attempts.
3. **Admin menu** – After a successful login, you can choose admin actions from a menu (add animal, view report, update schedule).
4. **Protected operations** – Menu actions call functions in `zoo_admin.py`, which are guarded by `@require_admin`.
5. **Activity logging** – Each successful admin action prints a timestamped log block before and after it runs.
6. **Logout** – Option 4 ends the session; protected actions are blocked again until you log in.

**Demo credentials:** username `admin`, password `zoo2026`

## How the decorator is implemented

Two decorators are used (the assignment requires at least one):

### `@require_admin`

Defined in `decorators.py`. It wraps admin functions and calls `is_admin_logged_in()` from `auth.py` before the real function runs.

```python
def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_admin_logged_in():
            print("Access denied: Please log in as an admin first.")
            return None
        return func(*args, **kwargs)
    return wrapper
```

When you write `@require_admin` above a function, Python replaces that function with `wrapper`. Calls like `add_animal(...)` hit the wrapper first; only logged-in admins reach the original `add_animal` body.

### `@log_admin_activity`

Also in `decorators.py`. It prints a log header (function name and time), runs the function, then prints a completion message. It does not check login—that is handled by `@require_admin`.

Decorators can be **stacked**. In `zoo_admin.py`, `@require_admin` is placed above `@log_admin_activity`, so the order is: check login → log start → run action → log end.

## Run the project

From the `Activity2` folder:

```bash
python main.py
```

Expected flow:

1. Enter username and password when prompted  
2. On success → admin menu appears  
3. Choose options 1–3 to run protected actions (each is logged by the decorator)  
4. Choose option 4 to log out and exit the menu  

Example login: username `admin`, password `zoo2026`

## GitHub

This project lives in the [MSE800](https://github.com/siam-abdulllah/MSE800) repository under `MSE800-PSD/Week6/Activity2/`.
