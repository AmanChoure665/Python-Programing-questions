"""
Q59. Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

def rev_lst(nums):
    new_lst = []
    n = len(nums)
    for i in range(n,0,-1):
        new_lst.append(nums[i-1])

    return new_lst


nums = [-6, -5, -4, -12, -10, -91, -75, -49, -9]

print(f"Reversed list = {rev_lst(nums)}")