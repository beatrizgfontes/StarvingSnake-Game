import pygame

length = 1280
height = 650

class Lagartixa1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        lagartixa1 = pygame.image.load("food_images/lagartixa1.png")
        self.image = lagartixa1
        self.image = pygame.transform.scale(self.image,(34*2,34*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 275,120
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30