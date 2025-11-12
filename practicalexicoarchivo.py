import re
import os
import tkinter as tk
from tkinter import filedialog


class Token:
    def __init__(self, tipo, valor, Linea):
        self.tipo = tipo # Ej: 'KEYWORD', 'IDENTIFIER'
        self.valor = valor
        self.linea = Linea

    def __str__(self):
        return f"Línea {self.linea}: {self.tipo:<15} -> '{self.valor}'"


class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1

        # Especificación de tokens (el orden importa)
        self.patrones = [
            ('KEYWORD',    r'\b(if|while|for|return|int|float|else)\b'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NUMBER',     r'\d+(\.\d*)?'),
            ('OPERATOR',   r'==|!=|<=|>=|[\+\-\*/=<>]'),
            ('DELIMITER',  r'[;(){}]'),
            ('WHITESPACE', r'[ \t]+'),
            ('NEWLINE',    r'\n'),
            ('ERROR',      r'.')
        ]


    def tokenizar (self):
        tokens = []

        while self.pos < len(self.codigo):
            encontrado = False


            for tipo, patron in self.patrones:

                regex = re.compile(patron)
                match = regex.match(self.codigo, self.pos)

                # If a match is found
                if match:

                    valor = match.group(0)

                    if tipo == 'NEWLINE':

                        self.linea += 1

                    elif tipo not in ['WHITESPACE', 'NEWLINE']:
                        tokens.append(Token (tipo, valor, self.linea))

                    self.pos = match.end()

                    encontrado = True
                    break

            if not encontrado:
                self.pos += 1


        return tokens
    
def analizar_y_guardar(ruta_archivo_entrada):
    """Lee un archivo, lo analiza y guarda la tabla de tokens en otro archivo."""
    try:
        with open(ruta_archivo_entrada, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo_entrada}' no fue encontrado.")
        return

    print(f"Analizando el archivo: {ruta_archivo_entrada}")

    lexer = AnalizadorLexico(codigo)
    tokens = lexer.tokenizar()

    # Generar nombre para el archivo de salida
    # 1. Obtener solo el nombre del archivo de la ruta completa (ej. 'codigo.txt')
    nombre_archivo_base = os.path.basename(ruta_archivo_entrada)
    # 2. Separar el nombre del archivo de su extensión (ej. 'codigo', '.txt')
    nombre_sin_extension, extension = os.path.splitext(nombre_archivo_base)
    ruta_archivo_salida = f"resultado_{nombre_sin_extension}.txt"

    try:
        with open(ruta_archivo_salida, 'w', encoding='utf-8') as f_salida:
            # Escribir encabezado de la tabla
            f_salida.write("Tabla de Tokens Generada\n")
            f_salida.write("-" * 60 + "\n")
            f_salida.write(f"{'Renglón':<10} {'Token':<15} {'Lexema':<15} {'Categoría':<15}\n")
            f_salida.write("-" * 60 + "\n")

            # Escribir cada token en el archivo
            for token in tokens:
                linea_tabla = f"{token.linea:<10} {token.tipo:<15} {repr(token.valor):<15} {token.tipo:<15}\n"
                f_salida.write(linea_tabla)

            f_salida.write("-" * 60 + "\n")
        
        print(f"¡Análisis completado! La tabla de tokens se ha guardado en '{ruta_archivo_salida}'")

    except IOError as e:
        print(f"Error al escribir en el archivo de salida: {e}")


if __name__ == "__main__":
    # Configurar la ventana raíz de tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter

    # Abrir el explorador de archivos para que el usuario seleccione un archivo
    print("Abriendo el explorador de archivos para seleccionar el documento...")
    nombre_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo de código para analizar",
        filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*"))
    )

    # Si el usuario seleccionó un archivo, proceder con el análisis
    if nombre_archivo: # askopenfilename retorna una cadena vacía si se cancela
        analizar_y_guardar(nombre_archivo)
    else:
        print("Operación cancelada. No se seleccionó ningún archivo.")
