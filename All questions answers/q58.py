"""
Q58. Find the largest and smallest number in a list without using built-in functions
like max() or min().
"""

def lar_num(nums):
    maxi = float("-inf")
    for i in nums:
        if i > maxi:
            maxi = i
    return f"Largest element = {maxi}"

def small_num(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return f"Smallest element = {min}"



nums = [-6, -5, -4, -12, -10, -91, -75, -49, -9]

print(lar_num(nums))
print(small_num(nums))