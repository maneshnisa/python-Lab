a = 20
b = 29
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print('\n')
#
a = int(input("The value of a "))
b = int(input("The value of b "))
print("A") if a > b else print("=") if a == b else print("B")
