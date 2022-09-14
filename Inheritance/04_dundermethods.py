class Employee:

    def __init__(self,a):
        self.a = a

    def __add__(self, obj):
        return self.a + obj.a

a = Employee(450)
b = Employee(585)

print(a + b)