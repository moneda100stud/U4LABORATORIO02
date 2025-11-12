## Analizador Léxico en Python

### Descripción del Proyecto

Este proyecto es un analizador léxico (o *scanner*) desarrollado en Python. Su función principal es leer un archivo de texto que contiene código fuente simple, procesarlo para identificar sus componentes léxicos básicos (tokens) y generar una tabla formateada con los resultados en un nuevo archivo de texto.

Este es el primer paso fundamental en el proceso de compilación o interpretación de un lenguaje de programación. El proyecto fue construido de manera iterativa, comenzando con un script básico y evolucionando hasta convertirse en una herramienta más robusta y fácil de usar.

---

### Características Principales

*   **Análisis desde Archivo**: Lee el código fuente directamente desde un archivo de texto.
*   **Interfaz Gráfica**: Utiliza una ventana de explorador de archivos (`tkinter`) para que el usuario pueda seleccionar el archivo a analizar de forma intuitiva.
*   **Generación de Reporte**: Guarda la tabla de tokens resultante en un archivo de texto separado (ej. `resultado_codigo.txt`).
*   **Tabla de Tokens Formateada**: Presenta los resultados en una tabla clara con las columnas: `Renglón`, `Token`, `Lexema` y `Categoría`.
*   **Reconocimiento de Tokens**: Identifica los siguientes tipos de tokens mediante expresiones regulares:
    *   `KEYWORD`: Palabras reservadas como `if`, `while`, `int`, etc.
    *   `IDENTIFIER`: Nombres de variables y funciones.
    *   `NUMBER`: Números enteros y de punto flotante.
    *   `OPERATOR`: Operadores aritméticos y de comparación como `+`, `*`, `==`, etc.
    *   `DELIMITER`: Símbolos de agrupación y terminación como `(`, `)`, `{`, `}` y `;`.
*   **Conteo de Líneas**: Realiza un seguimiento del número de línea donde aparece cada token.

---

### ¿Cómo Usarlo?

1.  **Requisitos**: Tener instalado Python 3.
2.  **Ejecutar el Script**: Abre una terminal y ejecuta el archivo principal:
    ```bash
    python practicalexicoarchivo.py
    ```
3.  **Seleccionar Archivo**: Se abrirá una ventana del explorador de archivos. Navega y selecciona el archivo `.txt` que contiene el código que deseas analizar (por ejemplo, `codigo.txt`).
4.  **Ver el Resultado**: Una vez finalizado el análisis, se creará un nuevo archivo en el mismo directorio con el nombre `resultado_<nombre_original>.txt`. Este archivo contendrá la tabla de tokens generada.

---

### Estructura del Código

El proyecto se centra en el archivo `practicalexicoarchivo.py`, que contiene:

*   **Clase `Token`**: Una estructura de datos simple para almacenar la información de cada token (tipo, valor y número de línea).
```python
class Token:
    def __init__(self, tipo, valor, Linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = Linea
```

### 3.2. Clase `AnalizadorLexico`

Esta es la clase principal que realiza el análisis léxico.

-   **`__init__(self, codigo)`**: El constructor inicializa el analizador con el código fuente a procesar, un puntero de posición (`self.pos`) y un contador de línea (`self.linea`).

-   **`self.patrones`**: Es una lista de tuplas donde cada tupla contiene el `tipo` de token y su `patrón` de expresión regular. **El orden en esta lista es crucial**:
    -   `KEYWORD` va antes que `IDENTIFIER` para que palabras como `if` o `int` sean reconocidas como palabras clave y no como identificadores genéricos.
    -   `WHITESPACE` y `NEWLINE` se identifican para poder ignorarlos y para actualizar el contador de línea.
    -   `ERROR` va al final para capturar cualquier carácter que no coincida con los patrones anteriores.

-   **`tokenizar(self)`**: Este es el método central del analizador.
    1.  Inicia un bucle `while` que se ejecuta mientras no se haya recorrido todo el código (`self.pos < len(self.codigo)`).
    2.  Dentro del bucle, itera sobre la lista `self.patrones`.
    3.  Para cada patrón, intenta hacer una coincidencia (`regex.match()`) desde la posición actual (`self.pos`).
    4.  Si encuentra una coincidencia:
        -   Extrae el valor del token (`match.group(0)`).
        -   Si el token es `NEWLINE`, incrementa el contador de línea.
        -   Si el token no es un espacio en blanco o una nueva línea, crea un objeto `Token` y lo añade a la lista de `tokens`.
        -   Actualiza la posición (`self.pos`) al final del token encontrado.
        -   Rompe el bucle interno y comienza una nueva búsqueda desde la nueva posición.
    5.  Si no se encuentra ninguna coincidencia para ningún patrón (lo cual no debería ocurrir gracias al patrón `ERROR`), avanza la posición en uno para evitar un bucle infinito.
    6.  Finalmente, devuelve la lista completa de `tokens` encontrados.

## 4. Conclusión

A través de una serie de mejoras iterativas, el script ha evolucionado desde un prototipo básico a un analizador léxico funcional y robusto. Las correcciones en la visualización, el uso de cadenas crudas y la depuración de las expresiones regulares han sido pasos clave para lograr un resultado preciso y fácil de interpretar.