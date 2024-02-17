import pyautogui
from pyautogui import moveTo, size

"""
L'attributo di classe .FAILSAFE, se impostato a True, fa sollevare un eccezione se il puntatore si posiziona in uno dei 4 angoli dei nostri schermi,
per risolvere i problemi della dimensioni dello schermo, orientamento e numero di monitor ho trovato questa soluzione. Dato che non è raccomandato di disabilitare .FAILSAFE, 
faccio una sorta di gioco attacca e stacca. La disabilito quando parto dall'angolo dello schermo o da fuori lo schermo e lo riattivo quando mi muovo in delle coordinate accettabili per lo schermo
"""


coordinate = [(1921, 1082), (10, 60), (-100, 80), (1678, 44), (3000, -4000), (0, 0)]    # test che effettuerò, vedete questa struttura dati come una matrice, () indica una tuple, struttura dati in cui i dati sono immutabili.
print(f"Dimensione schermo: {size()}")
for i in range(len(coordinate)):
    try:
        x = coordinate[i][0]
        y = coordinate[i][1]
        moveTo(coordinate[i][0], coordinate[i][1])
        pyautogui.FAILSAFE = True   # abilito il .FAILSAFE

    except Exception as error:
        print(f"Punto non valido: P({coordinate[i][0]}; {coordinate[i][1]})\nEccezione: {error}\n\n")
        pyautogui.FAILSAFE = False  # disabilito il .FAILSAFE
print(pyautogui.FAILSAFE)   # prova per vedere se il .FAILSAFE alla fine dell'esecuzione è attivo
