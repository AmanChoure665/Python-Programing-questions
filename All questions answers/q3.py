"""
Q3: Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""


age = int(input())

print(f"Eligible for voting {age>=18}")
print(f"Senior citizen {age>=60}")