import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_Equipo = {
            1:["Gonzalez Gabriel Uriel","Estudiar",20,"c+",":/Variadas/Imagenes/Uriel.jpg"],
            2:["Badillo Gonzalez Victor Manuel", "Estudiar", 20, "c+",""],
            3:["Fernandez Arrazola Sofia Mariana", "Estudiar", 20, "c+"],
            4: ["Juarez Beltran Moses Eduardo", "Estudiar", 20, "c+"]
        }

        self.btn_adelante.clicked.connect(self.adelante)
        self.btn_atras.clicked.connect(self.atras)
        self.index_control = 0
        self.bnt_atra

    def atras (self):
        if self.index_control > 1:
            self.index_control -=1
            datos=self.datos_Equipo[self.index_control]
            print(datos)
            self.btn_adelante.setEnable(True)
            ##change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))


        if self.index_control == 1:
            self.bnt_atras.setEnable(False)

    def adelante (self):
        if self.index_control < 5:
            self.btn_atras.setEnable(True)
            self.index_control +=1
            datos=self.datos_Equipo[self.index_control]
            print(datos)

    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

