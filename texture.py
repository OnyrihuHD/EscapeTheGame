import pygame

BACKGROUND = pygame.image.load('images/background/bg0.jpg')
BRICK = pygame.image.load('images/terrain/brick.jpg')
CHAR_WALK_LEFT = [pygame.image.load('images/main_char/L' + str(i) + '.png') for i in range(1, 10)]
CHAR_WALK_RIGHT = [pygame.image.load('images/main_char/R' + str(i) + '.png') for i in range(1, 10)]
