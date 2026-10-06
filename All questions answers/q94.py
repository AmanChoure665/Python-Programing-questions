"""
Q94. Reverse a String

Accept a string as input. Print its reverse using string slicing.
"""


def reverse_a_string(string):
    return string[::-1]

string = input("Enter a string: ")
print(reverse_a_string(string))