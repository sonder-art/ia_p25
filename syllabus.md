<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Sílabo del Curso: **Inteligencia Artificial** 
*(32 Clases, 2 horas cada una, con 10 minutos de descanso. Las presentaciones finales se realizarán en otra fecha.)*

---

## ÍNDICE DE CONTENIDOS

1. [Objetivos Principales](#objetivos-principales)  
2. [Estructura del Curso](#estructura-del-curso)  
3. [Semana 1: Introducción Histórica y GOFAI (Clases 1-2)](#semana-1-introducción-histórica-y-gofai-clases-1-2)  
4. [Semana 2: Búsqueda No Informada e Informada (Clases 3-4)](#semana-2-búsqueda-no-informada-e-informada-clases-3-4)  
5. [Semana 3: Representación del Conocimiento y Razonamiento (Clases 5-6)](#semana-3-representación-del-conocimiento-y-razonamiento-clases-5-6)  
6. [Semana 4: Teoría de Juegos I - Fundamentos y Mecanismos (Clases 7-8)](#semana-4-teoría-de-juegos-i---fundamentos-y-mecanismos-clases-7-8)  
7. [Semana 5: Teoría de Juegos II - Juegos Repetidos y Torneos de Axelrod (Clases 9-10)](#semana-5-teoría-de-juegos-ii---juegos-repetidos-y-torneos-de-axelrod-clases-9-10)  
8. [Semana 6: Búsqueda Adversaria: Minimax y Alpha-Beta (Clases 11-12)](#semana-6-búsqueda-adversaria-minimax-y-alpha-beta-clases-11-12)  
9. [Semana 7: Autómatas Finitos y Celulares (Clases 13-14)](#semana-7-autómatas-finitos-y-celulares-clases-13-14)  
10. [Semana 8: Modelado Basado en Agentes (ABM) (Clases 15-16)](#semana-8-modelado-basado-en-agentes-abm-clases-15-16)  
11. [Semana 9: Algoritmos Genéticos: Fundamentos (Clases 17-18)](#semana-9-algoritmos-genéticos-fundamentos-clases-17-18)  
12. [Semana 10: Algoritmos Genéticos y Aplicaciones (Clases 19-20)](#semana-10-algoritmos-genéticos-y-aplicaciones-clases-19-20)  
13. [Semana 11: Aprendizaje por Refuerzo: Fundamentos (Clases 21-22)](#semana-11-aprendizaje-por-refuerzo-fundamentos-clases-21-22)  
14. [Semana 12: Aprendizaje por Refuerzo Avanzado (Clases 23-24)](#semana-12-aprendizaje-por-refuerzo-avanzado-clases-23-24)  
15. [Semana 13: Integración de Técnicas Clásicas (Clases 25-26)](#semana-13-integración-de-técnicas-clásicas-clases-25-26)  
16. [Semana 14: Torneos de Axelrod y Co-Evolución (Clases 27-28)](#semana-14-torneos-de-axelrod-y-co-evolución-clases-27-28)  
17. [Semana 15: Autómatas Celulares Avanzados y ABM (Clases 29-30)](#semana-15-autómatas-celulares-avanzados-y-abm-clases-29-30)  
18. [Semana 16: Revisión y Cierre (Clases 31-32)](#semana-16-revisión-y-cierre-clases-31-32)  
19. [Entornos y Mecanismos Clave](#entornos-y-mecanismos-clave)  
20. [Método de Evaluación (Orientativo)](#método-de-evaluación-orientativo)  
21. [Conclusión](#conclusión)  

---

## OBJETIVOS PRINCIPALES

1. **Comprender** la evolución histórica de la IA y los fundamentos de la IA clásica (GOFAI).  
2. **Implementar** y comparar algoritmos de búsqueda (BFS, DFS, A*, etc.) en entornos de prueba.  
3. **Diseñar** sistemas de razonamiento simbólico y basados en reglas.  
4. **Dominar** los conceptos centrales de la **Teoría de Juegos**, con énfasis en **mecanismos de diseño**, juegos repetidos y torneos estilo Robert Axelrod.  
5. **Implementar** búsqueda adversaria (Minimax, Alpha-Beta) en juegos de tablero.  
6. **Explorar** autómatas finitos y **autómatas celulares** (ej. Conway’s Game of Life) para entender comportamiento emergente.  
7. **Aplicar** algoritmos evolutivos (genéticos) en problemas de optimización y experimentación.  
8. **Introducir** conceptos de aprendizaje por refuerzo y desarrollar agentes Q-learning.  
9. **Utilizar** entornos compartidos para experimentar, comparar y competir con diferentes estrategias de IA.

---

## ESTRUCTURA DEL CURSO
- **32 clases** en **16 semanas** (2 clases por semana, 2 horas cada clase).  
- Cada semana se enfoca en un **tema** central (teoría + práctica).  
- Se crean o utilizan **entornos** para probar y comparar algoritmos.  
- Las **presentaciones finales** se realizarán fuera de este calendario.

---

## SEMANA 1: INTRODUCCIÓN HISTÓRICA Y GOFAI (CLASES 1-2)

### Clase 1
- **Tema Principal:** Historia de la IA y Fundamentos de GOFAI  
- **Contenido:**
  - Orígenes de la IA, “inviernos” de la IA, reaparición del aprendizaje automático  
  - Visión general del curso y sus proyectos  
- **Actividades:**
  - Debate: “¿Qué es inteligencia en máquinas?”  
  - Descripción de los principales **entornos** y proyectos

### Clase 2
- **Tema Principal:** Razonamiento Simbólico y Reglas  
- **Contenido:**
  - GOFAI: sistemas basados en reglas, representación del conocimiento (nociones básicas)  
- **Actividades:**
  - Demostración de un **chatbot** o **solucionador de acertijos** con reglas if-then  
  - **Proyecto 1**: Iniciar un agente de reglas sencillo (mini-sistema experto o puzzle)

---

## SEMANA 2: BÚSQUEDA NO INFORMADA E INFORMADA (CLASES 3-4)

### Clase 3
- **Tema Principal:** Búsqueda No Informada (BFS, DFS, Coste Uniforme)  
- **Contenido:**
  - Representación de grafos, espacios de estados  
  - Implementaciones de BFS/DFS en problemas simples  
- **Actividades:**
  - **Entorno Laberinto** o **8-Puzzle**: comparar BFS y DFS  
  - Iniciar **Proyecto 2** (resolver el problema con búsqueda no informada)

### Clase 4
- **Tema Principal:** Búsqueda Informada (A*, Greedy Best-First)  
- **Contenido:**
  - Diseño de heurísticas, comparación A* vs BFS/DFS  
- **Actividades:**
  - Implementar A* y medir rendimiento  
  - Finalizar **Proyecto 2** con pruebas de heurísticas

---

## SEMANA 3: REPRESENTACIÓN DEL CONOCIMIENTO Y RAZONAMIENTO (CLASES 5-6)

### Clase 5
- **Tema Principal:** Redes Semánticas, Ontologías y Sistemas Expertos  
- **Contenido:**
  - Ontologías (RDF, frames) y razonamiento simbólico  
  - Diferencias entre búsqueda y razonamiento basado en conocimiento  
- **Actividades:**
  - Demostración de ontologías simples (familia, medicina básica, etc.)  
  - **Proyecto 3**: Iniciar sistema experto (motor de reglas + base de conocimiento)

### Clase 6
- **Tema Principal:** Inferencia y Limitaciones de GOFAI  
- **Contenido:**
  - Encadenamiento hacia adelante y atrás  
  - Ventajas y desventajas de la IA simbólica  
- **Actividades:**
  - Programar reglas de inferencia en Python  
  - Validar **Proyecto 3** en distintos escenarios

---

## SEMANA 4: TEORÍA DE JUEGOS I - FUNDAMENTOS Y MECANISMOS (CLASES 7-8)

### Clase 7
- **Tema Principal:** Conceptos Básicos de Teoría de Juegos  
- **Contenido:**
  - Payoff matrices, juegos de suma cero y no cero  
  - Equilibrio de Nash, ejemplos clásicos (Dilema del Prisionero, etc.)  
- **Actividades:**
  - Simulador básico de un juego (Dilema del Prisionero de 1 ronda)  
  - Discusión sobre estrategias dominantes y equilibrios

### Clase 8
- **Tema Principal:** Diseño de Mecanismos y Tipos de Juegos  
- **Contenido:**
  - Cómo diseñar payoff matrices o recompensas para influir en la conducta  
  - Juegos con información completa/incompleta, subastas, negociación  
- **Actividades:**
  - Análisis de distintos mecanismos (subasta sellada, Vickrey, etc.)  
  - Preparar el terreno para juegos repetidos y estrategias evolutivas

---

## SEMANA 5: TEORÍA DE JUEGOS II - JUEGOS REPETIDOS Y TORNEOS DE AXELROD (CLASES 9-10)

### Clase 9
- **Tema Principal:** Juegos Repetidos y Estrategias Clásicas  
- **Contenido:**
  - Iterated Prisoner’s Dilemma (IPD), tit-for-tat, grim trigger  
  - Concepto de recíproca, estabilidad y cooperación  
- **Actividades:**
  - **Proyecto 4**: Diseñar estrategias de IPD  
  - Ajustes de payoff y análisis de convergencia al cooperar o traicionar

### Clase 10
- **Tema Principal:** Torneos de Axelrod y Mecanismos Evolutivos  
- **Contenido:**
  - Robert Axelrod, estudio empírico de estrategias, ruido en iteraciones  
  - Co-evolución de estrategias en un ambiente repetido  
- **Actividades:**
  - **Torneo de Axelrod** (round-robin) con registro de puntuaciones  
  - Observación de estrategias ganadoras, “eye for eye” vs. “always defect”, etc.

---

## SEMANA 6: BÚSQUEDA ADVERSARIA: MINIMAX Y ALPHA-BETA (CLASES 11-12)

### Clase 11
- **Tema Principal:** Minimax en Juegos Adversarios  
- **Contenido:**
  - Árboles de juego, evaluación de posiciones, podas iniciales  
  - Aplicación en juegos como Tres en Raya (Tic-Tac-Toe)  
- **Actividades:**
  - **Proyecto 5**: Crear agente adversario para un juego de tablero (Tic-Tac-Toe, Conecta 4)  
  - Programar versión básica de Minimax

### Clase 12
- **Tema Principal:** Alpha-Beta y Heurísticas de Evaluación  
- **Contenido:**
  - Poda Alpha-Beta para mejorar la eficiencia  
  - Profundidad limitada y evaluación heurística  
- **Actividades:**
  - Integrar Alpha-Beta en el mismo juego  
  - Competir agentes con limitación de tiempo o profundidad

---

## SEMANA 7: AUTÓMATAS FINITOS Y CELULARES (CLASES 13-14)

### Clase 13
- **Tema Principal:** Teoría de Autómatas Finitos (AFD/AFN)  
- **Contenido:**
  - Máquinas de estados y su uso en IA  
  - Ejemplos: reconocimiento de patrones, máquinas expendedoras  
- **Actividades:**
  - **Proyecto 6**: Implementar un autómata finito y probar entradas/estados  
  - Visualización de transiciones

### Clase 14
- **Tema Principal:** Autómatas Celulares y Conway’s Game of Life  
- **Contenido:**
  - Reglas de nacimiento y muerte, comportamiento emergente  
  - Variantes (Highlife, Seeds) y aplicaciones de AC  
- **Actividades:**
  - Programar **Game of Life**  
  - Observar ciclos, estabilidad y patrones (planeadores, etc.)

---

## SEMANA 8: MODELADO BASADO EN AGENTES (ABM) (CLASES 15-16)

### Clase 15
- **Tema Principal:** Introducción a ABM y Sistemas Complejos  
- **Contenido:**
  - Depredador-presa, Boids (flocking)  
  - Librerías como Mesa (Python)  
- **Actividades:**
  - Plantear **Proyecto 7**: un ABM sencillo (recursos, interacción entre agentes)

### Clase 16
- **Tema Principal:** Implementación y Análisis de ABM  
- **Contenido:**
  - Parámetros de comportamiento, reglas locales y efectos globales  
  - Visualización y medición de resultados (densidad, poblaciones, etc.)  
- **Actividades:**
  - Programar el ABM y experimentar con valores  
  - Discutir posibles extensiones (cooperación vs. competencia)

---

## SEMANA 9: ALGORITMOS GENÉTICOS: FUNDAMENTOS (CLASES 17-18)

### Clase 17
- **Tema Principal:** Conceptos Básicos de Algoritmos Genéticos (AG)  
- **Contenido:**
  - Población, selección, cruce, mutación  
  - Función de aptitud y codificación  
- **Actividades:**
  - Ejemplo simple (maximizar f(x))  
  - **Proyecto 8**: GA para TSP, Knapsack u otro problema de optimización

### Clase 18
- **Tema Principal:** Ajuste de Parámetros y Convergencia  
- **Contenido:**
  - Tasas de mutación, tipos de selección (ruleta, torneo)  
  - Visualización de convergencia de generaciones  
- **Actividades:**
  - Competencia: ¿Quién logra la mejor aptitud tras X generaciones?  
  - Documentar conclusiones de rendimiento

---

## SEMANA 10: ALGORITMOS GENÉTICOS Y APLICACIONES (CLASES 19-20)

### Clase 19
- **Tema Principal:** Aplicaciones Avanzadas de AG y Co-Evolución  
- **Contenido:**
  - Estrategias evolutivas, programación genética (GP)  
  - Co-evolución en entornos multi-agente  
- **Actividades:**
  - Refinar la implementación del GA  
  - Comparar modos de selección y su impacto en la velocidad de convergencia

### Clase 20
- **Tema Principal:** Integración de AG con Otros Métodos  
- **Contenido:**
  - GA para generar heurísticas en búsqueda adversaria  
  - Evolución de estrategias en IPD (combinación con teoría de juegos)  
- **Actividades:**
  - Probar variantes de GA en distintos entornos  
  - Discutir hallazgos y posibilidades futuras

---

## SEMANA 11: APRENDIZAJE POR REFUERZO: FUNDAMENTOS (CLASES 21-22)

### Clase 21
- **Tema Principal:** Fundamentos de Aprendizaje por Refuerzo (RL)  
- **Contenido:**
  - Agente, entorno, recompensas, estados y acciones  
  - Diferencias con búsqueda clásica y algoritmos evolutivos  
- **Actividades:**
  - **Proyecto 9**: Q-Learning en un Gridworld o Maze sencillo  
  - Configurar funciones de recompensa y castigo

### Clase 22
- **Tema Principal:** Q-Learning, $\epsilon$-Greedy y Parametrización  
- **Contenido:**
  - Tasa de aprendizaje ($\alpha$), factor de descuento ($\gamma$), exploración ($\epsilon$)  
  - Visualización de la Q-Table  
- **Actividades:**
  - Ajustar hiperparámetros y comparar convergencia  
  - Evaluar desempeño del agente en varios escenarios

---

## SEMANA 12: APRENDIZAJE POR REFUERZO AVANZADO (CLASES 23-24)

### Clase 23
- **Tema Principal:** Ajustes Avanzados y Shaping de Recompensas  
- **Contenido:**
  - Decaimiento de $\epsilon$, shaping de recompensas, atascos  
  - Problemas de convergencia  
- **Actividades:**
  - Mejorar el agente Q-Learning con técnicas de shaping  
  - Comparar resultados de velocidad/calidad de la política aprendida

### Clase 24
- **Tema Principal:** Extensión a Entornos Complejos o Multi-Agente  
- **Contenido:**
  - Visión general de SARSA, DQN (opcional)  
  - RL en sistemas cambiantes o multi-agente  
- **Actividades:**
  - Debate: escenarios multi-agente con RL  
  - Ejercicios de diseño de recompensas en sistemas complejos

---

## SEMANA 13: INTEGRACIÓN DE TÉCNICAS CLÁSICAS (CLASES 25-26)

### Clase 25
- **Tema Principal:** Retrospectiva y Combinación de Métodos  
- **Contenido:**
  - Ejemplos de IA híbrida: reglas + búsqueda + RL + GA  
  - Casos reales donde conviven enfoques clásicos  
- **Actividades:**
  - Revisión de proyectos pasados  
  - Brainstorm de un proyecto integrador con varios métodos

### Clase 26
- **Tema Principal:** Diseño de Mecanismos en Profundidad  
- **Contenido:**
  - Subastas, negociación, reglas avanzadas de juego  
  - Énfasis en la ética y la equidad en el diseño  
- **Actividades:**
  - Taller: crear un mini-entorno de subasta o negociación  
  - Discusión de cómo afectan las reglas a los agentes

---

## SEMANA 14: TORNEOS DE AXELROD Y CO-EVOLUCIÓN (CLASES 27-28)

### Clase 27
- **Tema Principal:** Ampliación de los Torneos de Axelrod  
- **Contenido:**
  - IPD con variaciones (ruido, mutaciones de estrategia)  
  - Observación de cooperación emergente y estabilidad  
- **Actividades:**
  - Programar un entorno que permita “evolucionar” estrategias a lo largo de rondas  
  - Medir y graficar evolución de la población

### Clase 28
- **Tema Principal:** Análisis de Resultados y Comparaciones  
- **Contenido:**
  - Relación con sistemas evolutivos y aprendizaje por refuerzo  
  - Estrategias estables y dinámicas de traición/cooperación  
- **Actividades:**
  - Ajustar reglas (payoff, ruido) y observar cambios  
  - Discusión sobre implicaciones en teoría de juegos e IA

---

## SEMANA 15: AUTÓMATAS CELULARES AVANZADOS Y ABM (CLASES 29-30)

### Clase 29
- **Tema Principal:** Variantes del Game of Life y Sistemas Complejos  
- **Contenido:**
  - Alteraciones de reglas (nacimiento/muerte), bordes toroidales, etc.  
  - Aplicaciones en biología, sociología, urbanismo  
- **Actividades:**
  - Probar cambios de reglas en Game of Life  
  - Analizar patrones y comportamiento emergente

### Clase 30
- **Tema Principal:** ABM + RL o ABM + AG  
- **Contenido:**
  - Hibridar ABM con aprendizaje o evolución  
  - Retos en simulaciones de muchos agentes  
- **Actividades:**
  - Experimentar con un ABM donde los agentes aprendan o muten  
  - Discusión sobre complejidad y escalabilidad

---

## SEMANA 16: REVISIÓN Y CIERRE (CLASES 31-32)

### Clase 31
- **Tema Principal:** Exploración de Temas Opcionales y Ajustes Finales  
- **Contenido:**
  - Discusión de subtemas (subastas multi-agente, teoría de contratos, etc.)  
  - No hay presentaciones formales (se programan aparte)  
- **Actividades:**
  - Demostraciones informales o pruebas extremas en entornos  
  - Debate: IA clásica vs. IA moderna

### Clase 32
- **Tema Principal:** Reflexiones Finales y Perspectivas Futuras  
- **Contenido:**
  - Resumen de aprendizajes clave y conexiones con Deep Learning o Robótica  
  - Conclusiones sobre Teoría de Juegos, Búsqueda, RL, etc.  
- **Actividades:**
  - Retroalimentación entre estudiantes e instructor  
  - **Cierre del curso** (sin presentaciones formales; examen/proyecto final en otra fecha)

---

## ENTORNOS Y MECANISMOS CLAVE

1. **Proyecto 1 (Reglas/GOFAI)**: Agente simbólico (chatbot/puzzle).  
2. **Proyecto 2 (Búsqueda)**: Laberinto o 8-puzzle con BFS/DFS/A*.  
3. **Proyecto 3 (Sist. Experto)**: Base de conocimiento + motor de inferencia.  
4. **Proyecto 4 (Teoría de Juegos / IPD)**: Torneos repetidos al estilo Axelrod, analizando payoff y cooperación.  
5. **Proyecto 5 (Búsqueda Adversaria)**: Juegos de tablero (Tic-Tac-Toe, Conecta 4) con Minimax/Alpha-Beta.  
6. **Proyecto 6 (Autómatas)**: FSM simple + Conway’s Game of Life.  
7. **Proyecto 7 (ABM)**: Depredador-presa, boids u otro modelo de agentes.  
8. **Proyecto 8 (AG)**: TSP, Knapsack o problemas de optimización; co-evolución de estrategias.  
9. **Proyecto 9 (RL)**: Gridworld/Maze con Q-Learning (y variantes).  

El **diseño de mecanismos** aparece en teoría de juegos (estructurar payoff matrices, subastas), en RL (recompensas) y en GA (función de aptitud). Así, se investiga cómo los cambios en las reglas impactan la conducta emergente de los agentes.

---

## MÉTODO DE EVALUACIÓN (ORIENTATIVO)

- **Proyectos y Tareas Prácticas** (implementación y documentación).  
- **Exámenes Teóricos Parciles** . (Por definir de 3 a 5)  
- **Proyecto Final / Presentaciones** (fuera de las 32 clases, de carácter integrador o de investigación adicional).  


---

## CONCLUSIÓN

Este programa abarca **IA Clásica** con un enfoque especial en la **Teoría de Juegos**, expandiendo los conceptos de **juegos repetidos**, **mecanismos de diseño** y **torneos de Axelrod**, además de cubrir la búsqueda, los sistemas expertos, la búsqueda adversaria, autómatas, algoritmos genéticos y aprendizaje por refuerzo. A lo largo de 32 clases, los estudiantes tienen oportunidades de:

- **Experimentar** con distintos métodos en **entornos específicos**.  
- **Comparar** resultados y reflexionar sobre la influencia de la estructura de recompensas y la dinámica de interacción.  
- **Obtener** una base sólida de IA Clásica para luego profundizar en técnicas más modernas de Machine Learning o Deep Learning.

Las **presentaciones finales** y el **examen** se llevarán a cabo fuera de este cronograma, permitiendo que cada participante muestre su proyecto integrador o realice investigaciones complementarias. 


