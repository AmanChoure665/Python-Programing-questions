'''Student Profile 
Create a dictionary for a student, including keys like name, age, city, and
marks (as a list of scores). Print each piece of information using its key.'''


student_profile = {"name": "Aman",
                   "age": 21,
                   "city": "Multai",
                   "marks":[55, 65, 76, 98, 84]}


print(f"""Student Profile
    Name = {student_profile["name"]}
    Age = {student_profile["age"]}
    City = {student_profile["city"]}
    Marks = {student_profile["marks"]}
    """)