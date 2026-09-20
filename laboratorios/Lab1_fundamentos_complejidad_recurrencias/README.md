# Laboratorio 1 - Fundamentos, complejidad y recurencias

**Mariana Garcia**

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