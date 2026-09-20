import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

def ejecutar_experimento():
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400] # Tamaños de los lotes a probar

    comp_aleatorio, comp_casi, comp_inverso = [], [], [] # Listas para almacenar el número de comparaciones
    tiempos_aleatorio, tiempos_casi, tiempos_inverso = [], [], [] # Listas para almacenar los tiempos de ejecución

    for n in tamanios:
        # Escenario A: Aleatorio
        data_a = generar_aleatorio(n) # Generar datos aleatorios
        t_inicio = time.perf_counter() # Iniciar el temporizador
        _, comp_a = insertion_sort(data_a) # Ordenar y contar comparaciones
        t_fin = time.perf_counter() # Detener el temporizador
        tiempos_aleatorio.append(t_fin - t_inicio) # Almacenar el tiempo de ejecución
        comp_aleatorio.append(comp_a) # Almacenar el número de comparaciones

        # Escenario B: Casi ordenado
        data_b = generar_casi_ordenado(n) # Generar datos casi ordenados
        t_inicio = time.perf_counter() # Iniciar el temporizador
        _, comp_b = insertion_sort(data_b) # Ordenar y contar comparaciones
        t_fin = time.perf_counter() # Detener el temporizador
        tiempos_casi.append(t_fin - t_inicio) # Almacenar el tiempo de ejecución
        comp_casi.append(comp_b) # Almacenar el número de comparaciones

        # Escenario C: Inverso
        data_c = generar_inverso(n) # Generar datos en orden inverso
        t_inicio = time.perf_counter() # Iniciar el temporizador
        _, comp_c = insertion_sort(data_c) # Ordenar y contar comparaciones
        t_fin = time.perf_counter() # Detener el temporizador
        tiempos_inverso.append(t_fin - t_inicio) # Almacenar el tiempo de ejecución
        comp_inverso.append(comp_c) # Almacenar el número de comparaciones

    # Graficar comparaciones vs tamaño de entrada
    plt.figure(figsize=(8, 5)) # Crear una figura para el gráfico
    plt.plot(
        tamanios, comp_aleatorio, marker='o', label='Aleatorio'
    ) # Graficar comparaciones para escenario A
    plt.plot(
        tamanios, comp_casi, marker='s', label='Casi Ordenado'
    ) # Graficar comparaciones para escenario B
    plt.plot(
        tamanios, comp_inverso, marker='^', label='Inverso'
    ) # Graficar comparaciones para escenario C
    plt.title("Insertion Sort: Comparaciones vs Tamaño de entrada") # Título del gráfico
    plt.xlabel("Tamaño de entrada (n)") # Etiqueta del eje x
    plt.ylabel("Número de comparaciones") # Etiqueta del eje y
    plt.grid(True) # Mostrar cuadrícula en el gráfico
    plt.legend() # Mostrar leyenda para identificar cada escenario
    plt.tight_layout() # Ajustar el diseño para que no se corten elementos
    plt.savefig("graficas/parte3_comparaciones.png") # Guardar el gráfico como imagen

    # Graficar tiempos de ejecución vs tamaño de entrada
    plt.figure(figsize=(8, 5)) # Crear una figura para el gráfico
    plt.plot(
        tamanios,
        tiempos_aleatorio,
        marker='o',
        label='Aleatorio'
    ) # Graficar tiempos de ejecución para escenario A
    plt.plot(
        tamanios,
        tiempos_casi,
        marker='s',
        label='Casi Ordenado'
    ) # Graficar tiempos de ejecución para escenario B
    plt.plot(
        tamanios,
        tiempos_inverso,
        marker='^',
        label='Inverso'
    ) # Graficar tiempos de ejecución para escenario C
    plt.title("Insertion Sort: Tiempos de ejecución vs Tamaño de entrada") # Título del gráfico
    plt.xlabel("Tamaño de entrada (n)") # Etiqueta del eje x
    plt.ylabel("Tiempo de ejecución (s)") # Etiqueta del eje y
    plt.grid(True) # Mostrar cuadrícula en el gráfico
    plt.legend() # Mostrar leyenda para identificar cada escenario
    plt.tight_layout() # Ajustar el diseño para que no se corten elementos
    plt.savefig("graficas/parte3_tiempos.png") # Guardar el gráfico como imagen


    print ("Experimento completado. Gráficas guardadas en la carpeta 'graficas'.") # Mensaje de finalización

if __name__ == "__main__":
    ejecutar_experimento() # Ejecutar el experimento si se ejecuta este archivo directamente
