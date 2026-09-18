"""
Given a list of numbers, write Python code using a loop to find and print the
largest element. Do not use the built-in max() function.
"""

nums = [-6, -5, -4, -12, -10, -91, -75, -49, -9]

lar = []
maxi = float("-inf")
for i in nums:
    if i > maxi:
        maxi = i
print(f"Largest element = {maxi}")