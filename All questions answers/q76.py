'''Create a tuple of marks of 6 students. 
Print the highest, lowest, total, and average'''

def marks_calc(marks):
    # for total and average
    average = 0
    total = 0
    n = len(marks)
    for i in marks:
        total += i
        average = total/n

    # for highest
    highest = marks[0]
    for i in marks:
            if i > highest:
                highest = i

    # for lowest
    lowest = marks[0]
    for i in marks:
         if i < lowest:
              lowest = i

    return total, highest, lowest, average
marks = (45, 32, 11, 55, 98, 34)
# marks = (1, 2, 8, 4, 5, 6)

totl,high,low,avg = marks_calc(marks)

print(f"Highest marks: {high}")
print(f"Lowest marks: {low}")
print(f"Total marks: {totl}")
print(f"Average marks: {avg:.2f}")
