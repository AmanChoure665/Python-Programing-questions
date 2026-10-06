"""
Q105. Palindrome Check

Write a function is_palindrome(text) that returns True if the given string is
a palindrome (ignoring case and spaces).
"""

def is_palindrome(text:str):
    text = text.lower().replace(" ","")
    
    for char in range(0,(len(text)//2)):
        if text[char] == text[len(text)-char-1]:
            return True
        return False
    
print(is_palindrome("racecar"))
print(is_palindrome("Never sdd or even"))
print(is_palindrome("hello"))