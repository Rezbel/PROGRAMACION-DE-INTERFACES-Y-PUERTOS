import math
import sys

import numpy
from PyQt5 import uic, QtWidgets
from numpy import double

qtCreatorFile = "P_04_OpaAritmeticas_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_mult.clicked.connect(self.multiplicacion)
        self.btn_division.clicked.connect(self.division)
        self.txt_C.setEnabled(False)

    def sumar(self):
        A= int (self.txt_A.text())
        B=int(self.txt_B.text())
        r= A+B
        self.txt_C.setText(str(r))

    def resta(self):
        A= int (self.txt_A.text())
        B=int(self.txt_B.text())
        r= A-B
        self.txt_C.setText(str(r))

    def multiplicacion(self):
        A= int (self.txt_A.text())
        B=int(self.txt_B.text())
        r= A+B
        self.txt_C.setText(str(r))

    def division(self):
        A= int (self.txt_A.text())
        B=int(self.txt_B.text())
        r= A/B
        self.txt_C.setText(str(r))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

