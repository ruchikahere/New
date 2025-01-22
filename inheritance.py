# constructo in multi level inheritance
class Human_being(object):
    def __init__(self):
        print("Human being constructor called")
        self.name = input ("Enter your name:")

class Employee(Human_being):
    def __init__(self):
        print("Employee constructor called")
        self.salary = float(input("Enter your salary"))
class Manager(Employee):
    def __init__(self):
        print("Managers constructor called")
        self.bonus = float(input("Enter your bonus:"))

m1 = Manager()
print(m1.bonus) 