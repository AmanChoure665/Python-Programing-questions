'''Take 5 number as input from the user, store them in a tuple, 
and print the tuple along with it's minimum and maximum.'''


def users_tupl():
    a = []
    for i in range(1,6):
        n = int(input())
        a.append(n)
    nums = tuple(a)
    print(f"Numbers = {nums}")


    # for maximum 
    maxi = nums[0]
    for i in nums:
        if i > maxi:
            maxi = i
    print(f"Maximum = {maxi}")

    # for minimum
    mini= nums[0]
    for i in nums:
        if i < mini:
            mini = i
    print(f"Minimum = {mini}")

users_tupl()