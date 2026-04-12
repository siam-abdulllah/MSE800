def CalculatePower(a, b):
    return a ** b

if __name__ == "__main__":
    a = float(input("enter base (a): "))
    b = float(input("enter exponent (b): "))
    
    result = CalculatePower(a, b)
    print(f"{a} taken to the power of {b} is {result}")