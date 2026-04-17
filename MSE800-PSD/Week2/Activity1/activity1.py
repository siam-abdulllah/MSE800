import math

def basic_operations(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else "Error: Division by zero"
    if op == '%': return a % b
    return "Invalid Operator"

def complex_operations(c1, c2, op):
    if op == '+': return c1 + c2
    if op == '-': return c1 - c2
    if op == '*': return c1 * c2
    if op == '/': return c1 / c2
    return "Invalid Operator"

def special_operations(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    return math.factorial(int(n))

def main():
    print("--- Multi-Type Calculator ---")
    
    print(f"Addition (10 + 5): {basic_operations(10, 5, '+')}")
    print(f"Modulo (10 % 3): {basic_operations(10, 3, '%')}")

    comp1 = complex(2, 3) # 2 + 3j
    comp2 = complex(1, 2) # 1 + 2j
    print(f"Complex Multiplication: {complex_operations(comp1, comp2, '/')}")

    print(f"Factorial of 5: {special_operations(5)}")

if __name__ == "__main__":
    main()