"""
Print all the numbers which are divisible by 3 and 5, from 1 to 100.
"""
start = int(input("start: "))
end = int(input("end: "))
s = start
e = end

while s <= e:
    if s%3==0 and s%5==0:
        print(s,end=" ")
    s += 1