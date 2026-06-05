# Office IoT Management System

## Introduction

The [Internet of Things (IoT)](https://www.ibm.com/think/topics/internet-of-things) is a network of physical devices-such as appliances, vehicles, and office equipment-embedded with sensors, software, and network connectivity so they can collect and share data. In an office environment, IoT can automate lighting, climate control, and ventilation to improve efficiency, reduce energy waste, and support data-driven decisions.

This mini-project simulates a simple **office IoT system** that manages three types of smart devices:

- **Smart Light** - controls brightness
- **Smart Fan** - controls fan speed
- **Smart Air Conditioner** - controls temperature and mode

Users interact through a command-line menu to add devices dynamically, view their status, and control them. The design uses **object-oriented programming (OOP)** with inheritance, encapsulation, and polymorphism, together with two classic **design patterns**: **Factory** and **Singleton**.

## Design Patterns

### Factory Pattern (`devices.py`)

The **Factory Pattern** hides object creation behind a single interface. The client (`main.py`) does not call `SmartLight()`, `SmartFan()`, or `SmartAirConditioner()` directly. Instead, it asks `DeviceFactory` to create the correct device based on user input:

```python
device = DeviceFactory.create(device_type, device_id, location, **options)
```

**Why use it here?** Device types share a common `SmartDevice` base class but have different attributes (brightness, speed, temperature). The factory centralises creation logic and makes it easy to add new device types later without changing the main menu code.

### Singleton Pattern (`config.py`)

The **Singleton Pattern** ensures only **one** `SystemConfiguration` instance exists for the entire application runtime. Every call to `SystemConfiguration()` returns the same object, which holds:

- Office name and network status
- Maximum device limit
- The registry of all registered devices

```python
config = SystemConfiguration()  # always the same instance
config.register_device(device)
```

**Why use it here?** An IoT deployment should have a single system configuration manager-one place to track all devices and settings-rather than multiple conflicting copies.

## OOP Concepts Demonstrated

| Concept | How it is used |
|---------|----------------|
| **Abstraction** | `SmartDevice` abstract base class defines `get_status()` and `device_type` |
| **Inheritance** | `SmartLight`, `SmartFan`, and `SmartAirConditioner` extend `SmartDevice` |
| **Encapsulation** | Each device stores its own state (`is_on`, `brightness`, etc.) |
| **Polymorphism** | All devices implement `get_status()` differently; the menu calls the same method on any device |

## Project Structure

```
Activity3/
├── main.py            # CLI menu - user input and device control
├── devices.py         # SmartDevice hierarchy and DeviceFactory
├── config.py          # SystemConfiguration (Singleton)
├── sample_output.txt  # Example console session
└── README.md
```

## Requirements

- Python 3.10+ (standard library only - no extra packages)

## How to Run

```bash
cd Activity3
python main.py
```

## Sample Output

Below is an example session (full transcript in `sample_output.txt`):

```
Welcome to Office IoT Management System
Office: MSE800 Smart Office
Network: Connected
Registered devices: 0/10

1. Add smart device
2. View all device status
3. Control a device
4. View system configuration
5. Exit
Choose an option (1-5): 1

Device types: Smart Light, Smart Fan, Smart Air Conditioner
Enter device type: Smart Light
Enter device ID (e.g. L001): L001
Enter location (e.g. Meeting Room A): Meeting Room A
Brightness 0-100 (default 50): 80

Device created: Smart Light
[L001] Smart Light @ Meeting Room A - OFF, Brightness: 80%

Choose an option (1-5): 2

--- Office IoT Device Status ---
  [L001] Smart Light @ Meeting Room A - OFF, Brightness: 80%
  [F001] Smart Fan @ Open Office - OFF, Speed: 3/5
  [AC001] Smart Air Conditioner @ Server Room - OFF, 20°C, Mode: Cool
--------------------------------------------------
```

> **Screenshots:** Run `python main.py` locally and capture screenshots of the menu, device creation, and status view for your submission. Place them in this folder (e.g. `screenshots/menu.png`) and link them here if desired.

## GitHub Repository

Push this folder to your GitHub repository and add the repository URL to your assignment submission.

Example remote setup:

```bash
git add Activity3/
git commit -m "Add Week 7 Activity 3 Office IoT mini-project"
git push origin main
```

## References

- IBM - [What is the Internet of Things (IoT)?](https://www.ibm.com/think/topics/internet-of-things)
