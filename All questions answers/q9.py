"""
Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""
m = int(input())

if m >= 90:
    print("A")
elif m >= 75:
    print("B")
elif m >= 60:
    print("C")
elif m >= 40:
    print("D")
else:
    print("F")