from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class LevelsMenu():
    def level_set_up(self, Levels):
        Levels.setObjectName('Levels')
        Levels.resize(250, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Levels)
        self.verticalLayout.setObjectName('vLayout')

        self.label = QtWidgets.QLabel(Levels)
        self.label.setEnabled(True)

        font = QtGui.QFont('Ramia')
        font.setPointSize(25)

        self.easy_bttn = QtWidgets.QPushButton(Levels)
        self.medium_bttn = QtWidgets.QPushButton(Levels)
        self.hard_bttn = QtWidgets.QPushButton(Levels)
        self.vh_bttn = QtWidgets.QPushButton(Levels)

        self.easy_bttn.setObjectName('easy_bttn')
        self.medium_bttn.setObjectName('medium_bttn')
        self.hard_bttn.setObjectName('hard_bttn')
        self.vh_bttn.setObjectName('vh_bttn')

        font_dif = QtGui.QFont('Papyrus')
        font_dif.setPointSize(18)
        self.easy_bttn.setFont(font_dif)
        self.medium_bttn.setFont(font_dif)
        self.hard_bttn.setFont(font_dif)
        self.vh_bttn.setFont(font_dif)

        self.easy_bttn.setStyleSheet('QPushButton {background-color: #C5B8FF; color: white;}')
        self.medium_bttn.setStyleSheet('QPushButton {background-color: #5CFFA4; color: white;}')
        self.hard_bttn.setStyleSheet('QPushButton {background-color: #ffb8a2; color: white;}')
        self.vh_bttn.setStyleSheet('QPushButton {background-color: #ff495f; color: white;}')

        self.verticalLayout.addWidget(self.easy_bttn)
        self.verticalLayout.addWidget(self.medium_bttn)
        self.verticalLayout.addWidget(self.hard_bttn)
        self.verticalLayout.addWidget(self.vh_bttn)

        self.renaming(Levels)
        QtCore.QMetaObject.connectSlotsByName(Levels)

    def renaming(self, Levels):
        rename = QtCore.QCoreApplication.translate
        Levels.setWindowTitle(rename('Levels', 'Which one you prefer more?'))
        self.easy_bttn.setText(rename('Levels', 'ASPIRIN'))
        self.medium_bttn.setText(rename('levels', 'CODEINE'))
        self.hard_bttn.setText(rename('Levels', 'MORPHINE'))
        self.vh_bttn.setText(rename('levels', 'COCAINE'))

