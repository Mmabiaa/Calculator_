# gui.py

from tkinter import *
from tkinter import messagebox
from calculator import Calculator
from utils import show_error  # Ensure you have this utility for error handling

class CalculatorApp:
    def __init__(self):
        self.root = Tk()
        self.calculator = Calculator()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Simple Calculator - Mmabiaa")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        self.root.configure(bg='pink')

        # Entry widget for user input
        self.entry = Entry(self.root, font=("Arial", 24), borderwidth=5, relief="ridge")
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Create buttons for the calculator
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('+', 1, 0), ('-', 1, 1), ('*', 1, 2), ('/', 1, 3), ('%', 1, 4), ('√', 1, 5),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('cos', 2, 3), ('sin', 2, 4), ('tan', 2, 5),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('pi', 3, 3), ('x²', 3, 4), ('1/x', 3, 5),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('!', 4, 3), ('(', 4, 4), (')', 4, 5),
            ('0', 5, 0), ('.', 5, 1), ('log', 5, 2), ('DEL', 5, 3), ('=', 5, 4), ('C', 5, 5)
        ]

        for (text, row, col) in buttons:
            button = Button(self.root,
                            text=text,
                            font=("Arial", 18),
                            command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Configure grid weights for resizing
        for i in range(6):
            self.root.grid_rowconfigure(i + 1, weight=1)
            self.root.grid_columnconfigure(i % len(buttons[0]), weight=1)

    def on_button_click(self, char):
        if char == "=":
            result = self.calculator.evaluate(self.entry.get())
            self.clear()
            self.entry.insert(END, result)
        elif char == "DEL":
            self.backspace()
        elif char == "C":
            self.clear()
        elif char in ['sin', 'cos', 'tan', '√', 'x²', '1/x', 'log', 'pi', '!', '%']:
            result = self.calculator.advanced_operations(char, self.entry.get())
            self.clear()
            self.entry.insert(END, result)
        else:
            self.entry.insert(END, char)

    def clear(self):
        """Clear the entry field."""
        self.entry.delete(0, END)

    def backspace(self):
        """Delete the last character in the entry field."""
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) - 1)

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

# Ensure this file is executed directly to run the application
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()