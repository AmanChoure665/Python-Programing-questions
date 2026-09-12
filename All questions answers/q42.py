"""
Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""

def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b < c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

smallest = min_of_three(a,b,c)
print(f"{smallest} is the smallest number")