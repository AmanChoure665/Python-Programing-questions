"""
Write a program that takes a list of numbers and, using a loop, determines
whether it is sorted in ascending order. Print True if it is sorted,
and False otherwise.
"""

def check_asc_ord(lst):
    n = len(lst)
    for i in range(0,(n-1)):
        if lst[i]>lst[i+1]:
            return False
            
    return True

nums1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(check_asc_ord(nums2))
