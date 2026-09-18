"""
Write a program that takes a list and a target number. Use a loop to determine if
the target number exists in the list. Do not use the in operator.
"""

def target_exist(list,target):
    for i in list:
        if i == target:
            return True
    return False

target = int(input())

list = [6, -5, 4, 2, 10, 91, -75, 49, 9]

print(target_exist(list,target))