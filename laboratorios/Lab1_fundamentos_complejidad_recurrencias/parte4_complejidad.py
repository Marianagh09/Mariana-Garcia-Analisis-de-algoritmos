import time 
import matplotlib.pyplot as plt
from datos import generar_aleatorio
from algoritmos import insertion_sort, merge_sort

def realizar_experimento_parte4():
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400] # Tamaños de los lotes a probar

    tiempos_insertion, tiempos_merge = [], [] # Listas para almacenar los tiempos de ejecución
    comparaciones_insertion, comparaciones_merge = [], [] # Listas para almacenar el número de comparaciones

    print ("Ejecutando experimento para Insertion Sort y Merge Sort...") # Mensaje de inicio del experimento

    for n in tamanios:
        datos = generar_aleatorio(n) # Generar datos aleatorios

        # Medir tiempo y comparaciones para Insertion Sort
        t_inicio = time.perf_counter() # Iniciar el temporizador
        _, comp_insertion = insertion_sort(datos) # Ordenar y contar comparaciones
        t_fin = time.perf_counter() # Detener el temporizador
        tiempos_insertion.append(t_fin - t_inicio) # Almacenar el tiempo de ejecución
        comparaciones_insertion.append(comp_insertion) # Almacenar el número de comparaciones

        # Medir tiempo y comparaciones para Merge Sort
        t_inicio = time.perf_counter() # Iniciar el temporizador
        _, comp_merge = merge_sort(datos) # Ordenar y contar comparaciones
        t_fin = time.perf_counter() # Detener el temporizador
        tiempos_merge.append(t_fin - t_inicio) # Almacenar el tiempo de ejecución
        comparaciones_merge.append(comp_merge) # Almacenar el número de comparaciones

    # Graficar comparaciones vs tamaño de entrada
    plt.figure(figsize=(9, 6)) # Crear una figura para el gráfico
    plt.plot(tamanios, tiempos_insertion, 'o-', label='Insertion Sort', color= 'tab:red') # Graficar tiempos para Insertion Sort
    plt.plot(tamanios, tiempos_merge, 's-', label='Merge Sort', color= 'tab:blue') # Graficar tiempos para Merge Sort
    plt.title("Comparacion tiempos de ejecución: Insertion Sort vs Merge Sort") # Título del gráfico
    plt.xlabel("Tamaño de entrada (n)") # Etiqueta del eje x
    plt.ylabel("Tiempo de ejecución (segundos)") # Etiqueta del eje y
    plt.grid(True) # Mostrar cuadrícula en el gráfico
    plt.legend() # Mostrar leyenda para identificar cada algoritmo
    plt.tight_layout() # Ajustar el diseño para que no se corten elementos
    plt.savefig("graficas/parte4_tiempos.png") # Guardar el gráfico como imagen
    

    plt.figure(figsize=(9, 6)) # Crear una figura para el gráfico
    plt.plot(tamanios, comparaciones_insertion, 'o-', label='Insertion Sort', color= 'tab:red') # Graficar comparaciones para Insertion Sort
    plt.plot(tamanios, comparaciones_merge, 's-', label='Merge Sort', color= 'tab:blue') # Graficar comparaciones para Merge Sort
    plt.title("Comparacion de numeros de comparaciones: Insertion Sort vs Merge Sort") # Título
    plt.xlabel("Tamaño de entrada (n)") # Etiqueta del eje x
    plt.ylabel("Número de comparaciones") # Etiqueta del eje y
    plt.grid(True) # Mostrar cuadrícula en el gráfico
    plt.legend() # Mostrar leyenda para identificar cada algoritmo
    plt.tight_layout() # Ajustar el diseño para que no se corten elementos
    plt.savefig("graficas/parte4_comparaciones.png") # Guardar el gráfico como imagen

print("Experimento completado. Gráficas guardadas en la carpeta 'graficas'.")

if __name__ == "__main__":
    realizar_experimento_parte4() # Ejecutar el experimento si se ejecuta este archivo directamente 