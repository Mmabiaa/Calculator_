# utils.py

from tkinter import messagebox

def show_error(message):
    """Display an error message box."""
    messagebox.showerror("Error", message)

def is_valid_expression(expression):
    """Check if the given expression is valid."""
    # Basic validation: check for empty input and invalid characters
    if not expression:
        return False
    allowed_chars = set("0123456789+-*/().%√x²sincostanpi!log ")
    return all(char in allowed_chars for char in expression)