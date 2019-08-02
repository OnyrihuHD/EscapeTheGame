import const
from classes.location import Location


class Level:
    front = [[]]
    back = [[]]

    def __init__(self, _lv):
        self.id = _lv
        self.generate(_lv)

    def getID(self):
        return self.id

    def generate(self, _lv):
        fileName = 'stages/lv' + str(_lv)
        fileFront = open(fileName, 'r')
        fileBack = open(fileName + '_bg', 'r')

        front, back = [], []
        for line in fileFront:
            front.append([k for k in line if k != '\n'])
        self.front = front

        for line in fileBack:
            back.append([k for k in line if k != '\n'])
        self.back = back

    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

    def getStarting(self):
        x, y = 0, 0
        for i in range(len(self.getFront())):
            for j in range(len(self.getFront()[i])):
                if self.getFront()[i][j] == 'D':
                    x, y = const.LEVEL_RES * j, const.LEVEL_RES * (i + 1)
        return Location(x, y)

    def getEnding(self):
        x, y = 0, 0
        for i in range(len(self.getFront())):
            for j in range(len(self.getFront()[i])):
                if self.getFront()[i][j] == 'A':
                    x, y = const.LEVEL_RES * j, const.LEVEL_RES * (i + 1)
        return Location(x, y)

    def isSolid(self, _loc):
        x = int(_loc.getX() // const.LEVEL_RES)
        y = int(_loc.getY() // const.LEVEL_RES)
        if y < 0 or y > len(self.getFront()) - 1:
            return False
        if x < 0 or x > len(self.getFront()[y]) - 1:
            return False
        return self.getFront()[y][x] in const.SOLID
