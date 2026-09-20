import random 

"""Generadores de lotes de registros para los escenarios de Tamiza."""

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:

    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
     # TODO: implemente el escenario A.
    random.seed(semilla)
    datos = list(range(1, n + 1))
    random.shuffle(datos)
    return datos

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:

    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    # TODO: implemente el escenario B.
    random.seed(semilla)
    n_ordenado = int(n * 0.98)  # 98% de n
    n_desordenado = n - n_ordenado  # 2% de n

    parte_ordenada = list(range(n, n - n_ordenado, -1))  # Genera la parte ordenada en orden descendente
    parte_desordenada = list(range(n_desordenado, 0, -1))  # Genera la parte desordenada en orden descendente
    random.shuffle(parte_desordenada)  # Mezcla la parte desordenada

    return parte_ordenada + parte_desordenada 

def generar_inverso(n: int) -> list[int]:

    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # TODO: implemente el escenario C.

    return list(range(n, 0, -1))  # Genera la lista en orden inverso 
   

