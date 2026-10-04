'''
Q87. Student Details
Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print the
full details of each student in a clear, readable format.
'''


students = {
    "101": {"name": "Aman", "age": 19, "city": "Bhopal"},
    "102": {"name": "Rohit", "age": 18, "city": "Nagpur"},
    "103": {"name": "Yash", "age": 16, "city": "Indore"},
}

print("Students details: \n")
for roll_no,details in students.items():
    print(f"Name = {details["name"]} \nAge = {details["age"]} \nCity = {details["city"]}")
    print()
    