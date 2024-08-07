#pgzero
import random

# M6.L2: Tarea #8: "Volver a empezar el juego (tarea extra)"
# Objetivo: Crear función que reinicie el juego

"""
Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-space-expansion
"""

""" ##################
   # VENTANA PGZERO #
  ################## """

WIDTH = 600
HEIGHT = 450

TITLE = "Guerra Galáctica"
FPS = 30

""" ***************************************************************** """

# Objetos y Variables
CANT_ENEMIGOS = 5 # Cantidad de enemigos a spawnear
CANT_METEORITOS = 5 # Cantidad de meteoritos a spawnear
modo_actual = "menu"
puntuacion = 0

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Modelos Naves

tipo1 = Actor("ship1", (100, 225))
tipo2 = Actor("ship2", (300, 225))
tipo3 = Actor("ship3", (500, 225))

# Listas
lista_enemigos = []
lista_meteoritos = []
lista_planetas = []
lista_proyectiles = []

# Creamos los lista_planetas
planeta_1 = Actor("plan1", (random.randint(0, WIDTH), random.randint(-400, -50)))
planeta_1.angle = random.randint(0,359)
lista_planetas.append(planeta_1)

planeta_2 = Actor("plan2", (random.randint(0, WIDTH), random.randint(-800, -450)))
planeta_2.angle = random.randint(0,359)
lista_planetas.append(planeta_2)

planeta_3 = Actor("plan3", (random.randint(0, WIDTH), random.randint(-1200, -850)))
planeta_3.angle = random.randint(0,359)
lista_planetas.append(planeta_3)

""" ***************************************************************** """

""" #####################
   # FUNCIONES PROPIAS #
  ##################### """

def spawn_nvo_enemigo(tipo=""):

  # Determinar tipo de enemigo a añadir:
    if tipo == "":
        tipo = "enemy"
  
    # Setear coordenadas random (importamos la librería)
    x = random.randint(50, WIDTH-50)
    y = random.randint(-200, -50)
  
    # To-do: permitir que haya más de un tipo de enemigo
  
    # Crear nvo_enemigo según el tipo:
    nvo_enemigo = Actor(tipo, (x, y))
    nvo_enemigo.velocidad = random.randint(4, 8) # o variable global
      
    """ Nota: Si yo quiero que la velocidad de los enemigos sea un factor
              de la dificultad del juego, en lugar de ser random p/cada
              nave, puedo crear una variable global llamada "velocidad_naves_enemigas"
              (o algo así) y actualizarlo cuando lo necesite
              
        # Si mis enemigos tienen cambios según su tipo:
    
        if tipo == "enemy":
          *modificamos lo que tengamos que modificar: velocidad, salud, bonus que dropea, etc*
              
    """
               
    lista_enemigos.append(nvo_enemigo)
    ##########################################

def spawn_nvo_meteorito(tipo=""):

  # Determinar tipo de meteoro a añadir:
    if tipo == "":
        tipo = "meteor"
  
    # Setear coordenadas random (importamos la librería)
    x = random.randint(50, WIDTH-50)
    y = random.randint(-200, -50)
  
    # To-do: permitir que haya más de un tipo de enemigo
  
    # Crear nvo_enemigo según el tipo:
    nvo_meteorito= Actor(tipo, (x, y))
    nvo_meteorito.angle = random.randint(0, 359)
    nvo_meteorito.velocidad = random.randint(5, 10) # o variable global
      
    """ VER NOTAS SPAWN NVO ENEMIGO """
               
    lista_meteoritos.append(nvo_meteorito)
    ##########################################

def mov_flota_enemiga():
  
  for nave_enemiga in lista_enemigos:
    if (nave_enemiga.y > (HEIGHT + nave_enemiga.height)): # Si se salió de la pantalla
            # La reciclamos:
            nave_enemiga.y = random.randint(-200, -50)
            nave_enemiga.x = random.randint(50, WIDTH - 50)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            nave_enemiga.velocidad = random.randint(4, 8) # o variable global
      
    else:
      nave_enemiga.y += nave_enemiga.velocidad

def mov_meteoritos():
  
  for meteorito in lista_meteoritos:
    if (meteorito.y > (HEIGHT + meteorito.height)): # Si se salió de la pantalla
            # Lo reciclamos:
            meteorito.y = random.randint(-200, -50)
            meteorito.x = random.randint(50, WIDTH - 50)
            meteorito.angle = random.randint(0, 359)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            meteorito.velocidad = random.randint(5, 10) # o variable global
      
    else:
      meteorito.y += meteorito.velocidad
      meteorito.angle += 1
      if (meteorito.angle > 360):
        meteorito.angle -= 360

def mov_planetas(delta_y):
  for planeta_actual in lista_planetas:
    planeta_actual.y += delta_y

    if (planeta_actual.y > (HEIGHT + planeta_actual.height)):
      planeta_actual.x = random.randint(0, WIDTH)
      planeta_actual.y = random.randint(-1200, -850)
      planeta_actual.angle = random.randint(0,359)

