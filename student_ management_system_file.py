class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name} | Roll No: {self.roll_number} | Marks: {self.marks} | Grade: {self.get_grade()}")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, marks):
        student = Student(name, roll_number, marks)
        self.students.append(student)
        print(f"Student '{name}' added successfully.")

    def remove_student(self, roll_number):
        for s in self.students:
            if s.roll_number == roll_number:
                self.students.remove(s)
                print(f"Student with Roll No {roll_number} removed.")
                return
        print("Student not found.")

    def display_all(self):
        if not self.students:
            print("No students found.")
        else:
            print("\n--- All Students ---")
            for s in self.students:
                s.display()

    def search_student(self, roll_number):
        for s in self.students:
            if s.roll_number == roll_number:
                s.display()
                return
        print("Student not found.")


# Main program
sm = StudentManagement()

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        sm.add_student(name, roll, marks)
    elif choice == "2":
        roll = input("Enter roll number to remove: ")
        sm.remove_student(roll)
    elif choice == "3":
        sm.display_all()
    elif choice == "4":
        roll = input("Enter roll number to search: ")
        sm.search_student(roll)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")