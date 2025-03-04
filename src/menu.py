import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import tkinter.font as tkfont
from utils.conversions import (
    obtener_lista_unidades_longitud, 
    obtener_lista_unidades_peso, 
    obtener_lista_unidades_temperatura,
    convertir_unidad
)

class MenuApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversor Universal Pro")
        master.geometry("600x700")
        master.configure(bg='#f0f0f0')

        # Custom styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.subtitle_font = tkfont.Font(family="Helvetica", size=14)

        # Main container
        self.main_container = tk.Frame(master, bg='#f0f0f0')
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Hamburger menu
        self.create_hamburger_menu()

        # Conversion frame
        self.conversion_frame = tk.Frame(self.main_container, bg='#ffffff', padx=20, pady=20)
        self.conversion_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Current conversion type
        self.current_conversion_type = None

    def create_hamburger_menu(self):
        """Create a hamburger-style side menu"""
        # Hamburger menu frame
        self.hamburger_frame = tk.Frame(self.main_container, width=250, bg='#2c3e50')
        self.hamburger_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.hamburger_frame.pack_propagate(False)

        # Menu title
        title_label = tk.Label(self.hamburger_frame, text="Conversor Universal", 
                               font=self.title_font, 
                               bg='#2c3e50', 
                               fg='white')
        title_label.pack(pady=20)

        # Conversion types
        conversion_types = [
            ("📏", "Longitud", obtener_lista_unidades_longitud()),
            ("⚖️", "Peso", obtener_lista_unidades_peso()),
            ("🌡️", "Temperatura", obtener_lista_unidades_temperatura())
        ]

        for emoji, tipo, unidades in conversion_types:
            btn = tk.Button(
                self.hamburger_frame, 
                text=f"{emoji} {tipo}", 
                bg='#34495e', 
                fg='white', 
                font=("Arial", 12),
                command=lambda t=tipo, e=emoji, u=unidades: self.setup_conversion_frame(t, e, u)
            )
            btn.pack(fill=tk.X, padx=10, pady=5)

    def setup_conversion_frame(self, conversion_tipo, emoji, unidades):
        """Setup the conversion frame for the selected type"""
        # Clear previous conversion frame
        for widget in self.conversion_frame.winfo_children():
            widget.destroy()

        # Title
        title_label = tk.Label(
            self.conversion_frame, 
            text=f"{emoji} Conversión de {conversion_tipo}", 
            font=self.title_font, 
            bg='#ffffff'
        )
        title_label.pack(pady=10)

        # Origen frame
        origen_frame = tk.Frame(self.conversion_frame, bg='#ffffff')
        origen_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(origen_frame, text="Unidad de Origen", font=("Arial", 12), bg='#ffffff').pack(side=tk.LEFT)

        # Unidades de origen
        self.origen_combobox = ttk.Combobox(
            origen_frame, 
            values=unidades,
            state="readonly",
            width=20
        )
        self.origen_combobox.pack(side=tk.RIGHT)

        # Destino frame
        destino_frame = tk.Frame(self.conversion_frame, bg='#ffffff')
        destino_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(destino_frame, text="Unidad de Destino", font=("Arial", 12), bg='#ffffff').pack(side=tk.LEFT)

        # Unidades de destino
        self.destino_combobox = ttk.Combobox(
            destino_frame, 
            values=unidades,
            state="readonly",
            width=20
        )
        self.destino_combobox.pack(side=tk.RIGHT)

        # Valor input frame
        valor_frame = tk.Frame(self.conversion_frame, bg='#ffffff')
        valor_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(valor_frame, text="Valor", font=("Arial", 12), bg='#ffffff').pack(side=tk.LEFT)

        self.valor_entry = tk.Entry(valor_frame, font=("Arial", 12), width=20)
        self.valor_entry.pack(side=tk.RIGHT)

        # Conversion button
        convert_btn = tk.Button(
            self.conversion_frame, 
            text="Convertir", 
            command=self.realizar_conversion,
            bg='#3498db', 
            fg='white', 
            font=("Arial", 12)
        )
        convert_btn.pack(pady=10)

        # Resultado frame
        self.resultado_frame = tk.Frame(self.conversion_frame, bg='#ffffff')
        self.resultado_frame.pack(fill=tk.X, padx=20, pady=10)

        # Formula frame
        self.formula_frame = tk.Frame(self.conversion_frame, bg='#ffffff')
        self.formula_frame.pack(fill=tk.X, padx=20, pady=10)

        # Store current conversion type
        self.current_conversion_type = conversion_tipo

    def realizar_conversion(self):
            """Perform the conversion based on selected units"""
        #try:
            # Validate input
            if not self.origen_combobox.get() or not self.destino_combobox.get():
                messagebox.showwarning("Advertencia", "Selecciona unidades de origen y destino")
                return

            valor = float(self.valor_entry.get())
            origen = self.origen_combobox.get()
            destino = self.destino_combobox.get()

            # Clear previous results
            for widget in self.resultado_frame.winfo_children():
                widget.destroy()
            for widget in self.formula_frame.winfo_children():
                widget.destroy()

            # Perform conversion
            resultado, mensaje, formula = convertir_unidad(origen, destino, valor)

            # Display result
            tk.Label(
                self.resultado_frame, 
                text=f"Resultado: {resultado} {destino}", 
                font=("Arial", 14, "bold"), 
                bg='#ffffff'
            ).pack()

            # Display formula
            tk.Label(
                self.formula_frame, 
                text=f"Fórmula: {formula}", 
                font=("Arial", 10), 
                bg='#ffffff', 
                wraplength=500
            ).pack()

        #except ValueError:
            #messagebox.showerror("Error", "Ingresa un valor numérico válido")
        #except Exception as e:
            #messagebox.showerror("Error", str(e))

