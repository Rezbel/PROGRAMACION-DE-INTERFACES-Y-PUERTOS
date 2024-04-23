import sys
import random
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

qtCreatorFile = "E2_SimulacionDeUnTemporizador.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.startButton.clicked.connect(self.iniciar)
        self.stopButton.clicked.connect(self.detener)
        self.resetButton.clicked.connect(self.reiniciar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timeElapsed = 0

    # Área de los Slots
    def iniciar(self):
        self.timer.start(1000)  # Iniciar temporizador con intervalo de 1 segundo

    def detener(self):
        self.timer.stop()

    def reiniciar(self):
        self.timer.stop()
        self.timeElapsed = 0
        self.update_timer()

    def update_timer(self):
        self.timeElapsed += 1
        self.timerLabel.setText(f"Tiempo transcurrido: {self.timeElapsed} segundos")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

