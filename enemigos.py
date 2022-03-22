import pygame
gm= False
posicionX = 1300
w= 1200
velocidad=0
posicionX2=2700
play2= False
def obtener(contador,play, gameover):
    global contadorNow,play2, gm
    contadorNow= contador
    gm= gameover
    play2=play
        
def reinicio(gameover):
    global posicionX, posicionX2 
    
    if gameover==True:
        posicionX = 1300
        posicionX2 = 2865
    

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
        global posicionX2, play
        posicionX2=2865
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Imagenes/Piedra.png'), (100, 50))
        self.rect = self.image.get_rect()    
        self.rect.center = (posicionX2 , 400)  
    
    def update(self):
            
        global posicionX2, velocidad,contadorNow
        self.rect.center = (posicionX2 , 400)  
        if contadorNow < 25 and play2 == True and gm==False:
            if posicionX2 <= -700:
                posicionX2=2700
            posicionX2-=25
        elif play2 == True and gm == False:
            if posicionX2 <= -1200:
                posicionX2=2700
            posicionX2-=38
        
        
