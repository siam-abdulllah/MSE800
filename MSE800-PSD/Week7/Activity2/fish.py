# Valid fish categories in the Auckland aquarium
FISH_CATEGORIES = ["Goldfish", "Shark", "Angelfish", "Tuna", "Salmon"]


class Fish:
    """A fish with a category name, color, and water type."""

    def __init__(self, category, color, fish_type):
        self.category = category
        self.color = color
        self.type = fish_type

    def describe(self):
        return (
            f"{self.category} — Color: {self.color}, "
            f"Type: {self.type}"
        )


class FishFactory:
    """Factory — creates a Fish object from user input."""

    @staticmethod
    def create(name, color, fish_type):
        key = name.strip().lower()
        for category in FISH_CATEGORIES:
            if category.lower() == key:
                return Fish(category, color.strip(), fish_type.strip())
        options = ", ".join(FISH_CATEGORIES)
        raise ValueError(f"Unknown fish '{name}'. Choose from: {options}")

    @staticmethod
    def categories():
        return FISH_CATEGORIES
