# Documento Introductorio sobre Sistemas Expertos

## 1. Introducción

Los **sistemas expertos** son programas de computadora diseñados para resolver problemas que normalmente requieren la pericia y experiencia de un especialista humano. Se consideran una rama importante de la Inteligencia Artificial (IA), enfocada en capturar y modelar el conocimiento de expertos para que las máquinas puedan procesarlo de manera automatizada, ofreciendo soluciones y recomendaciones de alto nivel de confiabilidad.

En este documento, se presentarán diversas formas de aproximación a la definición de sistemas expertos (colloquial, intuitiva, formal y matemática) para que puedas tener una visión completa y rigurosa de este concepto. Además, se incluirá un **ejemplo práctico** para ilustrar cómo funciona un sistema experto y cuáles son sus componentes principales.

## 2. Definición coloquial

Empecemos con una explicación sencilla y directa:

> **Un sistema experto es como un "experto virtual"** que utiliza conocimientos y reglas establecidas por personas con gran experiencia en un área (por ejemplo, medicina, finanzas o ingeniería) y las aplica para resolver problemas o responder preguntas específicas.

En la vida cotidiana, si te duele la cabeza y tienes fiebre, le preguntas al médico qué medicamento debes tomar. Un sistema experto sería un programa que, con base en la "sabiduría" y datos de muchos médicos, pudiera orientarte de forma similar, siguiendo cierto razonamiento similar al que haría un doctor.

La idea central es que el sistema "razona" siguiendo un conjunto de reglas o conocimientos previamente obtenidos de profesionales humanos. En lugar de simplemente mostrar datos, emula la forma en que un experto analiza y toma decisiones.

## 3. Definición intuitiva

Avancemos un paso más allá:

- **Un sistema experto** intenta **imitar el comportamiento** de un profesional humano.  
- Se basa en la **representación explícita** del conocimiento de ese profesional.  
- Utiliza un **motor de inferencia** que combina dichos conocimientos para alcanzar conclusiones o recomendaciones.

Imagina un gran "libro de recetas" (la *base de conocimiento*) que describe en detalle qué hacer ante cada situación. El sistema experto, valiéndose de un mecanismo de deducción (*motor de inferencia*), toma los datos de un caso particular (por ejemplo, los síntomas de un paciente) y va siguiendo la lógica del experto para llegar a un diagnóstico o recomendación (por ejemplo, "El paciente sufre migraña y debe tomar un analgésico específico").

Este proceso intuitivo se basa en la combinación de:

1. **Hechos**: información concreta y actual sobre el problema (p. ej., síntomas, parámetros de un proceso industrial, datos de un paciente).
2. **Reglas** (o conocimiento experto): pautas del tipo "si ocurre A y se cumple B, entonces hacer C", o "si la temperatura supera los 100°C y la presión se eleva, entonces abrir la válvula de seguridad".

La **intuición** detrás de un sistema experto es capturar el "razonamiento" que un ser humano haría de forma automática en su cabeza, pero expresándolo en un conjunto de reglas y hechos que la computadora puede procesar.

## 4. Definición formal

Desde un punto de vista más académico y estructurado, un sistema experto puede definirse como un:

> **Sistema de razonamiento automático basado en una base de conocimiento y un motor de inferencia, cuyo objetivo es proveer conclusiones, diagnósticos o recomendaciones de calidad experta ante problemas específicos de un dominio.**

Los elementos principales que componen un sistema experto son:

1. **Base de conocimiento (KB, Knowledge Base)**  
   - Contiene la información y experiencia de expertos, normalmente representada en forma de reglas de producción (del tipo *if-then*), ontologías, redes semánticas o marcos lógicos.  
   - Abarca tanto conocimientos declarativos (hechos, definiciones, descripciones) como procedimentales (cómo hacer algo, bajo qué condiciones aplicar ciertas reglas).