def mov_proyectiles():
    for p in lista_proyectiles:
        if (p.y < -20): # Si se salió de la pantalla
            lista_proyectiles.remove(p)
        else:
            # Nota: si cambiamos la velocidad de los proyectiles según power-ups, modificar:
            p.y -= 10 # velocidad de proyectiles

def comprobar_colisiones():
    
  global modo_actual, puntuacion
    
  # Comprobar colisiones con enemigos
  for nave_enemiga in lista_enemigos:
    if nave.colliderect(nave_enemiga):
      modo_actual = "game_over" # Terminamos el juego

    for p in lista_proyectiles:
            if p.colliderect(nave_enemiga):
                puntuacion += 100
                # To-do: agregar explosión
                lista_enemigos.remove(nave_enemiga)
                lista_proyectiles.remove(p)
                spawn_nvo_enemigo()

  for meteorito in lista_meteoritos:
    if nave.colliderect(meteorito):
      modo_actual = "game_over" # Terminamos el juego

    for p in lista_proyectiles:
            if p.colliderect(meteorito):
                puntuacion += 20
                # To-do: agregar explosión
                lista_meteoritos.remove(meteorito)
                lista_proyectiles.remove(p)
                spawn_nvo_meteorito()
                
################################

""" #####################
   # FUNCIONES PG ZERO #
  ##################### """

def on_mouse_down(button, pos):
    global modo_actual
    
    if ((modo_actual == "menu") and (tipo1.collidepoint(pos))):
        nave.image = "ship1"
        modo_actual = "juego"
        
    elif ((modo_actual == "menu") and (tipo2.collidepoint(pos))):
        nave.image = "ship2"
        modo_actual = "juego"
    
    elif ((modo_actual == "menu") and (tipo3.collidepoint(pos))):
        nave.image = "ship3"
        modo_actual = "juego"
        
    #############################

    if (modo_actual == "juego") and (button == mouse.LEFT):
        nvo_proyectil = Actor("missiles", nave.pos)
        # NOTA: si quiero tener distintos tipos de proyectiles con distintas velocidades debería agregar un atributo al Actor
        lista_proyectiles.append(nvo_proyectil)

def draw():

  if (modo_actual == "juego"):
    fondo.draw()

    for planeta in lista_planetas:
      planeta.draw()
    
    for nave_enemiga in lista_enemigos:
      nave_enemiga.draw()

    for meteorito in lista_meteoritos:
      meteorito.draw()

    for proyectil in lista_proyectiles:
        proyectil.draw()
    
    #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")
  
    #texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
    #screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)

    screen.draw.text(str(puntuacion), midleft=(20, 20), color = "white", fontsize = 24)
      
    nave.draw()

  elif (modo_actual == "menu"):
      fondo.draw()

      screen.draw.text("ELIGE TU NAVE", center=(int(WIDTH/2), int(HEIGHT/4)), color = "white", background="black", fontsize = 36)

      tipo1.draw()
      tipo2.draw()
      tipo3.draw()
  
  elif (modo_actual == "game_over"):

    fondo.draw()

    screen.draw.text("¡TE ESTRELLASTE!", center=(int(WIDTH/2), int(HEIGHT/3)), color = "red", background = "black", fontsize = 48)
    screen.draw.text(("Puntaje final : " + str(puntuacion)), center = (300,300), color="yellow", fontsize = 24)
    screen.draw.text("Pulsa [Enter] para reiniciar", center = (300, 400), color = "white", fontsize = 24)
    #        -> To-Do: agregar función reset_game()
    
def on_mouse_move(pos):
  if (modo_actual == "juego"):
    nave.pos = pos

#####################
# INICIALIZAR JUEGO #
#####################

def reiniciar_juego():
    global modo_actual, puntuacion

    nave.image = "ship"  # resetear modelo nave
    puntuacion = 0       # resetear puntuacion
    modo_actual = "menu" # cambiar modo a menú

    # Vaciar listas:
    del lista_enemigos[:]
    del lista_meteoritos[:]  
    del lista_proyectiles[:]

    # resetear posición planetas
    for planeta_actual in range(len(lista_planetas)):
        lista_planetas[planeta_actual].pos = (random.randint(0, WIDTH), random.randint( (-400 * (1 + planeta_actual)), (-50 - (-400 * planeta_actual))))
        lista_planetas[planeta_actual].angle = random.randint(0,359)

    # Spawnear enemigos    
    for e in range(CANT_ENEMIGOS):
        # Nota: en caso de agregar más tipos de enemigos, modificar el spawn para que sea random
        spawn_nvo_enemigo()
    
    for m in range(CANT_METEORITOS):
        spawn_nvo_meteorito()
########################################

reiniciar_juego() # inicializamos el juego

##################
# BUCLE DE JUEGO #
##################

def update(dt):
  global modo_actual
  
  if (modo_actual == "juego"):
    mov_planetas(1) # Check: si modifico el juego asegurarme de actualizar el delta_y
    mov_meteoritos()
    mov_flota_enemiga()
    mov_proyectiles()
    comprobar_colisiones()
  
  elif modo_actual == "game_over":
    if keyboard.enter:
      reiniciar_juego()
      # To-Do: agregar función reset_game()
#################################