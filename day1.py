import re

sum = 0

filepath = input("Input location: ")
f = open(filepath,"r")
lines = f.readlines()

for i in lines:
    # reset strings
    num = ""
    first = ""
    last = ""

    # find first number
    first = re.findall(r"\d",i)[0]
    #print(first)

    # find last number
    last = re.findall(r"\d",i)[-1]
    #print(last)

    # append together
    num = first + last
    #print(num)

    # turn num into int
    num = int(num)

    # add to sum
    sum = sum + num
    #print(sum)

print(sum)
