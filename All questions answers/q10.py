"""
Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400.

200 - not a leap year
204 - leap

800 - leap year
"""

y = int(input())

if (y%4==0 and y%100 != 0) or (y % 400 == 0):
    print("It's an Leap Year")
else:
    print("It's not")