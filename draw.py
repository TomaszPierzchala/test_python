import random
import tkinter as tk

_SUCCESSES = 0
_HOW_MANY = 60
_P = 0.08
# random.seed(11)

def did_I_win(p):
    if not 0 <= p <= 1:
        raise ValueError("Probability must be between 0 and 1.")
    return random.random() < p

def draw():
    try:
        p = float(entry.get())
        if not 0 <= p <= 1:
            raise ValueError
    except ValueError:
        result_label.config(text="Incorrect probability. Enter a number between 0 and 1.")
        return

    success = _SUCCESSES
    HOW_MANY = _HOW_MANY
    for _ in range(HOW_MANY):
        if did_I_win(p):
            success += 1

    result_label.config(text=f"You won {success} times of {HOW_MANY} attempts.")

root = tk.Tk()
root.title("Winning Simulation")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Propability (0-1):")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.insert(0, _P)  # Set initial value
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Draw", command=draw)
button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
