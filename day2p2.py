import re
from re import finditer

sum = 0

filepath = input("Input location: ")
f = open(filepath,"r")
lines = f.readlines()

for i in lines:
    # reset counters
    red = ""
    green = ""
    blue = ""
    red_all = []
    green_all = []
    blue_all = []
    power = 0

    # find game id
    id = int(i[(i.find(" ")+1):i.find(":")])
    #print(id)

    # look for all instances of red cubes in that game
    for j in finditer((" red"),i):
        # find the string position of the number preceding " red"
        endnum = j.span()[0]
        startnum = endnum-1

        # some numbers are two digits instead of one
        if i[startnum-1:startnum] != " ":
            startnum = endnum-2

        # find the actual count substring
        red = i[startnum:endnum]

        # add count to red_all list
        red_all.append(int(red))

    # do the same for blue and green
    for k in finditer((" blue"),i):
        # find the string position of the number preceding " red"
        endnum = k.span()[0]
        startnum = endnum-1

        # some numbers are two digits instead of one
        if i[startnum-1:startnum] != " ":
            startnum = endnum-2

        # find the actual count substring
        blue = i[startnum:endnum]

        # add count to red_all list
        blue_all.append(int(blue))

    for l in finditer((" green"),i):
        # find the string position of the number preceding " red"
        endnum = l.span()[0]
        startnum = endnum-1

        # some numbers are two digits instead of one
        if i[startnum-1:startnum] != " ":
            startnum = endnum-2

        # find the actual count substring
        green = i[startnum:endnum]

        # add count to red_all list
        green_all.append(int(green))

    red_min = max(red_all)
    green_min = max(green_all)
    blue_min = max(blue_all)
    #print(id, "|", red_all, red_min, "|", green_all, green_min, "|", blue_all, blue_min)

    power = int(red_min) * int(green_min) * int(blue_min)
    #print(id, power)

    sum = sum + power

    print(id, red_min, green_min, blue_min, power, sum)

print(sum)
