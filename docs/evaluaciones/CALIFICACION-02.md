# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Mariana Garcia · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `c39cead`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 17 / 25 |
| Calidad del análisis de las gráficas | 14 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **72 / 100** |
| **Nota (0–5)** | **3.60** |

## 1. Corrección conceptual (14 / 20)
**Lo que hizo bien:**
- La comparación con hallar el máximo de un arreglo es clara: dividir no mejora porque combinar cuesta `Θ(1)` y la recurrencia da `Θ(n)`.
- Recomienda divide y vencerás y declara que lo de 1.000.000 de registros es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3 dice que divide y vencerás gana desde `n < 20`, pero lo explica solo con conteos teóricos. Su gráfica no permite ver los tamaños pequeños; debía apoyarse en una tabla o gráfica con los tiempos medidos.
- La estimación de la pregunta 5 parte de tiempos (3.32 s y 0.012 s en n = 8000) que no coinciden con su gráfica publicada (cerca de 1.5 s y 0.018 s), así que las cifras finales quedan en duda.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Resuelve con el método maestro verificando el caso 2.
- Justifica bien el `Θ(n²)` de la fuerza bruta con la suma de pares.

**Lo que puede mejorar:**
- Podría explicar por qué el caso cruzado cuesta lineal con una frase más sobre el tamaño de cada barrido.

## 3. Corrección de la implementación (17 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- Tiene `type hints` y docstrings en las funciones.

**Lo que puede mejorar:**
- En las 25 listas aleatorias de `pruebas.py` y en la verificación de `medicion.py` se compara el segundo valor de la tupla (el índice final), no la suma. La prueba pasa, pero no comprueba lo que dice comprobar.
- En `pruebas.py` las pruebas están sueltas fuera de `ejecutar_pruebas`, que solo imprime un mensaje.
- Falta dejar dos líneas en blanco entre algunas funciones.

## 4. Calidad del análisis de las gráficas (14 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calcula el factor de crecimiento al duplicar n y lo contrasta con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los valores del informe no coinciden con la gráfica publicada. Para fuerza bruta dice 0.83 s en n = 4000 y 3.32 s en n = 8000 (factor 4.00); en la gráfica se leen cerca de 0.92 s y 1.5 s (factor cercano a 1.6). Para divide y vencerás dice 0.0055 s y 0.012 s; en la gráfica se leen cerca de 0.012 s y 0.018 s.
- Parece que el informe se escribió con una corrida distinta a la que quedó publicada. Las afirmaciones deben salir de la gráfica entregada.
- No incluye una tabla con los tiempos medidos y no dice si repitió las mediciones.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta está en una ubicación válida, el informe sigue el orden pedido, la gráfica se ve y los enlaces al código funcionan.
- Hay más de tres commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción dicen `cd lab2-divide-y-vencer`, pero la carpeta está dentro de `laboratorios/`, y el entorno se busca en `../env`. Ajústelas a su estructura real.
- La gráfica aparece incrustada dos veces y el bloque de código de las instrucciones quedó sin cerrar.
- Se publicaron `.gitignore.txt` y un `main.py` suelto; conviene usar un solo `.gitignore`.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos funciones coinciden en listas aleatorias que probé por mi cuenta, y `medicion.py` corre y genera la gráfica.

## Para el próximo laboratorio
- Compare las sumas (no los índices) en las pruebas y en la verificación del experimento.
- Escriba en el informe solo valores leídos de la gráfica publicada, y vuelva a generarla antes de redactar.
- Agregue una tabla con los tiempos medidos para sustentar sus afirmaciones.
- Deje dos líneas en blanco entre funciones y revise que todas tengan docstring con `Args` y `Returns`.
- Pruebe sus instrucciones de reproducción desde cero con las rutas reales.
