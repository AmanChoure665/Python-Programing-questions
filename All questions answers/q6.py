#start and end by user
# end to start, print even numbers using while loop

start = int(input("start: "))
end = int(input("end: "))
s = start
e = end

while s <= e:
    if e%2==0:
        print(e,end=" ")
    e -= 1