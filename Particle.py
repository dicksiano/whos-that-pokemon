from PyQt5.QtGui import QVector2D

class Particle:
    """Particle class to simulate physics"""
    def __init__(self, pos:QVector2D, **kwargs):
        """Constructor to create a particle, receives a QtVector2D and can \
        receive 'r' that is radius and 'vel' that is velocity, both of them \
        are QtVector2D"""
        self.pos = pos
        self.rad = kwargs.get('r', 10)
        self.vel = kwargs.get('vel', 5)

    def hasCollidedX(self, width):
        """Return true if the particle has collided with the vertical \
        borders"""
        pass

    def hasCollidedY(self, height):
        """Return true if the particle has collided with the horizontal \
        borders"""
        pass

    def update(self):
        """Update the motion of the particle"""
        pass

    def show(self):
        """Show particle on the screen"""
        pass
