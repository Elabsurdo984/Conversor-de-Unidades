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

def obtener_lista_unidades_temperatura():
    """Retorna una lista completa de unidades de temperatura."""
    return [
        "Celsius", "Fahrenheit", "Kelvin"
    ]

def convertir_unidad(origen, destino, valor):
    """
    Conversión dinámica entre diferentes unidades con fórmula explicativa.
    
    Args:
        origen (str): Unidad de origen
        destino (str): Unidad de destino
        valor (float): Valor a convertir
    
    Returns:
        tuple: (resultado convertido, mensaje, fórmula utilizada)
    """
    # Conversiones de Longitud
    longitud_conversiones = {
        # De Metros a...
        ("Metros", "Kilómetros"): (valor / 1000, f"{valor} metros = {valor} ÷ 1000", "X ÷ 1000"),
        ("Metros", "Centímetros"): (valor * 100, f"{valor} metros = {valor} × 100", "X × 100"),
        ("Metros", "Milímetros"): (valor * 1000, f"{valor} metros = {valor} × 1000", "X × 1000"),
        ("Metros", "Pulgadas"): (valor * 39.37, f"{valor} metros = {valor} × 39.37", "X × 39.37"),
        ("Metros", "Pies"): (valor * 3281, f"{valor} metros = {valor} × 3281", "X × 3281"),
        ("Metros", "Yardas"): (valor * 1094, f"{valor} metros = {valor} × 1094", "X × 1094"),
        ("Metros", "Millas"): (valor / 1609, f"{valor} metros = {valor} ÷ 1609", "X ÷ 1609"),

        # De Kilometros a...
        ("Kilómetros", "Metros"): (valor * 1000, f"{valor} kilómetros = {valor} × 1000", "X × 1000"),
        ("Kilómetros", "Centímetros"): (valor * 100000, f"{valor} kilómetros = {valor} × 100000", "X × 100000"),
        ("Kilómetros", "Milimetros"): (valor * 1000000, f"{valor} kilómetros = {valor} × 1000000", "X × 1000000"),
        ("Kilómetros", "Pulgada"): (valor * 39370, f"{valor} kilómetros = {valor} × 39370", "X × 39370"),
        ("Kilómetros", "Pies"): (valor * 3281, f"{valor} kilómetros = {valor} × 3281", "X × 3281"),
        ("Kilómetros", "Yardas"): (valor * 1094, f"{valor} kilómetros = {valor} × 1094", "X × 1094"),
        ("Kilómetros", "Millas"): (valor / 1609, f"{valor} kilómetros = {valor} ÷ 1609", "X ÷ 1609"),

        # De Centimetros a...
        ("Centímetros", "Metros"): (valor / 100, f"{valor} centímetros = {valor} ÷ 100", "X ÷ 100"),
        ("Centímetros", "Kilometros"): (valor / 100000, f"{valor} centímetros = {valor} ÷ 100000", "X ÷ 100000"),
        ("Centímetros", "Pulgadas"): (valor / 2.54, f"{valor} centímetros = {valor} ÷ 2.54", "X ÷ 2.54"),
        ("Centímetros", "Milímetros"): (valor * 10, f"{valor} centímetros = {valor} × 10", "X × 10"),
        ("Centímetros", "Pies"): (valor / 30.48, f"{valor} centímetros = {valor} ÷ 30.48", "X ÷ 30.48"),
        ("Centímetros", "Yardas"): (valor / 91.44, f"{valor} centímetros = {valor} ÷ 91.44", "X ÷ 91.44"),
        ("Centímetros", "Millas"): (valor / 160900, f"{valor} centímetros = {valor} ÷ 160900", "X ÷ 160900"),

        # De Milimetros a...
        ("Milímetros", "Metros"): (valor / 1000, f"{valor} milímetros = {valor} ÷ 1000", "X ÷ 1000"),
        ("Milímetros", "Kilometros"): (valor / 1000000, f"{valor} milímetros = {valor} ÷ 1000000", "X ÷ 1000000"),
        ("Milímetros", "Pulgadas"): (valor / 25.4, f"{valor} milímetros = {valor} ÷ 25.4", "X ÷ 25.4"),
        ("Milímetros", "Pies"): (valor / 304.8, f"{valor} milímetros = {valor} ÷ 304.8", "X ÷ 304.8"),
        ("Milímetros", "Yardas"): (valor / 914.4, f"{valor} milímetros = {valor} ÷ 914.4", "X ÷ 914.4"),
        ("Milímetros", "Centímetros"): (valor / 10, f"{valor} milímetros = {valor} ÷ 10", "X ÷ 10"),
        ("Milimetros", "Millas"): (valor / 1609000, f"{valor}  = {valor} ÷ 1609000", "X ÷ 1609000"),

        # De Pulgadas a... 
        ("Pulgadas", "Centímetros"): (valor * 2.54, f"{valor} pulgadas = {valor} × 2.54", "X × 2.54"),
        ("Pulgadas", "Milímetros"): (valor * 25.4, f"{valor} pulgadas = {valor} × 25.4", "X × 25.4"),
        ("Pulgadas", "Pies"): (valor / 12, f"{valor} pulgadas = {valor} ÷ 12", "X ÷ 12"),
        ("Pulgadas", "Metros"): (valor / 39.37, f"{valor} pulgadas = {valor} ÷ 39.37", "X ÷ 39.37"),
        ("Pulgadas", "Kilómetros"): (valor / 39370, f"{valor} pulgadas = {valor} ÷ 39370", "X ÷ 39370"),
        ("Pulgadas", "Yardas"): (valor / 36, f"{valor} pulgadas = {valor} ÷ 36", "X ÷ 36"),
        ("Pulgadas", "Millas"): (valor / 63360, f"{valor} pulgadas = {valor} ÷ 63360", "X ÷ 63360"),

        # De Pies a... 
        ("Pies", "Pulgadas"): (valor * 12, f"{valor} pies = {valor} × 12", "X × 12"),
        ("Pies", "Metros"): (valor / 3.281, f"{valor} pies = {valor} ÷ 3.281", "X ÷ 3.281"),
        ("Pies", "Centímetros"): (valor * 30.48, f"{valor} pies = {valor} × 30.48", "X × 30.48"),
        ("Pies", "Milímetros"): (valor * 304.8, f"{valor} pies = {valor} × 304.8", "X × 304.8"),
        ("Pies", "Kilómetros"): (valor / 3281, f"{valor} pies = {valor} ÷ 3281", "X ÷ 3281"),
        ("Pies", "Yardas"): (valor / 3, f"{valor} pies = {valor} ÷ 3", "X ÷ 3"),
        ("Pies", "Millas"): (valor / 5280, f"{valor} pies = {valor} ÷ 5280", "X ÷ 5280"),

        # De Yardas a... 
        ("Yardas", "Metros"): (valor / 1.094, f"{valor} yardas = {valor} ÷ 1.094", "X ÷ 1.094"),
        ("Yardas", "Centímetros"): (valor * 91.44, f"{valor} yardas = {valor} × 91.44", "X × 91.44"),
        ("Yardas", "Milímetros"): (valor * 914.4, f"{valor} yardas = {valor} × 914.4", "X × 914.4"),
        ("Yardas", "Pulgadas"): (valor * 36, f"{valor} yardas = {valor} × 36", "X × 36"),
        ("Yardas", "Pies"): (valor * 3, f"{valor} yardas = {valor} × 3", "X × 3"),
        ("Yardas", "Kilómetros"): (valor / 1094, f"{valor} yardas = {valor} ÷ 1094", "X ÷ 1094"),
        ("Yardas", "Millas"): (valor / 1760, f"{valor} yardas = {valor} ÷ 1760", "X ÷ 1760"),

        # De Millas a... 
        ("Millas", "Metros"): (valor * 1609, f"{valor} millas = {valor} × 1609", "X × 1609"),
        ("Millas", "Kilómetros"): (valor * 1.609, f"{valor} millas = {valor} × 1.609", "X × 1.609"),
        ("Millas", "Centímetros"): (valor * 160900, f"{valor} millas = {valor} × 160900", "X × 160900"),
        ("Millas", "Milímetros"): (valor * 1609000, f"{valor} millas = {valor} × 1609000", "X × 1609000"),
        ("Millas", "Pulgadas"): (valor * 63360, f"{valor} millas = {valor} × 63360", "X × 63360"),
        ("Millas", "Pies"): (valor * 5280, f"{valor} millas = {valor} × 5280", "X × 5280"),
        ("Millas", "Yardas"): (valor * 1760, f"{valor} millas = {valor} × 1760", "X × 1760"),
    }

    # Conversiones de Peso
    peso_conversiones = {
        # De Gramos a...
        ("Gramos", "Kilogramos"): (valor / 1000, f"{valor} gramos = {valor} ÷ 1000", "X ÷ 1000"),
        ("Gramos", "Libras"): (valor / 454, f"{valor} gramos = {valor} ÷ 454", "X ÷ 454"),
        ("Gramos", "Onzas"): (valor / 28.35, f"{valor} gramos = {valor} ÷ 28.35", "X ÷ 28.35"),
        ("Gramos", "Toneladas"): (valor / 1000000, f"{valor} gramos = {valor} ÷ 1000000", "X ÷ 1000000"),
        ("Gramos", "Miligramos"): (valor * 1000, f"{valor} gramos = {valor} × 1000", "X × 1000"),

        # De Kilogramos a...
        ("Kilogramos", "Gramos"): (valor * 1000, f"{valor} kilogramos = {valor} × 1000", "X × 1000"),
        ("Kilogramos", "Libras"): (valor * 2.20462, f"{valor} kilogramos = {valor} × 2.20462", "X × 2.20462"),
        ("Kilogramos", "Onzas"): (valor * 35.274, f"{valor} kilogramos = {valor} × 35.274", "X × 35.274"),
        ("Kilogramos", "Toneladas"): (valor / 1000, f"{valor} kilogramos = {valor} ÷ 1000", "X ÷ 1000"),
        ("Kilogramos", "Miligramos"): (valor * 1000000, f"{valor} kilogramos = {valor} × 1000000", "X × 1000000"),

        # De Libras a...
        ("Libras", "Gramos"): (valor * 454, f"{valor} libras = {valor} × 454", "X × 454"),
        ("Libras", "Kilogramos"): (valor / 2.20462, f"{valor} libras = {valor} ÷ 2.20462", "X ÷ 2.20462"),
        ("Libras", "Onzas"): (valor * 16, f"{valor} libras = {valor} × 16", "X × 16"),
        ("Libras", "Toneladas"): (valor / 2240, f"{valor} libras = {valor} ÷ 2240", "X ÷ 2240"),
        ("Libras", "Miligramos"): (valor * 453592, f"{valor} libras = {valor} × 453592", "X × 453592"),

        # De Onzas a...
        ("Onzas", "Gramos"): (valor * 28.35, f"{valor} onzas = {valor} × 28.35", "X × 28.35"),
        ("Onzas", "Kilogramos"): (valor / 35.274, f"{valor} onzas = {valor} ÷ 35.274", "X ÷ 35.274"),
        ("Onzas", "Libras"): (valor / 16, f"{valor} onzas = {valor} ÷ 16", "X ÷ 16"),
        ("Onzas", "Toneladas"): (valor / 35840, f"{valor} onzas = {valor} ÷ 35840", "X ÷ 35840"),
        ("Onzas", "Miligramos"): (valor * 28350, f"{valor} onzas = {valor} × 28350", "X × 28350"),

        # De Toneladas a...
        ("Toneladas", "Gramos"): (valor * 1000000, f"{valor} toneladas = {valor} × 1000000", "X × 1000000"),
        ("Toneladas", "Kilogramos"): (valor * 1000, f"{valor} toneladas = {valor} × 1000", "X × 1000"),
        ("Toneladas", "Libras"): (valor * 2240, f"{valor} toneladas = {valor} × 2240", "X × 2240"),
        ("Toneladas", "Onzas"): (valor * 35840, f"{valor} toneladas = {valor} × 35840", "X × 35840"),
        ("Toneladas", "Miligramos"): (valor * 1000000000, f"{valor} toneladas = {valor} × 1000000000", "X × 1000000000"),

        # De Miligramos a...
        ("Miligramos", "Gramos"): (valor / 1000, f"{valor} miligramos = {valor} ÷ 1000", "X ÷ 1000"),
        ("Miligramos", "Kilogramos"): (valor / 1000000, f"{valor} miligramos = {valor} ÷ 1000000", "X ÷ 1000000"),
        ("Miligramos", "Libras"): (valor / 453592, f"{valor} miligramos = {valor} ÷ 453592", "X ÷ 453592"),
        ("Miligramos", "Onzas"): (valor / 28350, f"{valor} miligramos = {valor} ÷ 28350", "X ÷ 28350"),
        ("Miligramos", "Toneladas"): (valor / 1000000000, f"{valor} miligramos = {valor} ÷ 1000000000", "X ÷ 1000000000"),
    }

    # Conversiones de Temperatura
    temperatura_conversiones = {
        # De Celsius a...
        ("Celsius", "Fahrenheit"): ((valor * 9/5) + 32, f"{valor}°C = ({valor} × 9/5) + 32", "(X × 9/5) + 32"),
        ("Celsius", "Kelvin"): (valor + 273.15, f"{valor}°C = {valor} + 273.15", "X + 273.15"),

        # De Fahrenheit a...
        ("Fahrenheit", "Celsius"): ((valor - 32) * 5/9, f"{valor}°F = ({valor} - 32) × 5/9", "(X - 32) × 5/9"),
        ("Fahrenheit", "Kelvin"): ((valor - 32) * 5/9 + 273.15, f"{valor}°F = (({valor} - 32) × 5/9) + 273.15", "((X - 32) × 5/9) + 273.15"),
        
        # De Kelvin a...
        ("Kelvin", "Celsius"): (valor - 273.15, f"{valor}K = {valor} - 273.15", "X - 273.15"),
        ("Kelvin", "Fahrenheit"): ((valor - 273.15) * 9/5 + 32, f"{valor}K = (({valor} - 273.15) × 9/5) + 32", "((X - 273.15) × 9/5) + 32"),
    }

    # Combinar todas las conversiones
    todas_conversiones = {**longitud_conversiones, **peso_conversiones, **temperatura_conversiones}

    # Buscar la conversión directa
    conversion_key = (origen, destino)
    if conversion_key in todas_conversiones:
        resultado, mensaje, formula = todas_conversiones[conversion_key]
        return round(resultado, 4), mensaje, formula
    
    # Si la conversión directa no existe, intentar conversión inversa
    conversion_inversa_key = (destino, origen)
    if conversion_inversa_key in todas_conversiones:
        resultado_inverso, mensaje_inverso, formula_inversa = todas_conversiones[conversion_inversa_key]
        resultado_final = 1 / resultado_inverso * valor
        return round(resultado_final, 4), f"{valor} {origen} = {round(resultado_final, 4)} {destino}", f"(1 ÷ ({mensaje_inverso.split('=')[1].strip()})) × {valor}"

    # Si no se encuentra ninguna conversión, lanzar un error personalizado
    raise ValueError(f"Conversión no soportada entre {origen} y {destino}. Asegúrate de que las unidades sean compatibles.")