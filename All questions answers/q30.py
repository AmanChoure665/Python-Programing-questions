"""
Q30.
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
n = int(input())

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(i*2-1)+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(i*2-1)+1):
        print("*",end=" ")
    print()