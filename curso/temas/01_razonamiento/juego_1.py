import random

# ===============================================================================
# LISTAS DE FIGURAS Y COLORES (sin acentos ni mayusculas)
# ===============================================================================
FIGURAS = ["circulo", "cuadrado", "triangulo", "hexagono"]
COLORES = ["rojo", "verde", "azul", "amarillo", "morado"]

# Numero minimo y maximo de observaciones que se mostraran antes de la pregunta.
MIN_OBS = 6
MAX_OBS = 10

# ===============================================================================
# FUNCIONES AUXILIARES PARA FORMATO Y VALIDACION
# ===============================================================================

def es_respuesta_valida(respuesta_str, modo="figura->color"):
    """
    Verifica que la 'respuesta_str' sea adecuada segun el modo.
    
    - Si modo = "figura->color", la respuesta debe ser un color valido (de COLORES).
      Ejemplo: 'rojo', 'verde', 'azul'...
    - Si modo = "color->figura", la respuesta debe ser una figura valida (de FIGURAS).
      Ejemplo: 'circulo', 'cuadrado'...
    """
    respuesta_str = respuesta_str.strip().lower()
    if modo == "figura->color":
        return respuesta_str in COLORES
    elif modo == "color->figura":
        return respuesta_str in FIGURAS
    else:
        return False

def solicitar_votos(modo="figura->color"):
    """
    Permite ingresar multiples respuestas y el numero de votos para cada una.
    Se finaliza con 'fin'.
    
    - modo = "figura->color" => esperamos colores como respuesta
    - modo = "color->figura" => esperamos figuras como respuesta
    
    Retorna un dict: { 'rojo': 10, 'azul': 3, ... } segun la cantidad de votos.
    """
    votos = {}
    print("\nIngresa las posibles respuestas y sus votos. Escribe 'fin' para terminar.")
    
    if modo == "figura->color":
        print("Ejemplo de respuestas validas: 'rojo', 'verde', 'azul', etc.")
    else:
        print("Ejemplo de respuestas validas: 'circulo', 'cuadrado', 'triangulo', etc.")
    
    while True:
        resp = input("Respuesta (o 'fin'): ").strip().lower()
        if resp == "fin":
            break
        
        # Validar la respuesta segun el modo
        if not es_respuesta_valida(resp, modo=modo):
            print("Respuesta invalida para este escenario. Intenta de nuevo.")
            continue
        
        while True:
            num_str = input(f"Numero de votos para '{resp}': ").strip()
            if not num_str.isdigit():
                print("Debes ingresar un entero.")
            else:
                num_votos = int(num_str)
                break
        
        if resp not in votos:
            votos[resp] = 0
        votos[resp] += num_votos
    
    return votos

def mostrar_votos(votos):
    """
    Muestra la distribucion de votos
    """
    total = sum(votos.values())
    if total == 0:
        print("No hubo votos registrados.")
        return
    
    print("Resumen de votos:")
    for resp, cant in votos.items():
        print(f"  '{resp}': {cant} voto(s)")
    print(f"Total de votos: {total}")

def comparar_con_respuesta_oficial(votos, respuesta_oficial):
    """
    Compara los votos con la respuesta_oficial, contando aciertos y porcentaje.
    respuesta_oficial es un string (p. ej. 'rojo' o 'circulo').
    """
    total = sum(votos.values())
    if total == 0:
        print("No hubo votos, no hay aciertos.")
        return
    
    aciertos = votos.get(respuesta_oficial, 0)
    porc = (aciertos / total) * 100
    print(f"La respuesta oficial del sistema es: '{respuesta_oficial}'")
    print(f"Aciertos: {aciertos} voto(s) => {porc:.1f}% de los votos")

# ===============================================================================
# FUNCIONES PARA CREAR ESCENARIOS
# Cada escenario define:
#   - observaciones: lista de (figura, color)
#   - modo: "figura->color" o "color->figura"
#   - item_conocido: la parte conocida en la pregunta (ej. 'hexagono' si modo=figura->color)
#   - respuesta_correcta: la parte faltante (ej. 'rojo')
#   - logica_interna: breve explicacion final
# ===============================================================================

