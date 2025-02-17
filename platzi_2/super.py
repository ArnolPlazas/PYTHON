class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
            print(f'Hello, my name is {self.name}')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greeting(self):
        super().greeting()
        print(f'I am student with ID {self.student_id}')

student = Student('John', 25, '1234')
student.greeting()