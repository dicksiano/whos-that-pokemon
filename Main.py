from PyQt5.QtWidgets import QApplication, \
    QWidget, QPushButton, QFrame, QSlider, QCheckBox, QFileDialog,\
    QGraphicsScene, QGraphicsView, QVBoxLayout, QGroupBox,\
    QHBoxLayout, QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtGui import QPainter, QImage, QColor, QPainterPath, \
    QPen, QMouseEvent, QPolygon, QPalette, QColor, QPixmap, QImage
from PyQt5.QtCore import Qt, QRect, QPointF, QRandomGenerator, QTimer,\
    QObject, QRectF
import sys
import random
import time

from Particle import Particle
import randomChooser


BUTTON_MIN_WIDTH = 100
BUTTON_x = 120
BUTTON_Y = 430

pokemons = ['Goldeen', 'Kadabra', 'Vaporeon', 'Grimer', 'Machamp', 'Oddish',\
'Poliwhirl', 'Squirtle', 'Doduo', 'Charmander', 'Golem', 'Horsea', 'Magmar',\
'Dragonite', 'Charizard', 'Drowzee', 'Electrode', 'Ponyta', 'Rhydon', 'Caterpie',\
'Zapdos', 'Pidgey', 'Voltorb', 'Shellder', 'Bulbasaur', 'Clefable', 'Omanyte',\
'Hitmonchan', 'Mankey', 'Nidoking', 'Magnemite', 'Geodude', 'Zubat', 'Cubone',\
'Nidorino', 'Gastly', 'Seaking', 'Magneton', 'Ditto', 'Articuno', 'Alakazam',\
'Pikachu', 'Koffing', 'Golbat', 'Pidgeotto', 'Eevee', 'Muk', 'Starmie', 'Rattata',\
'Slowpoke', 'Cloyster', 'Nidoran', 'Nidorina', 'Hitmonlee', 'Aerodactyl', 'Ekans',\
'Weepinbell', 'Gengar', 'Nidoqueen', 'Magikarp', 'Metapod', 'Machoke', 'Tentacruel',\
'Tauros', 'Venomoth', 'Exeggutor', 'Onix', 'Spearow', 'Mr.Mime', 'Kingler',\
'Gloom', 'Sandslash', 'Raichu', 'Moltres', 'Staryu', 'Lickitung', 'Abra',\
'Arbok', 'Psyduck', 'Diglett', 'Wartortle', 'Slowbro', 'Dodrio', 'Raticate',\
'Dratini', 'Porygon', 'Beedrill', 'Tentacool', 'Omastar', 'Poliwag', 'Kakuna',\
'Gyarados', 'Machop', 'Dragonair', 'Venusaur', 'Victreebel', 'Arcanine', 'Flareon',\
'Rapidash', 'Clefairy', 'Growlithe', 'Vulpix', 'Scyther', 'Jynx', 'Seadra',\
'Paras', 'Weezing', 'Dugtrio', 'Golduck', 'Charmeleon', 'Primeape', 'Blastoise',\
'Seel', 'Farfetch', 'Mewtwo', 'Marowak', 'Ivysaur', 'Tangela', 'Ninetales',\
'Pidgeot', 'Bellsprout', 'Krabby', 'Electabuzz', 'Chansey', 'Pinsir', 'Persian',\
'Lapras', 'Fearow', 'Exeggcute', 'Hypno', 'Parasect', 'Kangaskhan', 'Haunter',\
'Kabutops', 'Dewgong', 'Venonat', 'Sandshrew', 'Weedle', 'Wigglytuff', 'Jolteon',\
'Graveler', 'Vileplume', 'Jigglypuff', 'Butterfree', 'Poliwrath', 'Rhyhorn', 'Kabuto'] 

class states:
    normal=0

class GrafScene(QGraphicsScene):
    def __init__(self, parent):
        super().__init__(parent)
        self.view = QGraphicsView(self)
        self.image = QImage()

    def initUI(self):
        self.setItemIndexMethod(QGraphicsScene.BspTreeIndex)
        self.setBackgroundBrush(QColor(255, 0, 0))
        # pokemon = QGraphicsPixmapItem(QPixmap("assets/gengar.png"))
        bgimg = QPixmap("assets/whosthatpokemon.jpg")
        # print(bgimg.width(), bgimg.height())
        self.addPixmap(QPixmap("assets/whosthatpokemon.jpg"))

        # img = image.load("assets/gengar.png")
        self.pokemon = QGraphicsPixmapItem()
        self.setNewPokemon("Gengar")

        self.answer = QGraphicsPixmapItem()

        # pokemon.pixmap(
        self.addItem(self.pokemon)
        self.addParticles(150)
        self.view.setFixedSize(761,431)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scene.setSceneRect(5, 5, self.width()-10, 300)
        self.view.setBackgroundBrush(QColor(0, 255, 0))#QImage("assets/whosthatpokemon.png"))
        # self.view.setCacheMode(QGraphicsView.CacheBackground)
        self.view.setRenderHint(QPainter.Antialiasing)
        # self.scene.views

    def addParticles(self, count: int):
        gen = QRandomGenerator()
        for i in range(count):
            # print(random(self.scene.width()))
            part = Particle(QPointF(gen.bounded(self.width()),\
                gen.bounded(self.height())))
            part.setVisible(False)
            self.addItem(part)

    def setNewPokemon(self, name):
        self.image.load("assets/" + name.lower() + ".png")
        for i in range(self.image.width()):
            for j in range(self.image.height()):
                color = self.image.pixelColor(i,j)
                if color.alpha() != 0:
                    color.setAlpha(5)
                    self.image.setPixel(i,j,color.rgba())
        self.pokemon.setPixmap(QPixmap().fromImage(self.image))
        pokepix = self.pokemon.pixmap()
        self.pokemon.setPos(220-self.image.width()/2,220-self.image.height()/2)

    def setAnswer(self, name):
        self.image.load("assets/" + name.lower() + ".png")
        self.pokemon.setPixmap(QPixmap().fromImage(self.image))
        pokepix = self.pokemon.pixmap()
        self.pokemon.setPos(220-self.image.width()/2,220-self.image.height()/2)

    def upAlpha(self, particle: QGraphicsItem):
        if self.pokemon.collidesWithItem(particle):
            # particle.setVisible(False)
            pos = QPointF(particle.pos().x()-220+self.image.width()/2,particle.pos().y()-220+self.image.height()/2)# self.pokemon.mapToItem(self.pokemon, particle.pos())
            border = 2
            if pos.x() > border and pos.x() < self.image.width()-border and\
                pos.y() > border and pos.y() < self.image.height()-border:
                for i in range(-border,border):
                    for j in range(-border,border):
                        color = self.image.pixelColor(pos.x()+i, pos.y()+j)
                        if color.alpha() > 0 and color.alpha() < 245:
                            color.setAlpha(color.alpha()+10)
                            self.image.setPixel(pos.x()+i, pos.y()+j, color.rgba())
                            self.pokemon.setPixmap(QPixmap().fromImage(self.image))
                            self.pokemon.show()


