"""
Write a function that print all the factors of a number entered by user.
"""


def factors():
    n = int(input("Enter an number: "))
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
   

factors()