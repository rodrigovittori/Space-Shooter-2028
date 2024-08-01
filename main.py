#pgzero
import random

# M6.L1: Actividad #8: "Planetas (Asignación extra)"

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
modo_actual = "juego"

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Listas
lista_enemigos = []
planetas = []

# Creamos los planetas
planeta_1 = Actor("plan1", (random.randint(0, WIDTH), random.randint(-400, -50)))
planeta_1.angle = random.randint(0,359)
planetas.append(planeta_1)

planeta_2 = Actor("plan2", (random.randint(0, WIDTH), random.randint(-800, -450)))
planeta_2.angle = random.randint(0,359)
planetas.append(planeta_2)

planeta_3 = Actor("plan3", (random.randint(0, WIDTH), random.randint(-1200, -850)))
planeta_3.angle = random.randint(0,359)
planetas.append(planeta_3)

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

def mov_flota_enemiga():
  
  for nave_enemiga in lista_enemigos:
    if (nave_enemiga.y > (HEIGHT + 50)): # Si se salió de la pantalla
            # La reciclamos:
            nave_enemiga.y = random.randint(-200, -50)
            nave_enemiga.x = random.randint(50, WIDTH - 50)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            nave_enemiga.velocidad = random.randint(4, 8) # o variable global
      
    else:
      nave_enemiga.y += nave_enemiga.velocidad

def mov_planetas(delta_y):
  for planeta_actual in planetas:
    planeta_actual.y += delta_y

    if (planeta_actual.y > (HEIGHT + planeta_actual.height)):
      planeta_actual.x = random.randint(0, WIDTH)
      planeta_actual.y = random.randint(-1200, -850)
      planeta_actual.angle = random.randint(0,359)

def comprobar_colisiones():
  global modo_actual
  # Comprobar colisiones con enemigos
  for nave_enemiga in lista_enemigos:
    if nave.colliderect(nave_enemiga):
      modo_actual = "game_over" # Terminamos el juego

""" #####################
   # FUNCIONES PG ZERO #
  ##################### """

def draw():

  if (modo_actual == "juego"):
    fondo.draw()

    for planeta in planetas:
      planeta.draw()
    
    for nave_enemiga in lista_enemigos:
      nave_enemiga.draw()
    
    #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")
  
    texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
    screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)
  
    nave.draw()

  elif (modo_actual == "game_over"):

    fondo.draw()

    screen.draw.text("¡TE ESTRELLASTE!", center=(int(WIDTH/2), int(HEIGHT/2)), color = "red", background = "black", fontsize = 48)

    # To-do: agregar mostrar puntuación final
    # To-do: Mostrar cartel presione enter para reiniciar
    #        -> To-Do: agregar función reset_game()
    
def on_mouse_move(pos):
  if (modo_actual == "juego"):
    nave.pos = pos

#####################
# INICIALIZAR JUEGO #
#####################

# To-do: convertir a FN p/ iniciar/reiniciar el juego
for e in range(CANT_ENEMIGOS):
  spawn_nvo_enemigo()

##################
# BUCLE DE JUEGO #
##################

def update(dt):
  global modo_actual
  
  if (modo_actual == "juego"):
    mov_planetas(1) # Check: si modifico el juego asegurarme de actualizar el delta_y
    mov_flota_enemiga()
    comprobar_colisiones()
  
  elif modo_actual == "game_over":
    if keyboard.enter:
      modo_actual = "juego"
      # To-Do: agregar función reset_game()