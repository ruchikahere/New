#Using the Python while statement to build a simple command prompt program
command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")

#WAP to find a x=36 in the given tuple.
nums= (1,4,24,67,36,84,90,18)
x=36
i=0
while i<= len(nums):
    if (nums[i]== x):
     print ("Found at indx", i)
     break
    i+=1

#Break keyword is used for terminating the loop when it is countered
i=1
while i<= 8:
    print(i)
    if (i== 5):
       break
    i += 1
    print ("Ending of loop")

#Another example
print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color:')
    if color.lower() == 'quit':
        break

#Continue statement is used for skipping the current iterations and move on to next one.
j=0
while j < 10:
    j = j + 1
    if (j%2==0):
        continue
    print(j)

# For loop - is used for sequential traversiong order
list = [1, 2,3,4,5,6,7,8,9,10]
for values in list:
    print(values)

tup = (1,3,6,9)
for num in tup:
    print(num)

str = "Ruchika Sharma"
for char in str:
    print(char)

# for loop with else
str = "this is a string"
for char in str:
    if (char== "s"):
     print("s found")
     break
    print(char)

    print("End ")

#Range (start,stop,step)- starting value bydefault 0 hoti h , increment step by default 1 s hota h )
for i in range (2,100, 2):
    print (i) 

for j in range(100, 0, -1):
    print (j)

for index in range(0, 10):
    print(index)
    if index == 3:
        break


for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")

for index in range(10):
    if index % 2:
        continue

    print(index)

#WAP to find the sum of first n numbers.
n = 8
sum=0
for i in range(1,n+1):
    sum +=i

    print ("total sum=", sum)

#WAP for finding the factorial of 5
num = int (input("Enter the number:"))
fact =1
for i in range(1, num +1):
    fact *= i
    print ("factorial=", fact)

#exception handling
num1 = int(input("Enter first number:"))
num2 = int(input("Enter the second number:"))
try: 
    div = num1/num2
    print (div)
except (ZeroDivisionError, NameError) as obj:
    print("divisior by zero is not possible")
print("rest of code")

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2


def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'


def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print(error)
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

main()
