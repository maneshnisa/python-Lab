#range() Function
#To loop through a set of code a specified number of times,
#we can use the range() function,
#The range() function returns a sequence of numbers,
#starting from 0 by default, and increments by 1 (by default),
#and ends at a specified number.

#PRG-1
for x in range(6):
  print(x)
print('\n')

#PRG-2
#Using the start parameter:
for x in range(2, 6):
  print(x)

print('\n')

#PRG-3
#it is possible to specify the increment value by adding a third parameter
#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

print('\n')

#PRG-4
# range() 
print(range(10))

print(list(range(10)))

print(tuple(range(2, 8)))

print(list(range(2, 20, 3)))
print('\n')

#PRG-5
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
print('\n')

#PRG-6
# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')

# PRG-7
# Program to print the sum of all multiples of either 3 or 5 within a range of 100

total = 0
#print(list(range(100)))
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
