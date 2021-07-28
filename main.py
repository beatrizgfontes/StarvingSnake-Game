import pygame
from pygame.locals import *
from random import randrange

""" INICIALIZAR JOGO """
pygame.init() # Inicializa todas as funções e variáveis da biblioteca pygame.

""" CORES """
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
aqua = (20,255,255)
blue = (0,0,255)
forestgreen = (34,139,34)

""" CONFIGURAÇÕES DA TELA """
length = 1280
height = 650
score = 0
tamanho = 100

""" CENÁRIOS DO JOGO """
floresta = pygame.image.load("images/Cenário Floresta3D.png")
floresta = pygame.transform.scale(floresta,(length,height))

cidade = pygame.image.load("images/Cenário Cidade3D.png")
cidade = pygame.transform.scale(cidade,(length,height))

deserto = pygame.image.load("images/Cenário Deserto3D.png")
deserto = pygame.transform.scale(deserto,(length,height))

""" POSIÇÃO COBRA """
#axis_x = randint(tamanho, (length-tamanho))
#axis_y = randint(tamanho, (height-tamanho))
axis_x = length/2
axis_y = height/2

""" DEFINIÇÃO DE TELA """
gamescreen = pygame.display.set_mode((length,height)) #  Inicializa uma janela ou tela para exibição.
pygame.display.set_caption("Starving Snake") # Nome na janela do jogo.

""" FONTES DO JOGO """
textfont1 = pygame.font.SysFont('arial', 40, True, True)
textfont2 = pygame.font.SysFont('arial', 100, True, True)
textfont3 = pygame.font.SysFont('arial', 80, True, False)
textfont4 = pygame.font.SysFont('arial', 45, True, False)

