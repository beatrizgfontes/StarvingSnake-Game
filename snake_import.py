import pygame

length = 1280
height = 650

class Snake1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes1 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes1[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 700,120
        
        self.above = False
        self.below = False
        self.east = False #Right
        self.west = False #Left
 
 
    def up(self):
        self.above = True
 
    def down(self):
         self.below = True
 
    def right(self):
        self.east = True
 
    def left(self):
        self.west = True
     
 
    def update(self):
        self.currently = self.currently + 1
        if self.above == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes1.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes1.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes1.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes1.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes1[0:4]
            self.snakes1.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes1.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes1):
            self.currently = 0
        self.image = self.snakes1[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

class Snake2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes2 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes2[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 565,0
        
        self.above = False
        self.below = False
        self.east = False #Right
        self.west = False #Left
 
 
    def up(self):
        self.above = True
 
    def down(self):
         self.below = True
 
    def right(self):
        self.east = True
 
    def left(self):
        self.west = True
     
 
    def update(self):
        self.currently = self.currently + 1
        if self.above == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes2.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes2.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes2.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes2.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes2[0:4]
            self.snakes2.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes2.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes2):
            self.currently = 0
        self.image = self.snakes2[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))

class Snake3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes3 = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes3[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 650,120
        
        self.above = False
        self.below = False
        self.east = False #Right
        self.west = False #Left
 
 
    def up(self):
        self.above = True
 
    def down(self):
         self.below = True
 
    def right(self):
        self.east = True
 
    def left(self):
        self.west = True
     
 
    def update(self):
        self.currently = self.currently + 1
        if self.above == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes3.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes3.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 50
            self.above = False
                    
        if self.below == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes3.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 50
            self.below = False
 
        if self.east == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes3.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 50
            self.east = False
 
        if self.west == True:
            del self.snakes3[0:4]
            self.snakes3.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes3.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 50
            self.west = False
            
        if self.currently >= len(self.snakes3):
            self.currently = 0
        self.image = self.snakes3[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))