import re

intersect = []

filepath = input("Input location: ")
f = open(filepath,"r")
file = f.read()

numbers = [(m.group(), m.start(), m.end()) for m in re.finditer("\d{2,3}",file)]
symbols = [n.start() for n in re.finditer("[#%$!@$\/*&+=-]",file)]

for i in numbers:
    if (int(i[1]) in symbols) or (int(i[2]) in symbols) or (int(i[1])-1 in symbols) or (int(i[2])-1 in symbols) or (int(i[1])-140 in symbols) or (int(i[2])-140 in symbols) or (int(i[1])+140 in symbols) or (int(i[2])+140 in symbols) or (int(i[1])-139 in symbols) or (int(i[1])-141 in symbols) or (int(i[2])-139 in symbols) or (int(i[2])-141 in symbols):
        intersect.append(int(i[0]))

print(intersect)
exit()
