"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""


def find_max(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f"{n1} is largest")
    elif n2 > n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")

find_max(2,1,1)
find_max(-65,-45,-10)