"""
Q67. Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""

marks = [45, 55, 66, 76, 86, 97, 94, 85]
print(marks, id(marks))

new_lst = [i for i in marks if i > 75]
print(new_lst, id(new_lst))