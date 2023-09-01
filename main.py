import pyautogui
import time
from tqdm import tqdm

# def display_progress_bar(duration):
#     width = 50  # Szerokość paska postępu
#     for i in range(1, duration + 1):
#         progress = int((i/duration) * width)
#         bar = "#" * progress + " " * (width - progress)
#         print(f"[{bar}] {i}/{duration} sekund", end="\r", flush=True)
#         time.sleep(1)
#     print()  # Drukuj nową linię po zakończeniu

def automate_tasks(start_number, repetitions):
    baseName = start_number + "_01_"
    pause_duration = 70
    for i in range(1, repetitions + 1):
        # Klik myszką
        pyautogui.click(1165, 975)
        time.sleep(1)
        # Wpisuje nazwę
        suffix = str(i).zfill(2)  # Dodaje zera na początku, jeśli i jest jednocyfrowe
        fullName = baseName + suffix
        pyautogui.write(fullName)
        time.sleep(1)
        # Enter
        pyautogui.press('enter')

        # Przerwa kilkusekundowa
        for _ in tqdm(range(pause_duration), desc="Przerwa", ncols=100):
            time.sleep(1)

        # Klik myszką
        pyautogui.click(442, 376)
        time.sleep(1)
        # Przycisk ->
        pyautogui.press(']')
        time.sleep(1)
        # Przycisk "P"
        pyautogui.press('p')
        time.sleep(2)
        # Tu możesz dodać dodatkową przerwę przed następnym obiegiem pętli, jeśli to konieczne

if __name__ == "__main__":
    start_number = input("Podaj numer albumu: ")
    repetitions = int(input("Podaj liczbę powtórzeń: "))
    time.sleep(3)
    automate_tasks(start_number,repetitions)
