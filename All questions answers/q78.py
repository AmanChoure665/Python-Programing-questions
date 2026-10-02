'''Print the performance of all the subjects
and print the number of subjects passed'''


marks = {
    "science": 99, 
    "maths": 100, 
    "comp": 88, 
    "hindi": 43, 
    "history": 71
}

print("<------ Subject performance ------>")

for sub, score in marks.items():
    if score >= 90:
        print(f"{sub}: Excellent")
    elif score >= 60:
        print(f"{sub}: Good")
    else:
        print(f"{sub}: Need improvements")
        
       
passed_subjects = 0
for score in marks.values():
    if score >= 50:
        passed_subjects += 1
print(f"Subjects passed: {passed_subjects}")