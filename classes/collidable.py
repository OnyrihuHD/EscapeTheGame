from classes.location import Location
from classes.vector import Vector


class Collidable:
    hitbox = (0, 0)
    location = Location(0, 0)

    def getLocation(self):
        return self.location

    def setLocation(self, _loc):
        self.location = _loc

    def getHitbox(self):
        loc = self.getLocation()
        return loc.getX(), loc.getY(), self.hitbox[0], self.hitbox[1]

    def setHitbox(self, _hitbox):
        self.setLocation(Location(_hitbox[0], _hitbox[1]))
        self.hitbox = _hitbox[2], _hitbox[3]

    def isColliding(self, obj):
        if not isinstance(obj, Collidable):
            return False

        H1, H2 = self.getHitbox(), obj.getHitbox()
        x1, y1 = self.getLocation().toXY()
        x2, y2 = obj.getLocation().toXY()
        L1, R1 = [x1, y1], [x1 + H1[0], y1 + H1[1]]
        L2, R2 = [x2, y2], [x2 + H2[0], y2 + H2[1]]

        if L1[0] > R2[0] or L2[0] > R1[0] or L1[1] < R2[1] or L2[1] < R1[1]:
            return False
        return True

    def getSafeMatrix(self, _loc, _level):
        fn = _level.isSolid
        trX = Vector(self.getHitbox()[2] // 2, 0)
        trY = Vector(0, self.getHitbox()[3] // 2)
        return [[not fn(_loc.addVec(trY.mult(y)).addVec(trX.mult(x))) for x in range(3)] for y in range(3)]

    def isSafePlace(self, _loc, _level):
        mat = self.getSafeMatrix(_loc, _level)
        for line in mat:
            if False in line:
                return False
        return True

    def nearestSafePlace(self, _loc, _level):
        _loc = _loc.floor()
        mat = self.getSafeMatrix(_loc, _level)

        # SOL (PLAT) OU OBSTACLE
        while not (mat[2][0] or mat[2][2]) or not mat[2][1]:
            _loc = _loc.addVec(Vector(0, -1))
            mat = self.getSafeMatrix(_loc, _level)

        # PLAFOND (PLAT) OU OBSTACLE
        while not (mat[0][0] or mat[0][2]) or not mat[0][1]:
            _loc = _loc.addVec(Vector(0, 1))
            mat = self.getSafeMatrix(_loc, _level)

        # MUR GAUCHE (PLAT) OU OBSTACLE
        while not (mat[0][0] or mat[2][0]) or not mat[1][0]:
            _loc = _loc.addVec(Vector(1, 0))
            mat = self.getSafeMatrix(_loc, _level)

        # MUR DROIT (PLAT) OU OBSTACLE
        while not (mat[0][0] or mat[2][0]) or not mat[1][0]:
            _loc = _loc.addVec(Vector(-1, 0))
            mat = self.getSafeMatrix(_loc, _level)

        # COIN SUP G
        while not (mat[0][0]):
            _loc = _loc.addVec(Vector(1, 1))
            mat = self.getSafeMatrix(_loc, _level)

        # COIN SUP D
        while not (mat[0][2]):
            _loc = _loc.addVec(Vector(-1, 1))
            mat = self.getSafeMatrix(_loc, _level)

        # COIN INF G
        while not (mat[2][0]):
            _loc = _loc.addVec(Vector(1, -1))
            mat = self.getSafeMatrix(_loc, _level)

        # COIN INF D
        while not (mat[2][2]):
            _loc = _loc.addVec(Vector(-1, -1))
            mat = self.getSafeMatrix(_loc, _level)

        return _loc
