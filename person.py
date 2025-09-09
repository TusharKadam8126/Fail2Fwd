class Person:
    def __init__(self, name):
        self.name = name
        print("Student name is :" + self.name)
class Student(Person):
    def __init__(self, rollnumber):
        self.rollnumber = rollnumber
        print(f"Student rollnumber is : {self.rollnumber}")
class Teacher(Student):
    def __init__(self,subject):
        self.subject = subject
        print("Subject name is :" + self.subject)
class TeachingAssistant(Student,Teacher):
    def __init__(self, name, rollnumber, subject):
        self.name = name
        self.rollnumber = rollnumber
        self.subject = subject
        print("Student name is :" + self.name)
        print("Roll number is :" + self.rollnumber)
        print("Subject name is :" + self.subject)
obj = TeachingAssistant("Tushar",36,"Maths")
obj.name
obj.rollnumber
obj.subject

