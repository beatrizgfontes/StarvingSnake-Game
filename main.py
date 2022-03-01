import pygame
from pygame.locals import *
from random import randrange

""" IMPORTAÇÕES DE OBJETOS """
from food_classes.apple import Maca1
from food_classes.gecko import Lagartixa1
from food_classes.rat import Rato1
from florest_s_objects.trees import *
from florest_s_objects.bush import *
from florest_s_objects.birds import *
from city_s_objects.cars import *
from city_s_objects.cat_and_person_s_object import *
from desert_s_objects.cactus import *
from desert_s_objects.scorpions import *
from snake_import import *

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
floresta = pygame.image.load("background_images/Cenário Floresta3D.png")
floresta = pygame.transform.scale(floresta,(length,height))

cidade = pygame.image.load("background_images/Cenário Cidade3D.png")
cidade = pygame.transform.scale(cidade,(length,height))

deserto = pygame.image.load("background_images/Cenário Deserto3D.png")
deserto = pygame.transform.scale(deserto,(length,height))

""" POSIÇÃO COBRA """
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

""" IMPORTANDO MÚSICAS """
music = pygame.mixer.Sound("sounds/background_music.wav")
music.set_volume(0.2) # 0 até 1
 
score_sound = pygame.mixer.Sound("sounds/score.wav")
score_sound.set_volume(1) # 0 até 1

""" CRIANDO OS SPRITES GROUPS """
all_florest = pygame.sprite.Group()
all_city = pygame.sprite.Group()
all_desert = pygame.sprite.Group()
gp_maca = pygame.sprite.Group()
gp_lagartixa = pygame.sprite.Group()
gp_rato = pygame.sprite.Group()

""" AGRUPANDO COBRA_FLORESTA """
snake1 = Snake1()
all_florest.add(snake1)

""" AGRUPANDO COBRA_CIDADE """
snake2 = Snake2()
all_city.add(snake2)

""" AGRUPANDO COBRA_DESERTO """       
snake3 = Snake3()
all_desert.add(snake3)

""" AGRUPANDO MAÇÃ """
apple1 = Maca1()
all_florest.add(apple1)
all_city.add(apple1)
all_desert.add(apple1)
gp_maca.add(apple1)

""" AGRUPANDO LAGARTIXA """
gecko1 = Lagartixa1()
all_florest.add(gecko1)
all_city.add(gecko1)
all_desert.add(gecko1)
gp_lagartixa.add(gecko1)

""" AGRUPANDO RATO """
rat1 = Rato1()
all_florest.add(rat1)
all_city.add(rat1)
all_desert.add(rat1)
gp_rato.add(rat1)

""" AGRUPANDO ÁRVORES """
# Árvore 1
obstaculos_floresta = pygame.sprite.Group()
arvore1 = Arvore1()
all_florest.add(arvore1)
obstaculos_floresta.add(arvore1)

# Árvore 2
arvore2 = Arvore2()
all_florest.add(arvore2)
obstaculos_floresta.add(arvore2)
 
""" AGRUPANDO ARBUSTOS """
# Arbusto 1
arbusto1 = Arbusto1()
all_florest.add(arbusto1)
obstaculos_floresta.add(arbusto1)
 
# Arbusto 2 
arbusto2 = Arbusto2()
all_florest.add(arbusto2)
obstaculos_floresta.add(arbusto2)
 
# Arbusto 3 
arbusto3 = Arbusto3()
all_florest.add(arbusto3)
obstaculos_floresta.add(arbusto3)
 
# Arbusto 4 
arbusto4 = Arbusto4()
all_florest.add(arbusto4)
obstaculos_floresta.add(arbusto4)

# Arbusto 5 
arbusto5 = Arbusto5()
all_florest.add(arbusto5)
obstaculos_floresta.add(arbusto5)
 
# Arbusto 6 
arbusto6 = Arbusto6()
all_florest.add(arbusto6)
obstaculos_floresta.add(arbusto6)
 
# Arbusto 7 
arbusto7 = Arbusto7()
all_florest.add(arbusto7)
obstaculos_floresta.add(arbusto7)
 
