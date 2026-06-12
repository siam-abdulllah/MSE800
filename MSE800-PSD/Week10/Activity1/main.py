"""Terminal-based login and signup system."""

import auth
import storage


def main_menu() -> None:
    print("\n===== Auth System =====")
    print("1. Sign Up")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")
    return input("Choose an option: ").strip()


def account_menu(user: dict) -> str:
    print(f"\n===== Welcome, {user['full_name']} =====")
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. Logout")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        auth.view_profile(user)
    elif choice == "2":
        user = auth.edit_profile(user)
    elif choice == "3":
        print("Logged out.")
        return "logout"

    return "stay"


def main() -> None:
    storage.init_db()
    current_user = None

    while True:
        if current_user is None:
            choice = main_menu()

            if choice == "1":
                current_user = auth.signup()
            elif choice == "2":
                current_user = auth.login()
            elif choice == "3":
                auth.forgot_password()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        else:
            if account_menu(current_user) == "logout":
                current_user = None


if __name__ == "__main__":
    main()
