import random
import tkinter as tk

def czy_wygralem(p):
    if not 0 <= p <= 1:
        raise ValueError("Prawdopodobieństwo musi być w zakresie od 0 do 1.")
    return random.random() < p

# random.seed(11)
# Przykład użycia
p = 0.08  # Prawdopodobieństwo sukcesu
sukces = 0
def losuj():
    try:
        p = float(entry.get())
        if not 0 <= p <= 1:
            raise ValueError
    except ValueError:
        result_label.config(text="Błędne prawdopodobieństwo. Wprowadź liczbę od 0 do 1.")
        return

    sukces = 0
    ILE = 60
    for _ in range(ILE):
        if czy_wygralem(p):
            sukces += 1

    result_label.config(text=f"Wygrałeś {sukces} razy na {ILE} prób.")

root = tk.Tk()
root.title("Symulacja wygranej")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Prawdopodobieństwo (0-1):")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Losuj", command=losuj)
button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
ILE = 60
for _ in range(ILE):
    if czy_wygralem(p):
        print("\033[93mWygrałeś!\033[0m")
        sukces += 1
    else:
        print("\033[91mPrzegrałeś!\033[0m")
print("Wygrałeś", sukces, "razy na ", ILE, "prób.")