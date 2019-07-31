from math import sqrt


class Location:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, _x):
        self.x = _x

    def setY(self, _y):
        self.y = _y

    def xDist(self, _loc):
        return abs(self.x - _loc.x)

    def yDist(self, _loc):
        return abs(self.y - _loc.y)

    def dist(self, _loc):
        return sqrt(self.xDist(_loc) ** 2 + self.yDist(_loc) ** 2)

    def __add__(self, _loc):
        return Location(self.x + _loc.x, self.y + _loc.y)

