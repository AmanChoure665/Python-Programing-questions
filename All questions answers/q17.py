# Sum of all the numbers from 1 to 100 divisible by 2 and 7.

start = int(input("start: "))
end = int(input("end: "))
s = start
e = end
b = 0

while s <= e:
    if s%2 ==0 and s%7 ==0:
        b += s
    s += 1
print("Total =",b)