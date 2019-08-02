import const
from classes.display import Display
from classes.level import Level
from classes.player import Player
from classes.texture import Texture
from classes.vector import Vector


class GameManager:
    currentLevel = Level(0)
    texture = Texture()

    def __init__(self):
        self.display = Display(self, (const.WIN_WIDTH, const.WIN_HEIGHT))
        self.player = Player(self)

    def getTexture(self):
        return self.texture

    def getDisplay(self):
        return self.display

    def getPlayer(self):
        return self.player

    def getCurrentLevel(self):
        return self.currentLevel

    def setCurrentLevel(self, _lv):
        self.currentLevel = _lv

    def start(self, _lv):
        self.setCurrentLevel(Level(_lv))
        loc = self.getCurrentLevel().getStarting()
        loc = loc.addVec(Vector((50 - const.CHAR_WIDTH) / 2, - const.CHAR_HEIGHT))
        self.getPlayer().setLocation(loc)
