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
        self.btn_sumar.clicked.connect(self.operacion)
        self.btn_resta.clicked.connect(self.operacion)
        self.btn_mult.clicked.connect(self.operacion)
        self.btn_division.clicked.connect(self.operacion)
        self.txt_C.setEnabled(False)

    def operacion(self):
        try:
            objeto = self.sender()
            nombre= objeto.objectName
            print(nombre)

            A= int(self.txt_A.text())
            B = int(self.txt_A.text())

            if nombre == "btn_sumar":
                r= A+B
            elif nombre == "btn_resta":
                r=A-B
            elif nombre== "btn_multiplicacion":
                r=A*B
            else:
                r=A/B
            self.txt_resultado.setText(str(r))
        except Exception as error:
            print(error)
        pass





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

