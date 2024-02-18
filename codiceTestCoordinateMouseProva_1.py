import pyautogui
from pyautogui import moveTo, size

"""
L'attributo di classe .FAILSAFE, se impostato a True, fa sollevare un eccezione se il puntatore si posiziona in uno dei 4 angoli dei nostri schermi,
per risolvere i problemi della dimensioni dello schermo, orientamento e numero di monitor ho trovato questa soluzione. Dato che non è raccomandato di disabilitare .FAILSAFE, 
lo disabilito durante l'uso del dispositivo e alla fine dell'esecuzione lo reimposto a True.

"""
coordinate = [(1921, 1082), (10, 60), (-100, 80), (1678, 44), (3000, -4000), (3000000, 1240000)]    # test che effettuerò, vedete questa struttura dati come una matrice, () indica una tuple, struttura dati in cui i dati sono immutabili.
print(f"Dimensione schermo: {size()}")
pyautogui.FAILSAFE = False
for i in range(len(coordinate)):
    x = coordinate[i][0]
    y = coordinate[i][1]
    moveTo(coordinate[i][0], coordinate[i][1], duration=1)
pyautogui.FAILSAFE = True

