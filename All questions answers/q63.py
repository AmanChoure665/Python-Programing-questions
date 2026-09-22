"""
Q63. Create a list containing the squares of numbers from
1 to 10 (i.e., [1, 4, 9, ..., 100]).
"""

def squares(n):
    new_lst = []

    for i in range(1,n+1):
        new_lst.append(i*i)

    return new_lst

print(squares(int(input("Enter a number: "))))