import tkinter as tk

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Pole wprowadzania z domyślną wartością")

# Tworzenie zmiennej typu StringVar z domyślną wartością
default_value = "Domyślna wartość"
entry_var = tk.StringVar()
entry_var.set(default_value)  # Ustawienie domyślnej wartości

# Tworzenie pola wprowadzania z domyślną wartością
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

# Funkcja obsługująca przycisk
def print_entry_value():
    value = entry_var.get()
    print(f"Wprowadzona wartość: {value}")

# Przycisk do wydrukowania wartości wpisanej w polu
button = tk.Button(root, text="Wypisz wartość", command=print_entry_value)
button.pack()

# Rozpoczęcie pętli głównej
root.mainloop()
