"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

num1 = int(input())
num2 = int(input())

if num1>num2:
    print(num1,"is greater")
elif num1<num2:
    print(num2,"is greater")
else:
    print("Both are equal")