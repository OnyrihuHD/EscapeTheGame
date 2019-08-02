import pygame

import const
from classes.collidable import Collidable
from classes.vector import Vector


class Player(Collidable):
    velocity = Vector(0, 0)
    speed = const.CHAR_BASE_SPEED
    jumping = False
    health = 100
    maxHealth = 100
    facing = 1
    walkSeq = 0

    def __init__(self, _gm):
        self.GM = _gm
        self.hitbox = (const.CHAR_WIDTH, const.CHAR_HEIGHT)

    def isJumping(self):
        return self.jumping

    def setJumping(self, _jump):
        self.jumping = _jump

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
        level = self.GM.getLevelManager().getGenerated()

        # CALCUL DE LA VITESSE
        vel = self.getVelocity()
        if _keys[pygame.K_LEFT]:
            self.setFacing(-1)
            if self.hasBlockLeft():
                vel.setX(0)
                self.walkSeq = 0
            else:
                vel.setX(-self.getSpeed())

        elif _keys[pygame.K_RIGHT]:
            self.setFacing(1)
            if self.hasBlockRight():
                vel.setX(0)
                self.walkSeq = 0
            else:
                vel.setX(self.getSpeed())

        else:
            vel.setX(0)
            self.walkSeq = 0

        if _keys[pygame.K_UP]:
            if not self.isJumping():
                self.setJumping(True)
                self.walkSeq = 0
                vel.setY(-const.CHAR_JUMP_SPEED)

        if self.hasBlockUp():
            if vel.getY() < 0:
                vel.setY(0)

        if self.hasBlockDown():
            if vel.getY() > 0:
                self.setJumping(False)
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

    def hasBlockDown(self):
        tr = Vector(0, 1)
        mat = self.getSafeMatrix(self.getLocation().addVec(tr), self.GM.getLevelManager().getGenerated())
        return not (mat[2][0] and mat[2][1] and mat[2][2])

    def hasBlockUp(self):
        tr = Vector(0, -1)
        mat = self.getSafeMatrix(self.getLocation().addVec(tr), self.GM.getLevelManager().getGenerated())
        return not (mat[0][0] and mat[0][1] and mat[0][2])

    def hasBlockLeft(self):
        tr = Vector(-1, 0)
        mat = self.getSafeMatrix(self.getLocation().addVec(tr), self.GM.getLevelManager().getGenerated())
        return not (mat[0][0] and mat[1][0] and mat[2][0])

    def hasBlockRight(self):
        tr = Vector(1, 0)
        mat = self.getSafeMatrix(self.getLocation().addVec(tr), self.GM.getLevelManager().getGenerated())
        return not (mat[0][2] and mat[1][2] and mat[2][2])
