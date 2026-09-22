"""
Q66. Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
"""
n = int(input(("Enter a number: ")))
squares = [i*i for i in range(0,n+1) if i%2 != 0]
print(squares)