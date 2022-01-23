import math as m

def st(a,b,c):
    delta = m.pow(b,2) - 4 * (a*c)

    if delta != 0:
        x1 = (-1 * b - m.sqrt(delta))/(2*a)
        x2 = (-1 * b + m.sqrt(delta))/(2*a)
        return x1 and x2
    else:
        x0 = (-1 * b)/(2*a)
        return x0

print(st(-4,7,12))

