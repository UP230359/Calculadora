import tkinter as tk
#from tkinter import messagebox
from index import evaluate_postfix
from infix_to_postfix import infix_to_postfix 

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.iconbitmap("./img/ico.ico")
        self.root.title("Calculadora")

        self.entry_input1 = tk.StringVar()
        self.entry_input2 = tk.StringVar()
        self.entry_input3 = tk.StringVar()
        self.shift_mode = False

        self.frameDisplay = tk.Frame(self.root, bg="#cccdcd")
        self.frameDisplay.pack(fill='both', expand=True)

        self.frameTeclado = tk.Frame(self.root, bg="#464648")
        self.frameTeclado.pack(fill='both', expand=True)

        self.create_Display()
        self.create_Teclado()

    def create_Display(self):
        self.label_shift = tk.Label(self.frameDisplay, text="", font=("Arial", 10), fg="#1c1c1c", bg="#cccdcd")
        self.label_shift.grid(row=0, column=1, sticky="nw", padx=10, pady=2)


        self.label_infix = tk.Label(self.frameDisplay, text="Infix", font=("Arial", 10), fg="#1c1c1c", bg="#cccdcd")
        self.label_infix.grid(row=0, column=0, sticky="nw", padx=10, pady=2)

        self.label_postfix = tk.Label(self.frameDisplay, text="Postfix", font=("Arial", 10), fg="#1c1c1c", bg="#cccdcd")
        self.label_postfix.grid(row=2, column=0, sticky="nw", padx=10, pady=2)

        self.label_result = tk.Label(self.frameDisplay, text="Result", font=("Arial", 10), fg="#1c1c1c", bg="#cccdcd")
        self.label_result.grid(row=5, column=0, sticky="nw", padx=10, pady=2)

        #Entry infix
        entry = tk.Entry(self.frameDisplay, textvariable=self.entry_input1, font=("Arial", 20), justify="right", bg="#cccdcd")
        entry.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=2)

        #Entry postfix
        entry = tk.Entry(self.frameDisplay, textvariable=self.entry_input2, font=("Arial", 20), justify="right", state="readonly", readonlybackground="#cccdcd")
        entry.grid(row=4, column=0, columnspan=4, sticky="we", padx=10, pady=2)

        #Entry result
        entry = tk.Entry(self.frameDisplay, textvariable=self.entry_input3, font=("Arial", 20), justify="right", bg="#cccdcd")
        entry.grid(row=6, column=0, columnspan=4, sticky="we", padx=10, pady=2)


    def create_Teclado(self):
        buttons_funciones = [
            ('sen', 'cos', 'tan', '^', '√'),
            ('ln', 'log','e', 'π', 'Shift')
        ]
        buttons_numeros_operadores = [
            ('7', '8', '9', '/', 'C'),
            ('4', '5', '6', '*', '←'),
            ('1', '2', '3', '-', '+'),
            ('0', '.', '(', ')', '=')
        ]
        inversas = [
            'asin', 'acos', 'atan', '^2', '^(1/2)',
            'aln', 'alog', '+/-', '', ''
        ]

        for i, row in enumerate(buttons_funciones):
            for j, button_text in enumerate(row):
                if button_text:
                    button_frame = tk.Frame(self.frameTeclado)
                    button_frame.grid(row=i, column=j, padx=5, pady=(10, 5))

                    label_inverso = tk.Label(button_frame, text=inversas[i * len(row) + j], 
                                            font=("Arial", 8), fg="white", bg="#454746", width=8, height=1)
                    label_inverso.pack(side="top", anchor="ne")

                    button = tk.Button(button_frame, text=button_text, fg="#2e3440", font=("Arial", 14),
                                      command=lambda text=button_text: self.on_click(text), width=4, height=1, bg="#bbc1cd")
                    button.pack(side="bottom", fill="both", expand=True)

        for i, row in enumerate(buttons_numeros_operadores, start=len(buttons_funciones)):
            for j, button_text in enumerate(row):
                if button_text:
                    button_frame = tk.Frame(self.frameTeclado)
                    button_frame.grid(row=i, column=j, padx=0, pady=0)

                    button = tk.Button(button_frame, text=button_text, fg="white", font=("Arial", 14),
                                      command=lambda text=button_text: self.on_click(text), width=4, height=1, bg="#1c1c1c")
                    button.pack(side="bottom", fill="both", expand=True)

    def on_click(self, button_text):
        current_input = self.entry_input1.get()
        function_map = {
            'sen': 'sin',
            'cos': 'cos',
            'tan': 'tan',
            'ln': 'ln',
            'log': 'log'
        }

        if button_text == "=":
            try:
                expression = self.entry_input1.get()

                infixtopostfix = infix_to_postfix(expression)

                result = evaluate_postfix(expression)

                if result is not None:
                    self.entry_input3.set(round(result, 4))
                    self.entry_input2.set(infixtopostfix)
                else:
                    self.entry_input3.set("Error")
            except Exception as e:
                self.entry_input3.set("Error", f"Expresión inválida: {e}")

        elif button_text == "C":
            self.entry_input1.set("")
            self.entry_input2.set("")
            self.entry_input3.set("")
        elif button_text == "←":
            self.entry_input1.set(current_input[:-1])
        elif button_text == "Shift":
            self.shift_mode = not self.shift_mode
            self.actualizar_label_shift()
        elif button_text == "e^x":
            self.entry_input1.set(current_input + "aln(")
        elif button_text == "10^x":
            self.entry_input1.set(current_input + "alog(")
        elif button_text in ['sen', 'cos', 'tan', 'ln', 'log', '√', 'e', '^']:
            if self.shift_mode:
                if button_text == "sen":
                    self.entry_input1.set(current_input + "asin(")
                elif button_text == "cos":
                    self.entry_input1.set(current_input + "acos(")
                elif button_text == "tan":
                    self.entry_input1.set(current_input + "atan(")
                elif button_text == "ln":
                    self.entry_input1.set(current_input + "aln(")
                elif button_text == "log":
                    self.entry_input1.set(current_input + "alog(")
                elif button_text == "^":
                    self.entry_input1.set(current_input + "^2")
                elif button_text == "√":
                    self.entry_input1.set(current_input + "^(1/2)")
                elif button_text == "e":
                    self.entry_input1.set(current_input + "-(")
                self.shift_mode = False
                self.actualizar_label_shift()
            else:
                if button_text == '√':
                    self.entry_input1.set(current_input + "√(")
                else:
                    func = function_map.get(button_text, button_text)
                    self.entry_input1.set(current_input + func + "(")
        elif button_text in ['π', 'e']:
            self.entry_input1.set(current_input + button_text)
        elif button_text in ['(', ')']:
            self.entry_input1.set(current_input + button_text)
        else:
            self.entry_input1.set(current_input + button_text)

    def actualizar_label_shift(self):
        self.label_shift.config(text="Shift" if self.shift_mode else "")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()