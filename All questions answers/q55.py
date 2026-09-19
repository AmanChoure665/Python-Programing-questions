"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get the count of elements, but avoid using
sum() for the total.
"""



def average(nums):
    n = len(nums)
    total = 0
    for i in nums:
        total += i
    return total/n

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]
avg = average(nums)

print(f"Average is = {avg:.3f}")