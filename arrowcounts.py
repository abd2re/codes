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




