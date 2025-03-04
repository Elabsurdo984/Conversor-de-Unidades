from menu import menu_principal

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Adiós!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("El programa se cerrará.")