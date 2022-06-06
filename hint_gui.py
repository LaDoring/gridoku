from PyQt5 import QtCore, QtWidgets, QtGui


class Hint_UI():
    def hint_gui(self, Hint):
        Hint.setObjectName('Hint')
        Hint.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Hint)
        self.verticalLayout.setObjectName('verticalLayout')

        font = QtGui.QFont('Ink free')
        font.setPointSize(22)

        self.label = QtWidgets.QTextEdit()
        self.label.setFont(font)
        self.label.setEnabled(False)
        self.label.setStyleSheet('QTextEdit {background-color: #de6467; color: white;}')
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label.setObjectName('label')
        self.verticalLayout.addWidget(self.label)

        self.close_hint_bttn = QtWidgets.QPushButton(Hint)
        self.close_hint_bttn.setObjectName('close_hint_bttn')

        font_lvl = QtGui.QFont('Jokerman')
        font_lvl.setPointSize(25)
        self.close_hint_bttn.setFont(font_lvl)

        self.verticalLayout.addWidget(self.close_hint_bttn)

        self.renaming(Hint)
        QtCore.QMetaObject.connectSlotsByName(Hint)

    def renaming(self, Hint):
        rename = QtCore.QCoreApplication.translate
        Hint.setWindowTitle(rename('Hint', '9 x 9 GRIDOKU'))
        self.close_hint_bttn.setText(rename('Hint', 'Get back'))
        self.label.setText(rename('Hint', 'There are no hints yet, but a joke \n\n\
Parallel lines have so much in common. it\'s a shame they\'ll never meet '))

