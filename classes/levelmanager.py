import stages.level0 as lv0


class LevelManager:

    def __init__(self, _gm, _level):
        self.gm = _gm
        self.currentLevel = _level

    def update(self):
        posX, posY = self.getTerrainPos()
        lv = self.getCurrentLevel()
        for i in range(len(lv)):
            for j in range(len(lv[i])):
                if lv[i][j] == 'B':
                    self.gm.winFrame.blit(self.gm.texture.brick, (50 * j - posX, 50 * i - posY))

    def getCharPos(self):
        return self.gm.mainChar.x, self.gm.mainChar.y

    def getCharAbsPos(self):
        return self.gm.winFrame.get_width() // 2, 2 * self.gm.winFrame.get_height() // 3

    def getTerrainPos(self):
        a = self.getCharPos()
        b = self.getCharAbsPos()
        return a[0] - b[0], a[1] - b[1]

    def getCurrentLevel(self):
        if self.currentLevel == 0:
            return lv0.load()
