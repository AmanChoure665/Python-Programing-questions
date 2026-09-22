"""
Q60. Given two lists, merge them into a single new list without modifying the originals.
"""

def merge_two_lists(lst1, lst2):
   new_lst = []

   for i in lst1:
    new_lst.append(i)
   for i in lst2:
    new_lst.append(i)
   return new_lst


nums1 = [-6, -5, -4, -12, -10, -91, -75, -49, -9]
nums2 = [2, 5, 6, 7, 8, 5, 6, 4, 5]

print(merge_two_lists(nums1,nums2))