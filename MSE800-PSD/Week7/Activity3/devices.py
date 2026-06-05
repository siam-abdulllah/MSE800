from abc import ABC, abstractmethod

DEVICE_TYPES = ["Smart Light", "Smart Fan", "Smart Air Conditioner"]


class SmartDevice(ABC):
    """Base class for all office IoT devices."""

    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    @abstractmethod
    def get_status(self):
        pass

    @property
    @abstractmethod
    def device_type(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self, device_id, location, brightness=50):
        super().__init__(device_id, location)
        self.brightness = brightness

    @property
    def device_type(self):
        return "Smart Light"

    def set_brightness(self, level):
        self.brightness = max(0, min(100, level))

    def get_status(self):
        state = "ON" if self.is_on else "OFF"
        return (
            f"[{self.device_id}] Smart Light @ {self.location} - "
            f"{state}, Brightness: {self.brightness}%"
        )


class SmartFan(SmartDevice):
    def __init__(self, device_id, location, speed=1):
        super().__init__(device_id, location)
        self.speed = speed

    @property
    def device_type(self):
        return "Smart Fan"

    def set_speed(self, level):
        self.speed = max(1, min(5, level))

    def get_status(self):
        state = "ON" if self.is_on else "OFF"
        return (
            f"[{self.device_id}] Smart Fan @ {self.location} - "
            f"{state}, Speed: {self.speed}/5"
        )


class SmartAirConditioner(SmartDevice):
    def __init__(self, device_id, location, temperature=22, mode="Cool"):
        super().__init__(device_id, location)
        self.temperature = temperature
        self.mode = mode

    @property
    def device_type(self):
        return "Smart Air Conditioner"

    def set_temperature(self, temp):
        self.temperature = max(16, min(30, temp))

    def set_mode(self, mode):
        allowed = ("Cool", "Heat", "Fan", "Dry")
        if mode in allowed:
            self.mode = mode

    def get_status(self):
        state = "ON" if self.is_on else "OFF"
        return (
            f"[{self.device_id}] Smart Air Conditioner @ {self.location} - "
            f"{state}, {self.temperature}°C, Mode: {self.mode}"
        )


class DeviceFactory:
    """Factory — creates the correct SmartDevice from user input."""

    @staticmethod
    def create(device_type, device_id, location, **options):
        key = device_type.strip().lower()

        if key in ("light", "smart light"):
            brightness = options.get("brightness", 50)
            return SmartLight(device_id, location, brightness)

        if key in ("fan", "smart fan"):
            speed = options.get("speed", 1)
            return SmartFan(device_id, location, speed)

        if key in ("ac", "air conditioner", "aircon", "smart air conditioner"):
            temperature = options.get("temperature", 22)
            mode = options.get("mode", "Cool")
            return SmartAirConditioner(device_id, location, temperature, mode)

        options_text = ", ".join(DEVICE_TYPES)
        raise ValueError(f"Unknown device '{device_type}'. Choose from: {options_text}")

    @staticmethod
    def types():
        return DEVICE_TYPES
