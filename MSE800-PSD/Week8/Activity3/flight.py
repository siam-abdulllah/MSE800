# Hybrid inheritance:
#   Multilevel:   AirlineEntity → Flight
#   Hierarchical: Flight → DomesticFlight, InternationalFlight
#   Multiple:     DomesticFlight / InternationalFlight also inherit FareCalculable


class AirlineEntity:
    def __init__(self, airline_name):
        self.airline_name = airline_name

    def get_airline_name(self):
        return self.airline_name

    def validate(self):
        return bool(self.airline_name)

    def get_info(self):
        return f"Airline: {self.airline_name}"


class Flight(AirlineEntity):
    def __init__(self, flight_number, origin, destination, ticket_price, baggage_allowance):
        super().__init__("Air New Zealand")
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price
        self.baggage_allowance = baggage_allowance
        self.status = "Scheduled"

    def display_details(self):
        print(f"Flight {self.flight_number}: {self.origin} → {self.destination}")
        print(f"Status: {self.status}")
        print(f"Ticket price: ${self.ticket_price:.2f}")
        print(f"Baggage: {self.baggage_allowance}")

    def update_status(self, new_status):
        self.status = new_status

    def get_route(self):
        return f"{self.origin} → {self.destination}"


class FareCalculable:
    def apply_discount(self, amount, percent):
        return round(amount * (1 - percent / 100), 2)

    def add_fee(self, amount, percent):
        return round(amount * (1 + percent / 100), 2)

    def format_price(self, amount):
        return f"${amount:.2f}"


class DomesticFlight(Flight, FareCalculable):
    def __init__(
        self, flight_number, origin, destination, region,
        ticket_price, baggage_allowance, number_of_baggage,
    ):
        super().__init__(flight_number, origin, destination, ticket_price, baggage_allowance)
        self.region = region
        self.number_of_baggage = number_of_baggage  # child-specific

    def display_details(self):
        super().display_details()
        print(f"Type: Domestic ({self.region})")
        print(f"Number of bags: {self.number_of_baggage}")

    def calculate_fare(self):
        return self.format_price(self.apply_discount(self.ticket_price, 10))

    def check_in(self):
        return f"Check-in open for {self.flight_number}"


class InternationalFlight(Flight, FareCalculable):
    def __init__(
        self, flight_number, origin, destination, country,
        ticket_price, baggage_allowance, number_of_baggage,
    ):
        super().__init__(flight_number, origin, destination, ticket_price, baggage_allowance)
        self.country = country
        self.number_of_baggage = number_of_baggage  # child-specific

    def display_details(self):
        super().display_details()
        print(f"Type: International ({self.country})")
        print(f"Number of bags: {self.number_of_baggage}")

    def calculate_fare(self):
        return self.format_price(self.add_fee(self.ticket_price, 5))

    def check_passport(self):
        return f"Passport required for {self.country}"