def generar_escenario_deduccion():
    """
    Inspirado en una regla p->q de la forma:
      "Si figura_especial => color_especial"
    Observaciones: se cumplen esas combinaciones mayormente.
    Pregunta: "Ahora ves la figura_especial, ¿que color es?"
    
    => modo = "figura->color"
    => item_conocido = figura_especial
    => respuesta_correcta = color_especial
    """
    num_obs = random.randint(MIN_OBS, MAX_OBS)
    fig_esp = random.choice(FIGURAS)
    col_esp = random.choice(COLORES)
    
    observaciones = []
    # Generar datos
    for _ in range(num_obs):
        if random.random() < 0.5:
            # usa la regla: fig_esp => col_esp
            observaciones.append((fig_esp, col_esp))
        else:
            # combina libremente
            f = random.choice(FIGURAS)
            c = random.choice(COLORES)
            # si coincidiera la figura esp, forzamos color esp (para ser consistentemente 'deductivo')
            if f == fig_esp:
                c = col_esp
            observaciones.append((f, c))
    
    item_conocido = fig_esp  # Modo: "figura->color"
    respuesta_correcta = col_esp
    logica_interna = (
        "esta regla interna asume que siempre que aparece la figura especial, debe ser el color especial."
    )
    
    escenario = {
        "observaciones": observaciones,
        "modo": "figura->color",
        "item_conocido": item_conocido,
        "respuesta_correcta": respuesta_correcta,
        "logica_interna": logica_interna
    }
    return escenario

def generar_escenario_induccion():
    """
    Inspirado en la idea de ver repetidamente 'figura_dominante' con 'color_dominante'.
    => modo = "figura->color"
    => item_conocido = figura_dominante
    => respuesta_correcta = color_dominante
    """
    num_obs = random.randint(MIN_OBS, MAX_OBS)
    fig_dom = random.choice(FIGURAS)
    col_dom = random.choice(COLORES)
    
    observaciones = []
    for _ in range(num_obs):
        # en la mayoria de casos, fig_dom-col_dom
        if random.random() < 0.7:
            observaciones.append((fig_dom, col_dom))
        else:
            f = random.choice(FIGURAS)
            c = random.choice(COLORES)
            observaciones.append((f, c))
    
    escenario = {
        "observaciones": observaciones,
        "modo": "figura->color",
        "item_conocido": fig_dom,
        "respuesta_correcta": col_dom,
        "logica_interna": (
            "esta regla interna frecuentemente asigna la misma combinacion a la figura dominante."
        )
    }
    return escenario

def generar_escenario_abduccion():
    """
    Inspirado en: "Si color_especial => probablemente figura_asociada."
    => modo = "color->figura"
    => item_conocido = color_especial
    => respuesta_correcta = figura_asociada
    """
    num_obs = random.randint(MIN_OBS, MAX_OBS)
    col_esp = random.choice(COLORES)
    fig_asoc = random.choice(FIGURAS)
    
    observaciones = []
    for _ in range(num_obs):
        if random.random() < 0.5:
            # preferimos color_esp
            c = col_esp
            # 80% prob de que sea fig_asoc
            if random.random() < 0.8:
                f = fig_asoc
            else:
                f = random.choice([x for x in FIGURAS if x != fig_asoc])
        else:
            f = random.choice(FIGURAS)
            c = random.choice([cc for cc in COLORES if cc != col_esp])
        observaciones.append((f, c))
    
    escenario = {
        "observaciones": observaciones,
        "modo": "color->figura",
        "item_conocido": col_esp,
        "respuesta_correcta": fig_asoc,
        "logica_interna": (
            "esta regla interna sugiere que siempre que aparece un color especial, "
            "la figura mas probable es la asociada."
        )
    }
    return escenario

