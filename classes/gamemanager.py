import pygame

from classes.levelmanager import LevelManager
from classes.mainchar import MainChar
from classes.texture import Texture


class GameManager:
    winWidth = 1200
    winHeight = 600

    def __init__(self):
        self.winFrame = pygame.display.set_mode((self.winWidth, self.winHeight))
        self.levelManager = LevelManager(self, 0)

        self.player = Player(self)
        self.startingX = self.levelManager.startingX
        self.startingY = self.levelManager.startingY
        self.player.x = self.startingX
        self.player.y = self.startingY - self.player.height

        self.texture = Texture(self)

    def updateView(self):
        self.winFrame.blit(self.texture.background, (0, 0))
        self.levelManager.update()
        self.mainChar.setDisplay()
        pygame.display.update()

    @staticmethod
    def isColliding(obj1, obj2):
        if not (hasattr(obj1, 'hitbox') and hasattr(obj2, 'hitbox')):
            return False

        H1, H2 = obj1.hitbox, obj2.hitbox
        L1, R1 = [obj1.x, obj1.y], [obj1.x + H1[2], obj1.y + H1[3]]
        L2, R2 = [obj2.x, obj2.y], [obj2.x + H2[2], obj2.y + H2[3]]

        if L1[0] > R2[0] or L2[0] > R1[0]:
            return False
        if L1[1] < R2[1] or L2[1] < R1[1]:
            return False
        return True