# Arbusto 8 
arbusto8 = Arbusto8()
all_florest.add(arbusto8)
obstaculos_floresta.add(arbusto8)
 
# Arbusto 9 
arbusto9 = Arbusto9()
all_florest.add(arbusto9)
obstaculos_floresta.add(arbusto9)
 
# Arbusto 10 
arbusto10 = Arbusto10()
all_florest.add(arbusto10)
obstaculos_floresta.add(arbusto10)
 
# Arbusto 11 
arbusto11 = Arbusto11()
all_florest.add(arbusto11)
obstaculos_floresta.add(arbusto11)

# Arbusto 12 
arbusto12 = Arbusto12()
all_florest.add(arbusto12)
obstaculos_floresta.add(arbusto12)
 
# Arbusto 13 
arbusto13 = Arbusto13()
all_florest.add(arbusto13)
obstaculos_floresta.add(arbusto13)

# Arbusto 14 
arbusto14 = Arbusto14()
all_florest.add(arbusto14)
obstaculos_floresta.add(arbusto14)

# Arbusto 15 
arbusto15 = Arbusto15()
all_florest.add(arbusto15)
obstaculos_floresta.add(arbusto15)
 
# Arbusto 16 
arbusto16 = Arbusto16()
all_florest.add(arbusto16)
obstaculos_floresta.add(arbusto16)

# Arbusto 17 
arbusto17 = Arbusto17()
all_florest.add(arbusto17)
obstaculos_floresta.add(arbusto17)

# Arbusto 18 
arbusto18 = Arbusto18()
all_florest.add(arbusto18)
obstaculos_floresta.add(arbusto18)

# Arbusto 19 
arbusto19 = Arbusto19()
all_florest.add(arbusto19)
obstaculos_floresta.add(arbusto19)
 
# Arbusto 20 
arbusto20 = Arbusto20()
all_florest.add(arbusto20)
obstaculos_floresta.add(arbusto20)
 
""" AGRUPANDO PÁSSAROS """
# Pássaro 2
bird2 = Bird2()
all_florest.add(bird2)
obstaculos_floresta.add(bird2)
 
# Pássaro 1
bird1 = Bird1()
all_florest.add(bird1)
obstaculos_floresta.add(bird1)

""" AGRUPANDO CARROS """
#Carro 1 
obstaculos_cidade = pygame.sprite.Group()
car1 = Carro1()
all_city.add(car1)
obstaculos_cidade.add(car1)

#Carro 2
car2 = Carro2()
all_city.add(car2)
obstaculos_cidade.add(car2)

""" AGRUPANDO PESSOA E GATO """
people = People()
all_city.add(people)
obstaculos_cidade.add(people)
 
gato = Gato()
all_city.add(gato)
obstaculos_cidade.add(gato)

""" AGRUPANDO CACTO """
#Cacto 1       
obstaculos_deserto = pygame.sprite.Group()
cacto1 = Cacto1()
all_desert.add(cacto1)
obstaculos_deserto.add(cacto1)

#Cacto 11       
cacto11 = Cacto11()
all_desert.add(cacto11)
obstaculos_deserto.add(cacto11)

#Cacto 12        
cacto12 = Cacto12()
all_desert.add(cacto12)
obstaculos_deserto.add(cacto12)
 
#Cacto 13        
cacto13 = Cacto13()
all_desert.add(cacto13)
obstaculos_deserto.add(cacto13)
 
#Cacto 2        
cacto2 = Cacto2()
all_desert.add(cacto2)
obstaculos_deserto.add(cacto2)
 
#Cacto 21        
cacto21 = Cacto21()
all_desert.add(cacto21)
obstaculos_deserto.add(cacto21)
 
#Cacto 22        
cacto22 = Cacto22()
all_desert.add(cacto22)
obstaculos_deserto.add(cacto22)
 
#Cacto 23        
cacto23 = Cacto23()
all_desert.add(cacto23)
obstaculos_deserto.add(cacto23)
 
#Cacto 24        
cacto24 = Cacto24()
all_desert.add(cacto24)
obstaculos_deserto.add(cacto24)
 
#Cacto 25        
cacto25 = Cacto25()
all_desert.add(cacto25)
obstaculos_deserto.add(cacto25)

