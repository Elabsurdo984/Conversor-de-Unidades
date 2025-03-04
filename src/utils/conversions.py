def convertir_longitud(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de longitud con mayor precisión."""
    if not isinstance(valor, (int, float)):
        raise ValueError("El valor debe ser un número")
    
    conversiones = {
        1: (round(valor / 1000, 6), f"{valor} metros son {round(valor / 1000, 6)} kilómetros"),
        2: (round(valor * 1000, 2), f"{valor} kilómetros son {round(valor * 1000, 2)} metros"),
        3: (round(valor / 100, 4), f"{valor} centímetros son {round(valor / 100, 4)} metros"),
        4: (round(valor * 100, 2), f"{valor} metros son {round(valor * 100, 2)} centímetros"),
        5: (round(valor / 10, 2), f"{valor} milímetros son {round(valor / 10, 2)} centímetros"),
        6: (round(valor * 10, 2), f"{valor} centímetros son {round(valor * 10, 2)} milímetros"),
        7: (round(valor * 1000, 2), f"{valor} metros son {round(valor * 1000, 2)} milímetros"),
        8: (round(valor / 1000, 6), f"{valor} milímetros son {round(valor / 1000, 6)} metros"),
        9: (round(valor / 100000, 6), f"{valor} centimetros son {round(valor / 100000, 6)} kilometros"),
        10: (round(valor * 100000, 2), f"{valor} kilometros son {round(valor * 100000, 2)} centimetros")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))

def convertir_peso(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de peso con mayor precisión y validación."""
    if not isinstance(valor, (int, float)):
        raise ValueError("El valor debe ser un número")
    
    conversiones = {
        1: (round(valor * 1000, 2), f"{valor} kilogramos son {round(valor * 1000, 2)} gramos"),
        2: (round(valor / 1000, 4), f"{valor} gramos son {round(valor / 1000, 4)} kilogramos"),
        3: (round(valor * 0.453592, 4), f"{valor} libras son {round(valor * 0.453592, 4)} kilogramos"),
        4: (round(valor * 2.20462, 4), f"{valor} kilogramos son {round(valor * 2.20462, 4)} libras")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))

def convertir_temperatura(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de temperatura con mayor precisión y validación."""
    if not isinstance(valor, (int, float)):
        raise ValueError("El valor debe ser un número")
    
    conversiones = {
        1: (round((valor * 9/5) + 32, 2), f"{valor} grados Celsius son {round((valor * 9/5) + 32, 2)} grados Fahrenheit"),
        2: (round((valor - 32) * 5/9, 2), f"{valor} grados Fahrenheit son {round((valor - 32) * 5/9, 2)} grados Celsius")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))

# Nuevas funciones adicionales
def obtener_lista_unidades_longitud():
    """Retorna una lista completa de unidades de longitud."""
    return [
        "Metros", "Kilómetros", "Centímetros", "Milímetros", 
        "Pulgadas", "Pies", "Yardas", "Millas"
    ]

def obtener_lista_unidades_peso():
    """Retorna una lista completa de unidades de peso."""
    return [
        "Kilogramos", "Gramos", "Libras", "Onzas", 
        "Toneladas", "Miligramos"
    ]