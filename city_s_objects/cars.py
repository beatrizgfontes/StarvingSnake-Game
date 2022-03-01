import pygame

length = 1280
height = 650

class Carro1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro1 = pygame.image.load("city_scenary_images/carro1.png")
        self.image = carro1
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,300
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 20

class Carro2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro2 = pygame.image.load("city_scenary_images/carro2.png")
        self.image = carro2
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,420
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 30