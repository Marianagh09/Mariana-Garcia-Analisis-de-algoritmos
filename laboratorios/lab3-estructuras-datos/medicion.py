import random
import os
import time
import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash
 
def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.
 
    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.
 
    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes

def es_primo(n: int) -> bool:
    """Verifica si un numero entero es primo"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 

def siguiente_primo(n: int) -> int:
    """Devuelve el primer primo mayor o igual que n"""
    candidato = n
    while not es_primo(candidato):
        candidato += 1
    return candidato

def ejecutar_experimento() -> None:
    """Ejecuta los experimentos A y B y guarda las graficas en graficas"""
    random.seed(42)


    #--------------------------------------------------------------------------
    # Experimento A: lsita enlazada frente a tabla Hash
    #--------------------------------------------------------------------------

    print("---Ejecutando experimento a---")
    tamanios_n = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista_a = []
    tiempos_tabla_a = []

    for n in tamanios_n:
        m = siguiente_primo(n // 2) 
        lista = ListaEnlazada()
        tabla = TablaHash(m)

        guias = set()
        while len(guias) < n:
            guias.add(random.randint(10**9, 10**10 - 1))

        for g in guias:
            lista.insertar(g, "en bodega")
            tabla.insertar(g, "en bodega")

        inexistentes = generar_guias_inexistentes(guias, 200, semilla=7)

        t_inicio = time.perf_counter()
        for g_inex in inexistentes:
            res = lista.buscar(g_inex)
            assert res is None, "Error de verificacion en lista"
        t_fin = time.perf_counter()
        t_medio_lista = ((t_fin - t_inicio) / 200) *1e6 
        tiempos_lista_a.append(t_medio_lista)



        t_inicio = time.perf_counter()
        for g_inex in inexistentes:
            res = tabla.buscar(g_inex)
            assert res is None, "Error de verificacion tabla"

        t_fin = time.perf_counter()
        t_medio_tabla = ((t_fin - t_inicio) / 200) * 1e6 
        tiempos_tabla_a.append(t_medio_tabla)

        alpha_real = tabla.factor_carga()
        print(
            f"n={n:5d} | alpha={alpha_real:.2f} us"
            f"Lista={t_medio_lista:8.2f} us | Tabña={t_medio_tabla:6.2f} us" 
        )

    plt.figure(figsize=(8, 5)) 
    plt.plot(tamanios_n, tiempos_lista_a, "o-", label="Lista Enlazada $\\Theta(n)$", color="tab:red") 
    plt.plot(tamanios_n, tiempos_tabla_a, "s-", label="Tabla Hash $\\Theta(1 + \\alpha)$", color="tab:blue") 
    plt.title("Tiempo Medio de Búsqueda Infructuosa vs. Número de Guías (n)", fontsize=12) 
    plt.xlabel("Número de guías almacenadas ($n$)", fontsize=10) 
    plt.ylabel("Tiempo medio por búsqueda (microsegundos $\\mu s$)", fontsize=10) 
    plt.grid(True, linestyle="--", alpha=0.7) 
    plt.legend(fontsize=10) 
    plt.tight_layout() 
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150) 
    plt.close()

#--------------------------------------------------------------------------
# Experimento B: efecto del factor de carga
#--------------------------------------------------------------------------

    print("\n--- Ejecutando experimento B (efecto del factor de carga) ---")

    n_fijo = 20000
    alfas_objetivo = [0.25, 0.5, 1.0, 2.0, 4.0, 10.0]
    tiempos_tabla_b = []
    alfas_reales = []

    guias_fijas = set()
    while len(guias_fijas) < n_fijo:
        guias_fijas.add(random.randint(10**9, 10**10 - 1))

    inexistentes_b = generar_guias_inexistentes(guias_fijas, 200, semilla=42)

    for target_alpha in alfas_objetivo:
        m_estimado = int(n_fijo / target_alpha)
        m = siguiente_primo(m_estimado) 

        tabla_b = TablaHash(m)
        for g in guias_fijas:
            tabla_b.insertar(g, "en reparto")

        alpha_real = tabla_b.factor_carga()
        alfas_reales.append(alpha_real)

        t_iniico = time.perf_counter()
        for g_inex in inexistentes_b:
            res = tabla_b.buscar(g_inex)
            assert res is None
        t_fin = time.perf_counter()
        t_medio = ((t_fin - t_inicio) / 200) * 1e6
        tiempos_tabla_b.append(t_medio)

        print(
            f"Target alpha={target_alpha:5.2f} | Real alpha={alpha_real:5.2f} | " 
            f"m={m:5d} | Tiempo={t_medio:5.2f} us"
        )

    plt.figure(figsize=(8, 5)) 
    plt.plot(alfas_reales, tiempos_tabla_b, "d-", color="tab:purple", label="Tabla Hash ($n=20.000$)")
    plt.title("Tiempo Medio de Búsqueda Infructuosa vs. Factor de Carga ($\\alpha$)", fontsize=12) 
    plt.xlabel("Factor de carga ($\\alpha = n / m$)", fontsize=10) 
    plt.ylabel("Tiempo medio por búsqueda (microsegundos $\\mu s$)", fontsize=10) 
    plt.grid(True, linestyle="--", alpha=0.7) 
    plt.legend(fontsize=10) 
    plt.tight_layout() 
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150) 
    plt.close()

    print("\n¡Experimentos finalizados! Gráficas guardadas en la carpeta 'graficas/'.") 
    
if __name__ == "__main__": 
    ejecutar_experimento()