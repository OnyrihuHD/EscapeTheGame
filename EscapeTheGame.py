import pygame
from pygame.locals import *
from classes.mainchar import MainChar

pygame.init()

winWidth = 1200
winHeight = 600
mainFrame = pygame.display.set_mode((winWidth, winHeight))

clock = pygame.time.Clock()
running = True
mainChar = MainChar(mainFrame)

while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    mainChar.moveUpdate(keys)

pygame.quit()
