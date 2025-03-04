import tkinter as tk
from tkinter import messagebox, simpledialog
from utils.conversions import convertir_longitud, convertir_peso, convertir_temperatura

class MenuApp:
    def __init__(self, master):
        self.master = master
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')

        self.create_main_menu()

    def create_main_menu(self):
        """Create the main menu with conversion options."""
        tk.Label(self.master, text="Conversor de Unidades", 
                 font=("Arial", 16, "bold"), 
                 bg='#f0f0f0').pack(pady=20)

        conversion_types = [
            ("Longitud", self.abrir_menu_longitud),
            ("Peso", self.abrir_menu_peso),
            ("Temperatura", self.abrir_menu_temperatura)
        ]

        for label, command in conversion_types:
            btn = tk.Button(self.master, text=label, 
                            command=command, 
                            width=20, 
                            font=("Arial", 12))
            btn.pack(pady=10)

        tk.Button(self.master, text="Salir", 
                  command=self.master.quit, 
                  width=20, 
                  font=("Arial", 12), 
                  bg='#ff6b6b').pack(pady=20)

    def abrir_menu_longitud(self):
        """Open Longitude Conversion Menu"""
        longitud_window = tk.Toplevel(self.master)
        longitud_window.title("Conversor de Longitud")
        longitud_window.geometry("400x500")

        tk.Label(longitud_window, text="Conversiones de Longitud", 
                 font=("Arial", 14, "bold")).pack(pady=10)

        conversiones = [
            "Metros a Kilómetros",
            "Kilómetros a Metros",
            "Centímetros a Metros",
            "Metros a Centímetros",
            "Milímetros a Centímetros",
            "Centímetros a Milímetros",
            "Metros a Milímetros",
            "Milímetros a Metros",
            "Centímetros a Kilómetros",
            "Kilómetros a Centímetros"
        ]

        for i, conv in enumerate(conversiones, 1):
            btn = tk.Button(longitud_window, text=conv, 
                            command=lambda x=i: self.realizar_conversion_longitud(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def abrir_menu_peso(self):
        """Open Weight Conversion Menu"""
        peso_window = tk.Toplevel(self.master)
        peso_window.title("Conversor de Peso")
        peso_window.geometry("400x300")

        tk.Label(peso_window, text="Conversiones de Peso", 
                 font=("Arial", 14, "bold")).pack(pady=10)

        conversiones = [
            "Kilogramos a Gramos",
            "Gramos a Kilogramos",
            "Libras a Kilogramos",
            "Kilogramos a Libras"
        ]

        for i, conv in enumerate(conversiones, 1):
            btn = tk.Button(peso_window, text=conv, 
                            command=lambda x=i: self.realizar_conversion_peso(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def abrir_menu_temperatura(self):
        """Open Temperature Conversion Menu"""
        temperatura_window = tk.Toplevel(self.master)
        temperatura_window.title("Conversor de Temperatura")
        temperatura_window.geometry("400x250")

        tk.Label(temperatura_window, text="Conversiones de Temperatura", 
                 font=("Arial", 14, "bold")).pack(pady=10)

        conversiones = [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius"
        ]

        for i, conv in enumerate(conversiones, 1):
            btn = tk.Button(temperatura_window, text=conv, 
                            command=lambda x=i: self.realizar_conversion_temperatura(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def realizar_conversion_longitud(self, tipo_conversion):
        """Perform Longitude Conversion"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:")
            if valor is not None:
                _, mensaje = convertir_longitud(tipo_conversion, valor)
                messagebox.showinfo("Resultado", mensaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def realizar_conversion_peso(self, tipo_conversion):
        """Perform Weight Conversion"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:")
            if valor is not None:
                _, mensaje = convertir_peso(tipo_conversion, valor)
                messagebox.showinfo("Resultado", mensaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def realizar_conversion_temperatura(self, tipo_conversion):
        """Perform Temperature Conversion"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:")
            if valor is not None:
                _, mensaje = convertir_temperatura(tipo_conversion, valor)
                messagebox.showinfo("Resultado", mensaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))