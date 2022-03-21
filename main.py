import pygame
from jugador import Jugador
from jugador import Saltar
from jugador import volver
from jugador import caer
from enemigos import Piedra
from enemigos import obtener
from enemigos import reinicio

###VARIABLES GLOBALES###
#Recursos#
fondo=pygame.image.load('Imagenes/Escenario.png')
icono=pygame.image.load('Imagenes/Dino1idle.png')
#Colores#
BlueSky= (44, 128, 201)
Orange= (255, 170, 79)
BlueNigth= (29, 56, 145)
Blanco = (255,255,255)
Negro= (0,0,0)
#Fuentes#
consolas= 'PressStart2P-Regular.ttf'
#Ancho y alto de Pantalla#
w=900
h=600
#Inicializar Variables#
FPS=18
#Auxiliares#
Clock = pygame.time.Clock()
posicionXFondo=0
recorrido=0
#Estados#
puntaje=0
corriendo=True
gameover=False
play = False
contador=0
x=0
y=0
maxi=0
cambio = 18
#Función Recargar Pantalla#
def recargaPantalla():
    global posicionXFondo, recorrido, cambio, play, gameover,x, y, puntaje, maxi
    colorFondo()
    if play== True and gameover==False:
        puntaje +=1
        if puntaje> maxi:
            maxi=puntaje
    
    x_relativa = posicionXFondo % fondo.get_rect().width
    
    Pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    enemigos.draw(Pantalla)
    sprites.draw(Pantalla)
    MostrarTexto(Pantalla, consolas, str(puntaje).zfill(7), Negro, 20, 803 , 40)
    MostrarTexto(Pantalla, consolas, str(puntaje).zfill(7), Blanco, 20, 800 , 40)
    MostrarTexto(Pantalla, consolas, "Max:" +str(maxi).zfill(7), Negro, 18, 113 , 40)
    MostrarTexto(Pantalla, consolas, "Max:" +str(maxi).zfill(7), Blanco, 18, 110 , 40)
    
    
    if x_relativa < w:
        recorrido +=1
        
        Pantalla.blit(fondo, (x_relativa, 0))
        if play== False:
            MostrarTexto(Pantalla, consolas, "Espacio=Iniciar", Negro, 30, 445 ,123)
            MostrarTexto(Pantalla, consolas, "Esc=Salir", Negro, 30, 445 , 53)
            MostrarTexto(Pantalla, consolas, "Abajo=Agacharse", Negro, 30, 445 , 283)
            MostrarTexto(Pantalla, consolas, "Espacio=Iniciar", Blanco, 30, 450 ,120)
            MostrarTexto(Pantalla, consolas, "Esc=Salir", Blanco, 30, 450 , 50)
            MostrarTexto(Pantalla, consolas, "Abajo=Agacharse", Blanco, 30, 450 , 280)
            MostrarTexto(Pantalla, consolas, "r=Volver a empezar", Negro, 30, 445 , 203)
            MostrarTexto(Pantalla, consolas, "r=Volver a empezar", Blanco, 30, 450 , 200)
            
        enemigos.draw(Pantalla)
   
        
        sprites.draw(Pantalla)
        pygame.display.flip()
        if play== False:
            MostrarTexto(Pantalla, consolas, "Espacio=Iniciar", Negro, 30, 445 ,123)
            MostrarTexto(Pantalla, consolas, "Esc=Salir", Negro, 30, 445 , 53)
            MostrarTexto(Pantalla, consolas, "Abajo=Agacharse", Negro, 30, 445 , 283)
            MostrarTexto(Pantalla, consolas, "Espacio=Iniciar", Blanco, 30, 450 ,120)
            MostrarTexto(Pantalla, consolas, "Esc=Salir", Blanco, 30, 450 , 50)
            MostrarTexto(Pantalla, consolas, "Abajo=Agacharse", Blanco, 30, 450 , 280)
            MostrarTexto(Pantalla, consolas, "r=Volver a empezar", Negro, 30, 445 , 203)
            MostrarTexto(Pantalla, consolas, "r=Volver a empezar", Blanco, 30, 450 , 200)
    
    if play == True and gameover==False:
        if cambio ==0:
            cambio=18
        posicionXFondo-=cambio
    else:
        cambio =0
    
    
    obtener(cambio)
    if gameover == True:
        caer(gameover)
    if keys[pygame.K_r] and gameover == True:
        puntaje =0
        volver()
        jugador.rect.center = (200 , 460) 
        recorrido=0 
        posicionXFondo=0
        reinicio(gameover)
        cambio=18
        Pantalla.blit(fondo, (x_relativa, 0))
        play=False
        gameover = False
        pygame.mixer.music.play(-1)
        jugador.image = pygame.transform.scale(pygame.image.load('Imagenes/Dinosaurio1.png'), (150, 175))
    
#Función Color Fondo#
def colorFondo():
    global recorrido, cambio
    if recorrido <=200:
        Pantalla.fill(BlueSky)
    if recorrido == 200:
        cambio = 20
    elif recorrido >200 and recorrido<290 :
        Pantalla.fill(Orange)
    if recorrido == 290:
        cambio = 25
        
    elif recorrido >=290 and recorrido<530:
        Pantalla.fill(BlueNigth)
    elif recorrido>=530:
        recorrido=0
    

def MostrarTexto(pantalla, fuente, texto, color, dimensiones, x , y):
    letra= pygame.font.Font(fuente, dimensiones)
    superficie= letra.render(texto, False, color)
    rectangulo= superficie.get_rect()
    rectangulo.center=(x , y)
    pantalla.blit(superficie, rectangulo)


pygame.init() #Iniciar Pygame#

###CARACTERISTICAS DEL JUEGO###
#Musica#
pygame.mixer.music.load('Sonidos/Musica1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.1)


Pantalla = pygame.display.set_mode((w,h))
Clock = pygame.time.Clock()
pygame.display.set_icon(icono)


#Grupos de Sprites#
sprites= pygame.sprite.Group()
enemigos = pygame.sprite.Group()
#Instancias#
jugador = Jugador()
sprites.add(jugador)

obstaculo = Piedra()
enemigos.add(obstaculo)


ejecutando = True #Bucle del juego#
while ejecutando:
    
    keys = pygame.key.get_pressed()
    Clock.tick(FPS) #FPS#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    
    recargaPantalla()
    
    enemigos.update()
    sprites.update()
    
    
    pygame.display.flip()
    if keys[pygame.K_ESCAPE]:
        ejecutando =False
    play= Saltar(keys, play, gameover)
    colision = pygame.sprite.spritecollide(jugador, enemigos,False)
    if colision:
        corriendo= False
        saltar=False
        gameover = True 
        jugador.image = pygame.transform.scale(pygame.image.load('Imagenes/DinosaurioMuerte.png'), (150, 175))
    
    
    # Control del audio
    #Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
    #Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
