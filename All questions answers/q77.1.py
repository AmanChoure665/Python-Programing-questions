'''Write a function get_stats(nums) that takes 
a tuple of numbers and return a tuple containing
the sum, average, minimum, Unpack the returned 
tuple and print each value.'''


def get_stats(nums):

    # for sum
    sum = 0
    for i in nums:
        sum += i

    # for average
    average = 0
    n = len(nums)
    average = sum/n

    # for mimimum
    minimum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i

    return sum, average, minimum




my_tuple = (45, 32, 11, 5, 98, 69, 77, 77)
print(my_tuple)
summ, avg, mini = get_stats(my_tuple)

print(f"Sum of numbers = {summ}")
print(f"Average of numbers = {avg:.2f}")
print(f"Minimum of numbers = {mini}")