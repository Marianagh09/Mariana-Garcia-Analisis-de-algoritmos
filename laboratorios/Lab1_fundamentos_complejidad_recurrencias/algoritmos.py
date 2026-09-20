"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente el algoritmo contando cada comparacion
    # entre dos elementos de la lista.

    arr = datos.copy()  # Crear una copia de la lista para no modificar la original
    comparaciones = 0  # Inicializar el contador de comparaciones

    for i in range(1, len(arr)):
        clave = arr[i] # Guardar el elemento actual
        j = i - 1 # Inicializar el índice del elemento anterior

        while j >=0:
            comparaciones += 1  # Contar la comparación
            # ordenamos de mayor a menor
            if arr[j] < clave:  # Comparar el elemento anterior con la clave
                arr[j + 1] = arr[j]  # Mover el elemento anterior hacia adelante
                j -= 1  # Mover al siguiente elemento anterior
            else:
                break  # Salir del bucle si no se necesita más comparaciones

        arr[j + 1] = clave  # Colocar la clave en su posición correcta
        return arr, comparaciones  # Devolver la lista ordenada y el número de comparaciones
