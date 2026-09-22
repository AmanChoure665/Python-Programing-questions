"""
Q64. Given a list of numbers (which may contain duplicates), write a Python script
that takes an integer as input from the user and removes all occurrences of that
integer from the list.
"""

def remove_duplicates(target, lst):

    # new_lst = []
    # for i in lst:
    #     if i != n:
    #         new_lst.append(i)
        
    # return new_lst

    while target in lst:
        lst.remove(target)
    return lst

nums = [2, 5, 5, 5, 7, 7, 8, 5, 6, 4, 5]
target = int(input("Enter a number: "))

print(remove_duplicates(target,nums))