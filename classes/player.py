import pygame


class Player(object):

    def __init__(self, _gm):
        self.gm = _gm
        self.jumping = False
        self.health = 100
        self.maxHealth = 100
        self.width = 40
        self.height = 60
        self.vel = 5
        self.x = self.gm.winFrame.get_width() // 2
        self.y = 2 * self.gm.winFrame.get_height() // 3
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.lastFacing = 'R'
        self.walkCount = 0
        self.hitbox = (self.x + 18, self.y + 11, 27, 50)

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

    def moveUpdate(self, _keys):
        if _keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.lastFacing = 'L'

        elif _keys[pygame.K_RIGHT] and self.x < self.gm.winFrame.get_width() - self.vel - self.width:
            self.x += self.vel
            self.left = False
            self.right = True
            self.lastFacing = 'R'

        else:
            self.left = False
            self.right = False
            self.walkCount = 0

        if not self.isJumping():
            if _keys[pygame.K_UP]:
                self.setJumping(True)
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.4
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.setJumping(False)

        self.gm.updateView()

    def setDisplay(self):
        posX, posY = self.gm.levelManager.getCharAbsPos()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            self.gm.winFrame.blit(self.gm.texture.mainWalkLeft[self.walkCount // 3], (posX, posY))
            self.walkCount += 1
        elif self.right:
            self.gm.winFrame.blit(self.gm.texture.mainWalkRight[self.walkCount // 3], (posX, posY))
            self.walkCount += 1
        else:
            if self.lastFacing == 'L':
                self.gm.winFrame.blit(self.gm.texture.mainWalkLeft[0], (posX, posY))
            else:
                self.gm.winFrame.blit(self.gm.texture.mainWalkRight[0], (posX, posY))
            self.walkCount = 0
        pygame.draw.rect(self.gm.winFrame, (255, 0, 0), self.hitbox, 2)

    def hasBlockDown(self):
        hasBlock = False
        idX_L = self.x // 50
        idX_R = (self.x + self.hitbox[2]) // 50
        idY = self.y + self.hitbox[3] // 50
        lv = self.gm.levelManager.getCurrentLevel()