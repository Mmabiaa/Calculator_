from tkinter import *
from tkinter import messagebox
import math  # Importing math module for mathematical functions
from calculator import Calculator
from utils import show_error  # Ensure you have this utility for error handling
from memory import Memory  # Importing the Memory class

class CalculatorApp:
    def __init__(self):
        self.root = Tk()
        self.calculator = Calculator()
        self.memory = Memory()  # Initialize Memory instance
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Simple Calculator - Mmabiaa")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        self.root.configure(bg='black')

        # Entry widget for user input
        entry = Entry(self.root, font=("Arial", 24), borderwidth=5, relief="ridge")
        entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
        self.entry = entry
        
        # Create buttons for the calculator
        self.create_buttons(self.root)

    def create_buttons(self, root):
        # A list of Buttons including memory functions
        buttons = [
            ('M+', 1, 0), ('M-', 1, 1), ('MR', 1, 2), ('MC', 1, 3), ('%', 1, 4), ('√', 1, 5),
            ('*', 2, 0), ('/', 2, 1), ('+', 2, 2), ('-', 2, 3), ('(', 2, 4), (')', 2, 5),
            ('sin', 3, 0), ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('x²', 3, 4), ('pi', 3, 5),
            ('cos', 4, 0), ('4', 4, 1), ('5', 4, 2), ('6', 4, 3), ('1/x', 4, 4), ('!', 4, 5),
            ('tan', 5, 0), ('1', 5, 1), ('2', 5, 2), ('3', 5, 3), ('=', 5, 4), ('.', 5,5),
            ('DEL',6 ,1),('0',6 ,2),('C',6 ,3)
        ]
        
        # A for loop to help arrange the buttons in text, rows and columns
        for (text,row,col) in buttons:
            if text == '=':
                bg_color = 'red'
                fg_color = 'white'
                bd =20
            elif text == 'DEL':
                bg_color = 'orange'
                fg_color = 'white'
            elif text == 'C':
                bg_color = 'blue'
                fg_color = 'black'
            elif text in ['+', '-', '*', '/']:
                bg_color = 'orange'
                fg_color = 'black'
            elif text in ['1','2','3','4','5','6','7','8','9','0']:
                bg_color = 'aqua'
                fg_color = 'black'
            elif text in ['cos','sin','tan','pi','x²','1/x','!','(',')', '√', '%','.']:
                bg_color = 'black'
                fg_color = 'white'
            else:
                bg_color = 'red'
                fg_color = 'white'

            # Creating a button using the variable name 'button'
            button = Button(root,
                            text=text,
                            font=("Arial",18),
                            command=lambda t=text: self.on_button_click(t),
                            fg=fg_color,
                            bg=bg_color
                            )
            button.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")

        # Allow the grid to be positioned relatively that when the window is resized
        for i in range(1 ,6):
            root.grid_rowconfigure(i , weight=1)
            root.grid_columnconfigure(i-1 , weight=1)

    def on_button_click(self,char):
        if char == "=":
            try:
                equation = str(eval(self.entry.get()))
                self.entry.delete(0 , END)
                self.entry.insert(END , equation)
            except Exception as e:
                messagebox.showerror("Error" , "Invalid Expression")
                self.clear()
        elif char == "DEL":
            self.backspace()
        elif char == "C":
            self.clear()
        
        # Memory operations
        elif char == "M+":
            try:
                value_to_add = float(self.entry.get())
                self.memory.add(value_to_add)
                messagebox.showinfo("Memory", f"Added {value_to_add} to memory.")
            except ValueError:
                messagebox.showerror("Error", "Invalid Input for M+")
        
        elif char == "M-":
            try:
                value_to_subtract = float(self.entry.get())
                self.memory.subtract(value_to_subtract)
                messagebox.showinfo("Memory", f"Subtracted {value_to_subtract} from memory.")
            except ValueError:
                messagebox.showerror("Error", "Invalid Input for M-")
        
        elif char == "MR":
            recalled_value = self.memory.recall()
            self.entry.delete(0 , END)
            self.entry.insert(END , recalled_value)
        
        elif char == "MC":
            self.memory.clear()
            messagebox.showinfo("Memory", "Memory cleared.")
        
        elif char in ['sin' ,'cos' ,'tan' ,'√' ,'x²' ,'1/x' ,'log' ,'pi' ,'!' ,'%']:
            try:
                if char == 'sin':
                    equation = str(math.sin(math.radians(float(self.entry.get()))))
                elif char == 'cos':
                    equation = str(math.cos(math.radians(float(self.entry.get()))))
                elif char == 'tan':
                    equation = str(math.tan(math.radians(float(self.entry.get()))))
                elif char == '√':
                    equation = str(math.sqrt(float(self.entry.get())))
                elif char == 'x²':
                    equation = str(math.pow(float(self.entry.get()),2))
                elif char == '1/x':
                    equation = str(1 / float(self.entry.get()))
                elif char == 'log':
                    equation = str(math.log10(float(self.entry.get())))
                elif char == 'pi':
                    equation = str(math.pi)
                elif char == '!':
                    equation = str(math.factorial(int(self.entry.get())))
                elif char == '%':
                    equation = str(float(self.entry.get()) /100)

                self.entry.delete(0 , END)
                self.entry.insert(END , equation)
                
            except Exception as e:
                messagebox.showerror("Error" , "Invalid Input")
                self.clear()
                
        else:
            if char == ".":
                text = self.entry.get()
                last_part = text.split()[-1] if " " in text else text.split("+-*/")[-1]
                if "." in last_part:
                    return
            self.entry.insert(END , char)

    def clear(self):
        """Clear the entry field."""
        self.entry.delete(0 , END)

    def backspace(self):
        """Delete the last character in the entry field."""
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) -1)

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