#Cacto 26
cacto26 = Cacto26()
all_desert.add(cacto26)
obstaculos_deserto.add(cacto26)

#Cacto 27
cacto27 = Cacto27()
all_desert.add(cacto27)
obstaculos_deserto.add(cacto27)

#Cacto 28
cacto28 = Cacto28()
all_desert.add(cacto28)
obstaculos_deserto.add(cacto28)

#Cacto 29
cacto29 = Cacto29()
all_desert.add(cacto29)
obstaculos_deserto.add(cacto29)

#Cacto 30
cacto30 = Cacto30()
all_desert.add(cacto30)
obstaculos_deserto.add(cacto30)

#Cacto 31
cacto31 = Cacto31()
all_desert.add(cacto31)
obstaculos_deserto.add(cacto31)

#Cacto 32
cacto32 = Cacto32()
all_desert.add(cacto32)
obstaculos_deserto.add(cacto32)

#Cacto 33
cacto33 = Cacto33()
all_desert.add(cacto33)
obstaculos_deserto.add(cacto33)

#Cacto 34
cacto34 = Cacto34()
all_desert.add(cacto34)
obstaculos_deserto.add(cacto34)

#Cacto 35
cacto35 = Cacto35()
all_desert.add(cacto35)
obstaculos_deserto.add(cacto35)

#Cacto 36
cacto36 = Cacto36()
all_desert.add(cacto36)
obstaculos_deserto.add(cacto36)

#Cacto 37
cacto37 = Cacto37()
all_desert.add(cacto37)
obstaculos_deserto.add(cacto37)

#Cacto 38
cacto38 = Cacto38()
all_desert.add(cacto38)
obstaculos_deserto.add(cacto38)

#Cacto 39
cacto39 = Cacto39()
all_desert.add(cacto39)
obstaculos_deserto.add(cacto39)

""" AGRUPANDO ESCORPIÃO"""
#Escorpião 1   
escorpiao1 = Escorpiao1()
all_desert.add(escorpiao1)
obstaculos_deserto.add(escorpiao1)
 
#Escorpião 2    
escorpiao2 = Escorpiao2()
all_desert.add(escorpiao2)
obstaculos_deserto.add(escorpiao2)

#Escorpião 3    
escorpiao3 = Escorpiao3()
all_desert.add(escorpiao3)
obstaculos_deserto.add(escorpiao3)

