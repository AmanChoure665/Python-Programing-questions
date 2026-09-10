"""
Q22.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

num1 = int(input())

for i in range(1,num1+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()