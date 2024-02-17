import math
import sys

import numpy
from PyQt5 import uic, QtWidgets
from numpy import double

qtCreatorFile = "P_06_SumNumeros_V2_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_sumar.clicked.connect(self.suma)
        self.txt_resultado.setEnabled(False)

    def suma(self):
        numeros=self.txt_numeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i)for i in lista]
        print(lista_en_numeros)

        suma = sum(lista_en_numeros)

        self.txt_resultado.setText(str(suma))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