#Escorpião 4    
escorpiao4 = Escorpiao4()
all_desert.add(escorpiao4)
obstaculos_deserto.add(escorpiao4)

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

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)
                                                
                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                        
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True                                            

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(5)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

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

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT
                                            
                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True                                            

                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(10)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

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

                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake1.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake1.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake1.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake1.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake1.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake1.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake1.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake1.left()
                                                                #x -= 20 #LEFT
                                            
                                                    obstacle_collides1 = pygame.sprite.spritecollide(snake1,obstaculos_floresta,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake1,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake1,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake1,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides1:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake1.rect.topleft = 700,120
                                                                score = 0

                                                                gamescreen.blit(floresta,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_florest.draw(gamescreen)
                                                                all_florest.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                    
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake1.rect.topleft = 700,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(floresta, (0,0))
                                                        all_florest.draw(gamescreen)
                                                        all_florest.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO CIDADE """
                                            if x > 495 and y > 360 and x < 725 and y < 440:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake2.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake2.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake2.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake2.left()

                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake2.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake2.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake2.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake2.left()
                                                                #x -= 20 #LEFT

                                                    obstacle_collides2 = pygame.sprite.spritecollide(snake2,obstaculos_cidade,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake2,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake2,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake2,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides2:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)
                                                                
                                                                OFF = True
                                                                snake2.rect.topleft = 565,0
                                                                score = 0

                                                                gamescreen.blit(cidade,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_city.draw(gamescreen)
                                                                all_city.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake2.rect.topleft = 565,0
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(cidade, (0,0))
                                                        all_city.draw(gamescreen)
                                                        all_city.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()

                                            """ BOTÃO DESERTO """
                                            if x > 495 and y > 490 and x < 725 and y < 570:
                                                
                                                music.play(-1) # -1 Para que recomece a música após o término.
                                                music.set_volume(0.2)

                                                """ LOOP DO JOGO """
                                                while OFF:
                                                    time.tick(15)
                                                    gamescreen.fill(white)
                                                    text9 = f"Score: {score}"
                                                    ftext9 = textfont1.render(text9, True, white)

                                                    for choice in pygame.event.get():
                                                        if choice.type == QUIT:
                                                            OFF = False
                                                            game_scenery = False
                                                            game_mode = False
                                                            play_screen = False
                                                        
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == pygame.K_UP:
                                                                snake3.up()
                                                            if choice.key == pygame.K_DOWN:
                                                                snake3.down()
                                                            if choice.key == pygame.K_RIGHT:
                                                                snake3.right()
                                                            if choice.key == pygame.K_LEFT:
                                                                snake3.left()
                                                
                                                        if choice.type == KEYDOWN:
                                                            if choice.key == K_w:
                                                                snake3.up()
                                                                #y -= 20 #UP
                                                            if choice.key == K_s:
                                                                snake3.down()
                                                                #y += 20 #DOWN
                                                            if choice.key == K_d:
                                                                snake3.right()
                                                                #x += 20 #RIGHT
                                                            if choice.key == K_a:
                                                                snake3.left()
                                                                #x -= 20 #LEFT
                                                
                                                    obstacle_collides3 = pygame.sprite.spritecollide(snake3,obstaculos_deserto,False)
                                                    apple_collides = pygame.sprite.spritecollide(snake3,gp_maca,False)
                                                    gecko_collides = pygame.sprite.spritecollide(snake3,gp_lagartixa,False)
                                                    rat_collides = pygame.sprite.spritecollide(snake3,gp_rato,False)

                                                    if apple_collides:
                                                        score_sound.play()
                                                        score += 2 
                                                        apple1.rect.x = randrange(320,950,50)
                                                        apple1.rect.y = randrange(120,440,50)

                                                    if gecko_collides:
                                                        score_sound.play()
                                                        score += 5
                                                        gecko1.rect.x = randrange(320,950,50)
                                                        gecko1.rect.y = randrange(120,440,50)
                                                            
                                                    if rat_collides:
                                                        score_sound.play()
                                                        score += 10
                                                        rat1.rect.x = randrange(320,950,50)
                                                        rat1.rect.y = randrange(120,440,50)

                                                    if obstacle_collides3:
                                                        """ LOOP DO GAME OVER """
                                                        music.set_volume(0)

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
                                                                music.set_volume(0.2)

                                                                OFF = True
                                                                snake3.rect.topleft = 650,120
                                                                score = 0

                                                                gamescreen.blit(deserto,(0,0)) # 7° Posicionar a imagem na tela do jogo. 
                                                                all_desert.draw(gamescreen)
                                                                all_desert.update()
                                                                gamescreen.blit(ftext9, (70,30))
                                                                
                                                                pygame.display.flip()

                                                            """ BOTÃO MENU """
                                                            if x > 690 and y > 290 and x < 920 and y < 370:
                                                                snake3.rect.topleft = 650,120
                                                                OFF = False
                                                                game_scenery = False
                                                                game_mode = True
                                                                    
                                                        pygame.display.update()

                                                    else:
                                                        gamescreen.blit(deserto, (0,0))
                                                        all_desert.draw(gamescreen)
                                                        all_desert.update()
                                                        pygame.draw.rect(gamescreen, (blue), (50,15,230,70))
                                                        gamescreen.blit(ftext9, (70,30))
                                                    
                                                        pygame.display.flip()
                    
                                    pygame.display.update()
                    
                    pygame.display.update()

    time.tick(0.5) # FPS
    pygame.display.update()

""" FINALIZAR JOGO """
pygame.quit()
quit()

'''if snake2.rect.x == 0:
    snake2.rect.x = length - 100
    if snake2.rect.y == 0:
        snake2.rect.y = height - 100
    if snake2.rect.x > length:
        snake2.rect.x = 0
    if snake2.rect.y > height:
        snake2.rect.y = 0'''