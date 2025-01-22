# Decorator is a function that takes another function as an argument and returns a new function  by modifying the behavior of functions.
def decorator(func):

    def wrapper():
        print("Before calling the function:")
        func()
        print("After calling tthe function.")
    return wrapper
# applying decorator to function
@decorator

def greet():
    print("Hello World!")

greet()

# Higher-Order Functions are functions that take one or more functions as arguments and return a functions as a result .
def fun(f,x):
    return f(x)
#another function bnaya 
def square(x):
    return x*x
# abh dono function ka result nikaldenge upr wale function ko combine krk
res = fun(square,5)
print(res)



#Functions as First-class objects
def greet(n):
    return f"Hello, {n}!"
say_hi = greet 
print(say_hi("Ruchika"))
# passing a function as an argument
def apply(f,v):
    return f(v)
res = apply(say_hi, "Tushar")
print(res)
def make_mult(f):
    def mult(x):
        return x* f
    return mult
dbl = make_mult(2)
print(dbl(5))

# Method decorator which used decorate methods within a class
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("after method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# Class decorator
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)

# @staticmethod 
class calculator:

    def add(self,a,b):
        return a+b
    
    @staticmethod
    def info():
        print("This is info class")

cal = calculator()
print(cal.add(10, 40))

cal.info()

# class method can access and modif the class state
class Employee:
    raise_aamount = 1.05

    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
Employee.set_raise_amount(8.09)
print(Employee.raise_amount)

# Generators is a special type of function that returns an iterator object and for returning the value we use the keyword yield
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

#example
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)

# # File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing of file
# file = open("C:\Users\Ruchika\Videos\Captures", "r")
# content = file.read()
# print(content)
# file.close()