import pygame
import const


class Texture:
    BACKGROUND = pygame.image.load('images/background/bg0.jpg')
    CHAR_WALK_LEFT = [pygame.image.load('images/main_char/L' + str(i) + '.png') for i in range(1, 10)]
    CHAR_WALK_RIGHT = [pygame.image.load('images/main_char/R' + str(i) + '.png') for i in range(1, 10)]

    TERRAIN_PATH = 'images/terrain/'

    def __init__(self):
        self.TERRAIN = {
            'B': self.asset('BRICK.jpg'),
            'b': self.asset('BRICK_2.jpg'),
            'C': self.asset('CACTUS_POT.png'),
            'P': self.asset('PLANT_POT.png'),
        }

    def asset(self, _str):
        return pygame.transform.scale(pygame.image.load(self.TERRAIN_PATH + _str), [const.LEVEL_RES, const.LEVEL_RES])
