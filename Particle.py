class Particle:
    def __init__(self, x, y, *kwargs):
        self.x = x
        self.y = y
        self.r = kwargs.get('r', 10)
        self.vel = kwargs.get('vel', 5)


