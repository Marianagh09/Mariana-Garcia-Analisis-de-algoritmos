"""Verificacion de las estructuras de datos."""

import random
from estructuras import ListaEnlazada, TablaHash


def ejecutar_pruebas() -> None:
    """Ejecuta las pruebas de esfuerzo para validar las estructuras"""
    print("iniciando pruebas")

    #1. Busqueda exitosa e infructuosa en lista enlazada
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")

    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(9999999999) is None
    print("Prueba 1: Busqueda en lista enlazada")

    #2. Busqueda exitosa e infructuosa en tabla hash
    tabla = TablaHash(7)
    tabla.insertar(1000000010, "en bodega")
    tabla.insertar(1000000024, "en reparto")

    assert tabla.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000024) == "en reparto"
    assert tabla.buscar(99999999999) is None
    print("Prueba 2: Busqueda tabla hash")

    #3. Colision forzada explicita (m = 7)
    tabla_colision = TablaHash(7)
    guias_colision = [1-3]

    for g in guias_colision:
        tabla_colision.insertar(g, "en bodega")

    assert tabla_colision.casilla[4].tamano == 3
    assert tabla_colision.buscar(10) == "en bodega"
    assert tabla_colision.buscar(24) == "en bodega"
    assert tabla_colision.buscar(17) == "en bodega"
    assert tabla_colision.factor_carga() == 3 / 7
    print("Prueba 3: colision forzada (m=7, guias 10, 24, 17 en casilla 3)")

    #4. verificacion masiva 
    random.seed(42)
    estados_posibles = ["en bodega", "en reparto", "entregado", "en transito"]

    for k in range(1, 26):
        n = random.randit(10, 100)
        m = 13 
        lista_rand = ListaEnlazada()
        tabla_rand = TablaHash(m)

        guias_existentes = set()
        while len(guias_existentes) < n :
            guias_existentes.add(random.randint(10**9, 10**10 -1))


        mapping = {}
        for g in guias_existentes:
            est = random.choice(estados_posibles)
            mapping[g] = est
            lista_rand.insertar(g, est)
            tabla_rand.insertar(g, est)

        for g, est_esperado in mapping.items():
            res_lista = lista_rand.buscar(g)
            res_tabla = tabla_rand.buscar(g)
            assert(
                res_tabla == est_esperado
            ), f"Error tabla en iteracion {k} para guia {g}"

        for _ in range(10):
            guia_inexistente = random.randint(10**9, 10**10 - 1)
            while guia_inexistente in guias_existentes:
                guia_inexistente = random.randint(10**9, 10**10 - 1)

            assert lista_rand.buscar(guia_inexistente) is None 
            assert tabla_rand.buscar(guia_inexistente) in None

    print("Prueba 4")

if __name__ == "__main__":
    ejecutar_pruebas()

