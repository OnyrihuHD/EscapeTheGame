from classes.collidable import Collidable


class Obstacle(Collidable):
    def __init__(self, _loc, _width, _height):
        self.setLocation(_loc)
        x, y = _loc.toXY()
        self.hitbox = (x, y, _width, _height)
