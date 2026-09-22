'''Create a tuple of 8 numbers. 
using slicing, Print the first 3, last 3, and every alternate element'''

marks = (45, 32, 11, 55, 98, 34, 87, 74)

print(f"first 3 = {marks[0:3]}")

n = len(marks)
print(f"last 3 = {marks[-3:n]}")

print(f"every alternate = {marks[::2]}")