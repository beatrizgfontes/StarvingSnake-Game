import pygame

length = 1280
height = 650

class Bird1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.bird1 = [pygame.image.load("florest_scenary_images/passaro1.1.png"),pygame.image.load("florest_scenary_images/passaro1.2.png"),pygame.image.load("florest_scenary_images/passaro1.3.png"),pygame.image.load("florest_scenary_images/passaro1.4.png"),pygame.image.load("florest_scenary_images/passaro1.5.png")]
        self.currently = 0
        self.image = self.bird1[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,350
 
    def update(self):
        self.currently +=1
        if self.rect.topright[0] < 0:
            self.rect.x = length
        self.rect.x -= 20
 
        if self.currently >= len(self.bird1):
            self.currently = 0
            
        self.image = self.bird1[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))

class Bird2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.bird2 = [pygame.image.load("florest_scenary_images/passaro2.1.png"),pygame.image.load("florest_scenary_images/passaro2.2.png"),pygame.image.load("florest_scenary_images/passaro2.3.png"),pygame.image.load("florest_scenary_images/passaro2.4.png"),pygame.image.load("florest_scenary_images/passaro2.5.png")]
        self.currently = 0
        self.image = self.bird2[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,220
 
    def update(self):
        self.currently +=1
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 35
 
        if self.currently >= len(self.bird2):
            self.currently = 0
            
        self.image = self.bird2[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))