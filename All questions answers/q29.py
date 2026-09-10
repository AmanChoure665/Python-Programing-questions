"""
Q29.
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""
n = int(input())

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(i*2-1)+1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(i*2-1)+1):
        print(j,end=" ")
    print()