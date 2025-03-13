import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Alineación Horizontal de Entry")

        # Crear un marco para alinear ambos Entry
        self.frameDisplay = tk.Frame(root)
        self.frameDisplay.pack(padx=10, pady=10, fill="x")

        # Variable compartida para ambos Entry (puedes cambiar esto si cada uno necesita su propio texto)
        self.entry_input1 = tk.StringVar()
        self.entry_input2 = tk.StringVar()

        # Entry 1 (Izquierda)
        self.entry1 = tk.Entry(self.frameDisplay, textvariable=self.entry_input1, font=("Arial", 20), justify="left", width=10, bg="#cccdcd")
        self.entry1.grid(row=0, column=0, sticky="we", padx=5, pady=10)

        # Entry 2 (Derecha)
        self.entry2 = tk.Entry(self.frameDisplay, textvariable=self.entry_input2, font=("Arial", 20), justify="right", width=10, bg="#cccdcd")
        self.entry2.grid(row=0, column=1, sticky="we", padx=5, pady=10)

        # Expande las columnas para que ambos Entry tengan el mismo tamaño
        self.frameDisplay.columnconfigure(0, weight=1)
        self.frameDisplay.columnconfigure(1, weight=1)

root = tk.Tk()
app = App(root)
root.mainloop()