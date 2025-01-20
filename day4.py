# #Functions is used for reducing redundancy in code
# def cal_sum(a,b):
#     return a+b

# sum = cal_sum(4,6)
# print(sum)

# def my_function():
#     print("Hello from a function")

# my_function()

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# #Arbitrary Arguments, *args is used basically when we don't known the number of arguments that we can simply add * before the parameter name
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def myfunction_(child3, child2, child1):
#   print("The youngest child is" + child3)

# myfunction_(child1 = "Emil", child2 = "Ruchika", child3 = "Yug")

# #Default parameter value
# def my_function(country = "Norway"):
#   print("I am from" + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# #Returning vakues after the functions
# def my_function(x):
#   return 5 * x
# print(my_function(4))
# print(my_function(8))

#Recursion function - when function calls itself repeatedly
#eg WAP to print 5,4,3,2,1
# def show(n):
#   if(n==0):
#     return
#   print(n)
#   show(n-1)

# show(5)

  #WAP to calculate the factorial n!
# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   return fact(n-1)*n
# print(fact(4))

#WAP of recursive function to calculate the sum of first n natural numbers
# def cal_sum(n):
#   if (n== 0):
#     return 0
#   return cal_sum(n-1)+n

# cal_sum(10)
# print(cal_sum(10))

# WAP  recursive func to print all element in a list
def print_list(li, idx=0):
  if(idx == len(li)):
    return 
  print(len(li))
  print_list(li, idx +1)



fruits =["mango","strawberry", "apple"]
print_list(fruits)
print(fruits)