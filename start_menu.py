from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class GridokuMenu():
    def set_up(self, Menu):
        Menu.setObjectName('Menu')
        Menu.resize(400, 300)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout = QtWidgets.QVBoxLayout(Menu)

        self.verticalLayout_2.setObjectName('vLayout_2')
        self.verticalLayout.setObjectName('vLayout')

        self.label = QtWidgets.QLabel(Menu)
        self.label.setEnabled(True)

        font = QtGui.QFont('Ravie')
        font.setPointSize(30)

        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        self.verticalLayout.addWidget(self.label)

        self.play_bttn = QtWidgets.QPushButton(Menu)
        self.lvl_bttn = QtWidgets.QPushButton(Menu)

        self.play_bttn.setObjectName('play_bttn')
        self.lvl_bttn.setObjectName('lvl_bttn')

        font_lvl = QtGui.QFont('Jokerman')
        font_lvl.setPointSize(18)

        self.play_bttn.setFont(font_lvl)
        self.lvl_bttn.setFont(font_lvl)

        self.verticalLayout.addWidget(self.play_bttn)
        self.verticalLayout_2.addWidget(self.lvl_bttn)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.renaming(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def renaming(self, Menu):
        rename = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(rename('Menu', '9 x 9 GRIDOKU'))
        self.play_bttn.setText(rename('Menu', 'Push me to start GRIDOKU'))
        self.lvl_bttn.setText(rename('Menu', 'Touch me to change \n difficulty level'))
        self.label.setText(rename('Menu', 'GRIDOKU'))


