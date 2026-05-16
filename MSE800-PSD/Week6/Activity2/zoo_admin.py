from decorators import log_admin_activity, require_admin


@require_admin
@log_admin_activity
def add_animal(name: str, species: str, enclosure: str) -> None:
    print(f"Added {name} ({species}) to enclosure {enclosure}.")


@require_admin
@log_admin_activity
def view_animal_report() -> None:
    print("Animal report: 42 animals across 12 enclosures. All feeding schedules up to date.")


@require_admin
@log_admin_activity
def update_feeding_schedule(animal_name: str, feeding_time: str) -> None:
    print(f"Updated feeding schedule for {animal_name} to {feeding_time}.")
