from PyQt5 import QtCore, QtWidgets


class Game_UI():
    def setup_gui(self, Game):
        Game.setObjectName('Game')
        Game.resize(445, 340)

        self.verticalLayout = QtWidgets.QVBoxLayout(Game)
        self.verticalLayout.setObjectName('verticalLayout')
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName('gridLayout')

        self.top_left = QtWidgets.QTableWidget(Game)
        self.top_left.setRowCount(3)
        self.top_left.setColumnCount(3)
        self.top_left.setObjectName('top_left')
        self.top_left.horizontalHeader().setVisible(False)
        self.top_left.horizontalHeader().setDefaultSectionSize(45)
        self.top_left.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.top_left, 0, 0, 1, 1)

        self.top_mid = QtWidgets.QTableWidget(Game)
        self.top_mid.setRowCount(3)
        self.top_mid.setColumnCount(3)
        self.top_mid.setObjectName('top_mid')
        self.top_mid.horizontalHeader().setVisible(False)
        self.top_mid.horizontalHeader().setDefaultSectionSize(45)
        self.top_mid.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.top_mid, 1, 0, 1, 1)

        self.top_right = QtWidgets.QTableWidget(Game)
        self.top_right.setRowCount(3)
        self.top_right.setColumnCount(3)
        self.top_right.setObjectName('top_right')
        self.top_right.horizontalHeader().setVisible(False)
        self.top_right.horizontalHeader().setDefaultSectionSize(45)
        self.top_right.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.top_right, 2, 0, 1, 1)

        self.mid_left = QtWidgets.QTableWidget(Game)
        self.mid_left.setRowCount(3)
        self.mid_left.setColumnCount(3)
        self.mid_left.setObjectName('mid_left')
        self.mid_left.horizontalHeader().setVisible(False)
        self.mid_left.horizontalHeader().setDefaultSectionSize(45)
        self.mid_left.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.mid_left, 0, 1, 1, 1)

        self.mid_mid = QtWidgets.QTableWidget(Game)
        self.mid_mid.setRowCount(3)
        self.mid_mid.setColumnCount(3)
        self.mid_mid.setObjectName('mid_mid')
        self.mid_mid.horizontalHeader().setVisible(False)
        self.mid_mid.horizontalHeader().setDefaultSectionSize(45)
        self.mid_mid.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.mid_mid, 1, 1, 1, 1)

        self.mid_right = QtWidgets.QTableWidget(Game)
        self.mid_right.setRowCount(3)
        self.mid_right.setColumnCount(3)
        self.mid_right.setObjectName('mid_right')
        self.mid_right.horizontalHeader().setVisible(False)
        self.mid_right.horizontalHeader().setDefaultSectionSize(45)
        self.mid_right.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.mid_right, 2, 1, 1, 1)

        self.bttn_left = QtWidgets.QTableWidget(Game)
        self.bttn_left.setRowCount(3)
        self.bttn_left.setColumnCount(3)
        self.bttn_left.setObjectName('bttn_left')
        self.bttn_left.horizontalHeader().setVisible(False)
        self.bttn_left.horizontalHeader().setDefaultSectionSize(45)
        self.bttn_left.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.bttn_left, 0, 2, 1, 1)

        self.bttn_mid = QtWidgets.QTableWidget(Game)
        self.bttn_mid.setRowCount(3)
        self.bttn_mid.setColumnCount(3)
        self.bttn_mid.setObjectName('bttn_mid')
        self.bttn_mid.horizontalHeader().setVisible(False)
        self.bttn_mid.horizontalHeader().setDefaultSectionSize(45)
        self.bttn_mid.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.bttn_mid, 1, 2, 1, 1)

        self.bttn_right = QtWidgets.QTableWidget(Game)
        self.bttn_right.setRowCount(3)
        self.bttn_right.setColumnCount(3)
        self.bttn_right.setObjectName('bttn_right')
        self.bttn_right.horizontalHeader().setVisible(False)
        self.bttn_right.horizontalHeader().setDefaultSectionSize(45)
        self.bttn_right.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.bttn_right, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName('hLayout')

        self.hint_bttn = QtWidgets.QPushButton(Game)
        self.hint_bttn.setObjectName('hint_bttm')
        self.hLayout.addWidget(self.hint_bttn)
        self.cancel_bttn = QtWidgets.QPushButton(Game)
        self.cancel_bttn.setObjectName('cancel_bttn')
        self.hLayout.addWidget(self.cancel_bttn)

        self.verticalLayout.addLayout(self.hLayout)

        self.renaming(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def renaming(self, Game):
        rename = QtCore.QCoreApplication.translate
        Game.setWindowTitle(rename('Game', 'GRIDOKU Solver'))
        self.hint_bttn.setText(rename('Game', 'Wanna get a hint?'))
        self.cancel_bttn.setText(rename('Game', 'Press me ot quit'))

