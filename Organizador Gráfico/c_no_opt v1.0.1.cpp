/* c_no_opt.c
   Versión: 1.0.1
   Victor 13/03/2026, Primera optimización, se hace mas corto el código.
   MOD: v1.0.1 - Se eliminaron líneas de código las cuales no tenían funcionalidad
                 en el código y solo lo hacían más lento.
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int N = 1000; /* ejemplo; en práctica puede leerse desde stdin */
    int count_primos = 0;
    long long suma_primos = 0;
    int primos_pares = 0;
    int primos_impares = 0;

    for (int m = 2; m <= N; m = m + 1) {
        int es_primo = 1; /* asumimos primo hasta demostrar lo contrario */

        /* comprobación ingenua: probar divisores desde 2 hasta m-1 */
        int d = 2;
        while (d < m) {
            if (m % d == 0) {
                es_primo = 0;
                }
             else {

            }
            d = d + 1;
        }

        if (es_primo) {
            count_primos = count_primos + 1;
            suma_primos = suma_primos + m;
            if (m % 2 == 0) {
                primos_pares = primos_pares + 1;
            } else {
                primos_impares = primos_impares + 1;
            }
        } else {
            /* rama para números compuestos */
            int z = 0;
            z = z + 1; /* operación inútil para mostrar código mejorable */
        }
    }

    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}
