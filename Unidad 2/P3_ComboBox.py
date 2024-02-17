import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.comboBox.addItem("Uriel", 1)
        self.comboBox.addItem("Victor", 2)
        self.comboBox.addItem("Mariana", 3)
        self.comboBox.addItem("Eduardo", 4)

        self.comboBox.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: "+ self.comboBox.currentText())
        print("Index: "+ str(self.comboBox.currentIndex()))
        print("Data: " + str(self.comboBox.currentData()))

        dataClave= self.comboBox.currentData()
        imagen= self.datos_Equipo[dataClave][-1]
        self.label_11.setPixmap(QtGui. QPixmap(imagen))
    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

