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
length = 1280 # Comprimento
height = 650 # Altura
score = 0
tamanho = 100

" FONTES DO JOGO "
textfont1 = pygame.font.SysFont('arial', 40, True, True)
textfont2 = pygame.font.SysFont('arial', 100, True, True)
textfont3 = pygame.font.SysFont('arial', 80, True, False)
textfont4 = pygame.font.SysFont('arial', 45, True, False)

""" POSIÇÃO COBRA """
axis_x = randint(tamanho, (length-tamanho))
axis_y = randint(tamanho, (height-tamanho))

""" DEFINIÇÃO DE TELA """
gamescreen = pygame.display.set_mode((length,height)) #  Inicializa uma janela ou tela para exibição.
pygame.display.set_caption("Starving Snake") # Nome na janela do jogo.

""" DEFINIÇÃO DO LOOP """
time = pygame.time.Clock() # Relógio do FPS.

OFF = True
game_over = False
while OFF:
    " LOOP DO GAME OVER "
    while game_over:
        gamescreen.fill(forestgreen) # Cor de fundo da tela.
        
        " ELEMENTOS DA TELA "
        text2 = ("Game Over")
        ftext2 = textfont2.render(text2, True, red)
        gamescreen.blit(ftext2, (380,40)) # Exibir o texto na tela.

        text3 = f"Score: {score}"
        ftext3 = textfont3.render(text3, True, white)
        gamescreen.blit(ftext3,(485,165))

        pygame.draw.rect(gamescreen, (blue), (395,290,230,80))
        text4 = (" Continuar")
        ftext4 = textfont4.render(text4, True, white)
        gamescreen.blit(ftext4, (393,305))

        pygame.draw.rect(gamescreen, (blue), (690,290,230,80))
        text5 = (" Sair")
        ftext5 = textfont4.render(text5, True, white)
        gamescreen.blit(ftext5, (750,305))


        for choice in pygame.event.get(): # Interação com ocorrência/Definição de eventos.
            if choice.type == QUIT: # Opção para sair do jogo.
                OFF = False
                game_over = False

            if choice.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 395 and y > 290 and x < 625 and y < 370:
                    OFF = True
                    game_over = False
                    axis_x = randint(tamanho, (length-tamanho))
                    axis_y = randint(tamanho, (height-tamanho))
                    score = 0
                if x > 690 and y > 290 and x < 920 and y < 370:
                    OFF = False
                    game_over = False

        pygame.display.update() # Atualização da tela (porções da tela).

    time.tick(80) # FPS

    if OFF:
        gamescreen.fill(white)
        text1 = f"Score: {score}"
        ftext1 = textfont1.render(text1, True, black)

        for choice in pygame.event.get():
            if choice.type == QUIT:
                OFF = False
        
        if pygame.key.get_pressed()[K_w]: # UP
            axis_y -= 10 
        if pygame.key.get_pressed()[K_s]: # DOWN
            axis_y += 10 
        if pygame.key.get_pressed()[K_d]: # RIGHT
            axis_x += 10 
        if pygame.key.get_pressed()[K_a]: # LEFT
            axis_x -= 10

        pygame.draw.circle(gamescreen, (230,0,210), (axis_x, axis_y) , 80)

        if axis_x + tamanho > length:
            game_over = True
        if axis_x < 0:
            game_over = True                    # Todo esse bloco é para colidir com a borda e o jogo finalizar
        if axis_y + tamanho > height:
            game_over = True
        if axis_y < 0:
            game_over = True

        gamescreen.blit(ftext1, (70,30))

        pygame.display.update()

""" FINALIZAR JOGO """
pygame.quit()
quit()