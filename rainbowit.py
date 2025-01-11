from colored import fg, attr
import tkinter as tk

def rainbow_it(text):
    colors = [
        "#990000",  # Ciemny czerwony
        "#FF6666",  # Jasny czerwony
        "#CC5500",  # Ciemny pomarańczowy
        "#FFB266",  # Jasny pomarańczowy
        "#FFFF66",  # Jasny żółty
        "#CCCC00",  # Ciemny żółty
        "#66FF66",  # Jasny zielony
        "#006600",  # Ciemny zielony
        "#6666FF",  # Jasny niebieski
        "#000099",  # Ciemny niebieski
        "#FF99FF",  # Jasny fioletowy
        "#800080"   # Ciemny fioletowy
    ]
    result_text.delete(1.0, tk.END)  # Clear existing text
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result_text.insert(tk.END, char, color)
    for color in colors:
        result_text.tag_configure(color, foreground=color)

# Example usage
# print_rainbow_text("Miłego dnia! Benio :-)")  # Prints rainbow-colored text

root = tk.Tk()
root.title("Rainbow text")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Wprowadź tekst:")
label.pack(pady=10)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Koloruj", command=lambda: rainbow_it(entry.get()))
button.pack(side=tk.LEFT)

result_text = tk.Text(root, height=1, width=40)
result_text.pack(pady=10)

root.mainloop()