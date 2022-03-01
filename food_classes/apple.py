import pygame

length = 1280
height = 650
""" IMPORTANDO MAÇÃ """
class Maca1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        maca1 = pygame.image.load("food_images/maca1.png")
        self.image = maca1
        self.image = pygame.transform.scale(self.image,(25*2,25*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 950,120
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30