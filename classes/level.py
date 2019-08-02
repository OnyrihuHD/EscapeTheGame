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
                    x, y = const.LEVEL_RES * j, const.LEVEL_RES * (i + 1)
        return Location(x, y)

    def getEnding(self):
        x, y = 0, 0
        for i in range(len(self.toArray())):
            for j in range(len(self.toArray()[i])):
                if self.toArray()[i][j] == 'A':
                    x, y = const.LEVEL_RES * j, const.LEVEL_RES * (i + 1)
        return Location(x, y)

    def isSolid(self, _loc):
        x = int(_loc.getX() // const.LEVEL_RES)
        y = int(_loc.getY() // const.LEVEL_RES)
        if y < 0 or y > len(self.toArray()) - 1:
            return False
        if x < 0 or x > len(self.toArray()[y]) - 1:
            return False
        return self.toArray()[y][x] in const.SOLID
