from math import sqrt


class Vector:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def getX(self):
        return self.x

    def setX(self, _x):
        self.x = _x

    def getY(self):
        return self.y

    def setY(self, _y):
        self.y = _y

    def add(self, _vec):
        return Vector(self.x + _vec.getX(), self.y + _vec.getY())

    def __add__(self, _vec):
        return self.add(_vec)

    def __neg__(self):
        return self.mult(-1)

    def __sub__(self, _vec):
        return self.add(_vec.mult(-1))

    def mult(self, _k):
        return Vector(self.x * _k, self.y * _k)

    def len(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        l = self.len()
        return Vector(self.x / l, self.y / l)

    def __abs__(self):
        return self.normalize()

    def sProd(self, _vec):
        return self.x * _vec.getX() + self.y * _vec.getY()
