'''
Check if the person is eligible for vote using string
'''

age = input("Enter age: ")

if age.isdigit():
    if int(age)>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Please enter valid age")