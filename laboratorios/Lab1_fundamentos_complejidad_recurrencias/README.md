# Laboratorio 1 - Fundamentos, complejidad y recurencias

**Mariana Garcia**

## Instrucciones para Reproducir el Experimento

Para ejecutar los scripts y reproducir las mediciones y gráficas generadas en este laboratorio, sigue estos pasos desde la terminal de VS Code o PowerShell:

### 1. Ubicarse en el directorio del laboratorio

**cd laboratorios/Lab1_fundamentos_complejidad_recurrencias**

### 2. Activar el entorno virtual

**..\..\env\Scripts\Activate.ps1**

## Parte 1 - Analizar el algoritmo antes de comprar el hardware

### ¿Por qué analizar el algoritmo si lleva 8 años funcionando? 

El hecho de que el programa entregue la respuesta correcta no quiere decir que sea viable para trabajar en producción; existe una clara diferencia entre que un sistema sea correcto y que sea eficiente:

* **Correcto:** Significa que el programa hace lo que se le pide sin errores. En este caso, el algoritmo de Tamiza cumple esto porque ordena el resultado de los pacientes de mayor a menor riesgo.
* **Eficiencia:** Mide el tiempo que demora el sistema para entregar el resultado dentro de un límite adecuado.

Tamiza tiene un algoritmo que entrega la respuesta correcta pero dejó de ser eficiente para las necesidades actuales. El sistema falla porque no cumple con la ventana estricta de 4 horas nocturnas; al no terminar el proceso, la lista queda incompleta y no se puede llamar a los pacientes en orden de prioridad, perdiendo su propósito.

### El problema con Insertion Sort y un nuevo servidor

Antes de gastar presupuesto, es necesario analizar el contexto completo. Tamiza usa *Insertion Sort*, un algoritmo que funciona bien con pocos datos, pero su tiempo de ejecución crece de forma cuadrática **O(n²)** a medida que aumentan los datos.

Al inicio la plataforma procesaba **20.000** registros y el volumen era pequeño, por lo que el servidor operaba sin problemas. Al aumentar el volumen a **1.200.000** registros, el número de datos aumentó **60 veces**; sin embargo, al ser un algoritmo cuadrático, el número de operaciones aumentó $60^2 = 3.600$ **veces más**.

La propuesta de comprar un servidor del doble de velocidad solo reduciría el tiempo a la mitad, lo cual no soluciona el problema frente a un incremento de **3.600 veces** en las operaciones, superando de nuevo las 4 horas límite.

### Ejemplo

En un sistema académico de consulta de notas con **15.000** estudiantes ingresando al mismo tiempo:

Si el sistema busca las notas una a una con ciclos anidados **O(n²)**, el servidor se satura y puede demorarse **3 horas** en procesar las solicitudes. Aunque el resultado final sea 100 % correcto, prácticamente no sirve porque incumple con el tiempo máximo de respuesta del servidor (**5 segundos**) y causa la caída de la página.



## Parte 2 - Responsabilidad ambiental y etica de la implementacion

### Dimension ambiental: Consumo energetico acumulado

Decidir que algoritmo se ejecuta en produccion tambien es una decision ambiental. Un algoritmo con poca eficiencia como *Insertion Sort* mantiene el procesador del servidor trabajando al $100%$ durante las 4 horas en la noche mientras se realiza el proceso. Por otro lado, un algoritmo optimizado y eficiente, resolveria esa misma cantidad de datos en cuestion de segundos.

Mantener la CPU al maximo durante horas es un gasto directo de energia electrica y tambien es un esfuerzo adicional de los sistemas de aire para refrigerar y enfriar el servidor. Cuando este gasto de energia se repite durante los 365 dias del año, durante varios años, la huella de carbono que deja es bastante alta e innecesaria que se habria podido evitar con un algoritmo mas eficiente. 


### Dimension etica: Impacto real en las personas y responsabilidad del costo

Cuando el proceso de analisis y ordenamiento no termina antes de las 6 a.m. entonces la lista de llamadas queda incompleta o desordenada, las consecuencias afectan a personas reales:

