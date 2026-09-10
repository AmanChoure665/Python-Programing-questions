"""
Q21.
*
* *
* * *
* * * *
* * * * *
"""

num1 = int(input())

for i in range(1,num1+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()