'''Create a tuple of 5 subjects marks. 
Print the first, last, and middile one using indexing'''

marks = (45, 32, 11, 55, 98)
n = len(marks)


print(f"first = {marks[0]}")
print(f"middle = {marks[(int(n//2))]}")
print(f"last = {marks[n-1]}")