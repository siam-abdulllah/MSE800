# Auckland Aquarium Management System

A simple command-line application to manage fish inventory at an aquarium in Auckland. The project demonstrates the **Factory** and **Singleton** design patterns with **SQLite** for persistence.

## Fish Categories

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

## Design Patterns

### Factory Pattern (`fish.py`)

The `FishFactory` class creates the correct fish object based on user input. Instead of calling `Goldfish()` or `Shark()` directly in the main program, the client asks the factory:

```python
fish = FishFactory.create("goldfish")
```

Each fish has **category**, **color**, and **type**. The user enters all three when adding fish, and the factory creates the `Fish` object from that input.

### Singleton Pattern (`database.py`)

The `Database` class uses the **Singleton pattern** via `get_instance()`. Only one SQLite connection is created and reused. Call `db.close()` when exiting to release the connection properly.

```python
db = Database.get_instance()
# ... use the app ...
db.close()
```

## Project Structure

```
Activity2/
├── main.py        # CLI menu — add fish and view inventory
├── fish.py        # Fish classes and FishFactory
├── database.py    # SQLite Singleton
├── aquarium.db    # Created automatically on first run
└── README.md
```

## Requirements

- Python 3.10+ (uses built-in `sqlite3` — no extra packages)

## How to Run

```bash
cd Activity2
python main.py
```

### Example Session

```
Welcome to Auckland Aquarium Management System

1. Add fish
2. View inventory
3. Exit
Choose an option (1-3): 1

Available categories: Goldfish, Shark, Angelfish, Tuna, Salmon
Enter fish category: Goldfish
Enter fish color: Orange
Enter fish type (e.g. Freshwater, Saltwater): Freshwater
How many to add? (default 1): 5

Added 5 Goldfish(s).
Goldfish — Color: Orange, Type: Freshwater
Total Goldfish in aquarium: 5

1. Add fish
2. View inventory
3. Exit
Choose an option (1-3): 2

--- Auckland Aquarium Inventory ---
  Angelfish: 0 fish | Color: Silver | Type: Freshwater
  Goldfish: 5 fish | Color: Orange | Type: Freshwater
  Salmon: 0 fish | Color: Pink | Type: Freshwater
  Shark: 0 fish | Color: Grey | Type: Saltwater
  Tuna: 0 fish | Color: Blue | Type: Saltwater
-------------------------------------------------------
```

## Database

SQLite table `fish_inventory`:

| Column   | Type    | Description                        |
|----------|---------|------------------------------------|
| category | TEXT PK | Fish name (Goldfish, Shark, etc.)  |
| count    | INTEGER | Number of fish in tank             |
| color    | TEXT    | Fish color                         |
| type     | TEXT    | Water type (Freshwater / Saltwater)|

The database file `aquarium.db` is created in the project folder when you first run the program.
