#nested lambda function
def outer():
    add = lambda num1, num2: num1 +num2
    return add
add = outer()
print(add(3,4))

# First class fuunctions  provides various features assign func to variable, passing func as arguments, returning func from another function and storing func in DS

# assigning function to variables
def msg(name):
    return f"Hello,{name}!"
f = msg    # assigning function to a variable
print(f("Ruchika"))   #calling the function using the variable

#Passing functions as arguments
def msg(name):
    return f"Hello, {name}!"
def fun1(fun2,name):
    return fun2(name)
print(fun1(msg,"Tushar"))  #passing the greet func as an argument

#Returning func from another func
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())

#Storing function in data structures
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))

#high order function take func as a parameter and return function as an output
# Python program to illustrate functions 
# Functions can return another function 
  
def create_adder(x): 
    def adder(y): 
        return x + y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))

# There are three built in high order functions are there= map(), reduce() and filter()
# data = [23, 22,84,69,24,32]
# def even(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
# filtered_object = filter(even,data)
# print(type(filtered_object))
# print(list(filtered_object))
# WAP to filter the vowels from given string
str1 = "Riya"

def vow(ch):
    vowels = ['a','e','i', 'o','u']
    if ch in vowels:
        return ch
    

filtered_obj = filter(vow, str1)
print(list(filtered_obj))

# Map() is also an high order built in function that perform operations on iterables and map an object
# example double of n
# numbers = [5,6,7,8,9]
# def double(numbers):
#     return numbers*2
# mapped_object = map(double, numbers)
# print(list(mapped_object))
# print(type(mapped_object))

#Reduce function is defined in functool module and returned single reduced value
#example sum of all numbers
# import functools
# nums =[5,8,2,10,9]
# print(functools.reduce(lambda a,b:a+b, nums))

#second example of reduce()
import functools
nums =[5,8,2,10,9]
def max1(a,b):
    if a>b:
        return a
    else:
         return b
print(functools.reduce(max1, nums))

#Chaining of decorators
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())

#File Handling
age = input('Enter your age:')
f = open("hii.txt",'r')
content = f.read()
f.write(age)
f.close()