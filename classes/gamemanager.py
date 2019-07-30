import pygame

from classes.levelmanager import LevelManager
from classes.mainchar import MainChar
from classes.texture import Texture


class GameManager:
    winWidth = 1200
    winHeight = 600

    def __init__(self):
        pygame.init()
        self.winFrame = pygame.display.set_mode((self.winWidth, self.winHeight))
        self.levelManager = LevelManager(self, 0)

        self.mainChar = MainChar(self)
        self.startingX = 100
        self.startingY = 500
        self.mainChar.x = self.startingX
        self.mainChar.y = self.startingY - self.mainChar.height

        self.texture = Texture(self)

    def updateView(self):
        self.winFrame.blit(self.texture.background, (0, 0))
        self.levelManager.update()
        self.mainChar.setDisplay()
        pygame.display.update()
