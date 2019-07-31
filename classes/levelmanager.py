import stages.level0 as lv0


class LevelManager:

    def __init__(self, _gm, _level):
        self.gm = _gm
        self.currentLevel = _level
        self.startingX, self.startingY = self.getStartingPos()




    def update(self):
        posX, posY = self.getTerrainPos()
        lv = self.generateLevel()
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



    def generateLevel(self):

        if self.currentLevel == 0:
            self.file = 'stages/lv0'

        if self.currentLevel:
            self.file = 'stages/lv1'


        with open(self.file,"r") as file:
            plan = []
            for ligne in file:
                lignePlan =[]
                for k in ligne:
                    if k !='\n':
                        lignePlan.append(k)
                plan.append(lignePlan)
            return plan



    def getStartingPos(self):
        x, y = 0, 0
        lv = self.generateLevel()
        for i in range(len(lv)):
            for j in range(len(lv[i])):
                if lv[i][j] == 'D':
                    x, y = 50*j, 50*(i+1)
        return x, y




    def setLevel(self,level):
        self.currentLevel = _level




