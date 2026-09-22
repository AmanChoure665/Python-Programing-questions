"""
Q68. Create a 3x3 matrix (a nested list) and then use nested loops to calculate
and print the sum of all its elements.
"""

# create a 3x3 matrix as a nested list

# use a variable to store the running sum, starting at 0

# use nested loops: outer loop for rows, inner loop for elements in each row

# add each element to the sum inside the inner loop

# print the final sum
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def matrix_sum(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

    rows = len(matrix)
    columns = len(matrix[0])
    total = 0
    for i in range(0,rows):
        for j in range(0,columns):
            total += matrix[i][j]
    return total

print(matrix_sum(matrix), end=" ")

    