import pyautogui
from serial import Serial

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0  # imposto il tempo di ritardo per ogni chiamata di un entità di pyautogui a 0ms
arduino = Serial ("COM5",
                  9600)  # creo l'oggetto, arduino sulla porta COM5, se sei su ubuntu allora identifica la porta: /dev/tty..
dati = 0
while True:
    try:
        dati = arduino.readline().decode('ascii').split(' ')  # con readline() leggo la singola riga, una volta che ho la riga la decodifico in stringa e con split lo trasformo in una lista.
        x, y, left, right, countLeft = int(dati[0]), int(dati[1]), int(dati[2]), int(dati[3]), int(dati[4].replace('\n', ''))  # assegno in base all'ordine dato sullo sketch di arduino.
        # il quinto dato ha bisogni di essere modificato in quanto contiene uno \n.

        print (f"X: {x} Y: {y} LEFT: {left} RIGHT: {right} COUNT LEFT CLICK: {countLeft}")  # piccolo "debug" per le letture dei dati
        if left:  # se il sensore tattile sinistro è premuto
            pyautogui.leftClick()
        if right:  # se il sensore tattile destro è premuto
            pyautogui.rightClick()
        if countLeft == 2:  # se clicco due volte il sensore tattile sinistro
            pyautogui.doubleClick()

        pyautogui.moveTo(x, y)  # muovo il cursore in base alla coordinate lette dalla seriale.
    except Exception as errore:
        """
        Se il flusso del programma entra qua, significa che:

        1) hai mandato dei dati non codificabili in ascii
        2) hai scollegato durante la lettura, arduino dal computer
        Oppure ci sono degli errori generici.

        """
        print(errore)
        print(dati)
