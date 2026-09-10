"""
Write a function that ask a number from user and prints if that
number is odd or even.
"""
def check():
    n = int(input("Enter an number: "))
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

check()