2. **Motor de inferencia (Inference Engine)**  
   - Es el mecanismo que utiliza la base de conocimiento para deducir conclusiones.  
   - Entra en juego cuando se presentan al sistema experto **hechos** o **evidencia** del problema. Mediante reglas lógicas, analiza la información y produce una recomendación o diagnóstico.  
   - Puede operar de forma hacia adelante (*forward chaining*) o hacia atrás (*backward chaining*).

3. **Base de hechos o memoria de trabajo (Working Memory)**  
   - Contiene la información actual del problema (los hechos que van surgiendo durante el razonamiento).  
   - Se actualiza conforme avanza la inferencia.

4. **Interfaz de usuario**  
   - Permite a los usuarios introducir datos o consultar los resultados de la inferencia.  
   - Puede incluir un módulo de **explicación**, que justifique o argumente cómo se llegó a cada conclusión.

### Esquema formal resumido

$Sistema Experto = \langle KB, Motor de Inferencia, Memoria de Trabajo \rangle$

donde

- $KB = \{ R_1, R_2, ..., R_n\}$ son las reglas y/o estructuras de conocimiento.
- $Motor de Inferencia$ es la función $I(\cdot)$ que, dadas las reglas y hechos actuales, produce nuevos hechos.
- $Memoria de Trabajo = \{ H_1, H_2, ..., H_m\}$ es el conjunto dinámico de hechos.

## 5. Definición matemática

Desde un punto de vista más formalizado —por ejemplo, empleando lógica proposicional o lógica de predicados—, las reglas y los hechos se pueden expresar como fórmulas lógicas. Así, la **base de conocimiento** $KB$ sería un conjunto de fórmulas o clausulas, y el **motor de inferencia** sería un *procedimiento de prueba* (puede ser un mecanismo de resolución, un encadenamiento hacia adelante o atrás, o cualquier otro método deductivo).

### Representación con lógica proposicional

- **Hechos**: fórmulas proposicionales (p. ej. $A, B, \neg C$).
- **Reglas**: implicaciones lógicas del tipo:  
  $(A \land B) \rightarrow C$  
  lo cual se lee como "si $A$ y $B$ son verdaderos, entonces $C$ es verdadero".

- **Motor de inferencia**: un mecanismo para determinar si, dada la base de conocimiento $KB$ y un nuevo conjunto de hechos $F$, se puede inferir una conclusión $G$. Formalmente:  
  $KB \cup F \models G$  
  donde $\models$ indica la relación de consecuencia lógica.

En resumen, la **definición matemática** de un sistema experto se puede concebir como un **sistema de deducción** $(KB, \vdash)$, donde $KB$ es la base de axiomas (reglas + hechos) y $\vdash$ es la relación de inferencia, de modo que si $KB \vdash X$, entonces $X$ es deducible en el sistema experto.

## 6. Ejemplo práctico: Sistema Experto para diagnóstico médico básico

A lo largo de esta sección, mostraremos un ejemplo sencillo de un **sistema experto para diagnóstico de dolores de cabeza**. Dicho sistema tendrá:

1. **Base de conocimiento**:  
   - Reglas acerca de diferentes tipos de dolor de cabeza (migraña, cefalea tensional, sinusitis).  
   - Conocimiento sobre síntomas relacionados (fiebre, congestión nasal, estrés, sensibilidad a la luz, náuseas).

2. **Hechos** (memoria de trabajo):  
   - Información suministrada por el usuario: temperatura, localización del dolor, duración, otros síntomas asociados, etc.

3. **Motor de inferencia**:  
   - Utilizará encadenamiento hacia adelante (*forward chaining*). Es decir, a partir de los hechos (síntomas) irá activando reglas hasta llegar a una conclusión sobre el posible diagnóstico.

### 6.1. Definición de reglas en la base de conocimiento

Podríamos representar las reglas de manera coloquial así:

- **R1**: Si el paciente tiene dolor de cabeza y presenta sensibilidad a la luz, entonces considerar migraña.  
  $(DolorCabeza \land SensibilidadLuz) \rightarrow PosibleMigraña$

- **R2**: Si el paciente tiene dolor de cabeza y se siente estresado, entonces considerar cefalea tensional.  
  $(DolorCabeza \land Estrés) \rightarrow PosibleCefaleaTensional$

