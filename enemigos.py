import pygame

posicionX = 1300
w= 1200
velocidad=0

def obtener(contador):
    global contadorNow 
    contadorNow= contador
    
        
def reinicio(gameover):
    global posicionX
    if gameover==True:
        posicionX = 1300

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

        
        
        
