class SystemConfiguration:
    """Singleton — one configuration manager for the whole application."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.office_name = "MSE800 Smart Office"
            cls._instance.network_connected = True
            cls._instance.max_devices = 10
            cls._instance.devices = []
        return cls._instance

    def register_device(self, device):
        if len(self.devices) >= self.max_devices:
            raise ValueError(
                f"Cannot add device. Maximum of {self.max_devices} devices reached."
            )
        for existing in self.devices:
            if existing.device_id == device.device_id:
                raise ValueError(f"Device ID '{device.device_id}' already exists.")
        self.devices.append(device)

    def find_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def get_all_devices(self):
        return list(self.devices)

    def summary(self):
        network = "Connected" if self.network_connected else "Disconnected"
        return (
            f"Office: {self.office_name}\n"
            f"Network: {network}\n"
            f"Registered devices: {len(self.devices)}/{self.max_devices}"
        )