- **R3**: Si el paciente tiene dolor de cabeza, congestión nasal y fiebre, entonces considerar sinusitis.  
  $(DolorCabeza \land CongestiónNasal \land Fiebre) \rightarrow PosibleSinusitis$

- **R4**: Si se considera migraña, preguntar por náuseas y, si las hay, reforzar diagnóstico de migraña.  
  $(PosibleMigraña \land Náuseas) \rightarrow MigrañaAltaProbabilidad$

Estas reglas se almacenan en la **base de conocimiento**.

### 6.2. Hechos iniciales

Suponiendo que un usuario responde a un cuestionario y proporciona:  
- *Dolor de cabeza*: Sí.  
- *Sensibilidad a la luz*: Sí.  
- *Fiebre*: No.  
- *Estrés*: Moderado.  
- *Congestión nasal*: No.  
- *Náuseas*: Sí.

La **memoria de trabajo** (o conjunto de hechos) se inicializa con:
$\{ DolorCabeza, SensibilidadLuz, \neg Fiebre, EstrésModerado, \neg CongestiónNasal, Náuseas \}$

### 6.3. Proceso de inferencia

1. **Motor de inferencia** revisa la regla **R1**:  
   - Se cumple $(DolorCabeza \land SensibilidadLuz)$?  
   - Sí, ambos son hechos verdaderos.  
   - Conclusión: se activa $PosibleMigraña$.  
   - Se agrega a la memoria de trabajo: $PosibleMigraña$.

2. Con **$PosibleMigraña$** en la memoria, el motor de inferencia evalúa la regla **R4**:  
   - Se cumple $PosibleMigraña \land Náuseas$?  
   - Sí, ya que $Náuseas$ es verdadero.  
   - Conclusión: $MigrañaAltaProbabilidad$.  
   - Se agrega a la memoria de trabajo.

3. El sistema puede chequear otras reglas, por ejemplo **R2** y **R3**, pero:  
   - **R2**: Requiere $DolorCabeza \land Estrés$. En este caso el estrés es moderado, podría considerarse un factor, pero no tan determinante. Habría que ver cómo se representa la intensidad de estrés. Aun así, el sistema podría sugerir considerar cefalea tensional, pero al mismo tiempo vio una fuerte coincidencia con migraña.  
   - **R3**: Requiere $Fiebre$ y $CongestiónNasal$, pero no se cumplen.

4. Finalmente, el sistema concluye "**Migraña con alta probabilidad**".

### 6.4. Salida del sistema experto

- El sistema indicará, de forma comprensible al usuario, algo como:  
  > "De acuerdo con tus síntomas, es muy probable que sufras de **migraña**. Te recomendamos consultar a un especialista para confirmar el diagnóstico y seguir el tratamiento adecuado."

## 7. Conclusiones

En resumen:

- **Coloquialmente**, un sistema experto es un *programa que actúa como un experto* y orienta en la resolución de problemas de un dominio específico.  
- **Intuitivamente**, es un *esquema de razonamiento* que imita el proceso de un profesional, utilizando **hechos** y **reglas**.  
- **Formalmente**, está compuesto por una **base de conocimiento**, un **motor de inferencia** y una **memoria de trabajo** que interactúan para obtener conclusiones expertas.  
- **Matemáticamente**, se puede describir mediante **lógica** y **mecanismos de deducción**, donde las reglas son implicaciones y el motor de inferencia es la función (o relación) que determina qué conclusiones se pueden derivar.

Los sistemas expertos se aplican en medicina, finanzas, diagnóstico de fallos en maquinaria industrial, configuración de sistemas computacionales, asesoramiento legal y muchos otros campos donde el conocimiento especializado es crucial. A medida que se refinan y complementan con otras técnicas de IA (como el aprendizaje automático y la minería de datos), los sistemas expertos siguen siendo una herramienta fundamental para capturar, representar y aprovechar la experiencia humana de forma automatizada.