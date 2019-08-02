import pygame
from pygame.locals import *

from classes.gamemanager import GameManager

pygame.init()
pygame.display.set_caption('Escape The Game - ver. 0.1')

GM = GameManager()
GM.start(0)

clock = pygame.time.Clock()
running = True

while running:

    clock.tick(30)  # 30 FPS

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    GM.getPlayer().moveUpdate(keys)
    GM.getDisplay().update()

pygame.quit()