* **Retraso en la atención de pacientes en estado crítico:** Si el sistema se corta a las 6 a. m., los pacientes con índices de riesgo cardiovascular muy altos que quedaron al final de la lista no son contactados ese día.
  * **¿Quién asume el costo?** El *paciente*, ya que su salud puede empeorar gravemente o sufrir un evento cardiaco que se pudo prevenir con una cita a tiempo.
* **Uso ineficiente de los recursos de salud:** El centro de llamadas pasa el día contactando a personas con riesgo bajo simplemente porque fueron los registros que el algoritmo alcanzó a procesar antes del corte.
  * **¿Quién asume el costo?** La **Secretaría de Salud**, que malgasta presupuesto y tiempo de los operadores en llamadas que no eran urgentes, dejando desprotegida a la población que más lo necesitaba.

  ### La resopnsabilidad tecnica sobre el orden de la lista

  En este caso, el ordenamiento de la lista no es un proceso meramente tecnico o que se haga porque si, funciona mas bien como un tipo de triaje medico que decide cual es la persona que debe ser atendida primero. 

  Por lo que se exige garantizar que el **algoritmo sea completamente correcto**. Si el sistema llega a fallar o sirve a medias, se altera el orden de prioridad, haciendo que el acceso a la atencion medica dependa mas del funcionamiento o fallos del software que de la urgencia de salud del paciente.


## Parte 3 - Peor caso, mejor caso y caso promedio en Insertion Sort

### 3.1 

> **Código de la Parte 3:** Ver el script de experimentos en [`parte3_casos.py`](parte3_casos.py). Los algoritmos de ordenamiento están implementados en [`algoritmos.py`](algoritmos.py) y los generadores de escenarios en [`datos.py`](datos.py).

### Definicion teorica de los casos

1. **Peor caso:** Es el escenario donde el algoritmo más sufre y hace la mayor cantidad de trabajo.
   * **¿Sobre qué se mide?:** Buscamos el **costo máximo** dentro de todo el grupo de entradas posibles que miden exactamente *n*. Nos da el "techo" o límite superior de tiempo que el algoritmo jamás va a superar para ese tamaño.
2. **Mejor caso :** Es el escenario ideal donde los datos vienen tan acomodados que el algoritmo termina lo más rápido posible.
   * **¿Sobre qué se mide?:** Buscamos el **costo mínimo** entre todas las entradas posibles que miden exactamente *n*. Nos muestra lo más rápido que puede llegar a correr si el orden inicial lo favorece al máximo.
3. **Caso promedio:** Es lo que esperamos que pase en un día normal de operación con datos reales o desordenados al azar.
   * **¿Sobre qué se mide?:** Se calcula sacando un **promedio ponderado** sobre todas las entradas de tamaño *n*, teniendo en cuenta qué tan probable es que nos llegue cada tipo de datos en la práctica. 

### Criterio de decision en produccion

Para definir si este algoritmo sirve para **Tamiza** dentro de las 4 horas necesarias, pues debemos basarnos si o si en el **peor caso** porque si nos confiamos y asumimos que siempre sera el caso promedio, el dia que los datos lleguen atipicamente invertidos, haria que el tiempo de produccion sobrepase las 4 horas, provocando que el proceso vuelva a colapsar. 

### Prediccion teorica para los escenarios 

Dado que muestroalgoritmo ordena de **mayor a menor** 
* **Prediccion del peor caso:** Escenario C (*Inverso*) porque en el caso completamente inverso, debe comparar elemento por elemento, reacomodando a cada uno en su ubicacion contraria, entonces para hacer la comparacion e insercion de cada elemento, es el caso que mas tiempo toma.
* **Prediccion del mejor caso:** Escenario B (*Casi ordenado*) porque aunque deba seguir lacomparacion de todos los elementos, pues la mayoria ya estan en su ubicacion excata, entonces demora menos tiempo, por ejemplo en este caso, solo el 2% de los elementos estan en un orden aleatorio, lo que hace que demore menos tiempo en ejecucion.
* **Prediccion caso promedio:** Escenario A (*Aleatorio*) porque demora la mitad de tiempo que el peor caso, porque como esta aleatoria pero no inversa, entonces encuentra su ubicacion correcta en la mitad del camino, por lo que demora la mitad del tiempo.

### Graficas y comparaciones

A continuación se presentan las gráficas obtenidas tras ejecutar los experimentos evaluando los tres escenarios sobre los tamaños $n \in \{100, 200, 400, 800, 1600, 3200, 6400\}$:

