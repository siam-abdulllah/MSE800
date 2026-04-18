college_name = "Yoobee College of Creative Innovation"

class StudentManager:

    def __init__(self):
        self.students = []

    def collect_student_data(self, count=3):
        print(f"--- Welcome to {college_name} ---")
        print(f"Recording data for {count} students:")
        
        for i in range(count):
            print(f"\nStudent {i + 1}:")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            student_id = input("Enter Student ID: ")
            
            self.students.append({"name": name, "age": age, "id": student_id})

    def display_sorted_students(self):
        print(type(self.students))
        if not self.students:
            print("No data found.")
            return

        sorted_list = sorted(self.students, key=lambda x: x['age'])

        print(f"\n--- {college_name} Enrollment List (By Age) ---")
        for student in sorted_list:
            print(f"Name: {student['name']} | Age: {student['age']}")

if __name__ == "__main__":
    manager = StudentManager()
    manager.collect_student_data(3)
    manager.display_sorted_students()