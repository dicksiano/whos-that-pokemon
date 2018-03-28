from PyQt5.QtWidgets import QApplication, \
    QWidget, QPushButton, QFrame, QSlider, QCheckBox, QFileDialog
from PyQt5.QtGui import QPainter, QImage, QColor, QPainterPath, \
    QPen, QMouseEvent, QPolygon, QPalette, QColor
from PyQt5.QtCore import Qt, QRect
import sys
import Particle

class states:
    normal=0

class GrafWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setMouseTracking(True)

        self.state=states.normal
        self.cursor=(10,10)
        self.polygons = []
        self.initUI()

    def initUI(self):
        self.setMinimumSize(380, 250)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        # qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.black)
        qp.setBrush(Qt.red)
        qp.end()

    def mouseMoveEvent(self, a0: QMouseEvent):
        self.cursor=(a0.x(),a0.y())
        # self.update(cx-20,cy-20,40,40)
        if self.state == states.normal:
            pass
            

    def mousePressEvent(self, e: QMouseEvent):
        self.cursor=(e.x(),e.y())
        if (self.state == states.normal):
            e.ignore()


    def mouseReleaseEvent(self, a0: QMouseEvent):
        self.cursor=(a0.x(),a0.y())
        if self.state == states.normal:
            a0.ignore()

    def setParams(self, diameter, trees):
        self.diameter = diameter
        self.trees = trees
        self.update()


class GrafWin(QFrame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Who\'s that Pokémon?')
        self.gf = GrafWidget(self)
        self.gf.setGeometry(5, 5, 590, 400)

        b1 = QPushButton("Generate", self)
        b1.setMinimumWidth(100)
        b1.move(245, 460)

        b2 = QPushButton("Pokemon 1", self)
        b2.setMinimumWidth(100)
        b2.move(5, 430)

        b3 = QPushButton("Pokemon 2", self)
        b3.setMinimumWidth(100)
        b3.move(125, 430)

        b4 = QPushButton("Pokemon 3", self)
        b4.setMinimumWidth(100)
        b4.move(245, 430)

        b5 = QPushButton("Pokemon 4", self)
        b5.setMinimumWidth(100)
        b5.move(365, 430)

        b6 = QPushButton("Pokemon 5", self)
        b6.setMinimumWidth(100)
        b6.move(485, 430)

        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = GrafWidget(None)
    ex = GrafWin()
    ex.show()
    sys.exit(app.exec_())
