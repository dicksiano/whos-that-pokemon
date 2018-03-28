from PyQt5.QtWidgets import QApplication, \
    QWidget, QPushButton, QFrame, QSlider, QCheckBox, QFileDialog
from PyQt5.QtGui import QPainter, QImage, QColor, QPainterPath, \
    QPen, QMouseEvent, QPolygon, QPalette, QColor
from PyQt5.QtCore import Qt, QRect
import sys
import random

import Particle
import randomChooser

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
            "jolteon", "graveler", "vileplume", "jigglypuff", "butterfree", "poliwrath", "rhyhorn", "kabuto" ] 

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
        listOfPokemons = []
        answerPokemon = ''

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Who\'s that Pokémon?')
        self.gf = GrafWidget(self)
        self.gf.setGeometry(5, 5, 590, 400)

        self.listOfPokemons = self.choosePokemon()
        self.answerPokemon = self.listOfPokemons[random.randint(0,4)]
        print(self.answerPokemon)

        b1 = QPushButton("Generate", self)
        b1.setMinimumWidth(100)
        b1.move(245, 460)
        b1.clicked.connect(self.on_click_start)

        b2 = QPushButton(self.listOfPokemons[0], self)
        b2.setMinimumWidth(100)
        b2.move(5, 430)
        b2.clicked.connect(self.on_click_choose)

        b3 = QPushButton(self.listOfPokemons[1], self)
        b3.setMinimumWidth(100)
        b3.move(125, 430)
        b3.clicked.connect(self.on_click_choose)

        b4 = QPushButton(self.listOfPokemons[2], self)
        b4.setMinimumWidth(100)
        b4.move(245, 430)
        b4.clicked.connect(self.on_click_choose)

        b5 = QPushButton(self.listOfPokemons[3], self)
        b5.setMinimumWidth(100)
        b5.move(365, 430)
        b5.clicked.connect(self.on_click_choose)

        b6 = QPushButton(self.listOfPokemons[4], self)
        b6.setMinimumWidth(100)
        b6.move(485, 430)
        b6.clicked.connect(self.on_click_choose)

        self.show()

    def choosePokemon(self):
        randomNumbers = randomChooser.generateList()
        listOfPokemons = []

        for i in range(5):
            listOfPokemons.append(pokemons[randomNumbers[i]])

        return listOfPokemons

        
    def on_click_start(self):
        print('Generate')

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
