from land import Rectangle

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Land Measurement Tool")
    
    l = get_valid_input("Enter the length of the land: ")
    w = get_valid_input("Enter the width of the land: ")

    my_land = Rectangle(l, w)

    my_land.display_info()

if __name__ == "__main__":
    main()