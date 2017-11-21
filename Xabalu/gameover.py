import os
import pygame
import sys


pygame.init()

folder = "img"

arq = open('pontos.txt','r')

total = arq.readline()

 
def mostra(pnts):
    fonte1 = pygame.font.Font(None, 50)
    pontos = fonte1.render(str(pnts), 1, (255,255,255))
    tela.blit(pontos,(315,155))

#Criação
tela = pygame.display.set_mode((600,400),0,32)


#Imagens
imagem = pygame.image.load(os.path.join(folder, "Game Over.jpg"))
fundo = pygame.transform.scale(imagem,(600,400))

estado = True

while estado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
               x,y = pygame.mouse.get_pos()
               if (x > 170 and x < 440) and (y > 240 and y < 275):
                   import Jogo
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                x,y = pygame.mouse.get_pos()
                if (x > 240 and x < 370) and (y > 305 and y < 350):
                    import Menu

    tela.blit(fundo,(0,0))
    mostra(total)
    pygame.display.flip()

    
