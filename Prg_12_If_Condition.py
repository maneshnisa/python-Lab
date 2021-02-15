
#Python If-else statements
#The if statement
#PRG-1
print("PGM 1")
num = int(input("enter the number ")) 
if num%2 == 0:  
    print("Number is even")
print('\n')

#Another Example
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
if b > a:
    print("b is greater than a")
print('\n')

#PRG-2
#if-else statement
print("PGM 2")
age = int(input("Enter your age? "))  
if age >= 18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");
print('\n')

#PRG-3


#Program to check whether a number is even or not.
print("PGM 3")
num = int(input("enter the number?"))  
if num%2 == 0:  
    print("Number is even...")  
else:  
    print("Number is odd...")  

print('\n')


#PRG-4
#elif statement
#if the previous conditions were not true, then try this condition
print("PGM 4")
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif b < a:
    print("b is less than a")
print('\n')

#another example
print("PGM 4.1")
number = int(input("Enter the number?"))  
if number <= 10:  
    print("number is less than or equal to 10")  
elif number > 10 and number < 50:  
    print("number is between 10 and 50");  
elif number > 50 and number < 100:  
    print("number is between 50 and 100");  
else:  
    print("Number is greater than 100");  
print('\n')

#another example
print("PGM 4.2")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print('\n')


#PRG-5
print("PGM 5")
marks = int(input("Enter the marks? "))  
if marks > 85 and marks <= 100:  
    print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
    print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
    print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
    print("You scored grade C ...")  
else:  
    print("Sorry you are fail ?")  
print('\n')

#Short Hand If
#One line if statement
#PRG-6
print("PGM 6")
a = 40
b = 10
if a > b: print("a is greater than b")
print('\n')

#One line if else statement
print("PGM 6.1")
a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions
print("PGM 6.2")
a = int(input("The value of a "))
b = int(input("The value of b "))
print("A") if a > b else print("=") if a == b else print("B")


#Nested If
#PRG-7
print("PGM 7")
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



    
    
