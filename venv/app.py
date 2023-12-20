print("Hello World")
#TUTORIAL FOR LEARN

'''
Print Statement
print("Hi Sachin Mudannayaka");
print("|    /")
print("|   /")
print("|  /")
print("| /")
print("|/")
'''

# Variable Declarations
'''
character_name="John"
print("His name is "+character_name+".")
age= 24
print("His name is "+character_name+".Age is "+str(age)+".")
'''

#String Handling
'''
print("Sachin Mudannayaka")
print("Sachin\nMudannayaka")
print("Sachin\" Mudannayaka")
name="Sachin Mudannayaka"
school="BANDARANAYAKE COLLEGE"
print(name+" "+school)
print(school.lower())
print(school.lower().islower())
print(len(school))
print(school[21-1])
print(school.index("D"))
print(school.replace(school[3],"S"))
'''

#Working with Numbers
'''
print(3.4)
print(5+4.6)
print(10*4)
print(10%3)
my_num=10
print(str(my_num))
print(abs(my_num))
'''

# from math import *
'''
print(sqrt(3.7))
'''

# Input from users
'''
name=input("ENTER YOUR NAME")
print("Hi "+name)
'''

#Create a basic Calculator
'''
num1= input("Enter the Number1: ")
num2= input("Enter the Number2: ")
result= float(num1)+float(num2)
print("Answer "+ str (result))
'''

#matLib Game
'''
color=input("Enter the color: ")
place=input("Enter the place: ")
celebrity=input("Enter the Celebrity: ")
print("Roses are "+color)
print(place+" is Blue")
print("I Love "+celebrity)
'''

#Lists
'''
friends=["Jim","Keren","Tom"]
print(friends[2][2])
'''

#List of function
'''
luky_numbers=[234,2,4,8,16,32]
friends=["Sachin","Vimukthi","Malshan","Mudannayaka","Hiranya"]
friends.extend(luky_numbers)
friends.append("Bhagya")
friends.insert(2,"Kelly")
friends.remove("Sachin")
friends.remove(2)
# friends.clear()
friends.pop()
luky_numbers.sort()
print(friends)
friends2=friends.copy()
print(friends2)
print(luky_numbers)
'''

#Tuples (Basic Data structure and containter for storing different types of values very similar to list)
'''
coordinates=[(4,5),(5,6),(89,56)]
print(coordinates[2][1])
'''

#functions(it is a collection of codes which perform a specific task)
'''
def say_hi():
     print("Say Hi")
say_hi()

def say_hi(name):
    print("Hi "+name)
say_hi("Sachin")
say_hi("Vimu")
say_hi("Nuwan")

def cube(num):
    result= str(num*num*num)
    return("CUBE : "+ result)

print(cube(11))
'''

#if statement
'''
is_tall=True
or is_tall: #and #not
gender_checker=input("Enter your gender: ")
if gender_checker=="Male":
    print("He is a male")
elif gender_checker=="Female":
    print("She is a female")
else:
    print('Gender is not identified')
'''

#Comparison operations
'''
def max_num(num1,num2,num3):
    if(num1>=num2) and (num1>=num3):
        print("Number one is the max number")
    elif (num2>=num1) and (num2>=num3):
        print("Number two is the max number")
    else:
        print("Number three is the max number")

max_num(10,1012,2)
'''

#Building a better calculator
'''
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
arithmetic_operator=input("Enter the arithmetic operator: ")
if(arithmetic_operator=="+"):
    answer=int(num1)+int(num2)
    print("The sum is "+ str(answer))
elif(arithmetic_operator=="-"):
    answer=int(num1)-int(num2)
    print("The substraction is "+ str(answer))

elif (arithmetic_operator == "*"):
        answer = int(num1) * int(num2)
        print("The multipication is " + str(answer))
elif(arithmetic_operator=="/"):
    answer=int(num1)/int(num2)
    print("The divide is "+ str(answer))
else:
    print("Your input is not identified")
'''

