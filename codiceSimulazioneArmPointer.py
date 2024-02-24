import pyautogui
from serial import Serial
pyautogui.FAILSAFE = False
arduino = Serial("COM5", 9600)
dati = 0
while True:
    try:
        # print(arduino.readline().decode())
        dati = arduino.readline().decode('ascii').split(' ')
        # print(dati)
        x, y = int(dati[0]), int(dati[1])
        print(f"X: {x} Y: {y}")
        pyautogui.dragTo(x, y)
    except Exception as errore:
        print(errore)
        print(dati)
