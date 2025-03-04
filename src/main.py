import tkinter as tk
from tkinter import messagebox
from menu import MenuApp

def main():
    try:
        root = tk.Tk()
        root.title("Conversor de Unidades")
        app = MenuApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()