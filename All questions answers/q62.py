"""
Q62. Separate a list of integers into two distinct lists: one containing all the
even numbers and the other containing all the odd numbers.
"""

def list_separater(lst):
    even_lst = []
    odd_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    print(f"Even list = {even_lst}")
    print(f"odd list = {odd_lst}")

nums = [2, 5, 6, 7, 8, 5, 6, 4, 5]
list_separater(nums)