#### Comparaciones vs. Tamaño de Entrada ($n$)
![Comparaciones de Insertion Sort](graficas/parte3_comparaciones.png)

#### Tiempo de Ejecución vs. Tamaño de Entrada ($n$)
![Tiempo de Ejecución de Insertion Sort](graficas/parte3_tiempos.png)

* **Peor Caso $\rightarrow$ Escenario C (Inverso - Línea Verde):** Curva parabólica ascendente con el crecimiento más pronunciado. En $n = 6400$, llegó a aproximadamente $2.0 \times 10^7$ comparaciones y cerca de 8 segundos de ejecución.
* **Mejor Caso $\rightarrow$ Escenario B (Casi Ordenado - Línea Naranja):** Curva completamente plana sobre el eje horizontal, registrando un número de comparaciones que escala de manera lineal y tiempos de ejecución prácticamente instantáneos (cercanos a 0 segundos).
* **Caso Promedio $\rightarrow$ Escenario A (Aleatorio - Línea Azul):** Curva cuadrática intermedia que crece con una pendiente proporcional a la mitad del peor caso (alrededor de $1.0 \times 10^7$ comparaciones en $n = 6400$). 

**Análisis de la coincidencia:**
Los resultados experimentales coinciden al 100% con la predicción inicial. Como el algoritmo ordena de **mayor a menor**:
1. Entregarle los datos ordenados en sentido contrario (ascendente, 1 a $n$) obligó a desplazar cada nuevo número a lo largo de todo el subarreglo ordenado antes de insertarlo, desencadenando el peor comportamiento posible $O(n^2)$.
2. Entregarle un vector preordenado casi al 98% de mayor a menor permitió que el bucle interno rompiera la condición en la primera evaluación la gran mayoría de las veces, confirmando la complejidad $O(n)$.
3. El escenario aleatorio requirió en promedio desplazar los elementos hasta la mitad de la secuencia ordenada, generando la mitad exacta del costo del peor caso.


## Parte 4 - Comparacion entre insertion Sort y Merge Sort

> **Código de la Parte 4:** Ver el script de medición comparativa en [`parte4_complejidad.py`](parte4_complejidad.py). La función `merge_sort` y `insertion_sort` se encuentran en [`algoritmos.py`](algoritmos.py) y la generación de arreglos aleatorios en [`datos.py`](datos.py).

### 4.1 Analisis teorico 

### Tabla Resumen de Complejidades Teóricas

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso | Espacio Auxiliar (Memoria) |
| :--- | :--- | :--- | :--- | :--- |
| **Insertion Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ *(In-place)* |
| **Merge Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ *(Arreglos auxiliares)* |

* **Notas sobre el comportamiento:**
  * **Insertion Sort:** Logra su mejor caso $\Omega(n)$ únicamente cuando el arreglo de entrada ya se encuentra en el orden deseado, evitando recorrer el bucle interno. Su peor caso $O(n^2)$ ocurre cuando la lista está completamente invertida.
  * **Merge Sort:** Mantiene la cota $\Theta(n \log n)$ de manera determinista en todos los escenarios, ya que la división recursiva y la fase de combinación (*merge*) realizan siempre el mismo número de particiones y comparaciones, independientemente del orden previo de los datos.

### 1. Recurrencia de Merge Sort

La ecuación de recurrencia que describe el tiempo de ejecución de Merge Sort es:

$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

#### Desglose de sus componentes:
* **$2$ (Subproblemas):** Al aplicar la estrategia de Divide y Vencerás, dividimos el arreglo original en 2 subarreglos de igual tamaño.
* **$T(n/2)$ (Tamaño del subproblema):** Corresponde al costo recursivo de procesar cada mitad, la cual contiene $n/2$ elementos.
* **$\Theta(n)$ (Costo de dividir y combinar):** La división en sí es una operación trivial de índice medio que toma $O(1)$. Sin embargo, la función de mezcla (*merge*) debe recorrer todos los elementos de ambas sublistas para ordenarlos de forma descendente, lo que requiere $n-1$ comparaciones en el peor caso y un total de $n$ copias de elementos. Por tanto, el costo de combinar es estrictamente lineal, $\Theta(n)$.

