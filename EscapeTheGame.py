import pygame
from pygame.locals import *

from classes.gamemanager import GameManager

pygame.init()
GM = GameManager()
GM.start(0)

clock = pygame.time.Clock()
running = True

while running:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    GM.getPlayer().moveUpdate(keys)
    GM.getDisplay().update()

pygame.quit()
