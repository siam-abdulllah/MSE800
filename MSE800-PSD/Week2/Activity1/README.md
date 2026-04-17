# Advanced Multi-Type Calculator

A Python project developed for **Week 2 – Activity 1**. This project performs basic mathematical operations using modular functions and supports multiple data types, including integers, floats, and complex numbers.

## Features
- **Basic Arithmetic:** Supports Addition (+), Subtraction (-), Multiplication (*), Division (/), and Modulo (%).
- **Complex Number Support:** Handles operations for complex data types (e.g., `2 + 3j`).
- **Factorial Calculation:** Includes a dedicated function to calculate factorials of non-negative integers.
- **Modular Design:** Logic is split into three distinct functions for clarity and maintainability.

## Project Structure
The project is organized into three primary functions:
1. `basic_operations(a, b, op)`: Handles standard real-number math.
2. `complex_operations(c1, c2, op)`: Specifically manages operations involving `complex` data types.
3. `special_operations(n)`: Utilizes the `math` library to compute factorials.

## Requirements
- Python 3.x
- Standard libraries: `math`, `cmath`

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Week2-Math-Activity.git
   ```
2. Navigate to the directory:
   ```bash
   cd Week2-Math-Activity
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Example Usage
```python
# Complex Addition
complex_operations(complex(2, 3), complex(1, 1), '+') # Result: (3+4j)

# Factorial
special_operations(5) # Result: 120
```
