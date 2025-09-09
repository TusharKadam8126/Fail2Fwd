class Employee:
    def __init__(self,name):
        self.name = name
        print("Employee Name is :" + self.name)
class Engineer(Employee):
    def develop(self):
        print(f"{self.name} is developing application.")
class Designer(Engineer):
    def design(self):
        print(f"{self.name} is designing a application.")
obj = Designer("GOJO")
obj.develop()
obj.design()
