def convertir_longitud(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de longitud."""
    conversiones = {
        1: (valor / 1000, f"{valor} metros son {valor / 1000} kilómetros"),
        2: (valor * 1000, f"{valor} kilómetros son {valor * 1000} metros"),
        3: (valor / 100, f"{valor} centímetros son {valor / 100} metros"),
        4: (valor * 100, f"{valor} metros son {valor * 100} centímetros"),
        5: (valor / 10, f"{valor} milímetros son {valor / 10} centímetros"),
        6: (valor * 10, f"{valor} centímetros son {valor * 10} milímetros"),
        7: (valor * 1000, f"{valor} metros son {valor * 1000} milímetros"),
        8: (valor / 1000, f"{valor} milímetros son {valor / 1000} metros"),
        9: (valor / 100000, f"{valor} centimetros son {valor / 100000} kilometros"),
        10: (valor * 100000, f"{valor} kilometros son {valor * 100000} centimetros")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))

def convertir_peso(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de peso."""
    conversiones = {
        1: (valor * 1000, f"{valor} kilogramos son {valor * 1000} gramos"),
        2: (valor / 1000, f"{valor} gramos son {valor / 1000} kilogramos"),
        3: (valor * 0.453592, f"{valor} libras son {valor * 0.453592} kilogramos"),
        4: (valor * 2.20462, f"{valor} kilogramos son {valor * 2.20462} libras")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))

def convertir_temperatura(tipo_conversion, valor):
    """Convierte valores entre diferentes unidades de temperatura."""
    conversiones = {
        1: ((valor * 9/5) + 32, f"{valor} grados Celsius son {(valor * 9/5) + 32} grados Fahrenheit"),
        2: ((valor - 32) * 5/9, f"{valor} grados Fahrenheit son {(valor - 32) * 5/9} grados Celsius")
    }
    
    return conversiones.get(tipo_conversion, (None, "Opción no válida"))