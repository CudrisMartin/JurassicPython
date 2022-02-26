import pygame

#VARIABLES GLOBALES#
#Caracteristicas#
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

#Auxiliares#

#Función Recargar Pantalla#
def recargaPantalla():
    #Variables globales
    global salto, x, i, z, j, ox, gameover
    if z <=200:
        Pantalla.fill(BlueSky)
        if z==200:
            j+=1
        
    elif z>200 and z<290 :
        Pantalla.fill(Orange)
        
    elif z>=290 and z<530:
        Pantalla.fill(BlueNigth)
    elif z>=530:
        j+=1
        z=0
    

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    Pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < w:
        Pantalla.blit(fondo, (x_relativa, 0))
        pygame.display.flip()
        z += 1;

    if gameover == True:
        x+=0
            
    if j ==0 and gameover == False:
        x -= 15
    if j ==1 and gameover == False:
        x -= 20
    if j >=2 and gameover == False:
        x -= 25
    if salto == False:
        if keys[pygame.K_SPACE]:
            salto = True
    if keys[pygame.K_5] and gameover == True:
        x=0
        i= 0
        j=0
        z=0
        gameover = False


pygame.init() #Iniciar Pygame#
Pantalla = pygame.display.set_mode((w,h))

pygame.display.set_icon(icono)
ejecutando = True #Bucle del juego#
while ejecutando:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
