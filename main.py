import pygame

###VARIABLES GLOBALES###
#Recursos#
fondo=pygame.image.load('Imagenes/Escenario.png')
icono=pygame.image.load('Imagenes/Dino1idle.png')
#Colores#
BlueSky= (9, 187, 214)
Orange= (242,172,81)
BlueNigth= (25, 37, 56)
#Ancho y alto de Pantalla#
w=1200
h=800
#Inicializar Variables#
FPS=18
#Auxiliares#
Clock = pygame.time.Clock()
posicionXFondo=0
recorrido=0
#Función Recargar Pantalla#
def recargaPantalla():
    global posicionXFondo, recorrido
    colorFondo()
    x_relativa = posicionXFondo % fondo.get_rect().width
    Pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < w:
        recorrido +=1
        Pantalla.blit(fondo, (x_relativa, 0))
        pygame.display.flip()
    posicionXFondo-=30
#Función Color Fondo#
def colorFondo():
    global recorrido
    if recorrido <=200:
        Pantalla.fill(BlueSky)
        
    elif recorrido >200 and recorrido<290 :
        Pantalla.fill(Orange)
        
    elif recorrido >=290 and recorrido<530:
        Pantalla.fill(BlueNigth)
    elif recorrido>=530:
        recorrido=0

pygame.init() #Iniciar Pygame#

###CARACTERISTICAS DEL JUEGO###
#Musica#
pygame.mixer.music.load('Sonidos/Musica1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.1)


Pantalla = pygame.display.set_mode((w,h))
Clock = pygame.time.Clock()
pygame.display.set_icon(icono)


ejecutando = True #Bucle del juego#
while ejecutando:
    keys = pygame.key.get_pressed()
    Clock.tick(FPS) #FPS#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    recargaPantalla()
    pygame.display.flip()
