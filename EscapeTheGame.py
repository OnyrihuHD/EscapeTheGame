

import pygame
from pygame.locals import *

pygame.init()

fenetre=pygame.display.set_mode((600,600))

continuer=1

while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            continuer=0
        