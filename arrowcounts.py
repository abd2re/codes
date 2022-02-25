p = input("Input:")
c = 0
h = []
v = []

for i in p:
    if i == '<' or i == ">": h.append(i)
    elif i == '^' or i == "v": v.append(i)


for i in h:
    if i == '>': c += 1
    elif i == '<': c -= 1


print(len(h)-abs(c) + len(v))

#Given a string of arrows ^ > V and <, find the minimum number of turns you 
#would need to make to point all the arrows in the same direction, eg. for ^^^>,
#1 turn to make it ^^^^, and for ^^v, 2 turns to make it ^^^


