# Air New Zealand — Single Inheritance

Simple demo: `DomesticFlight` inherits from `Flight`.

| Flight (parent) | DomesticFlight (subclass) |
|---|---|
| `flight_number`, `origin`, `destination`, `status` | `domestic_region` |
| `display_details()`, `update_status()` | `calculate_fare()`, overridden `display_details()` |

Open `Air_New_Zealand_Class_Diagram.drawio` in [draw.io](https://app.diagrams.net/).

```bash
python main.py
```
