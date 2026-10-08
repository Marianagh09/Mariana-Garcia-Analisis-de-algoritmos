"""Script de pruebas automaticas para la verificacion del subarreglo maximo."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def ejecutar_pruebas() -> None:
    """Ejecuta un conjunto completo de pruebas con assert."""
    print("iniciando verificacion de algoritmos...")

#1. Caso del enunciado (8 dias)
serie_enunciado = [-3, 5, -2, 8, -6, 3, 9, -4]
res_fb = subarreglo_fuerza_bruta(serie_enunciado)
res_dv = subarreglo_maximo(serie_enunciado, 0, len(serie_enunciado) - 1)
assert res_fb[2] == 17, f"Fuerza bruta fallo en enunciado: {res_fb[2]}"
assert res_dv[2] == 17, f"Divide y vencer fallo en enunciado: {res_dv[2]}"
print("Prueba 1: Serie de 8 dias del enunciado (suma = 17)")

#2. Serie de un solo elemento 
serie_un_elem = [5]
res_fb = subarreglo_fuerza_bruta(serie_un_elem)
res_dv = subarreglo_maximo(serie_un_elem, 0, 0)
assert res_fb[2] == 5
assert res_dv[2] == 5
print("Prueba 2: Serie de un solo elemento (suma = 5)")

#3. Serie con todos los valores negativos
serie_negativos = [-10, -3, -7, -1, -5]
res_fb = subarreglo_fuerza_bruta(serie_negativos)
res_dv = subarreglo_maximo(serie_negativos, 0, len(serie_negativos) - 1)
assert res_fb[2] == -1
assert res_dv[2] == -1
print("Prueba 3: Todos los valores negativos (retorna el menos negativo)")

# 4\. Serie con todos los valores positivos 
serie_positivos = [2.0, 4.0, 1.0, 3.0, 5.0]
res_fb = subarreglo_fuerza_bruta(serie_positivos) 
res_dv = subarreglo_maximo(serie_positivos, 0, len(serie_positivos) - 1) 
assert res_fb[2] == 15.0 
assert res_dv[2] == 15.0 
print("Prueba 4: Todos los valores positivos (suma la serie completa)")

# 5. Caso donde el mejor tramo cruza el punto medio 
# Medio está en índice 2 (valor -1.0). El tramo óptimo va del índice 1 al 4 (suma = 18.0) 
serie_cruzada = [-10.0, 8.0, -1.0, 11.0, -20.0] 
res_fb = subarreglo_fuerza_bruta(serie_cruzada) 
res_dv = subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1) 
assert res_fb[2] == 18.0 
assert res_dv[2] == 18.0 
print("Prueba 5: Tramo óptimo cruzado explícito")

#6. Al menos 20 listas aleatorias comparando que ambas sumas coincidan
random.seed(42) 
for k in range(1, 26):
    n = random.randint(5, 100) 
    lista_rand = [float(random.randint(-100, 100)) for _ in range(n)]
    suma_fb = subarreglo_fuerza_bruta(lista_rand)[1]
    suma_dv = subarreglo_maximo(lista_rand, 0, len(lista_rand) - 1)[1]
    assert (
        suma_fb == suma_dv
    ), f"Discrepancia en iteracion {k}: FB={suma_fb}, DV={suma_dv}"

print("Prueba 6: 25 listas aleatorias (coincidencia 100 % en sumas)")


if __name__ == "__main__":
    ejecutar_pruebas()
    print("Todas las pruebas pasaron correctamente.")