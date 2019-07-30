import pygame


class Texture:

    def __init__(self, _gm):
        self.gm = _gm
        self.background = pygame.image.load('images/background/bg0.jpg')
        self.brick = pygame.image.load('images/terrain/brick.jpg')
        self.mainWalkLeft = [pygame.image.load('images/main_char/L' + str(i) + '.png') for i in range(1, 10)]
        self.mainWalkRight = [pygame.image.load('images/main_char/R' + str(i) + '.png') for i in range(1, 10)]
