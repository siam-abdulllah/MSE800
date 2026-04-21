class MathToolkit:

    def __init__(self):
        self.numbers = {"a": 0, "b": 0}

    def get_user_input(self):
        print("--- Math Operations Lab ---")
        self.numbers["a"] = float(input("Enter first number: "))
        self.numbers["b"] = float(input("Enter second number: "))
        

    def calculate_results(self):
        a = self.numbers["a"]
        b = self.numbers["b"]
        
        results = {
            "Addition": a + b,
            "Subtraction": a - b,
            "Multiplication": a * b,
            "Division": a / b if b != 0 else "Undefined (Division by Zero)"
        }
        return results

    def display_report(self, data):
        print(f"\n--- Results for {self.numbers['a']} and {self.numbers['b']} ---")
        for operation, value in data.items():
            if isinstance(value, float):
                print(f"{operation}: {value:.2f}")
            else:
                print(f"{operation}: {value}")


def run_calculator():
    calc = MathToolkit()
    calc.get_user_input()
    outcomes = calc.calculate_results()
    calc.display_report(outcomes)

def show_footer():
    print("\nCalculation Complete. Stay curious!")

if __name__ == "__main__":
    run_calculator()
    show_footer()