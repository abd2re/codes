import math as m
c = 0
limit = 16
triples = []

for a in range(1,limit):
    for i in range(1,8,2):
        for b in range(1,a):
            u = 2*a*b*i
            v = int(m.pow(a,2) - m.pow(b,2))*i
            x = int(m.sqrt(m.pow(u,2)+m.pow(v,2)))
            if u > v: u,v = v,u
            else: u,v = u,v
            triples.append([u,v,x])

for i in range(len(triples)):
    for n in range(len(triples)-1):
        if sum(triples[n]) > sum(triples[n+1]):
            triples[n], triples[n+1] = triples[n+1], triples[n]

for i in triples:
    c+=1
    print(c,i)
    if c == limit:
        break







