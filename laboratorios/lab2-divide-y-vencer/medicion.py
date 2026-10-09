"""Script de experimentacion y generacion de graficas para el laboratorio"""

import os
import random
import time
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def ejecutar_experimento() -> None:
    """Ejecuta las mediciones de tiempo y guarda la grafica comparativa."""

    # Tamaños de entrada indicados (dos < 100 y uno >= 4000)
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]

    tiempos_fb, tiempos_dv = [], []  
   

    #Fijar semilla para garantizar reproducibilidad
    random.seed(42)

    print("Ejecutando mediciones experimentales...")

    for n in tamanios:
        #Generar datos aleatorios enteros entre -100 y 100
        datos = [float(random.randint(-100, 100)) for _ in range(n)]

        #1. Medir Fuerza bruta
        t_inicio = time.perf_counter()
        res_fb = subarreglo_fuerza_bruta(datos)
        t_fin = time.perf_counter()
        duracion_fb = t_fin - t_inicio
        tiempos_fb.append(duracion_fb)

        #2. Medir Divide y vencerás
        t_inicio = time.perf_counter()
        res_dv = subarreglo_maximo(datos, 0, len(datos)-1)
        t_fin = time.perf_counter()
        duracion_dv = t_fin - t_inicio
        tiempos_dv.append(duracion_dv)

        # Verificacion integrada: ambas sumas deben coincidir excatamente
        assert(
            res_fb[1] == res_dv[1]
        ), f"Error de coincidencia en n={n}: FB={res_fb[1]}, DV={res_dv[1]}"

        print(
            f"n={n:4d} | FB: {duracion_fb:8.5f} s | DV: {duracion_dv:8.5f} s | Suma: {res_fb[1]}"
        )

    #Generar grafica comparativa 
    plt.figure(figsize=(9, 6))
    plt.plot(tamanios, tiempos_fb, "o-", label="Fuerza bruta $\\Theta(n^2)$", color="tab:red")
    plt.plot(tamanios, tiempos_dv, "s-", label="Divide y Venceras $\\Theta(n \\log n)$", color="tab:blue")
    plt.title("Subarreglo Máximo: Tiempo de Ejecución vs. Tamaño de Entrada", fontsize=13)
    plt.xlabel("Tamaño de entrada ($n$ días)", fontsize=11)
    plt.ylabel("Tiempo de ejecución (segundos)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()

    ruta_grafica = os.path.join("graficas", "tiempo_vs_n.png")
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()

    print(f"Gráfica guardada en: {ruta_grafica}")

if __name__ == "__main__":
    ejecutar_experimento()



    