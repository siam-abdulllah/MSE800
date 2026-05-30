from flight import DomesticFlight, Flight


def main():
    """Demonstrate single inheritance with an Air New Zealand domestic flight."""
    print("Air New Zealand — Single Inheritance Demo\n")

    # Create a domestic flight (subclass)
    flight = DomesticFlight("NZ101", "Auckland", "Wellington", "North Island")

    # Use inherited attributes
    print("Inherited attributes:")
    print(f"  {flight.flight_number}, {flight.origin} → {flight.destination}")

    # Use inherited method
    flight.update_status("Boarding")

    # Use overridden method (shows inherited + domestic info)
    print("\nFlight details:")
    flight.display_details()

    # Use domestic-only method
    print(f"\nFare after discount: ${flight.calculate_fare(150)}")

    # Confirm inheritance
    print(f"\nIs DomesticFlight a Flight? {isinstance(flight, Flight)}")


if __name__ == "__main__":
    main()
