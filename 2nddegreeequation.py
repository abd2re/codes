import math as m

class second_degree_equ():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def st(self):
        delta = m.pow(self.b,2) - 4 * (self.a*self.c)

        if delta != 0:
            x1 = (-1 * self.b - m.sqrt(delta))/(2*self.a)
            x2 = (-1 * self.b + m.sqrt(delta))/(2*self.a)
            return str(x1)+" or "+str(x2)
        else:
            x0 = (-1 * self.b)/(2*self.a)
            return x0

param = second_degree_equ(-1,6,18)
print(param.st())


