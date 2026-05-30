from flight import DomesticFlight, Flight, InternationalFlight


def main():
    print("Air New Zealand — Hybrid Inheritance Demo\n")

    # Domestic flight
    domestic = DomesticFlight(
        "NZ101", "Auckland", "Wellington", "North Island", 150, "23 kg", 1
    )
    print(f"Airline: {domestic.get_airline_name()}")  # inherited (multilevel)
    domestic.update_status("Boarding")                  # inherited (hierarchical)
    domestic.display_details()
    print(f"Final fare: {domestic.calculate_fare()}")     # uses inherited ticket_price
    print(f"{domestic.check_in()}\n")

    # International flight
    international = InternationalFlight(
        "NZ8", "Auckland", "Los Angeles", "USA", 1200, "23 kg", 2
    )
    international.display_details()
    print(f"Final fare: {international.calculate_fare()}")
    print(f"{international.check_passport()}\n")

    # Inheritance checks
    print(f"Domestic is Flight: {isinstance(domestic, Flight)}")
    print(f"International is Flight: {isinstance(international, Flight)}")


if __name__ == "__main__":
    main()
