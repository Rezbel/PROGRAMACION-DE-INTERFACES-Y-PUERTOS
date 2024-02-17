import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P7_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #set.text_equipo.setPlainText("Hola \n mundo")

        self.R = 0
        self.G = 0
        self.B = 0

    # Área de los Slots

    def cambiarR(self):
        self.R=self.valorR.value()

    def cambiarG(self):
        pass

    def cambiarB(self):

        estilo= "background-color: rgb(0, 0, 0);"(self.uriel + self.victor + self.mariana + self.eduardo)
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

