"""
Write a function called absolute_value that takes a number and returns
its absolute value without using the built-in abs() function.
"""


def absolute_value(num):
    if num >= 0:
        return num
    return num * -1

num = int(input("Enter a number: "))
val = absolute_value(num)
print(f"{val} is the absolute value of {num}")