import pygame

import const
import texture
from classes.location import Location
from classes.vector import Vector


class Display:
    offX = 0
    offY = 0

    def __init__(self, _gm, _size):
        self.GM = _gm
        self.screen = pygame.display.set_mode(_size)

    def getScreen(self):
        return self.screen

    def displayBackground(self):
        self.getScreen().blit(texture.BACKGROUND, (0, 0))

    def displayLevel(self):
        lv = self.GM.getLevelManager().generateCurrentLevel().toArray()
        for i in range(len(lv)):
            for j in range(len(lv[i])):
                if lv[i][j] == 'B':
                    self.getScreen().blit(texture.BRICK,
                                          (const.LEVEL_RES * j + self.offX, const.LEVEL_RES * i + self.offY),
                                          [0, 0, const.LEVEL_RES, const.LEVEL_RES])

    def displayPlayer(self):
        p = self.GM.getPlayer()
        pos = self.addOffset(p.getTextureLocation()).toXY()
        if p.getWalkSeq() + 1 >= 27:
            p.setWalkSeq(0)
        if p.getFacing() == -1:
            self.getScreen().blit(texture.CHAR_WALK_LEFT[p.getWalkSeq() // 3], pos)
            p.setWalkSeq(p.getWalkSeq() + 1)
        elif p.getFacing() == 1:
            self.getScreen().blit(texture.CHAR_WALK_RIGHT[p.getWalkSeq() // 3], pos)
            p.setWalkSeq(p.getWalkSeq() + 1)
        else:
            if p.getFacing() == -1:
                self.getScreen().blit(texture.CHAR_WALK_LEFT[0], pos)
            else:
                self.getScreen().blit(texture.CHAR_WALK_RIGHT[0], pos)
            p.setWalkSeq(0)

        if const.DEBUG:
            loc = self.addOffset(p.getLocation())
            hitbox = (loc.getX(), loc.getY(), p.hitbox[0] + 1, p.hitbox[1] + 1)
            pygame.draw.rect(self.screen, (255, 0, 0), hitbox, 1)

    def update(self):
        self.calibrate(self.GM.getPlayer().getLocation())
        self.displayBackground()
        self.displayLevel()
        self.displayPlayer()
        pygame.display.update()

    def calibrate(self, _rel, _abs=Location(const.CHAR_POS_X, const.CHAR_POS_Y)):
        self.offX = _abs.getX() - _rel.getX()
        self.offY = _abs.getY() - _rel.getY()

    def addOffset(self, _loc):
        return _loc.addVec(Vector(self.offX, self.offY))
