import pygame

import const
from classes.collidable import Collidable
from classes.vector import Vector


class Player(Collidable):
    velocity = Vector(0, 0)
    speed = const.CHAR_BASE_SPEED
    health = 100
    maxHealth = 100
    facing = 1
    walkSeq = 0

    def __init__(self, _gm):
        super().__init__(_gm)
        self.hitbox = (const.CHAR_WIDTH, const.CHAR_HEIGHT)

    def getHealth(self):
        return self.health

    def setHealth(self, _amount):
        if _amount < 0:
            _amount = 0
        if _amount > self.maxHealth:
            _amount = self.maxHealth
        self.health = _amount

    def getSpeed(self):
        return self.speed

    def setSpeed(self, _speed):
        self.speed = _speed

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, _vel):
        self.velocity = _vel

    def getWalkSeq(self):
        return self.walkSeq

    def setWalkSeq(self, _s):
        self.walkSeq = _s

    def getFacing(self):
        return self.facing

    def setFacing(self, _f):
        self.facing = _f

    def getTextureLocation(self):
        offX = (const.CHAR_T_WIDTH - const.CHAR_WIDTH) / 2
        offY = (const.CHAR_T_HEIGHT - const.CHAR_HEIGHT) / 2 + 5
        return self.getLocation().addVec(-Vector(int(offX), int(offY)))

    def moveUpdate(self, _keys):
        level = self.GM.getCurrentLevel()

        # CALCUL DE LA VITESSE
        vel = self.getVelocity()
        if _keys[pygame.K_LEFT]:
            self.setFacing(-1)
            if self.hasBlockLeft(level):
                vel.setX(0)
                self.walkSeq = 0
            else:
                vel.setX(-self.getSpeed())

        elif _keys[pygame.K_RIGHT]:
            self.setFacing(1)
            if self.hasBlockRight(level):
                vel.setX(0)
                self.walkSeq = 0
            else:
                vel.setX(self.getSpeed())

        else:
            vel.setX(0)
            self.walkSeq = 0

        if self.hasBlockUp(level):
            if vel.getY() < 0:
                vel.setY(0)

        if self.hasBlockDown(level):
            if _keys[pygame.K_UP]:
                self.walkSeq = 0
                vel.setY(-const.CHAR_JUMP_SPEED)
            if vel.getY() > 0:
                vel.setY(0)
        else:
            vel.setY(vel.getY() + const.GRAVITY)
            if abs(vel.getY()) > const.MAX_FALL_SPEED:
                v = vel.getY() / abs(vel.getY())
                vel.setY(10 * v)

        # CALCUL DES POSITIONS
        loc = self.getLocation()
        if not self.isSafePlace(loc.addVec(vel), level):
            loc = self.nearestSafePlace(loc.addVec(vel), level)
        else:
            loc = loc.addVec(vel)
        self.setLocation(loc)
