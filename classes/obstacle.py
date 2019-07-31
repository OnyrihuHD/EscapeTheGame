class Obstacle:
    def __init__(self, _x, _y, _width, _height):
        self.x = _x
        self.y = _x
        self.hitbox = (_x + _width / 2, _y + _height / 2, _width, _height)
