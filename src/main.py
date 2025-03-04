import tkinter as tk
from tkinter import messagebox, simpledialog
from menu import MenuApp
import sys
import traceback

def custom_exception_handler(exctype, value, tb):
    """Custom global exception handler to log and display errors."""
    error_message = ''.join(traceback.format_exception(exctype, value, tb))
    messagebox.showerror("Error Fatal", 
                         f"Ha ocurrido un error inesperado:\n{error_message}")
    sys.__excepthook__(exctype, value, tb)

def main():
    try:
        # Set custom exception handler
        sys.excepthook = custom_exception_handler
        
        root = tk.Tk()
        root.title("Conversor de Unidades Pro")

        # Set application icon (replace with your actual icon path)
        try:
            root.iconbitmap('imgs/icon.ico')
        except Exception:
            pass  # Ignore if icon not found
        
        app = MenuApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error Inesperado", 
                             f"Ocurrió un error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()