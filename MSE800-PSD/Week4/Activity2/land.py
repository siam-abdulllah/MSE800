class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        
        print("\n--- Land Dimensions Report ---")
        print(f"Length:    {self.length:.2f} units")
        print(f"Width:     {self.width:.2f} units")
        print(f"Area:      {area:.2f} sq units")
        print(f"Perimeter: {perimeter:.2f} units")
        print("------------------------------")