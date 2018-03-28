from PyQt5.QtGui import QVector2D, QPainter, QColor
from PyQt5.QtWidgets import QGraphicsItem
# from PyQt5.QtCore import QRectF

class Particle(QGraphicsItem):
    """Particle class to simulate physics"""
    def __init__(self, pos: QVector2D, **kwargs):
        """Constructor to create a particle, receives a QtVector2D and can \
        receive 'r' that is radius (float) and 'speed' that is speed (QVector2d)"""
        self.setPos(pos.x(), pos.y())
        self.rad = kwargs.get('r', 10)
        self.speed = kwargs.get('speed', QVector2D(10, 10))

    def hasCollidedX(self):
        """Return true if the particle has collided with the vertical \
        borders"""
        newpos = self.mapToScene(self.pos())
        if(newpos.x() - self.rad < 0 or newpos.x()+self.rad > self.scene().width()):
            return True
        return False

    def hasCollidedY(self):
        """Return true if the particle has collided with the horizontal \
        borders"""
        newpos = self.mapToScene(self.pos())
        if(newpos.y() - self.rad < 0 or newpos.y()+self.rad > self.scene().height()):
            return True
        return False

    def advance(self, step):
        """Update the motion of the particle"""
        if not step:
            return
        self.setPos(self.pos + self.speed)
        if self.hasCollidedX():
            self.speed.setX(self.speed.x()*-1)
        if self.hasCollidedY():
            self.speed.setY(self.speed.y()*-1)

    def boundingRect(self):
        pass
        # return QRectF(-self.rad, -self.rad, self.rad*2, self.rad*2)

    def paint(self, painter: QPainter):
        """Show particle on the screen"""
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(self.boundingRect())
