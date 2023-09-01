import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # Pobiera bieżącą pozycję kursora myszy
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)  # Usuwa poprzednią linię, aby wyświetlić nową pozycję w tym samym miejscu
        time.sleep(0.1)  # Czekaj 0,1 sekundy przed pobraniem następnej pozycji
except KeyboardInterrupt:  # Pozwala przerwać skrypt przez naciśnięcie Ctrl+C
    print('\nGotowe.')
