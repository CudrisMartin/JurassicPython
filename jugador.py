
Corriendo = [pygame.image.load('Imagenes/Dino1run1.png'),
             pygame.image.load('Imagenes/Dino1idle.png'),
             pygame.image.load('Imagenes/Dino1run2.png'),
             pygame.image.load('Imagenes/Dino1idle.png'),
             pygame.image.load('Imagenes/Dino1run1.png'),
             pygame.image.load('Imagenes/Dino1idle.png')]

Salto = [pygame.image.load('Imagenes/Dino1idle.png'),
         pygame.image.load('Imagenes/Dino1idle.png'),]

class Jugador(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale(Salto[0], (150, 175))
        self.rect = self.image.get_rect() 
