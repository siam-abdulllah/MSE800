from config import SystemConfiguration
from devices import DeviceFactory


def show_menu():
    print("\n1. Add smart device")
    print("2. View all device status")
    print("3. Control a device")
    print("4. View system configuration")
    print("5. Exit")


def display_all_devices(config):
    devices = config.get_all_devices()
    print("\n--- Office IoT Device Status ---")
    if not devices:
        print("  No devices registered yet.")
    else:
        for device in devices:
            print(f"  {device.get_status()}")
    print("-" * 50)


def add_device(config):
    print("\nDevice types:", ", ".join(DeviceFactory.types()))
    device_type = input("Enter device type: ").strip()
    device_id = input("Enter device ID (e.g. L001): ").strip()
    location = input("Enter location (e.g. Meeting Room A): ").strip()

    if device_id == "" or location == "":
        print("Device ID and location cannot be empty.")
        return

    options = {}
    type_key = device_type.lower()

    if type_key in ("light", "smart light"):
        brightness_text = input("Brightness 0-100 (default 50): ").strip()
        if brightness_text != "":
            try:
                options["brightness"] = int(brightness_text)
            except ValueError:
                print("Brightness must be a whole number.")
                return

    elif type_key in ("fan", "smart fan"):
        speed_text = input("Speed 1-5 (default 1): ").strip()
        if speed_text != "":
            try:
                options["speed"] = int(speed_text)
            except ValueError:
                print("Speed must be a whole number.")
                return

    elif type_key in ("ac", "air conditioner", "aircon", "smart air conditioner"):
        temp_text = input("Temperature 16-30°C (default 22): ").strip()
        if temp_text != "":
            try:
                options["temperature"] = int(temp_text)
            except ValueError:
                print("Temperature must be a whole number.")
                return
        mode = input("Mode Cool/Heat/Fan/Dry (default Cool): ").strip()
        if mode != "":
            options["mode"] = mode.capitalize()

    try:
        device = DeviceFactory.create(device_type, device_id, location, **options)
        config.register_device(device)
    except ValueError as error:
        print(error)
        return

    print(f"\nDevice created: {device.device_type}")
    print(device.get_status())


def control_device(config):
    device_id = input("\nEnter device ID to control: ").strip()
    device = config.find_device(device_id)

    if device is None:
        print(f"No device found with ID '{device_id}'.")
        return

    print(f"\nCurrent: {device.get_status()}")
    print("1. Turn ON")
    print("2. Turn OFF")
    print("3. Adjust settings")
    choice = input("Choose action (1-3): ").strip()

    if choice == "1":
        device.turn_on()
        print("Device turned ON.")
    elif choice == "2":
        device.turn_off()
        print("Device turned OFF.")
    elif choice == "3":
        if device.device_type == "Smart Light":
            level = input("New brightness 0-100: ").strip()
            try:
                device.set_brightness(int(level))
            except ValueError:
                print("Please enter a whole number.")
                return
        elif device.device_type == "Smart Fan":
            level = input("New speed 1-5: ").strip()
            try:
                device.set_speed(int(level))
            except ValueError:
                print("Please enter a whole number.")
                return
        elif device.device_type == "Smart Air Conditioner":
            temp = input("New temperature 16-30: ").strip()
            mode = input("New mode Cool/Heat/Fan/Dry: ").strip()
            try:
                device.set_temperature(int(temp))
            except ValueError:
                print("Please enter a whole number for temperature.")
                return
            if mode != "":
                device.set_mode(mode.capitalize())
        else:
            print("No adjustable settings for this device.")
            return
    else:
        print("Invalid action.")
        return

    print(f"Updated: {device.get_status()}")


def main():
    config = SystemConfiguration()
    print("Welcome to Office IoT Management System")
    print(config.summary())

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_device(config)
        elif choice == "2":
            display_all_devices(config)
        elif choice == "3":
            control_device(config)
        elif choice == "4":
            print("\n--- System Configuration ---")
            print(config.summary())
            print("-" * 50)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
