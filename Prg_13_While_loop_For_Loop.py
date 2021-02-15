#The while Loop
#With the while loop we can execute a set of statements 
#as long as a condition is true
#PRG-1
#Print i as long as i is less than 6:
print("PGM 1")
i = 1
while i < 6:
  print(i)
  i += 1 # i = i + 1
print('\n')
# Same output as of before using for loop
j = 1
for j in range(1,6):
  print(j)
  j += 1
print('\n')

#PRG-2
#The break Statement
#With the break statement we can stop the loop even if the while
#condition is true:
print("PGM 2")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print('\n')


#The continue Statement
#With the continue statement we can stop the current iteration,
#and continue with the next
#PRG-3
print("PGM 3")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print('\n')

#PRG-4
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
print("PGM 4")

n = int(input("Enter n: "))
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum += i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
print('\n')


#PRG-5
#While loop with else
print("PGM 5")
'''Example to illustrate the use of else statement with the while loop'''

counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
print('\n')


# For Loops
#A for loop is used for iterating over a sequence
#(that is either a list, a tuple, a dictionary, a set, or a string).
#PRG-6
#Print each fruit in a fruit list:
print("PGM 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('\n')

#Loop through the letters in the word "banana":
#PRG-7
print("PGM 7")
for x in "banana":
  print(x)
print('\n')

#PRG-8
#Exit the loop when x is "banana":
print("PGM 8")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print('\n')

#Do not print banana:
#PRG-9
print("PGM 9")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print('\n')




