# Laboratorio 1 - Fundamentos, complejidad y recurencias

**Mariana Garcia**

## Parte 1 - Analizar el algoritmo antes de comprar el hardware

### ¿Por qué analizar el algoritmo si lleva 8 años funcionando? 

El hecho de que el programa entregue la respuesta correcta, no quiere decir que sea viable para trabajar en produccion, existe una diferencia entre que sea correcto y que sea eficiente

**Correcto:** Significa que el programa hace lo que se le pide sin errores, en este caso, el algoritmo de Tamiza cumple esto porque ordena el resultado de los pacientes de mayor a menor riesgo.
**Eficiencia:** Mide el tiempo que demora el sistema para entregar el resultado dentro de un limite adecuado.

Tamiza tiene un algoritmo que puede entregar la respuesta correcta pero que dejo de ser eficiente para las necesidades actuales. El sistema falla porque no cumple con la ventana estricta de 4 horas nocturnas, por lo que el sistema no termina el proceso, entonces la lista queda incompleta y no se pueden llamar a los pacientes en orden de prioridad, por lo que se estaria perdiendo su proposito. 

### El problema con Insertion Sort y un nuevo servidor##

Antes de gastar presupuesto, es bueno analizar el contexto completo, Tamiza usa "Insertion Sort" un algoritmo que funciona bien con pocos datos, pero su tiempo de ejecucion crece de forma cuadratica ($\mathcal{O}(n^2)$) a medida que aumentan los datos.

Al inicio la plataforma procesaba $20.000$ registros, el volumen era pequeño por lo que el servidor operaba sin problemas. Pero al aumentar el volumen a $1.200.000$ registros. En teoria el volumen aumento **60 veces**, pero por el algoritmo al ser cuadratico, entonces aumento $60^2 = 3.600$ **veces más**.

Entonces la propuesta de comprar un servidor del doble de velocidad solo solucionaria reducir el tiempo a la mitad, pero para un problema que se multiplico por **3.600** pues no solucionaria nada porque se sigue pasando de las 4 horas limites necesarias para cumplir con su objetivo.

### Ejemplo###

El sistema academico a la hora de consultar las notas, con $15.000$ estudiantes ingresando al mismo tiempo.
Si el sistema busca las notas una a una con ciclos anidados ($\mathcal{O}(n^2)$), el servidor se puede saturar y se puede llegar a demorar **3 horas** en procesar las solicitudes, esto no es eficiente porque aunque el resultado final sea $100\%$ correcto, practicamente no sirve porque incumple con el tiempo maximo aproximado de **5 segundos** y puede suceder que la pagina se caiga. 
