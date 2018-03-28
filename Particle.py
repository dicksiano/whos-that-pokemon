from PyQt5.QtGui import QVector2D

class Particle:
    """Particle class to simulate physics"""
    def __init__(self, pos:QVector2D, **kwargs):
        """Constructor to create a particle, receives a QtVector2D and can \
        receive 'r' that is radius (float) and 'vel' that is velocity (QVector2d)"""
        self.pos = pos
        self.rad = kwargs.get('r', 10)
        self.vel = kwargs.get('vel', QVector2D(10,10))

    def hasCollidedX(self, width : float):
        """Return true if the particle has collided with the vertical \
        borders"""
        if(self.pos.x() - self.rad < 0 or self.pos.x()+self.rad > width):
            return True
        return False

    def hasCollidedY(self, height : float):
        """Return true if the particle has collided with the horizontal \
        borders"""
        if(self.pos.y() - self.rad < 0 or self.pos.y()+self.rad > height):
            return True
        return False

    def update(self):
        """Update the motion of the particle"""
        self.pos += self.vel
        if(self.hasCollidedX()):
            self.vel.setX(self.vel.x()*-1)
        if(self.hasCollidedY()):
            self.vel.setY(self.vel.y()*-1)


    def show(self):
        """Show particle on the screen"""
        pass
