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


def merge_sort(datos: list[int]) -> tuple[list[int], int]:

    copia = list(datos)  # Crear una copia de la lista para no modificar la original

    def merge_sort_rec(arr: list[int]) -> tuple[list[int], int]: # 
        if len(arr) <= 1:
            return arr, 0  # Devolver la lista y 0 comparaciones si tiene 1 o menos elementos
        medio = len(arr) // 2  # Calcular el índice medio

        izquierda, comp_izq = merge_sort_rec(arr[:medio])  # Ordenar la mitad izquierda y contar comparaciones
        derecha, comp_der = merge_sort_rec(arr[medio:])  # Ordenar la mitad derecha y contar comparaciones

        resultado = []  # Lista para almacenar el resultado de la fusión
        i = j = 0  # Inicializar los índices para la fusión
        comp_mezcla = 0  # Inicializar el contador de comparaciones durante la fusión

        while i < len(izquierda) and j < len(derecha): 
            comp_mezcla += 1 # Contar la comparación entre los elementos de las dos mitades

            if izquierda[i] >= derecha[j]:  # Comparar los elementos de las dos mitades
                resultado.append(izquierda[i])  # Agregar el elemento de la izquierda al resultado
                i += 1  # Mover al siguiente elemento de la izquierda
            else:
                resultado.append(derecha[j])  # Agregar el elemento de la derecha al resultado
                j += 1  # Mover al siguiente elemento de la derecha

            # Agregar cualquier elemento restante de alguna de las dos mitades
        resultado.extend(izquierda[i:]) # Agregar los elementos restantes de la izquierda al resultado
        resultado.extend(derecha[j:]) # Agregar los elementos restantes de la derecha al resultado

        total_comparaciones = comp_izq + comp_der + comp_mezcla  # Sumar todas las comparaciones
        return resultado, total_comparaciones  # Devolver la lista ordenada y el número
    return merge_sort_rec(copia)  # Llamar a la función recursiva con la copia de la lista
    
