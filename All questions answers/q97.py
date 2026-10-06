"""
Q97. Email Validation

Take an email as input. Validate that it contains exactly one @ and at least
one .
Print "Valid" or "Invalid".
"""


# def check_email(user_email):
#     count = 0
#     count2 = 0

#     for ch in user_email:
#         if ch == "@":
#             count += 1
#         elif ch == ".":
#             count2 += 1
#         else:
#             pass
    
#     if count == 1 and count2 >= 1:
#         return "It's an valid email"
#     else:
#         return "It's an invalid email"
    

def check_email(email:str):
    if email.count("@") == 1 and "." in email:
        return "It's an valid email"
    return "It's an invalid email"

user_email = input("Enter your email: ")
print(check_email(user_email))
