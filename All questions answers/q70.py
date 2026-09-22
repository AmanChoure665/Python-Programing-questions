"""
Q70. Given a 3x3 matrix, print its upper triangle.
Replace all elements in the lower triangle (below the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

Expected Output:
1  2  3
*  5  6
*  *  9
"""

matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 1],
    [7, 8, 9, 7],
    [9, 7, 3, 1],
]


def lower_triangle(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    for i in range(0,rows):
        for j in range(0,col):
            if i>j:
                print("*",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print()

lower_triangle(matrix)