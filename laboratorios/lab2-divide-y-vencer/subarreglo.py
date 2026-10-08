""" Subarreglo maximo: fuerza bruta y divide y venceras """

def subarreglo_fuerza_bruta(valores: list[float])-> tuple[int, int, float]:
    """Encuentra la mejor recha probando todos los pares de dias (i, j).
    
    Acumula la suma dentro del ciclo interno en lugar de recalcular de cero para mantener una complejidad 
    de Theta(n^2)
    
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos un elemento.
        
    Returns:
        una tupla (i, j, suma) con los indices inclusivos del tramo de mayor suma y el valor de esa suma.
    """

    n = len(valores)
    max_suma = float('-inf')
    inicio_max = 0
    fin_max = 0

    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += valores[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
                inicio_max = i
                fin_max = j

    return inicio_max, fin_max, max_suma

def suma_cruzada(
        valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
    
    Realiza un barrido lineal hacia la izquierda desde el punto medio y el otro hacia la derecha desde medio + 1.
    
    Args:
        valores: variacion diria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
        
    Returns:
        una tupla (inicio, fin, suma) del mejor tramo que incluye al menos un elemento de cada mitad.
    """

    # Barrido hacia la izquierda
    suma_izq_max = float('-inf')
    suma_actual = 0
    ind_izq = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > suma_izq_max:
            suma_izq_max = suma_actual
            ind_izq = i

    # Barrido hacia la derecha
    suma_der_max = float('-inf')
    suma_actual = 0
    ind_der = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > suma_der_max:
            suma_der_max = suma_actual
            ind_der = j

    return ind_izq, ind_der, suma_izq_max + suma_der_max

def subarreglo_maximo(
        valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor recha usando divide y venceras.
    
    Evalua los tres casos posibles (izquierdo, derecho y cruzado) y retorna el tramo con la mayor suma.
    
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
        
    Returns:
        unba tupla (inicio, fin, suma) del mejor tramo dentro de valores[inicio..fin].
        
    """

    # Caso base: un solo elemento
    if inicio == fin:
        return inicio, fin, float(valores[inicio])

    medio = (inicio + fin) // 2

    #Caso 1: El subarreglo maximo esta totalmente en la mitad de la izquierda
    izq_i, izq_f, izq_suma = subarreglo_maximo(valores, inicio, medio)

    #Caso 2: El subarreglo maximo esta totalmente en la mitad derecha
    der_i, der_f, der_suma = subarreglo_maximo(valores, medio + 1, fin)

    #Caso 3: El subarreglo maximo cruza el punto medio
    cruz_i, cruz_f, cruz_suma = suma_cruzada(valores, inicio, medio, fin)

    # Combinar: Retornar el tramo que tenga la suma maxima
    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return izq_i, izq_f, izq_suma
    elif der_suma >= izq_suma and der_suma >= cruz_suma:
        return der_i, der_f, der_suma
    else:
        return cruz_i, cruz_f, cruz_suma 

    