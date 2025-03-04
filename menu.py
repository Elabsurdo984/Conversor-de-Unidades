from utils.conversions import convertir_longitud, convertir_peso, convertir_temperatura

def obtener_valor_numerico():
    """Solicita y valida un valor numérico del usuario."""
    while True:
        try:
            return float(input("Ingresa el valor a convertir: "))
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
            
def obtener_opcion(max_opcion):
    """Solicita y valida una opción del usuario."""
    while True:
        opcion = input(f"Selecciona una opción (1-{max_opcion}): ")
        try:
            opcion_num = int(opcion)
            if 1 <= opcion_num <= max_opcion:
                return opcion_num
            else:
                print(f"Error: Debes seleccionar un número entre 1 y {max_opcion}.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def menu_longitud():
    """Muestra el menú de conversión de longitud."""
    print("\n--- Conversor de Longitud ---")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Centímetros a Metros")
    print("4. Metros a Centímetros")
    print("5. Milímetros a Centímetros")
    print("6. Centímetros a Milímetros")
    print("7. Metros a Milímetros")
    print("8. Milímetros a Metros")
    
    opcion = obtener_opcion(8)
    valor = obtener_valor_numerico()
    
    _, mensaje = convertir_longitud(opcion, valor)
    print(mensaje)

def menu_peso():
    """Muestra el menú de conversión de peso."""
    print("\n--- Conversor de Peso ---")
    print("1. Kilogramos a Gramos")
    print("2. Gramos a Kilogramos")
    print("3. Libras a Kilogramos")
    print("4. Kilogramos a Libras")
    
    opcion = obtener_opcion(4)
    valor = obtener_valor_numerico()
    
    _, mensaje = convertir_peso(opcion, valor)
    print(mensaje)

def menu_temperatura():
    """Muestra el menú de conversión de temperatura."""
    print("\n--- Conversor de Temperatura ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    opcion = obtener_opcion(2)
    valor = obtener_valor_numerico()
    
    _, mensaje = convertir_temperatura(opcion, valor)
    print(mensaje)

def menu_principal():
    """Muestra el menú principal de la aplicación."""
    while True:
        print("\n--- Conversor de Unidades ---")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Salir")

        opcion = obtener_opcion(4)

        if opcion == 1:
            menu_longitud()
        elif opcion == 2:
            menu_peso()
        elif opcion == 3:
            menu_temperatura()
        elif opcion == 4:
            print("¡Adiós!")
            break