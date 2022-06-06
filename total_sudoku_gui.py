from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from random import randint
from gui_sukodu_game import Game_UI
from hint_gui import Hint_UI
from level_menu import LevelsMenu
from start_menu import GridokuMenu
import create_gridoku as cs
import sys

integer = 0


class Menu(QDialog, GridokuMenu):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.set_up(self)
        self.cs = Game(self)
        self.play_bttn.clicked.connect(self.open_the_game)
        self.levels = Levels(self)
        self.lvl_bttn.clicked.connect(self.open_the_level_list)

    def open_the_game(self):
        global integer
        integer = randint(36, 50)
        self.cs = Game(self)
        self.cs.show()
        return integer

    def open_the_level_list(self):
        self.levels.show()


class Levels(QDialog, LevelsMenu):
    def __init__(self, parent=None):
        super(Levels, self).__init__()
        self.level_set_up(self)
        self.easy_bttn.clicked.connect(self.level1)
        self.medium_bttn.clicked.connect(self.level2)
        self.hard_bttn.clicked.connect(self.level3)
        self.vh_bttn.clicked.connect(self.level4)

    def level1(self):
        global integer
        integer = randint(36, 41)
        self.cs = Game(self)
        self.cs.show()
        return integer

    def level2(self):
        global integer
        integer = randint(41, 50)
        self.cs = Game(self)
        self.cs.show()
        return integer

    def level3(self):
        global integer
        integer = randint(50, 58)
        self.cs = Game(self)
        self.cs.show()
        return integer

    def level4(self):
        global integer
        integer = randint(58, 64)
        self.cs = Game(self)
        self.cs.show()
        return integer


class Game(QDialog, Game_UI):

    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.setup_gui(self)
        self.squares = [[self.top_left, self.top_mid, self.top_right],
                        [self.mid_left, self.mid_mid, self.mid_right],
                        [self.bttn_left, self.bttn_mid, self.bttn_right]]
        self.new_click()
        self.cancel_bttn.clicked.connect(self.close)
        self.hint_bttn.clicked.connect(self.hint)

    def hint(self):
        self.hint_menu = Hint(self)
        self.hint_menu.show()

    def check(self):
        pass

    def new_click(self):
        global integer
        puzzle = cs.remove(cs.gridoku_main(cs.grid), integer)
        for r, row in enumerate(self.squares):
            for s, square in enumerate(row):
                for i in range(3):
                    for j in range(3):
                        value = puzzle[i + s * 3][j + r * 3]
                        if value != 0:
                            item = QTableWidgetItem(str(value))
                            item.setFlags(Qt.ItemIsSelectable or Qt.ItemIsEnabled)
                            font_item = QFont('Jokerman', 11, 57)
                            item.setTextAlignment(5)
                            item.setFont(font_item)
                            item.setBackground(QColor('#DDFFBB'))
                            item.setForeground(QColor('black'))
                        else:
                            item = QTableWidgetItem('')
                        square.setItem(i, j, item)
                    square.clearSelection()


class Hint(QDialog, Hint_UI):
    def __init__(self, parent=Game):
        super(Hint, self).__init__(parent)
        self.hint_gui(self)
        self.close_hint_bttn.clicked.connect(self.close)


def start():
    app = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
