import const
from classes.display import Display
from classes.levelmanager import LevelManager
from classes.player import Player
from classes.vector import Vector


class GameManager:

    def __init__(self):
        self.display = Display(self, (const.WIN_WIDTH, const.WIN_HEIGHT))
        self.levelManager = LevelManager(self)
        self.player = Player(self)

    def getDisplay(self):
        return self.display

    def getLevelManager(self):
        return self.levelManager

    def getPlayer(self):
        return self.player

    def start(self, _lv):
        self.getLevelManager().setCurrentLevel(_lv)
        loc = self.getLevelManager().generateCurrentLevel().getStarting()
        loc = loc.addVec(Vector((50 - const.CHAR_WIDTH) / 2, - const.CHAR_HEIGHT))
        self.getPlayer().setLocation(loc)
