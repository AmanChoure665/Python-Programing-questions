"""
Q72. Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).

1  2 3
4  5 6
7  8 9

Expected Output:
*  * 3
*  5 *
7  * *
"""

matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 1],
    [7, 8, 9, 7],
    [9, 7, 3, 1],
]


def anti_diagonal(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    for i in range(0,rows):
        for j in range(0,col):
            if i+j==3:
                print(matrix[i][j],end=" ")
            else:
                print("*",end=" ")
        print()

anti_diagonal(matrix)