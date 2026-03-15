# python_opt.py
# Versión: 2.0.0
# Autor: Gabriel
# Fecha: 14/03/2026
# Descripción: Versión modularizada con manejo de excepciones y soporte para 
# múltiples modas. Optimizado para integración en proyectos de mayor escala.

from collections import Counter

def calcular_estadisticas(lista_numeros):
    """
    Procesa una lista de números para obtener frecuencias, modas y 
    la suma de dígitos de la moda principal.
    """
    if not lista_numeros:
        raise ValueError("La lista de entrada no puede estar vacía.")

    # BLOQUE 1: Construcción de frecuencias
    frecuencias = Counter(lista_numeros)

    # BLOQUE 2: Determinar valor(es) modal(es)
    # Buscamos la frecuencia más alta para soportar casos bimodales
    max_frecuencia = max(frecuencias.values())
    modas = [num for num, count in frecuencias.items() if count == max_frecuencia]
    
    # Tomamos la primera moda para el cálculo de dígitos (consistencia v1.2.0)
    principal_modo = modas[0]

    # BLOQUE 3: Suma de dígitos
    # Usamos abs() para evitar errores con el signo negativo
    suma_digitos = sum(int(d) for d in str(abs(principal_modo)))

    return {
        "frecuencias": dict(frecuencias),
        "modas": modas,
        "max_cuenta": max_frecuencia,
        "suma_digitos_modo": suma_digitos
    }

# --- BLOQUE DE EJECUCIÓN (MAIN) ---
if __name__ == "__main__":
    datos = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]
    
    try:
        resultado = calcular_estadisticas(datos)
        
        print(f"--- Reporte Versión 2.0.0 ---")
        print(f"Frecuencias: {resultado['frecuencias']}")
        print(f"Modas encontradas: {resultado['modas']} (frecuencia: {resultado['max_cuenta']})")
        print(f"Suma de dígitos del primer modo: {resultado['suma_digitos_modo']}")
        
    except Exception as e:
        print(f"Error en el procesamiento: {e}")