class Employee:
    # name = "Tahmid"
    # occupation = "Software Engineer" 

    def __init__(self,name,occupation,center):
        self.name = name
        self.occupation = occupation
        self.center = center

    def printObject(self):
        print(f"The name is {self.name}")
        print(f"Occupation is {self.occupation}")
        print(f"The center is {self.center}")

    @staticmethod
    def greet():
        print("Good")


Tahmid = Employee("Tahmid","Software Engineer","Dhaka")
# Sth = Employee()
# print(Tahmid.name)
# print(Tahmid.occupation)
Tahmid.printObject()
# Employee.printObject(Sth)
Employee.greet()
Tahmid.greet()