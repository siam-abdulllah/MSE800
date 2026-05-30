# Parent class — general Air New Zealand flight


class Flight:
    """Parent class. Attributes and methods here are inherited by subclasses."""

    def __init__(self, flight_number, origin, destination):
        # Shared attributes (inherited by DomesticFlight)
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.status = "Scheduled"

    def display_details(self):
        """Shared method — prints basic flight info."""
        print(f"Flight {self.flight_number}: {self.origin} → {self.destination}")
        print(f"Status: {self.status}")

    def update_status(self, new_status):
        """Shared method — updates flight status."""
        self.status = new_status


# Subclass — domestic flight inherits from Flight


class DomesticFlight(Flight):
    """Subclass. Inherits from Flight and adds domestic-only features."""

    def __init__(self, flight_number, origin, destination, domestic_region):
        # Inherit parent attributes via super()
        super().__init__(flight_number, origin, destination)

        # Domestic-only attribute
        self.domestic_region = domestic_region

    def display_details(self):
        """Override parent method — calls super() then adds domestic info."""
        super().display_details()
        print(f"Region: {self.domestic_region}")

    def calculate_fare(self, base_fare):
        """Domestic-only method — 10% discount on domestic routes."""
        return round(base_fare * 0.9, 2)
