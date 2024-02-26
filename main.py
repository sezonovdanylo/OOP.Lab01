from math import pi


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Per(self):
        return (self.a + self.b + self.c)
    def Plo(self):
        p=(self.a + self.b + self.c)/2
        return ((p*(p-self.a)*(p-self.b)*(p-self.c))**0.5)



class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Per(self):
        return (2*self.a + 2*self.b)
    def Plo(self):
        return (self.a * self.b)



class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def Per(self):
        return (self.a + self.b + self.c + self.d)
    def Plo(self):
        m = ((self.a - self.b)**2 + self.c**2 - self.d**2)/(2*(self.a - self.b))
        h = (self.c**2 - m**2)**0.5
        return ((self.a + self.b)*h/2)


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def Per(self):
        return (2 * self.a + 2 * self.b)
    def Plo(self):
        return (self.a * self.h)



class Circle:
    def __init__(self, r):
        self.r = r
    def Per(self):
        return (2*pi*self.r)
    def Plo(self):
        return (pi * self.r * self.r)