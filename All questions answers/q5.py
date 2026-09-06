#start and end by user
# start to end print numbers which are divisible by 3 and 4, using while loop

start = int(input("start: "))
end = int(input("end: "))
s = start
e = end

while s <= e:
    if s%3==0 and s%4 ==0:
        print(s,end=" ")
    s += 1