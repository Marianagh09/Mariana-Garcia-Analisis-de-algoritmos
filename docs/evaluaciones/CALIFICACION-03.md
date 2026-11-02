# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Mariana García · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `36b158d`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 15 / 25 |
| Calidad del análisis de las gráficas | 14 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **76 / 100** |
| **Nota (0–5)** | **3.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y compara encadenamiento con direccionamiento abierto, con ventaja y costo de cada uno, usando el ejemplo de `10`, `24` y `17` con `m = 7`.
- Justifica con claridad por qué la tabla hash no sirve para rangos y qué ofrece el árbol de búsqueda.
- Estima la altura del árbol degenerado y la compara con la del equilibrado.
- Recomienda una combinación (tabla hash para consulta puntual y árbol equilibrado para rangos) y declara que la cifra de 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la estimación a 5.000.000 para la tabla hash repite el valor medido con 50.000 guías sin explicar por qué debería mantenerse así.
  → *Cómo corregirlo:* explique qué pasa con `α` si usted dimensiona la tabla para ese tamaño y cómo eso se refleja en el tiempo de la curva de la tabla.
- En la lista, la estimación depende de que la curva sea una recta, pero no lo argumenta con lo que se ve en su gráfica.
  → *Cómo corregirlo:* apóyese en los factores de crecimiento que ya calculó en la pregunta 2 para justificar por qué la forma de la curva permite extrapolar.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla, nombra el supuesto de hash uniforme simple y explica qué pasa si todas las guías caen en una casilla.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el caso de una sola casilla solo menciona `m = 1`; no distingue una función hash mala de una tabla pequeña.
  → *Cómo corregirlo:* añada una frase sobre qué tipo de guías podrían amontonarse en una casilla con `k mod m` aunque `m` sea grande.

## 3. Corrección de la implementación (15 /25)
**Lo que hizo bien:**
- `estructuras.py` está bien hecha: la lista inserta al inicio y busca con un ciclo, la tabla reutiliza la lista, no usa `dict`, `set` ni `hash()`, y `factor_carga` es correcto. Mis propias pruebas (colisión con `m = 7` y 30 colecciones aleatorias) dieron lo mismo en lista y tabla.
- Tiene *type hints* y *docstrings* completos en las estructuras.

**Lo que puede mejorar (y cómo corregirlo):**
- `pruebas.py` no se ejecuta: se detiene con error antes de terminar. Hay varios fallos: la lista de guías de la colisión está escrita como `[1-3]` (una resta) en vez de `10, 24, 17`; se consulta `tabla_colision.casilla` en vez de `casillas`; se espera la casilla 4 en vez de la 3; se escribió `random.randit`; y `assert ... in None` en lugar de `is None`.
  → *Cómo corregirlo:* ejecute `python pruebas.py` y corrija cada error que aparezca, uno por uno, hasta ver todas las pruebas pasar. Cambie `[1-3]` por `[10, 24, 17]` y recuerde que `10 % 7` da 3.
- En la prueba aleatoria solo se comprueba la tabla contra el estado esperado, no se compara la lista con la tabla guía por guía, y `m` es siempre 13.
  → *Cómo corregirlo:* dentro del ciclo, compare `lista_rand.buscar(g) == tabla_rand.buscar(g)` para guías existentes e inexistentes.
- En `medicion.py`, las funciones `es_primo` y `siguiente_primo` no tienen `Args` y `Returns` en su *docstring*, y falta una línea en blanco doble antes de algunas funciones.
  → *Cómo corregirlo:* agregue las secciones `Args:` y `Returns:` y deje dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (14 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con las dos curvas en los mismos ejes y la segunda seis valores de `α`.
- En la pregunta 2 calcula bien los factores de crecimiento de `n = 20.000` a `n = 50.000` (lista 2,97 veces, tabla 1,28 veces) y los contrasta con `Θ(n)` y `Θ(1)`. Esas cifras coinciden con lo que muestra `lista_vs_tabla.png`.

**Lo que puede mejorar (y cómo corregirlo):**
- La segunda gráfica (`tiempo_vs_alfa.png`) muestra tiempos de unos 6.000 a 7.000 microsegundos por búsqueda en la tabla, mientras que en la primera gráfica la tabla con `n = 20.000` tarda menos de 1 microsegundo. Son valores incompatibles: en el Experimento B el cronómetro de cada medición parte de una variable de otro experimento (`t_inicio`, y se escribió `t_iniico`), así que lo medido incluye tiempo ajeno a las búsquedas.
  → *Cómo corregirlo:* revise que `t_iniico = time.perf_counter()` y `t_fin - t_inicio` usen el mismo nombre; vuelva a ejecutar `medicion.py` y compare el orden de magnitud con la primera gráfica.
- Como esos valores no son los de las búsquedas, la lectura de la pregunta 2 sobre `α` (de 5.836 a 7.153 microsegundos) no está respaldada y no se puede contrastar bien con `Θ(1 + α)`.
  → *Cómo corregirlo:* con la medición corregida, vuelva a calcular cuánto cambia el tiempo cuando `α` crece y compárelo con la forma `1 + α`.
- La nota sobre la medición no menciona si repitió las mediciones para reducir el ruido.
  → *Cómo corregirlo:* si repite cada medición varias veces y promedia, dígalo en el informe.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab3-estructuras-datos/` (ubicación válida), con todos los archivos del entregable y las dos gráficas, que se ven en el informe con ruta relativa.
- El informe sigue el orden pedido, tiene su nombre, instrucciones de reproducción y enlaces a `estructuras.py`, `pruebas.py` y `medicion.py`. Hay seis commits descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- El informe dice que las pruebas cubrieron los cuatro casos y pasaron, pero `pruebas.py` no termina; la descripción no coincide con lo que realmente ocurre.
  → *Cómo corregirlo:* corrija las pruebas y vuelva a verificar que lo descrito en la Parte 1 es lo que su script comprueba.

## ¿El código funciona?
Las estructuras de `estructuras.py` funcionan bien. `pruebas.py` se detiene con un error y no termina, y `medicion.py` genera las gráficas, pero los tiempos del Experimento B salen mal calculados.
