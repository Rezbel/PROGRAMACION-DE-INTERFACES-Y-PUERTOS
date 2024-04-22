import Ejemplo_P2

import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

#qtCreatorFile = "P1_Ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ejemplo_P2.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ejemplo_P2.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_nuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nuevo.setGeometry(QtCore.QRect(320, 190, 131, 41))
        self.btn_nuevo.setObjectName("btn_saludar")

        self.btn_nuevo.setText("Nuevo Boton")



    #Area de Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())