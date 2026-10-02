"""
Q83. Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values() to
calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Math": 88,
    "Science": 76,
    "English": 91,
    "History": 65,
    "Computer": 95,
}
total = 0
n = len(marks)
for mark in marks.values():
    total += mark

avg = total/n
print(f"Total Marks = {total} \nAvarage Marks = {avg}")