import serial
import sys
from PyQt5 import uic, QtGui, QtWidgets, QtCore

qtCreatorFile = "ServomotorPir.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.btn_conectar.clicked.connect(self.conctar)
        self.QtTimer = QtCore.QTimer()
        self.QtTimer.timeout.connect(self.lecturaArduino)
        self.QtTimer.setInterval(1000)
        self.conexion = -1
        self.arduino = None

    def conctar(self):
        if self.conexion == -1:
            self.arduino = serial.Serial(port='com4', baudrate=9600, timeout=10)
            self.btnArduino.setText("Desconectar")
            self.conexion = 1
            self.QtTimer.start()

        if self.conexion == 0:
            self.arduino.open()
            self.btnArduino.setText("Desconectar")
            self.conexion = 1
            self.QtTimer.start()

        if self.conexion == 1:
            self.arduino.close()
            self.btnArduino.setText("Conectar")
            self.conexion = 0
            self.QtTimer.stop()

    def lecturaArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            arduinolectura = self.arduino.readline().decode().strip()
            if arduinolectura != "":
                self.lbEstadoLeds.setText(arduinolectura)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
