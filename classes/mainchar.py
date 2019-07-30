import pygame


class MainChar:
    background = pygame.image.load('images/background/bg0.jpg')

    def __init__(self, _win):
        self.jumping = False
        self.health = 100
        self.maxHealth = 100
        self.width = 40
        self.height = 60
        self.vel = 5
        self.window = _win
        self.x = 50
        self.y = self.window.get_height() - 100
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.lastFacing = 'R'
        self.walkCount = 0
        self.imgDir = 'images/main_char/'
        self.walkLeft = [pygame.image.load(self.imgDir + 'L' + str(i) + '.png') for i in range(1, 10)]
        self.walkRight = [pygame.image.load(self.imgDir + 'R' + str(i) + '.png') for i in range(1, 10)]

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

        elif _keys[pygame.K_RIGHT] and self.x < self.window.get_width() - self.vel - self.width:
            self.x += self.vel
            self.left = False
            self.right = True
            self.lastFacing = 'R'

        else:
            self.left = False
            self.right = False
            self.walkCount = 0

        if not self.isJumping():
            if _keys[pygame.K_SPACE]:
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

        self.redrawWindow()

    def redrawWindow(self):
        self.window.blit(self.background, (0, 0))

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            self.window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            self.window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.lastFacing == 'L':
                self.window.blit(self.walkLeft[0], (self.x, self.y))
            else:
                self.window.blit(self.walkRight[0], (self.x, self.y))
            self.walkCount = 0

        pygame.display.update()
