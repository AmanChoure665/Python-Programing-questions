"""
Q65. Write a Python script that iterates through a list of integers and replaces every
negative number found in the list with the value 0.
"""

def replace_num(lst): 
    n = len(lst)
    for i in range(0,n):
        if lst[i] < 0:
            lst[i] = 0
    return lst

nums = [-6, 5, 4, -12, 10, -91, 75, -49, -9]
print(replace_num(nums))