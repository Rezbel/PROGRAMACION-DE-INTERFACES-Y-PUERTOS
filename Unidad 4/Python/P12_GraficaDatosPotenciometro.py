
import serial as conn

arduino= conn.Serial(port="/dev/cu/.usbmodem11401", buadrate=9600, timeout=1)

print("CONEXION CON ARDUINO EXITOSA")
x = [i for i in range(100)]
y = [0 for i in range(100)]
i = 0
from matplotlib import pyplot as plt
while True:
    a = arduino.redline().decode().strip()
    y.pop(0)
    y.append(int(a))
    print(y)
    plt.plot(x, y)
    plt.grid = True
plt.show()
