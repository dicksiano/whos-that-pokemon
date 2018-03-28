from PyQt5.QtWidgets import QApplication, \
    QWidget, QPushButton, QFrame, QSlider, QCheckBox, QFileDialog,\
    QGraphicsScene, QGraphicsView, QVBoxLayout, QGroupBox,\
    QHBoxLayout
from PyQt5.QtGui import QPainter, QImage, QColor, QPainterPath, \
    QPen, QMouseEvent, QPolygon, QPalette, QColor, QPixmap, QImage
from PyQt5.QtCore import Qt, QRect, QPointF, QRandomGenerator, QTimer,\
    QObject
import sys
import random

from Particle import Particle
import randomChooser


BUTTON_MIN_WIDTH = 100
BUTTON_x = 120
BUTTON_Y = 430

pokemons = ["goldeen", "kadabra", "vaporeon", "grimer", "machamp", "oddish", "poliwhirl", "squirtle", "doduo",
            "charmander", "golem", "horsea", "magmar", "dragonite", "charizard", "drowzee", "electrode", "ponyta", "rhydon",
            "caterpie", "zapdos", "pidgey", "voltorb", "shellder", "bulbasaur", "clefable", "omanyte", "hitmonchan", "mankey",
            "nidoking", "magnemite", "geodude", "zubat", "cubone", "nidorino", "gastly", "seaking", "magneton", "ditto", "articuno",
            "alakazam", "pikachu", "koffing", "golbat", "pidgeotto", "eevee", "muk", "starmie", "rattata", "slowpoke", "cloyster",
            "nidoran", "nidorina", "hitmonlee", "aerodactyl", "ekans", "weepinbell", "gengar", "nidoqueen", "magikarp", "metapod", 
            "machoke", "tentacruel", "tauros", "venomoth", "exeggutor", "onix", "spearow", "mr.mime", "kingler", "gloom", "sandslash",
            "raichu", "moltres", "staryu", "lickitung", "abra", "arbok", "psyduck", "diglett", "wartortle", "slowbro", "dodrio", "raticate",
            "dratini", "porygon", "beedrill", "tentacool", "omastar", "poliwag", "kakuna", "gyarados", "machop", "dragonair", "venusaur",
            "victreebel", "arcanine", "flareon", "rapidash", "clefairy", "growlithe", "vulpix", "scyther", "jynx", "seadra", "paras",
            "weezing", "dugtrio", "golduck", "charmeleon", "primeape", "blastoise", "seel", "farfetch", "mewtwo", "marowak", "ivysaur",
            "tangela", "ninetales", "pidgeot", "bellsprout", "krabby", "electabuzz", "chansey", "pinsir", "persian", "lapras", "fearow", 
            "exeggcute", "hypno", "parasect", "kangaskhan", "haunter", "kabutops", "dewgong", "venonat", "sandshrew", "weedle", "wigglytuff",
            "jolteon", "graveler", "vileplume", "jigglypuff", "butterfree", "poliwrath", "rhyhorn", "kabuto"] 

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
        qp.setPen(Qt.black)
        qp.setBrush(Qt.red)
        qp.end()

    def mouseMoveEvent(self, a0: QMouseEvent):
        self.cursor=(a0.x(),a0.y())
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

        self.listOfPokemons = []
        self.answerPokemon = ''

        self.b1 = QPushButton("Generate", self)
        self.b1.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b1.move(5 + 2 * BUTTON_x, 30 + BUTTON_Y)
        self.b1.clicked.connect(self.on_click_start)

        self.b2 = QPushButton(self)
        self.b3 = QPushButton(self)
        self.b4 = QPushButton(self)
        self.b5 = QPushButton(self)
        self.b6 = QPushButton(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Who\'s that Pokémon?')
        # self.gf = GrafWidget(self)
        # self.gf.setGeometry(5, 5, 590, 400)        
        self.setLayout(QVBoxLayout())

        self.buttonsGroup = QGroupBox()
        self.createBtnsLayout()
        
        self.scene = QGraphicsScene()
        self.scene.setParent(self)
        self.scene.setSceneRect(5,5,500,300)
        self.scene.setItemIndexMethod(QGraphicsScene.BspTreeIndex)
        self.addParticles(200)

        self.view = QGraphicsView(self.scene)
        self.view.setBackgroundBrush(QColor(0,255,0))#QImage("assets/whosthatpokemon.png"))
        # self.view.setCacheMode(QGraphicsView.CacheBackground)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.layout().addWidget(self.view)
        # self.view.show()
        self.layout().addWidget(self.buttonsGroup)
        self.layout().addWidget(self.b1)

        self.timer = QTimer()
        self.timer.timeout.connect(self.scene.advance)
        self.timer.start(1000/66)

        self.show()

    def createBtnsLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.b2)
        layout.addWidget(self.b3)
        layout.addWidget(self.b4)
        layout.addWidget(self.b5)
        layout.addWidget(self.b6)
        self.buttonsGroup.setLayout(layout)

    def addParticles(self, count: int):
        gen = QRandomGenerator()
        for i in range(count):
            # print(random(self.scene.width()))
            part = Particle(QPointF(gen.bounded(self.scene.width()), gen.bounded(self.scene.height())))
            self.scene.addItem(part)

    def updatePokemons(self):
        self.choosePokemon()
        self.answerPokemon = self.listOfPokemons[random.randint(0,4)]
        print(self.answerPokemon)

    def updateButtons(self):
        print("atualiza butao")
        self.b2.setText(self.listOfPokemons[0])
        self.b2.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b2.move(5, BUTTON_Y)
        self.b2.clicked.connect(self.on_click_choose)
        self.b2.show()

        self.b3.setText(self.listOfPokemons[1])
        self.b3.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b3.move(5 + 1 * BUTTON_x, BUTTON_Y)
        self.b3.clicked.connect(self.on_click_choose)
        self.b3.show()

        self.b4.setText(self.listOfPokemons[2])
        self.b4.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b4.move(5 + 2 * BUTTON_x, BUTTON_Y)
        self.b4.clicked.connect(self.on_click_choose)
        self.b4.show()

        self.b5.setText(self.listOfPokemons[3])
        self.b5.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b5.move(5 + 3 * BUTTON_x, BUTTON_Y)
        self.b5.clicked.connect(self.on_click_choose)
        self.b5.show()

        self.b6.setText(self.listOfPokemons[4])
        self.b6.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b6.move(5 + 4 * BUTTON_x, BUTTON_Y)
        self.b6.clicked.connect(self.on_click_choose)
        self.b6.show()


    def choosePokemon(self):
        
        randomNumbers = randomChooser.generateList()
        self.listOfPokemons.clear()

        for i in range(5):
            self.listOfPokemons.append(pokemons[randomNumbers[i]])
        
    def on_click_start(self):
        print('Generate')
        self.updatePokemons()
        self.updateButtons()
        self.show()

    def on_click_nop(self):
        pass

    def on_click_choose(self):
        guessedPokemon = self.sender().text()
        answerPokemon = self.answerPokemon
        if guessedPokemon == answerPokemon:
            print("Acertou, Mizeravi!")
        else:
            print("Achou que era o " + guessedPokemon + "? Achou errado, otario. O pokemon correto era: " + answerPokemon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GrafWin()
    ex.show()
    sys.exit(app.exec_())
