"""
Q28.
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

num = int(input())
for i in range(num,0,-1):
    for j in range(num,i-1,-1):
        print(j,end=" ")
    print()
for i in range(2,num+1):
    for j in range(num,i-1,-1):
        print(j,end=" ")
    print()

