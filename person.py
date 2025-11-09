class Person:
    def __init__(self):
        self.name = (input("Enter student name: "))
    def __str__(self):
        return f"Name:{self.name}"