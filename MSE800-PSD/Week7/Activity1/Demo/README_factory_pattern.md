# Design Patterns Demo — Factory Pattern

Small Python demos for design patterns. This note explains `factory_pattern.py`.

## What is the Factory Pattern?

Instead of creating objects directly (`Dog()`), the client asks a **factory** to create them (`factory.create_product()`). Creation logic stays in the factory class.

## Classes in the sample

**Factories** (create objects):

- `Factory` — parent (abstract)
- `AnimalFactory` — creates `Dog` or `Cat` based on `kind` (`"dog"` / `"cat"`)
- `DogFactory` — always creates a `Dog`
- `CatFactory` — not implemented yet (`pass`)

**Products** (the objects being created):

- `Animals` — parent (abstract)
- `Dog`, `Cat` — subclasses with a `run()` method

Yes, there are **parent classes and subclasses** in both groups.

## How it runs

```bash
python factory_pattern.py
```

Output:

```
I'm a Dog, I can run!!
```

The client uses `DogFactory`, gets a `Dog`, and calls `run()`.

## Other demo files

- `singleton_pattern.py`
- `builder_pattern.py`
- `adapter_pattern.py`
- `observer_pattern.py`
