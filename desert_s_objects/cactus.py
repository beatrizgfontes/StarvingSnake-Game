import pygame

length = 1280
height = 650

class Cacto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto1 = pygame.image.load("desert_scenary_images/cacto1.png")
        self.image = self.cacto1
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0

class Cacto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto2 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto2
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 100

class Cacto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto11 = pygame.image.load("desert_scenary_images/cacto1.png")
        self.image = self.cacto11
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1200,0

class Cacto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto12 = pygame.image.load("desert_scenary_images/cacto1.png")
        self.image = self.cacto12
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,height - 100

class Cacto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto13 = pygame.image.load("desert_scenary_images/cacto1.png")
        self.image = self.cacto13
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1200,height - 100

class Cacto21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto21 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto21
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 300,0

class Cacto22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto22 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto22
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 400,0

class Cacto23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto23 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto23
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 600,0

class Cacto24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto24 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto24
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 700,0

class Cacto25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto25 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto25
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = length - 900,0

class Cacto26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto26 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto26
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1000,0

class Cacto27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto27 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto27
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 200

class Cacto28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto28 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto28
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 325

class Cacto29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto29 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto29
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 100,0 + 450

class Cacto30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto30 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto30
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 300,height - 100

class Cacto31(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto31 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto31
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 100

class Cacto32(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto32 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto32
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 200

class Cacto33(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto33 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto33
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 325

class Cacto34(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto34 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto34
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0 + 450

class Cacto35(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto35 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto35
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 400,height - 100

class Cacto36(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto36 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto36
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 600,height - 100

class Cacto37(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto37 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto37
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 700,height - 100

class Cacto38(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto38 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto38
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 900,height - 100

class Cacto39(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto39 = pygame.image.load("desert_scenary_images/cacto2.png")
        self.image = self.cacto39
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.topleft = length - 1000,height - 100