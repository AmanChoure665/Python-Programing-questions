# Sum of all the numbers from 1 to 100.

start = int(input("start: "))
end = int(input("end: "))
s = start
e = end
b = 0

while s <= e:
    b += s
    s += 1
print("Total =",b)