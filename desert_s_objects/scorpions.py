import pygame

length = 1280
height = 650

class Escorpiao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao1 = pygame.image.load("desert_scenary_images/escorpião1.png")
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 500,0
 
    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 20
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))

class Escorpiao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao2 = pygame.image.load("desert_scenary_images/escorpião1.png")
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 800, 550
 
    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 20
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))

class Escorpiao3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao3 = pygame.image.load("desert_scenary_images/escorpião1.png")
        self.image = self.escorpiao3
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 200,0
 
    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 10
        self.image = self.escorpiao3
        self.image = pygame.transform.scale(self.image,(64,64))

class Escorpiao4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao4 = pygame.image.load("desert_scenary_images/escorpião1.png")
        self.image = self.escorpiao4
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1100, 550
 
    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 10
        self.image = self.escorpiao4
        self.image = pygame.transform.scale(self.image,(64,64))