class GrafWin(QFrame):
    def __init__(self):
        super().__init__()

        self.listOfPokemons = []
        self.answerPokemon = ''
        self.time = 0

        self.createButtons()
        self.initUI()

    def initUI(self):
        self.setFixedSize(785,500)
        self.setWindowTitle('Who\'s that Pokémon?')
        # self.gf = GrafWidget(self)
        # self.gf.setGeometry(5, 5, 590, 400)
        self.setLayout(QVBoxLayout())

        self.buttonsGroup = QGroupBox()
        self.createBtnsLayout()
        self.buttonsGroup.hide()

        self.scene = GrafScene(self)
        self.scene.initUI()

        self.layout().addWidget(self.scene.view)
        self.layout().addWidget(self.buttonsGroup)
        self.layout().addWidget(self.b1)
        # self.layout().
        self.scene.setSceneRect(QRectF(self.scene.view.rect()))
        self.timer = QTimer()
        self.timer.timeout.connect(self.scene.advance)
        self.timer.start(1000/66)

        print(self.scene.width(),self.scene.height())
        self.show()

    def createBtnsLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.b2)
        layout.addWidget(self.b3)
        layout.addWidget(self.b4)
        layout.addWidget(self.b5)
        layout.addWidget(self.b6)
        self.buttonsGroup.setLayout(layout)

    def updatePokemons(self):
        self.choosePokemon()
        self.answerPokemon = self.listOfPokemons[random.randint(0, 4)]

    def createButtons(self):
        self.b1 = QPushButton("Generate", self)
        self.b1.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b1.move(5 + 2 * BUTTON_x, 30 + BUTTON_Y)
        self.b1.clicked.connect(self.on_click_start)

        self.b2 = QPushButton()
        self.b2.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b2.move(5, BUTTON_Y)
        self.b2.clicked.connect(self.on_click_choose)

        self.b3 = QPushButton()
        self.b3.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b3.move(5 + 1 * BUTTON_x, BUTTON_Y)
        self.b3.clicked.connect(self.on_click_choose)

        self.b4 = QPushButton()
        self.b4.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b4.move(5 + 2 * BUTTON_x, BUTTON_Y)
        self.b4.clicked.connect(self.on_click_choose)

        self.b5 = QPushButton()
        self.b5.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b5.move(5 + 3 * BUTTON_x, BUTTON_Y)
        self.b5.clicked.connect(self.on_click_choose)

        self.b6 = QPushButton()
        self.b6.setMinimumWidth(BUTTON_MIN_WIDTH)
        self.b6.move(5 + 4 * BUTTON_x, BUTTON_Y)
        self.b6.clicked.connect(self.on_click_choose)

    def updateButtons(self):
        self.b2.setText(self.listOfPokemons[0])
        self.b3.setText(self.listOfPokemons[1])
        self.b4.setText(self.listOfPokemons[2])
        self.b5.setText(self.listOfPokemons[3])
        self.b6.setText(self.listOfPokemons[4])

        self.buttonsGroup.show()
        self.b1.hide()


    def choosePokemon(self):

        randomNumbers = randomChooser.generateList()
        self.listOfPokemons.clear()

        for i in range(5):
            self.listOfPokemons.append(pokemons[randomNumbers[i]])

    def on_click_start(self):
        self.updatePokemons()
        self.updateButtons()
        self.scene.setNewPokemon(self.answerPokemon)
        self.show()
        self.time = time.time()


        for i in self.scene.items():
            if isinstance(i,Particle):
                i.setVisible(True)


    def on_click_nop(self):
        pass

    def on_click_choose(self):
        for i in self.scene.items():
            if isinstance(i,Particle):
                i.setVisible(False)
        self.scene.setAnswer(self.answerPokemon)

        self.time = time.time() - self.time
        print("Time: " + str(self.time))
        guessedPokemon = self.sender().text()
        answerPokemon = self.answerPokemon

        if guessedPokemon == answerPokemon:
            print("Acertou, Mizeravi!")
        else:
            print("Achou que era o " + guessedPokemon + "? Achou errado, otario.\
             O pokemon correto era: " + answerPokemon)

        self.b1.show()
        self.buttonsGroup.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GrafWin()
    ex.show()
    sys.exit(app.exec_())
