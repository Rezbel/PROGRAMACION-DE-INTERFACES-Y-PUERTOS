import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #set.text_equipo.setPlainText("Hola \n mundo")
        self.cb_uriel.toggled.connect(self.sel_uriel)
        self.cb_victor.toggled.connect(self.sel_victor)
        self.cb_mariana.toggled.connect(self.sel_mariana)
        self.cb_eduardo.toggled.connect(self.sel_eduardo)

        self.uriel = ""
        self.victor = ""
        self.mariana = ""
        self.eduardo = ""

    # Área de los Slots

    def sel_uriel(self):
        if self.cb_uriel.isChecked():
            print("Uriel True")
            self.uriel = "Uriel\n"
        else:
            print("Uriel False")
            self.uriel = ""
        self.txt_equipo.SetPlainText(self.uriel + self.victor + self.mariana + self.eduardo)

    def sel_victor(self):
        if self.cb_victor.isChecked():
            print("Victor True")
            self.victor = "Victor\n"
        else:
            print("Victor False")
            self.victor = ""
        self.txt_equipo.SetPlainText(self.uriel + self.victor + self.mariana + self.eduardo)

    def sel_mariana(self):
        if self.cb_mariana.isChecked():
            print("Mariana True")
            self.mariana = "Mariana\n"
        else:
            print("Mariana False")
            self.mariana = ""
        self.txt_equipo.SetPlainText(self.uriel + self.victor + self.mariana + self.eduardo)

    def sel_eduardo(self):
        if self.cb_eduardo.isChecked():
            print("Eduardo True")
            self.eduardo = "Eduardo\n"
        else:
            print("Eduardo False")
            self.eduardo = ""
        self.txt_equipo.SetPlainText(self.uriel + self.victor + self.mariana + self.eduardo)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

