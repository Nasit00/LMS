from course import Course

class Course_list:
    def __init__(self):
        self.list = []

    def menu(self):
        while True:
            user = input("Enter 1 for addition, 2 for removal, 3 for search, or 'exit' to quit: ")

            if user == "1":
                self.add_course()

            elif user == "2":
                code = input("Enter the course code or name to remove: ")
                removed = self.remove_course(code)
                if removed:
                    print(f"Removed course with code/name '{code}'")
                else:
                    print(f"Course '{code}' not found.")

            elif user == "3":
                code = input("Enter the course code or name to search: ")
                result = self.search_course(code)
                print(result)

            elif user.lower() == "exit":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again.")

    def add_course(self):
        course = Course()  # This will prompt for input
        self.list.append(course)

    def remove_course(self, course_code):
        for course in self.list:
            if course.course_code == course_code or course.course_name == course_code:
                self.list.remove(course)
                return True
        return False  # Course not found

    def search_course(self, course_code):
        for course in self.list:
            if course.course_code == course_code or course.course_name == course_code:
                return f"Found: {course}"
        return "Not Found"

    def __str__(self):
        if not self.list:
            return "No courses in the list."

    # Header
        result = "+----------------+------------+\n"
        result += "| Course Name    | Course Code|\n"
        result += "+----------------+------------+\n"

    # Rows
        for course in self.list:
            result += f"| {course.course_name:<14} | {course.course_code:<10}|\n"

        result += "+----------------+------------+"
        return result


