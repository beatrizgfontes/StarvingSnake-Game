import pygame
from pygame.locals import *
from random import randint

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

cidade = pygame.image.load("images/cenário cidade.png")
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

""" IMPORTING THE SNAKE """
 
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snakes = [pygame.image.load("front/snakefront_0.png"),pygame.image.load("front/snakefront_1.png")]
        self.currently = 0
        self.image = self.snakes[self.currently]
        self.image = pygame.transform.scale(self.image,(100,100))
 
        self.rect = self.image.get_rect()
        self.rect.topleft = 520,500
        
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

                                                        gamescreen.blit(cidade, (0,0))
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

                                                        gamescreen.blit(cidade, (0,0))
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

                                                        gamescreen.blit(cidade, (0,0))
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

    time.tick(5) # FPS
    pygame.display.update()

""" FINALIZAR JOGO """
pygame.quit()
quit()

'''if pink_object.colliderect(green_object): # Função para as colizoes
        otheraxis_x = randint(tamanho, (largura-tamanho)) # Para mudar de posição assim que colidir com o objeto principal
        otheraxis_y = randint(tamanho, (altura-tamanho))
        pontos = pontos + 1'''