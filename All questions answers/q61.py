"""
Q61. Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""


def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
        else:
            lst.remove(i)

    return new_lst

nums = [2, 5, 6, 7, 8, 5, 6, 4, 5]

print(remove_duplicates(nums))