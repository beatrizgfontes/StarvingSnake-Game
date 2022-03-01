import pygame

length = 1280
height = 650

class Rato1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        rato1 = pygame.image.load("food_images/rato1.png")
        self.image = rato1
        self.image = pygame.transform.scale(self.image,(27*2,27*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,400
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30