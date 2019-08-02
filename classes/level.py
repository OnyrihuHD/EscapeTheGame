import const
from classes.location import Location


class Level:

    def __init__(self, _plan):
        self.plan = _plan

    def toArray(self):
        return self.plan

    def getStarting(self):
        x, y = 0, 0
        for i in range(len(self.toArray())):
            for j in range(len(self.toArray()[i])):
                if self.toArray()[i][j] == 'D':
                    x, y = 50 * j, 50 * (i + 1)
        return Location(x, y)

    def getEnding(self):
        x, y = 0, 0
        for i in range(len(self.toArray())):
            for j in range(len(self.toArray()[i])):
                if self.toArray()[i][j] == 'A':
                    x, y = 50 * j, 50 * (i + 1)
        return Location(x, y)

    def isSolid(self, _loc):
        x = int(_loc.getX() // 50)
        y = int(_loc.getY() // 50)
        if y < 0 or y > len(self.toArray()) - 1:
            return False
        if x < 0 or x > len(self.toArray()[y]) - 1:
            return False
        return self.toArray()[y][x] in const.SOLID
