import pygame

length = 1280
height = 650

class Arvore1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arvore1 = pygame.image.load("florest_scenary_images/arvore1.png")
        self.image = self.arvore1
        self.image = pygame.transform.scale(self.image,(300,400))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,300
    
class Arvore2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arvore2 = pygame.image.load("florest_scenary_images/arvore1.png")
        self.image = self.arvore2
        self.image = pygame.transform.scale(self.image,(300,400))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1000,0