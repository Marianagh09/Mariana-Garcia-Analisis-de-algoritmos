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