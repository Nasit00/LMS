from course import Course
from course_list import Course_list
from student import Student
from student_list import StudentList
class app:
    def __init__(self):
        self.course_list = Course_list()
        self.student_list = StudentList()

    def main_menu(self):
        while True:
            user = input("Enter 1 for course management, 2 for student management, or 'exit' to quit: ")

            if user == "1":
                self.course_list.menu()

            elif user == "2":
                self.student_list.menu()

            elif user.lower() == "exit":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again.")
    
    def __str__(self):
        return f"Courses:\n{self.course_list}\n\nStudents:\n{self.student_list}"