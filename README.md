# Conversor de Unidades

Un programa de consola simple para convertir diferentes tipos de unidades de medida.

## Características

- Conversión de unidades de longitud:
    - Metros a kilómetros y viceversa
    - Centímetros a metros y viceversa
    - Milímetros a centímetros y viceversa
    - Metros a milímetros y viceversa
    - Centímetros a Kilómetros y viceversa

- Conversión de unidades de peso:
    - Kilogramos a gramos y viceversa
    - Libras a kilogramos y viceversa

- Conversión de unidades de temperatura:
    - Celsius a Fahrenheit y viceversa

## Requisitos

- Python 3.13

## Estructura del Proyecto

```
ConversorUnidades/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── menu.py
│   └── utils/
|       ├── __init__.py
│       └── conversions.py
├── LICENSE
└── README.md
```

## Uso si deseas clonar el repositorio

1. Ejecuta el archivo `main.py`
2. Selecciona el tipo de conversión que deseas realizar
3. Elige la conversión específica
4. Ingresa el valor a convertir
5. Obtén el resultado

## Como compilar

1. Clona el repositorio con `git clone https://github.com/Elabsurdo984/Conversor-de-Unidades.git`
2. Abre tu proyecto en tu editor de codigo favorito
3. Si no tienes Python instalado, instalalo ([aquí] (https://www.python.org))
4. Una vez que instalaste Python, vuelve al proyecto.
5. Con una terminal, viaja al proyecto `cd Conversor-de-Unidades/src`
6. Una vez en el proyecto, instala el compilador de python `pip install pyinstaller`
7. Compila el proyecto `pyinstaller --onefile main.py`
8. Esto generara una carpeta `dist` donde estara el ejecutable

## Control de Errores

El programa incluye:
- Validación de entrada numérica
- Manejo de interrupciones de teclado
- Validación de opciones de menú

## Contribuir

Si deseas contribuir al proyecto, puedes:
1. Hacer fork del repositorio
2. Crear una rama para tu característica (`git checkout -b feature/NuevaCaracteristica`)
3. Commit de tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Crear un Pull Request