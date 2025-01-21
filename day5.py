# Class is a blueprint for creating objects.
# class Email:
#     pass
# e1 = Email()
# e2 = Email()
# print(type(e1))
# print(type(e2))

#example
# class Employee:
#     def __init__(self, nm, ag):
#         self.name = nm
#         self.age = ag
#     def display(self):
#         print(self.name)

# e1 = Employee('raj', 21)
# e2 = Employee('jai', 22)

# Constructor helps for intializing an object of a class.
# This is an example of non parametrized constructor
# class Employee:
#     def __init__(self):
#         self.salary = 22000
#         self.age = 21

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

# Parameterized constructor
# class Employee:
#     def __init__(self, sal,ag,gender):
#         self.salary = sal
#         self.age = ag
#         self.gender = gender
# e1 = Employee(2000, 20, 'male')
# e2 = Employee(16000, 21, 'female')
# print(e2.__dict__)        

# # Default constructor
# class Employee:
#     pass
# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

## Acessing the attributes and methods
# class Employee:
#     def __init__(self,sal,age):
#         self.salary = sal
#         self.age = age
#     def display(self):
#         print(f"salary is {self.salary} and age is {self.age}")
# e1 = Employee(24000,21)
# e2 = Employee(38000, 27)
# # acessing the attributes
# print(e1.salary)
# e1.salary = 36000     # updating the attribute value
# print(e1.salary)
# # accessing the method
# e2.display()

## Built in functions
# class Employee:
#     def __init__(self,nm,ag):
#         self.name = nm
#         self.age =ag
# e1 =Employee('ruchika', 22)
# e2 =Employee('yug', 20)
# print(getattr(e1,'age')) # acessing the value
# setattr(e2,'name','chika')
# print(e2.__dict__)
# delattr(e2,'age')
# print(e2.__dict__)

# print(hasattr(e1,'name')) 
# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__module__)
# print(Employee.__bases__)
# print(Employee.__name__)

# isinstance() function
# class Demo:
#     pass
# d1 = Demo()
# class Employee:
#     '''This is employee class for maintaing the employee data'''
#     def __init__(self,nm,ag):
#         self.name = nm
#         self.age =ag
#         def display(self):
#             print(f"name is :{self.name} and age is {self.age}")
# e1 = Employee('tushu', 26)
# e2 = Employee('chika', 20)
# obj = d1
# classname = Employee
# print(isinstance(d1, Employee))
# if isinstance(obj,classname):
#     pass

#instance methods are consists of getter and setter methods
# class Employee:
#     def setName(self,nm):
#         self.Name = nm
#     def getName(self):
#             print("The name is:", self.Name)
# e1 = Employee()
# e2 = Employee()
# e1.setName(input("Enter the name:"))
# e2.setName(input("Enter the name:"))
# print("e1 object is:", e1.__dict__)
# print("e2 object is:", e2.__dict__)
# e1.getName()
# e2.getName()

#Inheritance - in this , child class inheretide the properties of the parent class.
class Person:    #parent class
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear = year
 #   Person.__init__(self,fname,lname)
# y = Student("MIKe", "Yug", 2024)
# y.printname()
  def welcome(self):
       print(f"welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}!")
x = Person("MIKe", "Yug")
x.printname()
# creating a student object
y= Student("MIKe", "Yug", 2024)
y.printname()
y.welcome()

#Iterator is an object that contains countable number of values . List, tuples, dictionary and sets are iterable objects.
# WAP to return an iterator from tuple and print each value:
# mytuple = ("strawbeery", "mango", "Cherry")
# myit =iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# WAP to Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


