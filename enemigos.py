import pygame
import random
gm= False
posicionX = 1300
w= 1200
velocidad=0
posicionX2=2700
posicionY2 = 0
play2= False
reloj = 0
actual = 0

animacion = [pygame.image.load('Imagenes/Pajaro1.png'),
                 pygame.image.load('Imagenes/Pajaro2.png')]

def obtener(contador,play, gameover):
    global contadorNow,play2, gm
    contadorNow= contador
    gm= gameover
    play2=play
        
def reinicio(gameover):
    global posicionX, posicionX2, posicionY2 
    
    if gameover==True:
        posicionX = 1300
        posicionX2 = 2865
        posicionY2 = random.randint(200, 400)
    

class Piedra(pygame.sprite.Sprite):
    
    def __init__(self):    
        global posicionX
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Imagenes/Piedra.png'), (95, 120))
        self.rect = self.image.get_rect()    
        self.rect.center = (posicionX ,490 )  
             
        
        
    def update(self):
        
        global posicionX, contadorNow, velocidad
        self.rect.center = (posicionX , 490 )  
        if posicionX <= -450:
            posicionX=1300
        posicionX-=contadorNow

class Volador(pygame.sprite.Sprite):
    
    def __init__(self):    
        global posicionX2, posicionY2, play
        posicionX2=2865
        posicionY2 = random.randint(200, 400)
        print(posicionY2)
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Imagenes/Pajaro2.png'), (75, 87))
        self.rect = self.image.get_rect()    
        self.rect.center = (posicionX2 , posicionY2)  
    
    def update(self):
            
        global posicionX2, posicionY2, velocidad, contadorNow, reloj, actual
        self.rect.center = (posicionX2 , posicionY2)  
        if contadorNow < 25 and play2 == True and gm==False:
            if posicionX2 <= -700:
                posicionX2=2700
                posicionY2 = random.randint(200, 400)
            posicionX2-=25
        elif play2 == True and gm == False:
            if posicionX2 <= -1200:
                posicionX2=2700
                posicionY2 = random.randint(200, 400)
            posicionX2-=38
        
        reloj += 1

        if reloj >= 4:
            actual += 1
            reloj = 0
            
            if actual >= 2:
                actual = 0
        
        self.image = pygame.transform.scale(animacion[actual], (75, 87))
        
        
