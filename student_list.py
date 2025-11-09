from unittest import result
from student import Student

class StudentList:
    def __init__(self):
        self.list = []

    def menu(self):
        while True:
            user = input("Enter 1 for addition, 2 for removal, 3 for search, or 'exit' to quit: ")

            if user == "1":
                self.add_student()

            elif user == "2":
                name = input("Enter the name or ID of the student to remove: ")
                removed = self.remove_student(name)
                if removed:
                    print(f"Removed {name}")
                else:
                    print(f"Student '{name}' not found.")
            
            elif user == "3":
                name = input("Enter the name or ID of the student to search: ")
                result = self.search_student(name)
                print(result)

            elif user.lower() == "exit":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again.")

    def add_student(self):
        student = Student()  # This will prompt for input
        self.list.append(student)

    def remove_student(self, name):
        for student in self.list:
            if student.name == name or student.student_id == name:
                self.list.remove(student)
                return True
        return False  # Student not found
    
    def search_student(self, name):
        for student in self.list:
            if student.name == name or student.student_id == name:
                return f"Found: {student}"
        return "Not Found"

    def __str__(self):
        if not self.list:
            return "No students in the list."

        # Header
        result = "+----------------+------------+----------------+------------+\n"
        result += "| Student Name   | Student ID | Course Name    | Course Code|\n"
        result += "+----------------+------------+----------------+------------+\n"

        # Rows
        for student in self.list:
            result += f"| {student.name:<14} | {student.student_id:<10} | {student.course.course_name:<14} | {student.course.course_code:<10}|\n"

        result += "+----------------+------------+----------------+------------+"
        return result



