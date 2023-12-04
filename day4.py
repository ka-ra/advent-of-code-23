sum = 0

filepath = input("Input location: ")
f = open(filepath,"r")
lines = f.readlines()

for i in lines:
    subtotal = 0
    j = i.split(': ')
    k = j[1].split('|')
    winning = list(filter(None,k[0].rstrip().split(' ')))
    scratch = list(filter(None,k[1].rstrip().split(' ')))
    overlap = list(set(winning).intersection(scratch))

    if len(overlap) > 0:
        count = len(overlap)-1
        subtotal = 2**count
    else:
        count = 0
        subtotal = 0

    sum = sum + subtotal
    print(count,subtotal,sum)

print(sum)
exit()
