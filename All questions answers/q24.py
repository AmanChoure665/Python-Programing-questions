"""
Q24.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

num = int(input())
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()