""" IMPORTANDO A COBRA """
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes[self.currently]
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
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("back/snakeback_0.png"))
            self.snakes.append(pygame.image.load("back/snakeback_1.png"))
            self.snakes.append(pygame.image.load("back/snakeback_2.png"))
            #self.snakes = [pygame.image.load("back/snakeback_0.png"),pygame.image.load("back/snakeback_1.png"),pygame.image.load("back/snakeback_2.png")]
            self.rect.y -= 100
            self.above = False
                    
        if self.below == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("front/snakefront_0.png"))
            self.snakes.append(pygame.image.load("front/snakefront_1.png"))
            #self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
            self.rect.y += 100
            self.below = False
 
        if self.east == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("right/snakeright_0.png"))
            self.snakes.append(pygame.image.load("right/snakeright_1.png"))
            #self.snakes = [pygame.image.load("right/snakeright_0.png"),pygame.image.load("right/snakeright_1.png")]
            self.rect.x += 100
            self.east = False
 
        if self.west == True:
            del self.snakes[0:4]
            self.snakes.append(pygame.image.load("left/snakeleft_0.png"))
            self.snakes.append(pygame.image.load("left/snakeleft_1.png"))
            #self.snakes = [pygame.image.load("left/snakeleft_0.png"),pygame.image.load("left/snakeleft_1.png")]
            self.rect.x -= 100
            self.west = False
            
        if self.currently >= len(self.snakes):
            self.currently = 0
        self.image = self.snakes[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
all = pygame.sprite.Group()
snake = Snake()
all.add(snake)

""" IMPORTANDO MAÇÃ """
class Maca1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        maca1 = pygame.image.load("images/maca1.png")
        self.image = maca1
        self.image = pygame.transform.scale(self.image,(25*2,25*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,420
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

gp_maca = pygame.sprite.Group()
apple1 = Maca1()
all.add(apple1)
gp_maca.add(apple1)

""" IMPORTANDO O LAGARTIXA """
class Lagartixa1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        lagartixa1 = pygame.image.load("images/lagartixa1.png")
        self.image = lagartixa1
        self.image = pygame.transform.scale(self.image,(34*2,34*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 800,250
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

gp_lagartixa = pygame.sprite.Group()
gecko1 = Lagartixa1()
all.add(gecko1)
gp_lagartixa.add(gecko1)

""" IMPORTANDO O RATO """
class Rato1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        rato1 = pygame.image.load("images/rato1.png")
        self.image = rato1
        self.image = pygame.transform.scale(self.image,(27*2,27*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 250,0
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        #self.rect.x += 30

gp_rato = pygame.sprite.Group()
rat1 = Rato1()
all.add(rat1)
gp_rato.add(rat1)

""" IMPORTANDO OS CARROS """
class Carro1(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro1 = pygame.image.load("images/carro1.png")
        self.image = carro1
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,300
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 20
 
obstaculos_cidade = pygame.sprite.Group()
car1 = Carro1()
all.add(car1)
obstaculos_cidade.add(car1)

class Carro2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        carro2 = pygame.image.load("images/carro2.png")
        self.image = carro2
        self.image = pygame.transform.scale(self.image,(400,150))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,420
 
    def update(self):
        if self.rect.topleft[0] > length:
            self.rect.x = 0
        self.rect.x += 30
 
car2 = Carro2()
all.add(car2)
obstaculos_cidade.add(car2)

""" IMPORTANDO PESSOA E GATO """
class People(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.pessoa = [pygame.image.load("images/pessoa2.png"),pygame.image.load("images/pessoa3.png"),pygame.image.load("images/pessoa4.png"),pygame.image.load("images/pessoa5.png")]
        self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,430
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] < 0:
            self.rect.x = length
        self.rect.x -= 20
 
        if self.currently >= len(self.pessoa):
            self.currently = 0
        self.image = self.pessoa[self.currently]
        self.image = pygame.transform.scale(self.image,(150,200))
 
people = People()
all.add(people)
obstaculos_cidade.add(people)
 
class Gato(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.gato = [pygame.image.load("images/gato0.png"),pygame.image.load("images/gato1.png"),pygame.image.load("images/gato2.png")]
        self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 230,230
 
    def update(self):
        self.currently = self.currently + 1
        if self.rect.topright[0] > length:
            self.rect.x = 0
        self.rect.x += 20
 
        if self.currently >= len(self.gato):
            self.currently = 0
        self.image = self.gato[self.currently]
        self.image = pygame.transform.scale(self.image,(33*2,33*2))
 
gato = Gato()
all.add(gato)
obstaculos_cidade.add(gato)

""" IMPORTANDO CACTO """
class Cacto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto1 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto1
        self.image = pygame.transform.scale(self.image,(100,200))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,0
        
obstaculos_deserto = pygame.sprite.Group()
cacto1 = Cacto1()
all.add(cacto1)
obstaculos_deserto.add(cacto1)

class Cacto11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto11 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto11
        self.image = pygame.transform.scale(self.image,(100,200))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,200
        
cacto11 = Cacto11()
all.add(cacto11)
obstaculos_deserto.add(cacto11)

class Cacto12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto12 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto12
        self.image = pygame.transform.scale(self.image,(100,200))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 750,280
        
cacto12 = Cacto12()
all.add(cacto12)
obstaculos_deserto.add(cacto12)
 
class Cacto13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto13 = pygame.image.load("images/cacto1.png")
        self.image = self.cacto13
        self.image = pygame.transform.scale(self.image,(100,200))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1000,420
        
cacto13 = Cacto13()
all.add(cacto13)
obstaculos_deserto.add(cacto13)
 
class Cacto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto2 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto2
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 1100,190
        
cacto2 = Cacto2()
all.add(cacto2)
obstaculos_deserto.add(cacto2)
 
class Cacto21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto21 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto21
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 780,0
        
cacto21 = Cacto21()
all.add(cacto21)
obstaculos_deserto.add(cacto21)
 
class Cacto22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto22 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto22
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,20
        
cacto22 = Cacto22()
all.add(cacto22)
obstaculos_deserto.add(cacto22)
 
class Cacto23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto23 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto23
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 150,470
        
cacto23 = Cacto23()
all.add(cacto23)
obstaculos_deserto.add(cacto23)
 
class Cacto24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto24 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto24
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,440
        
cacto24 = Cacto24()
all.add(cacto24)
obstaculos_deserto.add(cacto24)
 
class Cacto25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cacto25 = pygame.image.load("images/cacto2.png")
        self.image = self.cacto25
        self.image = pygame.transform.scale(self.image,(100,150))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 275,220
        
cacto25 = Cacto25()
all.add(cacto25)
obstaculos_deserto.add(cacto25)

""" IMPORTANDO ESCORPIÃO"""
class Escorpiao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao1 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 400,0
 
    def update(self):
        if self.rect.bottom > height:
            self.rect.y = 0
        self.rect.y += 20
        self.image = self.escorpiao1
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao1 = Escorpiao1()
all.add(escorpiao1)
obstaculos_deserto.add(escorpiao1)
 
class Escorpiao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.escorpiao2 = pygame.image.load("images/escorpião1.png")
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 900, 550
 
    def update(self):
        if self.rect.bottom < 0:
            self.rect.y = height
        self.rect.y -= 20
        self.image = self.escorpiao2
        self.image = pygame.transform.scale(self.image,(64,64))
    
escorpiao2 = Escorpiao2()
all.add(escorpiao2)
obstaculos_deserto.add(escorpiao2)

""" DEFINIÇÃO DO LOOP """
time = pygame.time.Clock() # Relógio do FPS.

play_screen = True
while play_screen:
    gamescreen.fill(forestgreen) # Cor de fundo da tela.

    text = ("Starving Snake")
    ftext = textfont2.render(text, True, white)
    gamescreen.blit(ftext, (280,40)) # Exibir o texto na tela.

    pygame.draw.rect(gamescreen, (blue), (460,290,360,100))
    text0 = ("Play")
    ftext0 = textfont3.render(text0, True, white)
    gamescreen.blit(ftext0, (560,293))

    for choice in pygame.event.get():
        if choice.type == QUIT:
            play_screen = False

        if choice.type == pygame.MOUSEBUTTONDOWN: # Eventos no mouse.
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            game_mode = True
            """ BOTÃO PLAY """
            if x > 460 and y > 290 and x < 820 and y < 390:

                """ LOOP DO MODO DE JOGO """
                while game_mode:
                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                    text1 = ("Starving Snake")
                    ftext1 = textfont2.render(text1, True, white)
                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                    text2 = ("Fácil")
                    ftext2 = textfont4.render(text2, True, white)
                    gamescreen.blit(ftext2, (560,243))

                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                    text3 = ("Médio")
                    ftext3 = textfont4.render(text3, True, white)
                    gamescreen.blit(ftext3, (550,373))

                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                    text4 = ("Difícil")
                    ftext4 = textfont4.render(text4, True, white)
                    gamescreen.blit(ftext4, (555,503))

                    for choice in pygame.event.get():
                        if choice.type == QUIT:
                            game_mode = False
                            play_screen = False
                        
                        if choice.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]

                            game_scenery = True
                            """ BOTÃO FÁCIL """
                            if x > 495 and y > 230 and x < 725 and y < 310:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False

                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                            if choice.type == KEYDOWN:
                                                                if choice.key == pygame.K_UP:
                                                                    snake.up()
                                                                if choice.key == pygame.K_DOWN:
                                                                    snake.down()
                                                                if choice.key == pygame.K_RIGHT:
                                                                    snake.right()
                                                                if choice.key == pygame.K_LEFT:
                                                                    snake.left()

                                                            if choice.type == KEYDOWN:
                                                                if choice.key == K_w:
                                                                    snake.up()
                                                                    #y -= 20 #UP
                                                                if choice.key == K_s:
                                                                    snake.down()
                                                                    #y += 20 #DOWN
                                                                if choice.key == K_d:
                                                                    snake.right()
                                                                    #x += 20 #RIGHT
                                                                if choice.key == K_a:
                                                                    snake.left()
                                                                    #x -= 20 #LEFT

                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(floresta, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))

                                                        all.draw(gamescreen)
                                                        all.update()
                                                        
                                                        pygame.display.flip()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40))

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    #axis_x = randint(tamanho, (length-tamanho))
                                                                    #axis_y = randint(tamanho, (height-tamanho))
                                                                    axis_x = length/2
                                                                    axis_y = height/2
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, black)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake,obstaculos_cidade,False)
                                                    apple_collides2 = pygame.sprite.spritecollide(snake,gp_maca,False)
                                                    gecko_collides2 = pygame.sprite.spritecollide(snake,gp_lagartixa,False)
                                                    rat_collides2 = pygame.sprite.spritecollide(snake,gp_rato,False)

                                                    if apple_collides2:
                                                        score += 2
                                                        apple1.rect.x = randrange(0,800,50)
                                                        apple1.rect.y = randrange(0,600,50)

                                                    if gecko_collides2:
                                                        score += 5
                                                        gecko1.rect.x = randrange(0,800,50)
                                                        gecko1.rect.y = randrange(0,600,50)
                                                        
                                                    if rat_collides2:
                                                        score += 10
                                                        rat1.rect.x = randrange(0,800,50)
                                                        rat1.rect.y = randrange(0,600,50)

                                                    if obstacle_collides2:

                                                        """ LOOP DO GAME OVER """
                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                OFF = True
                                                                snake.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all.draw(gamescreen)
                                                                all.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    

                                                        pygame.display.update()

                                                    else:
                                                        #all.update()
    
                                                        gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                        all.draw(gamescreen)
                                                        all.update()
                                                        gamescreen.blit(ftext9, (70,30))
                                                        
                                                        pygame.display.flip()

                                                    '''if axis_x + tamanho > length:
                                                        game_over = True
                                                    if axis_x < 0:
                                                        game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                    if axis_y + tamanho > height:
                                                            game_over = True
                                                    if axis_y < 0:
                                                        game_over = True'''

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                        if pygame.key.get_pressed()[K_w]: # UP
                                                            axis_y -= 10 
                                                        if pygame.key.get_pressed()[K_s]: # DOWN
                                                            axis_y += 10 
                                                        if pygame.key.get_pressed()[K_d]: # RIGHT
                                                            axis_x += 10 
                                                        if pygame.key.get_pressed()[K_a]: # LEFT
                                                            axis_x -= 10


                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(deserto, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))
                                                        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

                                                        pygame.display.update()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    axis_x = randint(tamanho, (length-tamanho))
                                                                    axis_y = randint(tamanho, (height-tamanho))
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()

                                    pygame.display.update() # Atualização da tela (porções da tela).

                            """ BOTÃO MÉDIO """
                            if x > 495 and y > 360 and x < 725 and y < 440:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False
                                            
                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            game_over = False
                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                        if pygame.key.get_pressed()[K_w]: # UP
                                                            axis_y -= 10 
                                                        if pygame.key.get_pressed()[K_s]: # DOWN
                                                            axis_y += 10 
                                                        if pygame.key.get_pressed()[K_d]: # RIGHT
                                                            axis_x += 10 
                                                        if pygame.key.get_pressed()[K_a]: # LEFT
                                                            axis_x -= 10


                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(floresta, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))
                                                        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

                                                        pygame.display.update()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    axis_x = randint(tamanho, (length-tamanho))
                                                                    axis_y = randint(tamanho, (height-tamanho))
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, black)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake,obstaculos_cidade,False)
                                                    apple_collides2 = pygame.sprite.spritecollide(snake,gp_maca,False)
                                                    gecko_collides2 = pygame.sprite.spritecollide(snake,gp_lagartixa,False)
                                                    rat_collides2 = pygame.sprite.spritecollide(snake,gp_rato,False)

                                                    if apple_collides2:
                                                        score += 2
                                                        apple1.rect.x = randrange(0,800,50)
                                                        apple1.rect.y = randrange(0,600,50)

                                                    if gecko_collides2:
                                                        score += 5
                                                        gecko1.rect.x = randrange(0,800,50)
                                                        gecko1.rect.y = randrange(0,600,50)
                                                        
                                                    if rat_collides2:
                                                        score += 10
                                                        rat1.rect.x = randrange(0,800,50)
                                                        rat1.rect.y = randrange(0,600,50)

                                                    if obstacle_collides2:

                                                        """ LOOP DO GAME OVER """
                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                OFF = True
                                                                snake.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all.draw(gamescreen)
                                                                all.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    

                                                        pygame.display.update()

                                                    else:
                                                        #all.update()
    
                                                        gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                        all.draw(gamescreen)
                                                        all.update()
                                                        gamescreen.blit(ftext9, (70,30))
                                                        
                                                        pygame.display.flip()

                                                    '''if axis_x + tamanho > length:
                                                        game_over = True
                                                    if axis_x < 0:
                                                        game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                    if axis_y + tamanho > height:
                                                            game_over = True
                                                    if axis_y < 0:
                                                        game_over = True'''

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                        if pygame.key.get_pressed()[K_w]: # UP
                                                            axis_y -= 10 
                                                        if pygame.key.get_pressed()[K_s]: # DOWN
                                                            axis_y += 10 
                                                        if pygame.key.get_pressed()[K_d]: # RIGHT
                                                            axis_x += 10 
                                                        if pygame.key.get_pressed()[K_a]: # LEFT
                                                            axis_x -= 10


                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(deserto, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))
                                                        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

                                                        pygame.display.update()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    axis_x = randint(tamanho, (length-tamanho))
                                                                    axis_y = randint(tamanho, (height-tamanho))
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()
                    

                                    pygame.display.update() # Atualização da tela (porções da tela).

                            """ BOTÃO DIFÍCIL """
                            if x > 495 and y > 490 and x < 725 and y < 570:

                                """ LOOP DOS CENÁRIOS """
                                while game_scenery:
                                    gamescreen.fill(forestgreen) # Cor de fundo da tela.

                                    text1 = ("Starving Snake")
                                    ftext1 = textfont2.render(text1, True, white)
                                    gamescreen.blit(ftext1, (280,40)) # Exibir o texto na tela.

                                    pygame.draw.rect(gamescreen, (blue), (495,230,230,80))
                                    text2 = ("Floresta")
                                    ftext2 = textfont4.render(text2, True, white)
                                    gamescreen.blit(ftext2, (525,243))

                                    pygame.draw.rect(gamescreen, (blue), (495,360,230,80))
                                    text3 = ("Cidade")
                                    ftext3 = textfont4.render(text3, True, white)
                                    gamescreen.blit(ftext3, (533,373))

                                    pygame.draw.rect(gamescreen, (blue), (495,490,230,80))
                                    text4 = ("Deserto")
                                    ftext4 = textfont4.render(text4, True, white)
                                    gamescreen.blit(ftext4, (525,503))

                                    for choice in pygame.event.get():
                                        if choice.type == QUIT:
                                            game_scenery = False
                                            game_mode = False
                                            play_screen = False
                                            
                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]

                                            game_over = False
                                            OFF = True
                                            """ BOTÃO FLORESTA """
                                            if x > 495 and y > 230 and x < 725 and y < 310:

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                        if pygame.key.get_pressed()[K_w]: # UP
                                                            axis_y -= 10 
                                                        if pygame.key.get_pressed()[K_s]: # DOWN
                                                            axis_y += 10 
                                                        if pygame.key.get_pressed()[K_d]: # RIGHT
                                                            axis_x += 10 
                                                        if pygame.key.get_pressed()[K_a]: # LEFT
                                                            axis_x -= 10


                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(floresta, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))
                                                        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

                                                        pygame.display.update()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    axis_x = randint(tamanho, (length-tamanho))
                                                                    axis_y = randint(tamanho, (height-tamanho))
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, black)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake,obstaculos_cidade,False)
                                                    apple_collides2 = pygame.sprite.spritecollide(snake,gp_maca,False)
                                                    gecko_collides2 = pygame.sprite.spritecollide(snake,gp_lagartixa,False)
                                                    rat_collides2 = pygame.sprite.spritecollide(snake,gp_rato,False)

                                                    if apple_collides2:
                                                        score += 2
                                                        apple1.rect.x = randrange(0,800,50)
                                                        apple1.rect.y = randrange(0,600,50)

                                                    if gecko_collides2:
                                                        score += 5
                                                        gecko1.rect.x = randrange(0,800,50)
                                                        gecko1.rect.y = randrange(0,600,50)
                                                        
                                                    if rat_collides2:
                                                        score += 10
                                                        rat1.rect.x = randrange(0,800,50)
                                                        rat1.rect.y = randrange(0,600,50)

                                                    if obstacle_collides2:

                                                        """ LOOP DO GAME OVER """
                                                        gamescreen.fill(forestgreen)
                                                            
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))

                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                        if choice.type == pygame.MOUSEBUTTONDOWN:
                                                            x = pygame.mouse.get_pos()[0]
                                                            y = pygame.mouse.get_pos()[1]

                                                            """ BOTÃO CONTINUAR """
                                                            if x > 395 and y > 290 and x < 625 and y < 370:
                                                                OFF = True
                                                                snake.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all.draw(gamescreen)
                                                                all.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        #all.update()
    
                                                        gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                        all.draw(gamescreen)
                                                        all.update()
                                                        gamescreen.blit(ftext9, (70,30))
                                                        
                                                        pygame.display.flip()

                                                    '''if axis_x + tamanho > length:
                                                        game_over = True
                                                    if axis_x < 0:
                                                        game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                    if axis_y + tamanho > height:
                                                            game_over = True
                                                    if axis_y < 0:
                                                        game_over = True'''

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    if OFF:
                                                        gamescreen.fill(white)
                                                        text9 = f"Score: {score}"
                                                        ftext9 = textfont1.render(text9, True, black)

                                                        for choice in pygame.event.get():
                                                            if choice.type == QUIT:
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False
                                                        
                                                        if pygame.key.get_pressed()[K_w]: # UP
                                                            axis_y -= 10 
                                                        if pygame.key.get_pressed()[K_s]: # DOWN
                                                            axis_y += 10 
                                                        if pygame.key.get_pressed()[K_d]: # RIGHT
                                                            axis_x += 10 
                                                        if pygame.key.get_pressed()[K_a]: # LEFT
                                                            axis_x -= 10


                                                        if axis_x + tamanho > length:
                                                            game_over = True
                                                        if axis_x < 0:
                                                            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
                                                        if axis_y + tamanho > height:
                                                            game_over = True
                                                        if axis_y < 0:
                                                            game_over = True

                                                        gamescreen.blit(deserto, (0,0))
                                                        gamescreen.blit(ftext9, (70,30))
                                                        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

                                                        pygame.display.update()

                                                    """ LOOP DO GAME OVER """
                                                    while game_over:
                                                        gamescreen.fill(forestgreen)
                                                        
                                                        """ ELEMENTOS DA TELA """
                                                        text10 = ("Game Over")
                                                        ftext10 = textfont2.render(text10, True, red)
                                                        gamescreen.blit(ftext10, (380,40)) # Exibir o texto na tela.

                                                        text11 = f"Score: {score}"
                                                        ftext11 = textfont3.render(text11, True, white)
                                                        gamescreen.blit(ftext11,(485,165))

                                                        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
                                                        text12 = ("Continuar")
                                                        ftext12 = textfont4.render(text12, True, white)
                                                        gamescreen.blit(ftext12, (403,305))

                                                        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
                                                        text13 = ("Menu")
                                                        ftext13 = textfont4.render(text13, True, white)
                                                        gamescreen.blit(ftext13, (750,305))


                                                        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
                                                            if choice.type == QUIT: # Opção para sair do jogo.
                                                                game_over = False
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = False
                                                                play_screen = False

                                                            if choice.type == pygame.MOUSEBUTTONDOWN:
                                                                x = pygame.mouse.get_pos()[0]
                                                                y = pygame.mouse.get_pos()[1]

                                                                """ BOTÃO CONTINUAR """
                                                                if x > 395 and y > 290 and x < 625 and y < 370:
                                                                    OFF = True
                                                                    game_over = False
                                                                    axis_x = randint(tamanho, (length-tamanho))
                                                                    axis_y = randint(tamanho, (height-tamanho))
                                                                    score = 0

                                                                """ BOTÃO MENU """
                                                                if x > 690 and y > 290 and x < 920 and y < 370:
                                                                    game_over = False
                                                                    OFF = False
                                                                    game_scenery = False
                                                                    game_mode = True

                                                        pygame.display.update()
                    
                                    pygame.display.update()
                    
                    pygame.display.update()

    time.tick(0.5) # FPS
    pygame.display.update()

""" FINALIZAR JOGO """
pygame.quit()
quit()