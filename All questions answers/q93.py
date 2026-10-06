"""
Q93. String Characters and Length

Take a name as input from the user. Print its first character, its last
character, and the total length of the name.
"""


name = input("Enter name: ")

print(f"first character = '{name[0]}'")
print(f"last character = '{name[-1]}'")
print(f"total length of the name = {len(name)}")