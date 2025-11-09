from person import Person
from course import Course
class Student(Person):

    def __init__(self):
        super().__init__()
        # Ask for input when object is created
        self.student_id = input("Enter student ID: ")
        self.course = Course()  # student linked with a Course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        if any(char.isdigit() for char in value): 
            raise ValueError("Name cannot contain numbers.")
        self._name = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Student ID must be a non-empty string.")
        self._student_id = value

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.student_id}"


# Example usage:
# a = Student()   # will ask for input
# print(a)