#Dictionaries
'''
monthConversions={
   "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}
print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Luv","Not a valid key"))
'''

#Using numbers
'''
weekDays={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    "weekendDays":"Saturday and Sunday"
}
print(weekDays.get("weekendDays"))
'''

#While Loop
'''
i=0
while i<=5:
    print(i)
    i+=1
'''

#Building a guessing game
'''
secret_word="Sachin"
guessing_word=""

guessing_time=0

while(guessing_time<=2):
    guessing_word=input("Enter the secret word: ")
    if guessing_word==secret_word:
        print("Successfully Entered the secret word")
        exit()
    else:
        print("Try again")
        print("You have "+ str(2-guessing_time) +" more")
    guessing_time+=1

print("You cannot attempt again")
'''

#For Loop
'''
for letter in "Sachin Mudannayaka":
    print(letter)

friends=["Sachin","Mudannayaka","Viran","Ranagajeewa","Anura"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index+1)

for index in range(2,7):
    print(index)

friends=["Sachin","Mudannayaka","Viran","Ranagajeewa","Anura"]
for index in range(len(friends)):
    print(friends[index] +" "+ str(index+1))
'''

#Exponent Function
'''
def rise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    print("Result : "+ str(result))
rise_to_power(2,10)
'''

#two D lists and nested Arrays
'''
number_grid=[
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]
print(number_grid)
print(number_grid[1][2])

for row in range(len(number_grid)):
    for col in range(len(number_grid[row])):
        print(number_grid[row][col])
'''


#Builiding a translator
'''
def translate(pharse):
    translation=""
    for letter in pharse:
            if letter.lower() in "aeiou":
                if letter.isupper():
                    translation=translation+"G"
                else:
                    translation=translation+"g"
            else:
                translation=translation+letter
    return translation
print(translate(input("Input a Letter: ")))
'''

#Comments
'''
Hi Sachin Mudannayaka... How are U?
'''
# print("Comments are fun Right?")

#Try Except
''''
try:
    number= int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")'''

'''
try:
    # 10/0
    number=int(input("Enter the number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Value is not matched")

'''
#
'''
try:
      10/0
    # number=int(input("Enter the number: "))
    # print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Value is not matched")
'''

#Reading files
'''
emp_file=open("employee.txt","r")
print(emp_file.readable())
# print(emp_file.readline())
# print(emp_file.readlines())
for employee in emp_file.readlines():
    print(employee)
emp_file.close()
'''

#Writing files append
'''
# emp_file=open("employee.txt","a")
# emp_file.write("\nKelly - Customer Service ")
'''


#Writing files
'''
emp_file=open("employee.txt","w")# can create a new file(with different extention) changing file name of this line
emp_file.write("\nKelly - Customer Service ")
'''

#Modules and pip
'''
import useful_tools
print(useful_tools.feet_in_miles)
print(useful_tools.roll_dice(10))
'''

#Classes and Objects
'''
from student import Student
stu1=Student("Sachin","IT",2.89,False)
print(stu1)
print(stu1.name)
'''

#Create a multiple choices Quiz
'''
from question import Question
questions_prompt=[
    "(1) What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "(2) What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "(3) What color are Strawberry?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions=[
    Question(questions_prompt[0],"a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+ " correct")
run_test(questions)
'''

#Object Functions
'''
from student import Student
stu1=Student("Sachin","IT",3.4,False)
stu2=Student("Vimu","SE",2.7,True)
print(stu1.on_honor_roll())
print(stu2.on_honor_roll())
'''

#Inheritance
'''
from Chef import Chef
from ChineeseChef import ChineeseChef
myChef= Chef()
myChinesChef=ChineeseChef()
myChef.make_chicken()
myChinesChef.makes_firedRice()
myChinesChef.make_chicken()
myChinesChef.make_special_dish()
'''
