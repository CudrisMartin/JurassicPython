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
max = 380
min = 150

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
        posicionY2 = random.randint(min, max)
    

class Piedra(pygame.sprite.Sprite):
    
    def __init__(self):    
        global posicionX
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Imagenes/Piedra2.png'), (95, 120))
        self.rect = self.image.get_rect()    
        self.rect.center = (posicionX ,420 )  
             
        
        
    def update(self):
        
        global posicionX, contadorNow, velocidad
        self.rect.center = (posicionX , 420 )  
        if posicionX <= -450:
            posicionX=1300
        posicionX-=contadorNow

class Volador(pygame.sprite.Sprite):
    
    def __init__(self):    
        global posicionX2, posicionY2, play, posicionX
        posicionX2=posicionX  + 900
        posicionY2 = random.randint(min, max)
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Imagenes/Pajaro2.png'), (75, 87))
        self.rect = self.image.get_rect()    
        self.rect.center = (posicionX2 , posicionY2)  
    
    def update(self):
            
        global posicionX2, posicionY2, velocidad, contadorNow, reloj, actual
        self.rect.center = (posicionX2 , posicionY2)  
        if contadorNow < 25 and play2 == True and gm==False:
            if posicionX2 <= -800:
                posicionX2=posicionX + 1000 
                posicionY2 = random.randint(min, max)
            posicionX2-=27
        elif play2 == True and gm == False:
            if posicionX2 <= -1200:
                posicionX2=posicionX  + 1000 
                posicionY2 = random.randint(min, max)
            posicionX2-=35
        
        reloj += 1

        if reloj >= 4:
            actual += 1
            reloj = 0
            
            if actual >= 2:
                actual = 0
        
        self.image = pygame.transform.scale(animacion[actual], (75, 87))
        
        
