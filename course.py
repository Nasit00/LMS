class Course:
    def __init__(self):
        self.course_name = input("Enter course name: ")
        self.course_code = input("Enter course code: ")

    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Course name must be a non-empty string.")
        self._course_name = value
    @property
    def course_code(self):
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Course code must be a non-empty string.")
        self._course_code = value
    def __str__(self):
        return f"Course Name: {self.course_name}, Course Code: {self.course_code}"