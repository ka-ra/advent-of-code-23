import re
from re import finditer

max_red = 12
max_green = 13
max_blue = 14

sum = 0

filepath = input("Input location: ")
f = open(filepath,"r")
lines = f.readlines()

for i in lines:
    # reset counters
    red = ""
    green = ""
    blue = ""
    red_possible = []
    green_possible = []
    blue_possible = []

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

        # check if the current count of reds exceeds the max allowable
        red_possible.append(int(red) <= max_red)

    #print(id, red_possible)

    # do the same for blue and green as done for red
    for k in finditer((" blue"),i):
        endnum = k.span()[0]
        startnum = endnum-1

        if i[startnum-1:startnum] != " ":
            startnum = endnum-2

        blue = i[startnum:endnum]

        blue_possible.append(int(blue) <= max_blue)
        #print(id)

    #print(id, blue_possible)

    for l in finditer((" green"),i):
        endnum = l.span()[0]
        startnum = endnum-1
        if i[startnum-1:startnum] != " ":
            startnum = endnum-2
        green = i[startnum:endnum]

        green_possible.append(int(green) <= max_green)
        #print(id)

    #print(id, green_possible)
    #print(id, all(red_possible), all(blue_possible), all(green_possible))

    # if all instances of all colors are possible, add the game id to the sum total
    if all(red_possible) & all(blue_possible) & all(green_possible):
        sum = sum + id

print(sum)

exit()
