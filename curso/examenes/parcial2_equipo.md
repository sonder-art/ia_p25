c.u (personal)                           __________________________________________  

c.u (otrx mienbro del equipo)            __________________________________________  

c.u (otrx mienbro del equipo)            __________________________________________  

c.u (otrx mienbro del equipo)            __________________________________________  


# Examen Parcial 2: Bandits y Cadenas de Markov (Equipo)
Escribe tu clave unica hasta arriba, y luego las claves unicas del resto del equipo.Este examen es en equipo y consta de dos partes: una escrita y otra oral. La parte oral también se realiza en equipos: de forma aleatoria, se les llamará a exponer su proyecto de manera breve. **Tienen 7 minutos para organizarse y 7 minutos para exponer.**La exposición se hará sin computadora; únicamente pueden usar plumón y pizarrón.  

Durante todo el examen está prohibido el uso de computadora o celular; únicamente se permite papel y lápiz. No se permite hablar mientras otros equipos están exponiendo, sique siendo examen. Se espera que presten atención y evalúen activamente a los demás equipos. Además, deberán realizar una evaluación (*review*) para cada presentación de equipo. 

**Instrucciones:**  

Escribe tu clave en la parte superior izquierda de esta hoja y en cada una de las páginas siguientes.  


## 1. Exposición  (34 puntos)
El equipo deberá responder las preguntas que haré de manera aleatoria. La calificación de la exposición se basará en esas respuestas.

## 2. Evaluación del Problema de Decisión  (34 puntos)
Cada equipo debe evaluar objetivamente a los demás equipos. **La evaluación que realicen no afectará la calificación del equipo evaluado, así que puede y debe hacerse con objetividad.** Por cada pregunta y respuesta, documenten qué estuvo bien, qué estuvo mal y qué cambiarían (o no). Pueden abordar aspectos técnicos, así como estrategias que hayan aprendido y que podrían aplicar para mejorar su propia solución.  


### 2.1 Ejemplo de respuesta  

**Equipo 2**

**Pregunta 1:**  
La estrategia que presentaron fue estructurada y clara en su presentación, lo cual facilitó entender su razonamiento. Sin embargo, se observó una limitación importante en el análisis: el equipo no consideró adecuadamente que la probabilidad de ganar está regida por un proceso de Markov conjunto.  

Este aspecto es fundamental, ya que en un entorno donde las decisiones están interrelacionadas en el tiempo, ignorar las transiciones de estado puede conducir a una pérdida significativa de información útil para la toma de decisiones óptimas.  

Habría sido valioso que explicaran cómo modelaron dichas transiciones o, en su defecto, por qué decidieron omitir ese componente del modelo. La omisión no fue justificada, lo que podría interpretarse como una falta de comprensión del marco teórico completo.

**Pregunta 2:**  
La heurística propuesta por el equipo fue interesante y aportó una perspectiva distinta al problema. Ellxs diseñaron una aproximación basada en inferencias sobre el estado inicial del sistema, lo cual abre la posibilidad de mejorar la exploración temprana del entorno.  

Nos pareció que este enfoque podría complementar eficazmente la estrategia que desarrollamos en nuestro equipo. En nuestro caso, no contemplamos la inferencia del estado inicial como un componente clave, y esta idea podría ayudarnos a refinar nuestro algoritmo en etapas tempranas de aprendizaje.  

Además, ellxs mostraron una buena capacidad para justificar su elección heurística, explicando cómo podría adaptarse dinámicamente a diferentes configuraciones del problema. Sería interesante explorar una combinación de ambas estrategias para evaluar posibles mejoras.