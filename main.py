import pygame
from jugador import Jugador
from jugador import Saltar
from jugador import volver
from jugador import caer
from enemigos import Piedra
from enemigos import Volador
from enemigos import obtener
from enemigos import reinicio

###VARIABLES GLOBALES###
#Recursos#
fondo=pygame.image.load('Imagenes/Fondo.png')
icono=pygame.image.load('Imagenes/Piedra.png')
#Colores#
BlueSky= (138, 220, 253)
Orange= (255, 170, 79)
BlueNigth= (29, 56, 145)
Yellow = (224, 211, 27)
Red = (197, 56, 13)
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
            pygame.draw.rect(Pantalla, Yellow, [5, 55, 460, 230], 0)
            pygame.draw.rect(Pantalla, Red, [10, 60, 450, 220], 0)
            MostrarTexto(Pantalla, consolas, "[Espacio]=Iniciar", Negro, 20, 190 ,133)
            MostrarTexto(Pantalla, consolas, "[Esc]=Salir", Negro, 20, 129 , 93)
            MostrarTexto(Pantalla, consolas, "[▼]=Agacharse", Negro, 20, 150 , 173)
            MostrarTexto(Pantalla, consolas, "[Espacio]=Iniciar", Blanco, 20, 190 ,130)
            MostrarTexto(Pantalla, consolas, "[Esc]=Salir", Blanco, 20, 129 , 90)
            MostrarTexto(Pantalla, consolas, "[▼]=Agacharse", Blanco, 20, 150 , 170)
            MostrarTexto(Pantalla, consolas, "[p]=♪+ Subir Volumen", Negro, 20, 220 , 213)
            MostrarTexto(Pantalla, consolas, "[p]=♪+ Subir Volumen", Blanco, 20, 220 , 210)
            MostrarTexto(Pantalla, consolas, "[o]=♪- Bajar Volumen", Negro, 20, 220 , 253)
            MostrarTexto(Pantalla, consolas, "[o]=♪- Bajar Volumen", Blanco, 20, 220 , 250)
        
            
        enemigos.draw(Pantalla)   
        sprites.draw(Pantalla)
        pygame.display.flip()
        
    if play == True and gameover==False:
        if cambio ==0:
            cambio=18
        posicionXFondo-=cambio
    else:
        cambio =0
    
    
    obtener(cambio, play, gameover)
    if gameover == True:
        MostrarTexto(Pantalla, consolas, "[r]=Volver a empezar", Negro, 20, 452 , 42)
        MostrarTexto(Pantalla, consolas, "[r]=Volver a empezar", Blanco, 20, 450 , 40)
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
ave = Volador()
enemigos.add(ave)
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
    if keys[pygame.K_o] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
    #Sube volumen
    if keys[pygame.K_p] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
