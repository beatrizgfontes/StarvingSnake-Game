import pygame

length = 1280
height = 650

class Arbusto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto1 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto1
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 175,545

class Arbusto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto2 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto2
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 300,545

class Arbusto3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto3 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto3
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 425,545

class Arbusto4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto4 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto4
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 550,545

class Arbusto5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto5 = pygame.image.load("florest_scenary_images/arbusto2.png")
        self.image = self.arbusto5
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0

class Arbusto6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto6 = pygame.image.load("florest_scenary_images/arbusto2.png")
        self.image = self.arbusto6
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,125

class Arbusto7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto7 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto7
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 500,0

class Arbusto8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto8 = pygame.image.load("florest_scenary_images/arbusto2.png")
        self.image = self.arbusto8
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1200,505

class Arbusto9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto9 = pygame.image.load("florest_scenary_images/arbusto2.png")
        self.image = self.arbusto9
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1200,380

class Arbusto10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto10 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto10
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 625,0

class Arbusto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto11 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto11
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 675,545

class Arbusto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto12 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto12
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 800,545

class Arbusto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto13 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto13
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 925,545

class Arbusto14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto14 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto14
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1050,545
 
class Arbusto15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto15 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto15
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 750,0

class Arbusto16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto16 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto16
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 750,0
 
class Arbusto17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto17 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto17
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 875,0
 
class Arbusto18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto18 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto18
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 375,0
 
class Arbusto19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto19 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto19
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 250,0

class Arbusto20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbusto20 = pygame.image.load("florest_scenary_images/arbusto.png")
        self.image = self.arbusto20
        self.image = pygame.transform.scale(self.image,(150,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 125,0