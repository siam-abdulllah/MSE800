from database import Database
from fish import FishFactory


def show_menu():
    print("\n1. Add fish")
    print("2. View inventory")
    print("3. Exit")


def display_inventory(db):
    print("\n--- Auckland Aquarium Inventory ---")
    for category, count, color, fish_type in db.get_inventory():
        color_text = color if color else "Not set"
        type_text = fish_type if fish_type else "Not set"
        print(f"  {category}: {count} fish | Color: {color_text} | Type: {type_text}")
    print("-" * 55)


def add_fish(db):
    print("\nFish categories:", ", ".join(FishFactory.categories()))
    name = input("Enter fish category: ").strip()
    color = input("Enter fish color: ").strip()
    fish_type = input("Enter fish type (e.g. Freshwater, Saltwater): ").strip()

    if color == "" or fish_type == "":
        print("Color and type cannot be empty.")
        return

    amount_text = input("How many to add? (default 1): ").strip()
    if amount_text == "":
        amount = 1
    else:
        try:
            amount = int(amount_text)
            if amount < 1:
                print("Amount must be at least 1.")
                return
        except ValueError:
            print("Please enter a whole number.")
            return

    try:
        fish = FishFactory.create(name, color, fish_type)
    except ValueError as error:
        print(error)
        return

    db.add_fish(fish.category, amount, fish.color, fish.type)
    total = db.get_count(fish.category)

    print(f"\nAdded {amount} {fish.category}(s).")
    print(fish.describe())
    print(f"Total {fish.category} in aquarium: {total}")


def main():
    db = Database.get_instance()
    print("Welcome to Auckland Aquarium Management System")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_fish(db)
        elif choice == "2":
            display_inventory(db)
        elif choice == "3":
            print("Goodbye!")
            db.close()
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