def generar_escenario_analogico():
    """
    Inspirado en: "Si f1-c1 y f1-c2 comparten caracteristicas, y f2-c1 tambien, 
    tal vez f2-c2 sea similar."
    
    => modo = "figura->color" o "color->figura" (podemos elegir; aqui usaremos figura->color).
    => item_conocido = f2
    => respuesta_correcta = c2
    """
    num_obs = random.randint(MIN_OBS, MAX_OBS)
    f1 = random.choice(FIGURAS)
    f2 = random.choice([x for x in FIGURAS if x != f1])
    c1 = random.choice(COLORES)
    c2 = random.choice([x for x in COLORES if x != c1])
    
    # generamos mayormente (f1, c1), (f1, c2), (f2, c1)
    observaciones = []
    for _ in range(num_obs):
        r = random.random()
        if r < 0.3:
            observaciones.append((f1, c1))
        elif r < 0.6:
            observaciones.append((f1, c2))
        else:
            observaciones.append((f2, c1))
    
    escenario = {
        "observaciones": observaciones,
        "modo": "figura->color",
        "item_conocido": f2,
        "respuesta_correcta": c2,
        "logica_interna": (
            f"esta regla interna asume una similitud: si {f1}-{c1} y {f1}-{c2} comparten propiedades, "
            f"y {f2}-{c1} es similar, entonces {f2}-{c2} completaria la analogia."
        )
    }
    return escenario

# ===============================================================================
# ARMAR TODOS LOS ESCENARIOS Y ORDENARLOS
# ===============================================================================

def generar_escenarios():
    escenarios = []
    escenarios.append(generar_escenario_deduccion())
    escenarios.append(generar_escenario_induccion())
    escenarios.append(generar_escenario_abduccion())
    escenarios.append(generar_escenario_analogico())
    
    random.shuffle(escenarios)
    return escenarios

# ===============================================================================
# FLUJO PRINCIPAL DEL JUEGO
# ===============================================================================

def juego_figuras():
    print("=== juego de figuras y colores (abstracto) ===")
    print("se mostraran varios escenarios con observaciones generadas por una regla interna.")
    print("deberas inferir la parte faltante de la nueva observacion.\n")
    
    escenarios = generar_escenarios()
    
    for idx, esc in enumerate(escenarios, start=1):
        print("\n" + "="*70)
        print(f"ESCENARIO {idx}")
        print("="*70)
        
        # Mostrar observaciones
        obs = esc["observaciones"]
        print("Observaciones anteriores:\n")
        for i, (f, c) in enumerate(obs, start=1):
            print(f" {i:2d}) {f}-{c}")
        
        # Preparar pregunta segun modo
        modo = esc["modo"]
        item_conocido = esc["item_conocido"]  # figura o color
        respuesta_oficial = esc["respuesta_correcta"]  # la parte faltante
        
        print()
        print("Pregunta:")
        if modo == "figura->color":
            # Sabemos la figura, preguntamos por el color
            print(f"ahora se ve la figura '{item_conocido}'. que color crees que es?")
            print("(ingresa tu propuesta de color y los votos)")
        else:
            # modo == "color->figura"
            # Sabemos el color, preguntamos por la figura
            print(f"ahora se detecta el color '{item_conocido}'. que figura crees que es?")
            print("(ingresa tu propuesta de figura y los votos)")
        
        # Solicitar votos
        votos = solicitar_votos(modo=modo)
        
        # Mostrar resumen
        mostrar_votos(votos)
        
        input("\npresiona enter para ver la 'respuesta oficial' y una breve explicacion...\n")
        
        # Comparar con la respuesta oficial
        resp_oficial_str = respuesta_oficial
        # si modo es figura->color => 'rojo'
        # si modo es color->figura => 'circulo', etc.
        comparar_con_respuesta_oficial(votos, resp_oficial_str)
        
        # Mostrar logica interna (breve)
        print("\nExplicacion interna (sin nombrar razonamientos explicitamente):")
        print("  " + esc["logica_interna"])
        
        input("\npresiona enter para pasar al siguiente escenario...")

    print("\n=== fin del juego ===")

# ===============================================================================
# EJECUCION
# ===============================================================================
if __name__ == "__main__":
    juego_figuras()
