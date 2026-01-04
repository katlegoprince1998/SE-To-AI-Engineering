class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} I am a student with ID: {self.student_id}."
    
class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} I teach {self.subject}."
    
# Example usage:
student = Student("Alice", 20, "S12345")
teacher = Teacher("Mr. Smith", 40, "Mathematics")

print(student.introduce())
print(teacher.introduce())

# Output:
# Hello, my name is Alice and I am 20 years old. I am a student with ID: S12345.
# Hello, my name is Mr. Smith and I am 40 years old. I teach Mathematics.
