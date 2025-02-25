# Ejercicios
En un jupyter notebook (puede ser colab) crea codigo para lo siguiente (ayudate de chatbots/llms):
## Definicion del Juego
0. Piensa lo que vas a hacer con hoja y papel para poder pasarselo al LLM de lo contrario no aprenderas las skills correctas de disenno conceptual, perderas el refuerzo de entendimiento de la clase y gastaras mas prompts.
0.1 Instala `pydantic >= 2.0` (segunda version o mas), puedes usar pip install o  el requirements.
1. Una estructura de datos en pydantic flexible que les permita definir de manera formal un juego (jugadores, matrices de pago, politicas, etc). La estructura de datos debe llamarse `EstructuraDeJuego`. Debe ser capaz de aceptar un numero arbitrario de estrategias por jugador y de pagos, ademas debe de validar que tu definicion de juego sea valido (osea no hay errores al instanciar un objeto que usa esa clase)
1.1 Incluye una estructura, campo o sub estructura de Pydantic para los `Pagos` y las `Estrategias`
2. Una funcion que dada la `EstructuraDeJuego` y las estrategias elegidas para cada jugador regrese el pago/utilidad. Se llama `def pagos_estrategia(juego:EstructuraDeJuego, estrategia) -> Pagos`
3. Un algoritmo que dado la `EstructuraDeJuego` encuentre todos los equilibros de nash (si existen), incluye pagos y estrategias como output. `def equilibrio_nash(juego:EstructuraDeJuego) -> (Estrategias,Pagos)`
## Juegos
Usando los juegos de `curso/temas/05_teoria_de_juegos/02_ejemplos_de_juegos.md` como inspiracion crea 3 juegos y analizalos. Cada juego puede ser completamente diferente, o puede ser re-interpretaciones del mismo con variaciones.
0. Piensa y disenna en papel los escenarios que quieres modelar
1. Incluye una descripcion de cada escenario que estas modelando, incluyendo la historia (storytelling), los pagos y las estrategias. definelo de manera formal y detallada para que se entienda el problema.
2. Pasa el problema a la estrucura de `EstructuraDeJuego`
3. Encuentra (o encuentra que no hay) equilibros de nash usando tus funciones anteriores, y da interpretaciones a cada uno de los equilibrios. Cual podria ser mas deseable o menos deseable y por que.

## Entregable
Entrega el jupyter notebook (o colab) que funcione.