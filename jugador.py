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

Agacharse = [pygame.image.load('Imagenes/Agacharse1.png'),
             pygame.image.load('Imagenes/Agacharse2.png'),
             pygame.image.load('Imagenes/Agacharse3.png'),
             pygame.image.load('Imagenes/Agacharse4.png'),
             pygame.image.load('Imagenes/Agacharse5.png'),
             pygame.image.load('Imagenes/Agacharse4.png'),
             pygame.image.load('Imagenes/Agacharse3.png'),
             pygame.image.load('Imagenes/Agacharse2.png'),
             pygame.image.load('Imagenes/Agacharse1.png'),
             pygame.image.load('Imagenes/Agacharse2.png'),]

Salto = [pygame.image.load('Imagenes/Dinosaurio1.png'),
         pygame.image.load('Imagenes/Dinosaurio1.png'),]

Muerto = [pygame.image.load('Imagenes/DinosaurioMuerte.png')]
muerto= False
px=190
py=400
corriendo=False
quieto=True
reloj=0
correr_actual = 0
i=0
k=0
saltar=False
gm= False
bajar=False
agachado=False
aux=0
play2=False

def Saltar(keys , play, gameover):
    global saltar, agachado, aux, bajar
    global py, key
    play2=play
    key= keys
    if saltar == False:
        if keys[pygame.K_SPACE] and gameover==False:
            sonisalto=pygame.mixer.Sound('Sonidos/Jump.mp3')
            pygame.mixer.Sound.play(sonisalto)
            sonisalto.set_volume(.2)
            saltar = True
            
        if bajar == False and corriendo == True:
            play2=True
        

    if keys[pygame.K_DOWN] and gameover==False and saltar==False and play2==True:
        agachado = True
        aux+=1
    else:
        agachado = False
        if aux>=1:
            py=400
        aux=0
    if gameover==True:
        saltar =False
        
    return play2

def volver():
    global px, saltar, quieto, muerto
    global py, bajar, gm
    px=180
    py=400
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
        self.image=pygame.transform.scale(Quieto[0], (110, 135))
        self.rect = self.image.get_rect() 
        self.rect.center = (px , py) 
        
    def update(self):
        global corriendo, reloj, correr_actual,i, bajar, saltar, quieto, gm, agachado
        global px, py, k
        
        if gm==True:
            corriendo= False
            quieto= False
            if px < 250:
                px+=15
            if py < 400:
                py +=10
            self.rect.center = (px , py) 
            self.image=pygame.transform.scale(Muerto[0], (110, 135))
            
            gm=False
            
        if quieto == True and muerto==False:
            self.image=pygame.transform.scale(Quieto[0], (110, 135))
        
        if corriendo == True: #PARA CORRER#
            reloj += 1

            if reloj >= 3:
                correr_actual += 1
                reloj = 0
            
            if correr_actual >= 10:
                correr_actual = 0
            self.image=pygame.transform.scale(Corriendo[correr_actual], (110, 135))
        if saltar == True: #PARA SALTAR#
            corriendo=False
            self.rect.center = (px , py) 
            if py >= 180 and bajar ==False:
                self.image=pygame.transform.scale(Salto[0], (110, 135))
                py -=30
            else:
                self.image=pygame.transform.scale(Salto[1], (110, 135))
                if bajar == False:
                    k+=1
                if k>=7:    
                    bajar = True
                    py +=30
                    if key[pygame.K_DOWN] and bajar==True:
                        py += 20
                    if py >= 400:
                        py=400
                        saltar=False        
                        corriendo= True
                        self.rect.center = (px , py)    
                        k=0
                        bajar = False
                        play2=True
        if agachado ==True:
            
            self.image=pygame.transform.scale(Agacharse[correr_actual], (110, 95))
            saltar=False
            bajar=False
            corriendo=True
            self.rect.center = (px , py+45) 
        else:
            self.rect.center = (px , py) 
        
    
