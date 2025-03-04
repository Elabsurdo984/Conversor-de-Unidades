# Unit Converter Pro 🔢📏

## Descripción del Proyecto

Unit Converter Pro es una aplicación de escritorio desarrollada en Python utilizando Tkinter que permite convertir unidades en tres categorías principales: Longitud, Peso y Temperatura. La aplicación ofrece una interfaz de usuario moderna e intuitiva con múltiples opciones de conversión.

## Características Principales ✨

- 📏 **Conversiones de Longitud**
  - Conversiones entre metros, kilómetros, centímetros, milímetros
  - Soporte para múltiples tipos de conversión

- ⚖️ **Conversiones de Peso**
  - Conversiones entre kilogramos, gramos, libras
  - Cálculos precisos con redondeo

- 🌡️ **Conversiones de Temperatura**
  - Conversiones entre Celsius y Fahrenheit
  - Fórmulas de conversión exactas

## Requisitos del Sistema 💻

- Python 3.13+
- Tkinter (generalmente incluido con instalaciones estándar de Python)

## Instalación 🚀

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Elabsurdo984/Conversor-de-Unidades.git
   cd Conversor-de-Unidades
   ```

2. (Opcional) Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Ejecutar la aplicación:
   ```bash
   python src/main.py
   ```

## Estructura del Proyecto 📂

```
Conversor-de-Unidades/
├── imgs/
|   ├── icon.ico
├── src/
│   ├── main.py            # Punto de entrada de la aplicación
│   ├── menu.py            # Definición de la interfaz de menú
│   └── utils/
│       ├── conversions.py  # Lógica de conversiones
│       └── __init__.py
├── .gitignore
├── LICENSE
└── README.md
```

## Funcionalidades Técnicas 🔧

- Manejo de excepciones personalizado
- Interfaz de usuario con diseño moderno
- Conversiones con alta precisión
- Soporte para múltiples unidades

## Contribuciones 🤝

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia 📄

Distribuido bajo la Licencia GPL. Consulte `LICENSE` para más información.
