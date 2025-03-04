import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from utils.conversions import convertir_longitud, convertir_peso, convertir_temperatura
import tkinter.font as tkfont

class MenuApp:
    def __init__(self, master):
        self.master = master
        master.title("Unit Converter Pro")
        master.geometry("500x600")
        master.configure(bg='#2c3e50')  # Dark background

        # Custom styles
        self.style = ttk.Style()
        self.style.theme_use('clam')  # More modern theme
        self.style.configure('TButton', 
                             font=('Arial', 12, 'bold'), 
                             background='#3498db', 
                             foreground='white')
        self.style.map('TButton', 
                       background=[('active', '#2980b9'), 
                                   ('pressed', '#34495e')])

        # Custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.subtitle_font = tkfont.Font(family="Helvetica", size=14)

        self.create_main_menu()
        self.create_sidebar()

    def create_main_menu(self):
        """Create the main menu with conversion options and improved design."""
        # Main frame
        main_frame = tk.Frame(self.master, bg='#2c3e50')
        main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        title_label = tk.Label(main_frame, text="Unit Converter Pro", 
                               font=self.title_font, 
                               bg='#2c3e50', 
                               fg='white')
        title_label.pack(pady=20)

        # Conversion types with icons and descriptions
        conversion_types = [
            ("📏 Longitud", "Convierte entre metros, kilómetros, centímetros...", self.abrir_menu_longitud),
            ("⚖️ Peso", "Cambia entre kilogramos, gramos, libras", self.abrir_menu_peso),
            ("🌡️ Temperatura", "Transforma Celsius a Fahrenheit y viceversa", self.abrir_menu_temperatura)
        ]

        for emoji, description, command in conversion_types:
            frame = tk.Frame(main_frame, bg='#34495e', bd=2, relief=tk.RAISED)
            frame.pack(pady=10, fill=tk.X)

            # Emoji and text
            label_frame = tk.Frame(frame, bg='#34495e')
            label_frame.pack(side=tk.LEFT, padx=10)

            emoji_label = tk.Label(label_frame, text=emoji, font=("Arial", 24), bg='#34495e', fg='white')
            emoji_label.pack()

            text_frame = tk.Frame(label_frame, bg='#34495e')
            text_frame.pack()

            title_label = tk.Label(text_frame, text=description.split()[1], 
                                   font=self.subtitle_font, 
                                   bg='#34495e', 
                                   fg='#bdc3c7')
            title_label.pack()

            desc_label = tk.Label(text_frame, text=description, 
                                  font=("Arial", 10), 
                                  bg='#34495e', 
                                  fg='#ecf0f1', 
                                  wraplength=250)
            desc_label.pack()

            # Button
            btn = ttk.Button(frame, text="Convertir", command=command)
            btn.pack(side=tk.RIGHT, padx=10)

        # Exit button with custom style
        exit_btn = ttk.Button(main_frame, text="Salir", 
                              command=self.master.quit, 
                              style='Danger.TButton')
        self.style.configure('Danger.TButton', 
                             background='#e74c3c', 
                             foreground='white')
        exit_btn.pack(pady=20)

    def create_sidebar(self):
        """Create a sidebar with additional information and quick links."""
        sidebar = tk.Frame(self.master, bg='#34495e', width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Sidebar title
        tk.Label(sidebar, text="Conversor Pro", 
                 font=self.title_font, 
                 bg='#34495e', 
                 fg='white').pack(pady=20)

        # Quick info sections
        quick_info = [
            ("✅ Precisión", "Conversiones exactas"),
            ("🌐 Múltiples Unidades", "Amplia variedad"),
            ("💡 Fácil de Usar", "Interfaz intuitiva")
        ]

        for icon, text in quick_info:
            frame = tk.Frame(sidebar, bg='#2c3e50', bd=1, relief=tk.RAISED)
            frame.pack(pady=5, padx=10, fill=tk.X)

            tk.Label(frame, text=icon, font=("Arial", 16), bg='#2c3e50', fg='white').pack(side=tk.LEFT, padx=5)
            tk.Label(frame, text=text, font=("Arial", 10), bg='#2c3e50', fg='#bdc3c7').pack(side=tk.LEFT)

    def abrir_menu_longitud(self):
        """Enhanced Longitude Conversion Menu"""
        longitud_window = tk.Toplevel(self.master)
        longitud_window.title("Conversor de Longitud")
        longitud_window.geometry("500x600")
        longitud_window.configure(bg='#2c3e50')

        tk.Label(longitud_window, text="Conversiones de Longitud", 
                 font=self.title_font, 
                 bg='#2c3e50', 
                 fg='white').pack(pady=10)

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
            btn = ttk.Button(longitud_window, text=conv, 
                             command=lambda x=i: self.realizar_conversion_longitud(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def abrir_menu_peso(self):
        """Enhanced Peso Conversion Menu"""
        peso_window = tk.Toplevel(self.master)
        peso_window.title("Conversor de Peso")
        peso_window.geometry("500x600")
        peso_window.configure(bg='#2c3e50')

        tk.Label(peso_window, text="Conversiones de Peso", 
                 font=self.title_font, 
                 bg='#2c3e50', 
                 fg='white').pack(pady=10)

        conversiones = [
            "Kilogramos a Gramos",
            "Gramos a Kilogramos",
            "Libras a Kilogramos",
            "Kilogramos a Libras"
        ]

        for i, conv in enumerate(conversiones, 1):
            btn = ttk.Button(peso_window, text=conv, 
                             command=lambda x=i: self.realizar_conversion_longitud(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def abrir_menu_temperatura(self):
        """Open Temperature Conversion Menu"""
        temperatura_window = tk.Toplevel(self.master)
        temperatura_window.title("Conversor de Temperatura")
        temperatura_window.geometry("400x250")
        temperatura_window.configure(bg='#2c3e50')

        tk.Label(temperatura_window, text="Conversiones de temperatura", 
                 font=self.title_font, 
                 bg='#2c3e50', 
                 fg='white').pack(pady=10)

        conversiones = [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius"
        ]

        for i, conv in enumerate(conversiones, 1):
            btn = tk.Button(temperatura_window, text=conv, 
                            command=lambda x=i: self.realizar_conversion_temperatura(x))
            btn.pack(pady=5, padx=20, fill=tk.X)

    def realizar_conversion_longitud(self, tipo_conversion):
        """Enhanced Longitude Conversion with more details"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:", 
                                           parent=self.master)
            if valor is not None:
                resultado, mensaje = convertir_longitud(tipo_conversion, valor)
                
                # Create a detailed result window
                result_window = tk.Toplevel(self.master)
                result_window.title("Resultado de Conversión")
                result_window.geometry("400x300")
                result_window.configure(bg='#2c3e50')

                tk.Label(result_window, text="Resultado", 
                         font=self.title_font, 
                         bg='#2c3e50', 
                         fg='white').pack(pady=10)

                tk.Label(result_window, text=mensaje, 
                         font=self.subtitle_font, 
                         bg='#2c3e50', 
                         fg='#ecf0f1', 
                         wraplength=350).pack(pady=20)

                ttk.Button(result_window, text="Cerrar", 
                           command=result_window.destroy).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def realizar_conversion_peso(self, tipo_conversion):
        """Enhanced Peso Conversion with more details"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:", 
                                           parent=self.master)
            if valor is not None:
                resultado, mensaje = convertir_peso(tipo_conversion, valor)
                
                # Create a detailed result window
                result_window = tk.Toplevel(self.master)
                result_window.title("Resultado de Conversión")
                result_window.geometry("400x300")
                result_window.configure(bg='#2c3e50')

                tk.Label(result_window, text="Resultado", 
                         font=self.title_font, 
                         bg='#2c3e50', 
                         fg='white').pack(pady=10)

                tk.Label(result_window, text=mensaje, 
                         font=self.subtitle_font, 
                         bg='#2c3e50', 
                         fg='#ecf0f1', 
                         wraplength=350).pack(pady=20)

                ttk.Button(result_window, text="Cerrar", 
                           command=result_window.destroy).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def realizar_conversion_temperatura(self, tipo_conversion):
        """Enhanced Temperature Conversion with more details"""
        try:
            valor = simpledialog.askfloat("Entrada", 
                                           "Ingresa el valor a convertir:", 
                                           parent=self.master)
            if valor is not None:
                resultado, mensaje = convertir_temperatura(tipo_conversion, valor)
                
                # Create a detailed result window
                result_window = tk.Toplevel(self.master)
                result_window.title("Resultado de Conversión")
                result_window.geometry("400x300")
                result_window.configure(bg='#2c3e50')

                tk.Label(result_window, text="Resultado", 
                         font=self.title_font, 
                         bg='#2c3e50', 
                         fg='white').pack(pady=10)

                tk.Label(result_window, text=mensaje, 
                         font=self.subtitle_font, 
                         bg='#2c3e50', 
                         fg='#ecf0f1', 
                         wraplength=350).pack(pady=20)

                ttk.Button(result_window, text="Cerrar", 
                           command=result_window.destroy).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))