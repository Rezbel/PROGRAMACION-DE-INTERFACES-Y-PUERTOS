
import serial as conn

arduino= conn.Serial(port="/dev/cu/.usbmodem11401", buadrate=9600, timeout=1)

print("CONEXION CON ARDUINO EXITOSA")

while True:
    a= arduino.readline()
    a= a.decode("utf-8")
    a= a.strip()
    print(a)