### 2. Resolución por Método Maestro

Para resolver $T(n) = 2T(n/2) + \Theta(n)$, extraemos los parámetros del modelo $T(n) = aT(n/b) + f(n)$:

1. **Parámetros principales:**
   * $a = 2$ (Llamadas recursivas por nivel)
   * $b = 2$ (Factor de división del tamaño)
   * $f(n) = \Theta(n)$ (Trabajo realizado fuera de las llamadas recursivas)

2. **Cálculo de la cota crítica $n^{\log_b a}$:**
   $$n^{\log_2 2} = n^1 = n$$

3. **Comparación y caso aplicable:**
   Comparamos $f(n)$ con $n^{\log_b a}$:
   $$f(n) = \Theta(n) \quad \text{y} \quad n^{\log_b a} = n$$

   Dado que $f(n) = \Theta\left(n^{\log_b a}\right)$, cae de forma exacta en el **Caso 2 del Método Maestro**.

4. **Conclusión:**
   Aplicando la fórmula del Caso 2, tenemos:
   $$T(n) = \Theta\left(n^{\log_b a} \cdot \log n\right) \implies T(n) = \Theta(n \log n)$$

### 4.2 — Validación Empírica y Análisis Comparativo

A continuación se presenta la gráfica comparativa de tiempos de ejecución entre **Insertion Sort** y **Merge Sort** obtenida a partir de las mediciones experimentales sobre el escenario aleatorio para tamaños de entrada de hasta $n = 6400$:

![Tiempo de Ejecución: Insertion vs Merge Sort](graficas/parte4_tiempo.png)


#### Análisis del Comportamiento de las Curvas

* **Curva de Insertion Sort (Línea Roja):** Muestra un crecimiento marcadamente parabólico. Para tamaños de entrada pequeños ($n \le 400$), el tiempo de ejecución se mantiene por debajo de los $0.05$ segundos. Sin embargo, a medida que $n$ aumenta hacia $3200$ y $6400$, la curva se dispara exponencialmente hacia arriba, alcanzando aproximadamente $1.38$ segundos para el tamaño máximo medido.
* **Curva de Merge Sort (Línea Azul):** Se mantiene prácticamente pegada al eje horizontal ($y \approx 0$) a lo largo de todo el experimento. Incluso al alcanzar $n = 6400$, el tiempo de ejecución permanece por debajo de $0.02$ segundos, mostrando una pendiente casi plana y un incremento apenas perceptible frente al aumento del tamaño de los datos.


#### Conclusión sobre el Mejor Algoritmo para Tamiza

Observando directamente el comportamiento de las curvas en la gráfica, **Merge Sort es indiscutiblemente el mejor algoritmo para la plataforma Tamiza**. 

La razón se evidencia en la brecha que se abre entre ambas líneas a medida que la carga de datos aumenta: mientras que la curva de *Insertion Sort* crece rápidamente mostrando un costo cuadrático inviable para volúmenes grandes, la curva de *Merge Sort* demuestra una resistencia excepcional al escalamiento. Para procesar grandes lotes de índices de riesgo, *Merge Sort* mantendrá los tiempos de ejecución en órdenes de magnitud sustancialmente menores.


#### Coincidencia con el Análisis Teórico

Esta conclusión **coincide al 100%** con las complejidades calculadas en el apartado 4.1: la gráfica refleja experimentalmente la diferencia abismal entre una complejidad cuadrática $O(n^2)$ para *Insertion Sort* y una complejidad logarítmico-lineal $O(n \log n)$ para *Merge Sort*.

* **Comportamiento en tamaños pequeños:** Para valores de $n \le 200$, ambas curvas se observan superpuestas cerca del origen debido a la sobrecarga inicial que representan las llamadas recursivas y la asignación de memoria en *Merge Sort*. En ese rango reducido, la simplicidad de *Insertion Sort* compensa su complejidad teórica, pero esta ventaja desaparece tan pronto como $n$ supera los pocos cientos de elementos.

### 4.3 — Concepto Técnico a la Secretaría de Salud


#### 1. Recomendación de Algoritmo Unificado

Considerando que el flujo de reproceso puede alterar el orden de los datos sin previo aviso y con el fin de mantener un código limpio y mantenible (evitando la redundancia de sostener múltiples algoritmos), **recomendamos adoptar Merge Sort como la única implementación estándar en Tamiza**. 

