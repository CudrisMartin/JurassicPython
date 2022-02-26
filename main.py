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

pygame.init() #Iniciar Pygame#
Pantalla = pygame.display.set_mode((w,h))

pygame.display.set_icon(icono)
ejecutando = True #Bucle del juego#
while ejecutando:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
