# Declare as Students function, outstanding balance and enrolled courses list
class Students:
    def __init__(self, name, email, students_id):
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0
        self.students_id = students_id

# Declare as Course function
class Courses:
    def __init__(self, courses_id, fee, name):
        self.courses_id = courses_id
        self.fee = fee
        self.name = name

#Declared as course registration and Course add function, Students dictionary, available courses
class RegistrationSystem:
    def __init__(self):
        self.students = {}
        self.courses = []

    def add_course(self, name, courses_id, fee):
        if any(course.courses_id == courses_id for course in self.courses):
            print("Error: Course is already added.")
        else:
            self.courses.append(Courses(courses_id, fee, name))
            print("Course added successfully!")

# Declared as function to enroll in courses as students
    def enroll_in_course(self, students_id, courses_id):
        student = self.students.get(students_id)
        course = next((c for c in self.courses if c.courses_id == courses_id), None)
        if student and course:
            if course in student.courses:
                print("Error: already enrolled in course")
            else:
                student.courses.append(course)
                student.balance += course.fee
                print("enrolled successfully!")

    def register_student(self, students_id, name, email):
        if students_id in self.students:
            print("Error: Student ID is already entered.")
        else:
            self.students[students_id] = Students(name, email, students_id)
            print("Student registered successfully!")

# Declared as function for student payment
    def calculate_payment(self, students_id):
        student = self.students.get(students_id)
        if student:
            print(f"Outstanding balance: ${student.balance}")
            try:
                amount = float(input("Enter payment amount: "))
                if amount < 0.4 * student.balance:
                    print("Error: Minimum payment is 40% of the balance.")
                else:
                    student.balance -= amount
                    print("Payment accepted.")
            except ValueError:
                print("Error: Please enter a valid amount.")
        else:
            print("Error: Student not found.")

 # Function to check balance
    def check_students_balance(self, students_id):
        student = self.students.get(students_id)
        if student:
            print(f"{student.name}'s current balance: ${student.balance}")
        else:
            print("Error: Student not found.")

# Function to show registered students
    def show_registered_students(self):
        for student in self.students.values():
            print(f"ID  {student.students_id}, Name  {student.name}, Email {student.email}")

# Function to show courses
    def show_courses(self):
         for course in self.courses:
                print(f"Name: {course.name}, ID: {course.courses_id}, Fee: ${course.fee}")

# Function to show students in courses
    def show_students_in_courses(self, courses_id):
        course = next((c for c in self.courses if c.courses_id == courses_id), None)
        if course:
            enrolled_students = [student.name for student in self.students.values() if course in student.courses]
            if enrolled_students:
                print(f"Students enrolled in {course.name}: {', '.join(enrolled_students)}")
            else:
                print(f"No students enrolled in {course.name}.")

# Main menu function
def main():
    system = RegistrationSystem()

    print("WELCOME")
    while True:
        print("\nMain Menu: ")
        print("1. Add Courses")
        print("2. Register Students")
        print("3. Enroll in Courses")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Courses")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            courses_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            try:
                fee = float(input("Enter course fee: "))
                system.add_course(name, courses_id, fee)
            except ValueError:
                print("Error: Please enter a valid fee amount.")
        elif choice == "2":
            students_id = input("Enter student ID #: ")
            name = input("Enter name for student: ")
            email = input("Enter the email of the student: ")
            system.register_student(students_id, name, email)
        elif choice == "3":
            students_id = input("Enter student ID #: ")
            courses_id = input("Enter course ID: ")
            system.enroll_in_course(students_id, courses_id)
        elif choice == "4":
            students_id = input("Enter the student ID #: ")
            system.calculate_payment(students_id)
        elif choice == "5":
            students_id = input("Enter the student ID #: ")
            system.check_students_balance(students_id)
        elif choice == "6":
            system.show_courses()
        elif choice == "7":
            system.show_registered_students()
        elif choice == "8":
            courses_id = input("Enter course ID#: ")
            system.show_students_in_courses(courses_id)
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Program run
if __name__ == "__main__":
    main()
