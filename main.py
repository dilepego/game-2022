import random

pers_x = random.randint (50,400)
pers_y = random.randint (100, 350)

pers_vel_x = 15
pers_vel_y = 15

vidas = 3

def respawn_c():
  x = 290
  y = -70
  return[x,y]
      


def respawn_d():
 x = 680
 y = 170
 return[x,y]

def respawn_e():
  x = -50
  y = 170
  return[x,y]
  

import pygame

largura = 640
altura = 480

pygame.init()

# font = pygame.font.sysfont('verdana, 50')

screen = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('overtaker')

personagem = pygame.image.load('scarlet.png').convert_alpha()

self = pygame.image.load('scarlet.png').convert_alpha()

imagem = pygame.image.load('pressione_espaço.png')

imagem_1 = pygame.image.load('tela_inicial.png')

geo_1 = pygame.image.load('tile020.png').convert_alpha()
geo_2 = pygame.image.load('tile047.png').convert_alpha()
geo_3 = pygame.image.load('tile500.png').convert_alpha()

geo_1 = pygame.transform.scale(geo_1,(60,60))
geo_2 = pygame.transform.scale(geo_2,(80,75))
geo_3 = pygame.transform.scale(geo_3,(80,75))

geo1_x = 290
geo1_y = 0

geo2_x = 600
geo2_y = 170

geo3_x = 0
geo3_y = 170

cristal_x = 255
cristal_y = 170


gameloop = True
no_menu = True
no_jogo = False



def draw():
    screen.fill((34, 28, 36))

#pintar a tela

clock = pygame.time.Clock()
delta_de_tempo = clock.tick(30)

while gameloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
             no_menu = True
             no_jogo = True 
          if event.key == pygame.K_UP and pers_y > 8:
            pers_y = pers_y - pers_vel_y
          if event.key == pygame.K_DOWN and pers_y < 310:
            pers_y = pers_y + pers_vel_y
          if event.key == pygame.K_LEFT and pers_x > 6:
            pers_x = pers_x - pers_vel_x
          if event.key == pygame.K_RIGHT and pers_x < 575:
            pers_x = pers_x + pers_vel_x
         
          #movimento
          geo1_y += random.randint(1,5)
          geo2_x -= random.randint(1,10)
          geo3_x += random.randint(1,10)
       

          
    if no_menu:
            screen.blit(imagem_1,(1,1))  
            screen.blit(imagem,(235, 240))
            #overtaker logo
    if no_jogo:
        imagem_2 = pygame.image.load("ultimochao.png").convert_alpha()
        imagem_2 = pygame.transform.scale(imagem_2,(largura,altura))
        screen.blit(imagem_2,(1,1))
      
        personagem = pygame.image.load('scarlet.png').convert_alpha()
        personagem = pygame.transform.scale(personagem,(60,55))
      
        personagem_rect = personagem.get_rect()
        personagem_rect.x = pers_x
        personagem_rect.y = pers_y
        screen.blit(personagem,personagem_rect)
      
        cristal = pygame.image.load('tile030.png').convert_alpha()
        cristal = pygame.transform.scale(cristal,(140,120))
        # cristal_rect = cristal.get_rect
        screen.blit(cristal,(255,140))

        geo1_rect = geo_1.get_rect()
        geo1_rect.x = geo1_x
        geo1_rect.y = geo1_y

        geo2_rect = geo_2.get_rect()
        geo2_rect.x = geo2_x
        geo2_rect.y = geo2_y

        geo3_rect = geo_3.get_rect()
        geo3_rect.x = geo3_x
        geo3_rect.y = geo3_y

        cristal_rect = cristal.get_rect()
        cristal_rect.x = cristal_x
        cristal_rect.y = cristal_y
      
        screen.blit(geo_1,geo1_rect)
        screen.blit(geo_2,(geo2_x,geo2_y))
        screen.blit(geo_3,(geo3_x,geo3_y))
      
        if personagem_rect.colliderect(geo1_rect):
          geo1_x = respawn_c()[0]
          geo1_y = respawn_c()[1]

        if personagem_rect.colliderect(geo2_rect):
          geo2_x = respawn_d()[0]
          geo2_y = respawn_d()[1]

        if personagem_rect.colliderect(geo3_rect):
          geo3_x = respawn_e()[0]
          geo3_y = respawn_e()[1]

        vidas = 9  
     
        if geo1_rect.colliderect(cristal_rect):
          vidas -= 3
          print (vidas)
          geo1_x = respawn_c()[0]
          geo1_y = respawn_c()[1]

        if geo2_rect.colliderect(cristal_rect):
          vidas -= 3
          print(vidas)
          geo2_x = respawn_d()[0]
          geo2_y = respawn_d()[1]

        if geo3_rect.colliderect(cristal_rect):
          vidas -= 3
          print(vidas)
          geo3_x = respawn_e()[0]
          geo3_y = respawn_e()[1]
          
        if vidas == 6:
          perdeu = pygame.image.load('game_over.png')
          screen.blit(perdeu,(10,50))
          gameloop = False

        # vidas_placar = font.render(f' vidas: {int(vidas)})',True , (255,255,255)
        # screen.blit(vidas_placar,(10,10))
          
  
    pygame.display.update() 