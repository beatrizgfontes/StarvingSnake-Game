import pygame

length = 1280
height = 650

class People(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.pessoa = [pygame.image.load("city_scenary_images/pessoa2.png"),pygame.image.load("city_scenary_images/pessoa3.png"),pygame.image.load("city_scenary_images/pessoa4.png"),pygame.image.load("city_scenary_images/pessoa5.png")]
        self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,430
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] < 0:
            self.rect.x = length
        self.rect.x -= 20
 
        if self.currently >= len(self.pessoa):
            self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))

class Gato(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.gato = [pygame.image.load("city_scenary_images/gato0.png"),pygame.image.load("city_scenary_images/gato1.png"),pygame.image.load("city_scenary_images/gato2.png")]
        self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 230,230
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] > length:
            self.rect.x = 0
        self.rect.x += 20
 
        if self.currently >= len(self.gato):
            self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))