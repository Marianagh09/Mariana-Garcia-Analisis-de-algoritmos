from typing import Sequence

def calcular_promedio(numeros: Sequence[float | int]) -> float:
    """ calcula el promedio aritmetico de una secuencia de numeros
    
    Args: 
        numeros: Lista o secuencia de numeros (enteros o flotantes)
        
    Returns:
        float: el promedio de los elementos de la secuencia
        """ 
    suma_total: float = 0.0
    for numero in numeros:
        suma_total += numero
    return suma_total/len(numeros)

def main() -> None:
    """Funcion principal que ejecuta la logica del programa"""
    lista_numeros: list[int]=[1,2,3,4,5]
    promedio: float = calcular_promedio(lista_numeros)
    print(f"El promedio de la lista {lista_numeros} es: {promedio}")

if __name__ == "__main__":
    main()