La decisión se fundamenta en la cota de rendimiento garantizada. Mientras que *Insertion Sort* presenta una degradación drástica cuando la entrada se desordena, *Merge Sort* mantiene una estabilidad predecible $O(n \log n)$ sin importar el estado inicial de la lista. Frente a la incertidumbre del canal de entrada, sacrificar la ligera ventaja de *Insertion Sort* en arreglos casi ordenados es un compromiso aceptable a cambio de blindar el sistema contra colapsos en el peor escenario.

#### 2. Extrapolación de Tiempos para 1.200.000 Registros

Para evaluar si el procesamiento de $N = 1.200.000$ registros cumple con la ventana límite de **4 horas (14.400 segundos)**, extrapolamos los tiempos a partir de las mediciones obtenidas en la gráfica de ejecución para $n = 6.400$:

* **Insertion Sort (Algoritmo Actual):**
  * En nuestras pruebas con $n = 6.400$, registró un tiempo de **1,38 segundos**.
  * Asumiendo un comportamiento cuadrático $T(n) \approx c \cdot n^2$, obtenemos una constante $c \approx \frac{1,38}{6.400^2} \approx 3,37 \times 10^{-8}\text{ s}$.
  * Extrapolando para $1.200.000$ datos: $T(1.200.000) \approx 3,37 \times 10^{-8} \times (1.200.000)^2 \approx \mathbf{48.528\text{ segundos (13,48 horas)}}$.
  * *Resultado:* **Incumple gravemente** la ventana operativa de 4 horas.

* **Merge Sort (Algoritmo Recomendado):**
  * En las mismas pruebas con $n = 6.400$, registró un tiempo de apenas **0,02 segundos** (como se observa en la gráfica de tiempo del punto 4.2).
  * Asumiendo un comportamiento logarítmico-lineal $T(n) \approx c \cdot n \log_2(n)$, la constante es $c \approx \frac{0,02}{6.400 \cdot 12,64} \approx 2,47 \times 10^{-7}\text{ s}$.
  * Extrapolando para $1.200.000$ datos: $T(1.200.000) \approx 2,47 \times 10^{-7} \times (1.200.000 \cdot 20,19) \approx \mathbf{5,98\text{ segundos}}$.
  * *Resultado:* **Cumple con holgura**, procesando la carga en menos de 10 segundos.

> *Aclaración:* Estas cifras representan una **estimación por extrapolación matemática** basada en el crecimiento de las curvas medidas localmente; no constituyen una medición directa en un entorno de producción con $1.200.000$ registros.

#### 3. Respuesta a la Propuesta de Adquisición de Hardware

**Se aconseja rotundamente NO hacer la compra del nuevo servidor con el doble de velocidad.** 

Revisando nuestros datos experimentales (tomados directamente de la gráfica de la Sección 4.2 para $n = 6.400$), *Insertion Sort* tardó **1,38 segundos**, mostrando una curva con pendiente casi vertical. Duplicar la velocidad del procesador solo reduciría el tiempo extrapolado de 13,48 horas a aproximadamente 6,74 horas, lo cual **sigue violando la restricción de 4 horas**. El cuello de botella no es el hardware, sino la ineficiencia del algoritmo; cambiar la lógica del software a *Merge Sort* resuelve el problema en la infraestructura actual sin realizar gasto alguno.

#### 4. Consideraciones Adicionales

* **Uso de Memoria:** *Merge Sort* requiere $O(n)$ de espacio auxiliar. Para 1,2 millones de enteros de 64 bits, la memoria adicional consumida es de aproximadamente $\sim 9,6\text{ MB}$, un impacto completamente despreciable para los servidores de la plataforma.
* **Estabilidad del Ordenamiento:** *Merge Sort* es un algoritmo estable, lo que garantiza que si dos registros tienen el mismo índice de riesgo, conservarán su orden de llegada original.
* **Riesgo Operativo:** Si el flujo de reproceso cambia y los datos dejan de estar parcialmente ordenados, *Insertion Sort* cae inmediatamente en su peor caso $O(n^2)$. *Merge Sort* elimina este riesgo arquitectónico por completo.

