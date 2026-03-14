# python_no_opt.py
# Versión: 1.1.0
# Autor: Axel
# Fecha: 14/03/2026
# Descripción: Optimización del cálculo de frecuencias y del modo utilizando un diccionario y operaciones originarioas de Python 
                #para reducir conversiones de estructuras y mejorar la eficiencia.
# Entrada esperada: Lista de números enteros.
# Salida esperada: Frecuencias de cada número, valor modal y suma de los dígitos del modo.


# Lista de entrada de ejemplo
numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]

# BLOQUE 1: Construcción del diccionario de frecuencias
# MOD: v1.1.0 — Se utiliza el método get() para simplificar la actualización
# de frecuencias evitando la estructura if/else.
frecuencias = {}  # Diccionario donde la clave es el número y el valor su frecuencia
for num in numeros:  # Recorre cada número de la lista
    frecuencias[num] = frecuencias.get(num, 0) + 1  
    # get(num,0) devuelve el valor actual o 0 si no existe, luego se suma 1


# BLOQUE 2: Determinar el valor modal (el número más frecuente)
# MOD: v1.1.0 — Se usa max() con key=frecuencias.get para encontrar directamente el valor con mayor frecuencia.
modo = max(frecuencias, key=frecuencias.get)  # Encuentra la clave con mayor valor
max_cuenta = frecuencias[modo]  # Obtiene la frecuencia del modo

# BLOQUE 3: Cálculo de la suma de los dígitos del valor modal
# MOD: v1.1.0 — Conversión del número a cadena para recorrer sus dígitos.
x_str = str(abs(modo))  
# abs() convierte el número en positivo y str() permite iterar sus dígitos
suma_digitos = sum(int(d) for d in x_str)  
# Convierte cada carácter en entero y suma todos los dígitos

# BLOQUE 4: Mostrar resultados
print("Frecuencias:", list(frecuencias.items()))  # Convierte el diccionario en lista de tuplas
print("Modo:", modo, "con cuenta:", max_cuenta)  # Muestra el valor modal
print("Suma de dígitos del modo:", suma_digitos)  # Muestra la suma de sus dígitos
