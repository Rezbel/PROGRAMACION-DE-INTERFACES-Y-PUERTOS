import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_uriel.clicked.connect(self.clic_uriel)
        self.rb_uriel.toggled.connect(self.toggled_uriel)

    # Área de los Slots
    def clic_uriel(self):
        print("hiciste clic al gato")

    def toggled_uriel(self):
        estado = self.rb_uriel.isCheked()
        print(f"Uriel cambio de estado (toggle). Nuevo Estado: {estado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

