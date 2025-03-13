# Notation Guide

Antes de sumergirnos en las **Cadenas de Markov** y su papel en los agentes de **AI**, pongámonos cómodos con la notación que usaremos. Piensa en estos símbolos como un lenguaje para describir cómo cambian los sistemas, cómo los agentes perciben y actúan y cómo predecimos lo que sigue. Están diseñados para ser intuitivos pero precisos, conectando las matemáticas con ideas del mundo real como cambios de clima o movimientos en un juego. Cada símbolo captura una parte del rompecabezas—estados, transiciones, observaciones y decisiones—y los iremos desarrollando a lo largo del capítulo.

## ¿De Qué Se Trata Todo Esto?

En esencia, esta notación registra los estados de un sistema (lo que sucede), cómo cambian con el tiempo o las acciones, lo que un agente percibe y cómo decide. Es lo suficientemente flexible como para modelar un robot navegando una habitación o un jugador trazando estrategias en un juego. Comenzaremos con las **Cadenas de Markov**—donde solo necesitamos los estados—y luego daremos indicios de cómo esto se expande hacia estados ocultos, acciones y creencias. ¿Listo? Aquí tienes el repertorio:

## Símbolos Principales

* **$s$**: Hidden States  
  Las "verdades" o condiciones subyacentes de un sistema—como el clima (soleado o lluvioso) o la ubicación de un robot (habitación A o B). Esto es lo que rastreamos o adivinamos. En los diagramas, aparecen en negritas ($s$) para captar tu atención como la base de todo.

* *$o$*: Observations  
  Las pistas o datos sensoriales que obtenemos sobre los estados—como ver nubes (sugiriendo lluvia) o escuchar un pitido (indicando una posición). Están en cursivas ($o$) en el texto para distinguirlos de los estados, ya que son lo que percibimos, no la verdad completa.

* <u>$a$</u>: Actions  
  Decisiones que un agente toma para influir en el sistema—como girar a la izquierda o accionar un interruptor. Están subrayadas ($a$) en los ejemplos para destacar las decisiones que moldean lo que sucede a continuación.

* $t(s,s')$: Transition Probability  
  La probabilidad de pasar del estado $s$ al estado $s'$—piensa en “¿cuál es el siguiente paso?”. Es un número entre 0 y 1 (p. ej., 0.7 de probabilidad de lluvia después de sol) que captura cómo evolucionan los estados. Para las **Cadenas de Markov**, esto es lo más importante.

* $t(s,s',a)$: Action-Driven Transition Probability  
  Cuán probable es que $s'$ siga a $s$ cuando se toma la acción $a$—como “si giro a la derecha, ¿qué sigue?”. Añade control a las transiciones, anticipando la toma de decisiones que veremos en los **MDPs**.

* $e(o|s)$: Emission Probability  
  La probabilidad de observar $o$ dado el estado $s$—respondiendo “¿qué veo si esto es verdad?”. Por ejemplo, una probabilidad de 0.9 de ver nubes si está lloviendo. Esto es un anticipo de los **HMMs**, donde los estados están ocultos tras las observaciones.

* $b(s)$: Belief Distribution  
  La mejor conjetura del agente sobre $s$, basada en lo que ha percibido—como “estoy 80% seguro de que llueve”. Es una distribución de probabilidad sobre los estados, un puente entre percepción y acción, y alude a los **POMDPs**.

* $r(s,a)$: Reward  
  La ganancia por estar en $s$ y tomar $a$—piensa en “¿fue una buena jugada?”. Podría ser +5 puntos por una victoria. Es clave para agentes orientados a objetivos, preparando el terreno para los **MDPs**.

## Cómo los Usaremos

En este capítulo, las **Cadenas de Markov** se basan en $s$ y $t(s,s')$ para modelar la evolución de estados—como la posición cambiante en un tablero de juego. Insinuaremos cómo $e(o|s)$ oculta estados en los **HMMs**, cómo $t(s,s',a)$ y $r(s,a)$ añaden decisiones en los **MDPs**, y cómo $b(s)$ maneja la incertidumbre en los **POMDPs**. Cada símbolo construye intuición para agentes que interactúan con entornos.

## En Comparación con Notaciones Clásicas

Nuestra notación es personalizada pero se asemeja a las clásicas:

* Sutton & Barto (MDPs): Usan $S$ para estados, $P(s'|s,a)$ para transiciones y $R(s,a)$ para recompensas. Simplificamos con $s$, $t$ y $r$, haciendo las transiciones más memorables (“t” por transition) y usando minúsculas para estados para mayor legibilidad.
  
* Rabiner (HMMs): Tiene $A$ para transiciones, $B$ para emisiones y $\pi$ para estados iniciales. Nuestros $t$ y $e$ son similares pero unificados en todos los conceptos, evitando letras adicionales.
  
* Probabilidad Estándar: A menudo se ve $P(s_{t+1}|s_t)$ para transiciones—lo condensamos a $t(s,s')$ por brevedad y enfoque en el agente. La nuestra está simplificada para estudiantes, mezclando la intuición del agente con las matemáticas, y a la vez permanece flexible para visualizaciones ($s$, $o$, $a$) y capítulos futuros.

*[Image Placeholder: Diagrama de $s$ y $t(s,s')$ en un sistema simple—agrega tu boceto aquí!]*  
