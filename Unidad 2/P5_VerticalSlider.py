import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.datos_Equipo = {
            1: ["Gonzalez Gabriel Uriel", "Estudiar", 20, "c+", ":/Variadas/Imagenes/Uriel.jpg"],
            2: ["Badillo Gonzalez Victor Manuel", "Estudiar", 20, "c+", ":/Variadas/Imagenes/VIctor.jpg"],
            3: ["Fernandez Arrazola Sofia Mariana", "Estudiar", 20, "c+", ":/Variadas/Imagenes/Sofia.jpg"],
            4: ["Juarez Beltran Moses Eduardo", "Estudiar", 20, "c+", ":/Variadas/Imagenes/Eduardo.jpg"]
        }

        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(4)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(1)
        self.verticalSlider.valueChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        dataClave= self.dial.value()
        print(dataClave)
        imagen = self.datos_Equipo[dataClave][-1]
        self.label_11.setPixmap(QtGui.QPixmap(imagen))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

