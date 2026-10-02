'''Safe Subject Access
Define a dictionary with five subjects and their respective marks. Utilize the
get() method to try accessing a subject that is not in the dictionary, ensuring
it prints "Not Available" as a default.'''


marks = {
    "science": 99, 
    "maths": 100, 
    "comp": 88, 
    "hindi": 43, 
    "history": 71
}


print(marks.get("hindi","Not Available"))
print(marks.get("english","Not Available"))