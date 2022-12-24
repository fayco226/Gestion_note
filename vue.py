import sys

from PySide2 import QtCore , QtGui , QtWidgets


class Acceuil(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.__bienvenu = QtWidgets.QLabel("Bienvenu Dans Gestion de Note")
        self.__boutonEtudiant = QtWidgets.QPushButton("Liste des étudiants")
        self.__boutonSemestre = QtWidgets.QPushButton("Semestre")
        self.__bouttonNote = QtWidgets.QPushButton("Les notes")
        self.__bouttonUe = QtWidgets.QPushButton("Unité d'enseignement")
        self.__bouttonEcu = QtWidgets.QPushButton("Liste des Matières")
        self.__bouttonQuitter = QtWidgets.QPushButton("Quitter")
        
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.__bienvenu, 0, 1)
        layout.addWidget(self.__boutonEtudiant, 1, 0)
        layout.addWidget(self.__boutonSemestre, 1, 2)
        layout.addWidget(self.__bouttonEcu, 2, 1)
        layout.addWidget(self.__bouttonNote, 3, 0)
        layout.addWidget(self.__bouttonUe, 3, 2)
        layout.addWidget(self.__bouttonQuitter, 5, 1)
        self.setLayout(layout)
        
        self.setWindowTitle("Gestion DE Note")
        self.__bouttonQuitter.clicked.connect(self.quitter)
    def quitter(self):
        self.accept()


    
app = QtWidgets.QApplication(sys.argv)
dialog = Acceuil()
dialog.exec_()