class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b: return True

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a



    def get_area_square(self):
        return self.a ** 2
class Circle:
    def __init__(self, r=None):
        self.r = r

    def get_area_circle(self):
        return 3.141529 * self.r ** 2

class Rectangle_:
    def __init__(self, x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = "Rectangle_"

    def __str__(self):
        return f'{self.name,  self.x, self.y, self.w, self.h}'
    def area_(self):
        return self.w*self.h
