import const
from classes.level import Level


class LevelManager:
    currentLevel = 0

    def __init__(self, _gm):
        self.GM = _gm
        self.generatedLevel = self.generateCurrentLevel()

    def getGenerated(self):
        return self.generatedLevel

    def setCurrentLevel(self, _lv):
        self.currentLevel = _lv

    def generateCurrentLevel(self):
        return self.generateLevel(self.currentLevel)

    def generateLevel(self, _lv):
        fileName = 'stages/lv0'
        if _lv in list(range(2)):
            fileName = 'stages/lv' + str(self.currentLevel)

        with open(fileName, 'r') as file:
            plan = []
            for line in file:
                plan.append([k for k in line if k != '\n'])
            return Level(plan)
