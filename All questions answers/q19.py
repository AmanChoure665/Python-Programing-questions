"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num1 = int(input())

i = 1
b = 0

while i <= num1:
    if num1%i == 0:
        b += 1
    
    i += 1
print("Total factors =",b)