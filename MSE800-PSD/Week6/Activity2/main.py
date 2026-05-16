from auth import admin_login, admin_logout, is_admin_logged_in
from zoo_admin import add_animal, update_feeding_schedule, view_animal_report


def prompt_login() -> bool:
    """Ask for username and password, then verify credentials."""
    print("=== Zoo Application - Admin Login ===\n")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    return admin_login(username, password)


def admin_menu() -> None:
    """Show admin options after a successful login."""
    while is_admin_logged_in():
        print("\n=== Admin Menu ===")
        print("1. Add animal")
        print("2. View animal report")
        print("3. Update feeding schedule")
        print("4. Logout")
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            name = input("Animal name: ").strip()
            species = input("Species: ").strip()
            enclosure = input("Enclosure ID: ").strip()
            add_animal(name, species, enclosure)

        elif choice == "2":
            view_animal_report()

        elif choice == "3":
            animal_name = input("Animal name: ").strip()
            feeding_time = input("Feeding time (e.g. 08:00): ").strip()
            update_feeding_schedule(animal_name, feeding_time)

        elif choice == "4":
            admin_logout()
            print("\nSession ended. Goodbye.")

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main() -> None:
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        if prompt_login():
            admin_menu()
            return

        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"\nPlease try again. ({remaining} attempt(s) left)\n")
        else:
            print("\nToo many failed login attempts. Exiting.")


if __name__ == "__main__":
    main()
