import pygame

Quieto =[
    pygame.image.load('Imagenes/Dinosaurio1.png')
]

Corriendo = [pygame.image.load('Imagenes/Dinosaurio1.png'),
             pygame.image.load('Imagenes/Dinosaurio2.png'),
             pygame.image.load('Imagenes/Dinosaurio3.png'),
             pygame.image.load('Imagenes/Dinosaurio4.png'),
             pygame.image.load('Imagenes/Dinosaurio5.png'),
             pygame.image.load('Imagenes/Dinosaurio4.png'),
             pygame.image.load('Imagenes/Dinosaurio3.png'),
             pygame.image.load('Imagenes/Dinosaurio2.png'),
             pygame.image.load('Imagenes/Dinosaurio1.png'),
             pygame.image.load('Imagenes/Dinosaurio2.png'),]

Salto = [pygame.image.load('Imagenes/Dinosaurio1.png'),
         pygame.image.load('Imagenes/Dinosaurio1.png'),]

Muerto = [pygame.image.load('Imagenes/DinosaurioMuerte.png')]
muerto= False
px=200
py=460
corriendo=False
quieto=True
reloj=0
correr_actual = 0
i=0
k=0
saltar=False
gm= False
bajar=False

def Saltar(keys , play, gameover):
    global saltar
    global py
    play2=play
    if saltar == False:
        if keys[pygame.K_SPACE] and gameover==False:
            saltar = True
            play2=True
            
    if gameover==True:
        saltar =False
        
    
    return play2

def volver():
    global px, saltar, quieto, muerto
    global py, bajar, gm
    px=200
    py=460
    saltar=False   
    bajar=False
    quieto = True
    muerto= False
    gm= False
    
def caer(gameover):
    global gm
    gm =gameover
    
       
    
    
class Jugador(pygame.sprite.Sprite):
    
    def __init__(self):
        global px, py
        super().__init__()
        self.image=pygame.transform.scale(Muerto[0], (150, 175))
        self.rect = self.image.get_rect() 
        self.rect.center = (px , py) 
        
    def update(self):
        global corriendo, reloj, correr_actual,i, bajar, saltar, quieto, gm
        global px, py, k
        
        if gm==True:
            corriendo= False
            quieto= False
            if px < 250:
                px+=15
            if py < 460:
                py +=15
            self.rect.center = (px , py) 
            self.image=pygame.transform.scale(Muerto[0], (150, 175))
            
            gm=False
            
        if quieto == True and muerto==False:
            self.image=pygame.transform.scale(Quieto[0], (150, 175))
        
        if corriendo == True: #PARA CORRER#
            reloj += 1

            if reloj >= 3:
                correr_actual += 1
                reloj = 0
            
            if correr_actual >= 10:
                correr_actual = 0
            self.image=pygame.transform.scale(Corriendo[correr_actual], (150, 175))
        if saltar == True: #PARA SALTAR#
            corriendo=False
            self.rect.center = (px , py) 
            if py >= 220 and bajar ==False:
                self.image=pygame.transform.scale(Salto[0], (150, 175))
                py -=30
            else:
                self.image=pygame.transform.scale(Salto[1], (150, 175))
                if bajar == False:
                    k+=1
                if k>=6:    
                    bajar = True
                    py +=30
                    if py == 460:
                        saltar=False        
                        corriendo= True
                        self.rect.center = (px , py)    
                        k=0
                        bajar = False
        
    
