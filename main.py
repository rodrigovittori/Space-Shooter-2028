#pgzero
import random

# M6.L1: Actividad #5: "Colisiones"

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

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Listas
lista_enemigos = []

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

def comprobar_colisiones():

  # Comprobar colisiones con enemigos
  for nave_enemiga in lista_enemigos:
    if nave.colliderect(nave_enemiga):
      exit() # cerramos el juego
      # To-do: modificar por game_over

""" #####################
   # FUNCIONES PG ZERO #
  ##################### """

def draw():
  fondo.draw()
  
  for nave_enemiga in lista_enemigos:
    nave_enemiga.draw()
  
  #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")

  texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
  screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)

  nave.draw()

def on_mouse_move(pos):
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
  mov_flota_enemiga()
  comprobar_colisiones()