# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Mariana García · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `d7150a9`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 18 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 13 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **70 / 100** |
| **Nota (0–5)** | **3.50** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre "correcto" y "eficiente" y nombra la restricción que se incumple: la ventana de 4 horas.
- Explica con números (60 veces más datos, 3.600 veces más operaciones) por qué un servidor el doble de rápido no basta.
- En la Parte 2 relaciona las horas de CPU con el gasto de energía repetido cada noche durante años, y da dos perjuicios con quién asume el costo.
- Explica que el orden de la lista funciona como un triaje médico y por eso exige un ordenamiento correcto.

**Lo que puede mejorar:**
- El segundo ejemplo (consulta de notas) es muy breve y sus cifras (3 horas, 5 segundos) parecen supuestas; explique de dónde salen y qué se procesa exactamente.
- En la Parte 2, el perjuicio al operador del centro de contacto no se desarrolla; hágalo más concreto.

## 2. Calidad de la explicación teórica (18 / 25)
**Lo que hizo bien:**
- La Parte 3.1 define los tres casos, dice sobre qué se toma el máximo, el mínimo y el promedio, justifica el uso del peor caso y deja la predicción escrita antes del experimento.
- La recurrencia de merge sort está bien planteada, con cada término explicado, y se resuelve con el método maestro verificando que `f(n) = Θ(n)` coincide con `n^(log2 2)`.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- Falta el cálculo de insertion sort línea a línea: cuántas veces se ejecuta cada línea del código y cómo se suman. Solo se enuncian los resultados `O(n²)` y `Ω(n)`.
- El caso promedio de la Parte 3 se explica de forma muy general ("la mitad del camino"); justifíquelo mejor.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no alteran la lista original y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `sort()`.
- Los generadores producen lotes del tamaño pedido, con valores distintos y semilla reproducible. El escenario B queda bien armado.

**Lo que puede mejorar:**
- `merge_sort` no tiene el *docstring* pedido y varias funciones internas y `parte3_casos.py`/`parte4_complejidad.py` tampoco tienen docstring ni *type hints*.
- Quedaron comentarios `TODO` de la guía en el código.
- Hay muchas líneas largas, espacios sobrantes y falta de líneas en blanco entre funciones (estilo PEP 8).
- En `datos.py`, la línea de `import` quedó antes del docstring del módulo.

## 4. Calidad del análisis de las gráficas (13 / 20)
**Lo que hizo bien:**
- Las gráficas tienen título, ejes rotulados y leyenda, y los tres escenarios van en los mismos ejes.
- Identifica correctamente el peor caso (C, inverso), el mejor (B, casi ordenado) y el promedio (A) con base en sus datos, y contrasta con su predicción.
- El concepto técnico recomienda merge sort, responde a la compra del servidor con el dato de n = 6.400, extrapola a 1.200.000 registros declarándolo como estimación y discute memoria y estabilidad.

**Lo que puede mejorar:**
- La gráfica de la Parte 4.2 no se ve en el informe (ver punto 5), así que ese análisis queda sin su apoyo visual.
- Los tiempos de insertion sort con n = 6.400 son distintos en la Parte 3 (unos 5 segundos para el escenario aleatorio) y en la Parte 4 (1,38 s). Explique por qué (por ejemplo, otras condiciones del equipo al medir) y use una sola medición coherente para extrapolar.
- Explique con una o dos frases qué pasa en los tamaños pequeños; hoy solo se dice que las curvas se superponen.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- El informe está dividido por partes, enlaza el código de cada parte práctica y tiene más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- No siguió la estructura de carpetas acordada: la carpeta se llama `Lab1_fundamentos_complejidad_recurrencias` (con mayúscula y guion bajo) y debía ser `lab1-fundamentos-complejidad-recurrencias`.
- La imagen de la Parte 4 apunta a `parte4_tiempo.png`, pero el archivo se llama `parte4_tiempos.png`; por eso no se ve en GitHub. Además la guía pedía los nombres `parte3_tiempo.png` y `parte4_tiempo.png`.
- Las instrucciones de reproducción solo indican cómo entrar a la carpeta y activar el entorno; faltan los comandos para ejecutar cada parte.
- Se generaron gráficas extra de comparaciones que no se usan en el informe.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan correctamente y generan las gráficas en la carpeta `graficas/`.

## Para el próximo laboratorio
- Use exactamente los nombres de carpetas y archivos que pide la guía, y abra el informe en GitHub para comprobar que las imágenes se ven.
- Incluya siempre el cálculo línea a línea cuando se pida analizar un código.
- Agregue docstrings y *type hints* a todas las funciones, y revise el estilo PEP 8.
- Escriba en el informe los comandos para ejecutar cada parte.
- Repita las mediciones y use los mismos datos en todo el informe para que los números sean coherentes.
