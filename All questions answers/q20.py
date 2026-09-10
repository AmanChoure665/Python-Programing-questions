"""
Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)
"""
total = 0

while True:
    num = int(input())

    if num < 0:
        continue
    elif num > 0:
        total += num
    else:
        break

print(total)