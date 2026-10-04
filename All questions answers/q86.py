'''
Q86. Subjects and Marks

Create a dictionary of 6 subjects and their respective marks. Print the
subject with the highest marks and the one with the lowest, using max()
and min() functions alongside a lambda expression.
'''


marks = {
    "science": 99, 
    "maths": 100, 
    "comp": 88, 
    "hindi": 43, 
    "history": 71,
    "english": 78
}

sub,mark = max(marks.items(), key = lambda x: x[1])
print(f"{sub} has highest marks = {mark}")


sub2,mark2 = min(marks.items(), key = lambda x: x[1])
print(f"{sub2} has lowest marks = {mark2}")
    