"""
Q58. Find the largest and smallest number in a list without using built-in functions
like max() or min().
"""

nums = [-6, -5, -4, -12, -10, -91, -75, -49, -9]

maxi = float("-inf")

for i in nums:
    if i > maxi:
        maxi = i

print(f"largest element = {maxi}")