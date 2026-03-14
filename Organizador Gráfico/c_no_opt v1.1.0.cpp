/* c_no_opt.c
   Versión: 1.1.0
   Autor: Axel
   Fecha: 14/03/2026
   Descripción: Optimización del algoritmo de verificación de números primos.
                Se detiene la búsqueda de divisores cuando se encuentra el
                primero, reduciendo el número de iteraciones innecesarias.
   Entrada esperada: Un número entero N que define el rango de búsqueda.
   Salida esperada: Cantidad de números primos encontrados, suma de primos,
                    número de primos pares e impares.
*/
#include <stdio.h>
#include <stdlib.h>
int main() {

    //BLOQUE 1: Inicialización de variables
    int N = 1000;              // límite superior del rango
    int count_primos = 0;      // contador de números primos encontrados
    long long suma_primos = 0; // acumulador de la suma de primos
    int primos_pares = 0;      // contador de primos pares
    int primos_impares = 0;    // contador de primos impares

    //BLOQUE 2: Generación de candidatos a número primo
    for (int m = 2; m <= N; m++) {  //recorre los números desde 2 hasta N
        int es_primo = 1;  // se asume que el número es primo inicialmente

        //BLOQUE 3: Verificación de divisores
        // MOD: v1.1.0 — Se agrega break para detener la búsqueda cuando se encuentra el primer divisor del número
        for (int d = 2; d < m; d++) {  // prueba divisores desde 2 hasta m-1
            if (m % d == 0) {          // verifica si d divide exactamente a m
                es_primo = 0;          // si es divisible, no es primo
                break;                 // termina el ciclo para evitar más pruebas
            }
        }

        //BLOQUE 4: Actualización de estadísticas de números primos
        if (es_primo) {                 // si el número es primo
            count_primos++;             // incrementa el contador de primos
            suma_primos += m;           // suma el valor del primo encontrado
            if (m % 2 == 0)             // verifica si el primo es par
                primos_pares++;
            else
                primos_impares++;
        }
    }

    //BLOQUE 5: Mostrar resultados
    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);
    return 0;
}
