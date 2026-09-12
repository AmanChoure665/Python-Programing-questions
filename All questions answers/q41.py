"""
Write a function called square that takes a number and returns its square.
Store the result and print it.
"""

def square(n):
    return n ** 2

n = int(input("Enter a number: "))
sqr = square(n)

print(f"{sqr} is the square of {n}")