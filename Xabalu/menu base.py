
import pygame
import sys



pygame.init()

def menu(estado):
    #Criação
    tela = pygame.display.set_mode((600,400),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None, 64)
    fonte2 = pygame.font.Font(None, 40)
    titulo = fonte1.render("Asteroids",1,(255,255,255))
    F_new_game = fonte2.render("New Game",1,(255,255,255))
    F_ajuda = fonte2.render("Help",1,(255,255,255))
    F_sair = fonte2.render("Exit",1,(255,255,255))

    #Imagens
    imagem = pygame.image.load("background.jpg")
    fundo = pygame.transform.scale(imagem,(700,500))
    
    while estado:
        # x- Sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              # New Game
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 240 and x < 380) and (y > 130 and y < 155):
                        import Jogo
                        estado = False
            #Help
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 280 and x < 345) and (y > 170 and y < 200):
                        return "ajuda"
                        estado = False
               #Sair         
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 280 and x < 340) and (y > 205 and y < 240):
                        return "sair"
                        estado = False
        
        tela.blit(fundo,(0,0))
        tela.blit(titulo,(200,60))
        tela.blit(F_new_game,(240,130))
        tela.blit(F_ajuda,(280,170))
        tela.blit(F_sair,(280,215))
        pygame.display.flip()

def ajuda(estado):
    #Criação
    tela = pygame.display.set_mode((785,600),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None,30)
    voltar = fonte1.render("Voltar",1,(255,255,255))
    
    #Imagens
    imagem = pygame.image.load("ajuda.jpg")
    fundo = pygame.transform.scale(imagem,(800,600))
    
    while estado:
        # x - sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Sair
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 220 and x < 280) and (y > 300 and y < 320):
                        pygame.quit()
                        sys.exit()
             #Menu
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 550 and x < 620) and (y > 550 and y < 600):
                        return "menu"
                        estado = False
                        
        tela.blit(fundo,(0,0))
        tela.blit(voltar,(560,550))
        pygame.display.flip()
def jogo(estado):
   
    #Criação
    tela = pygame.display.set_mode((600,400),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None, 20)
    voltar = fonte1.render("Voltar",1,(255,255,255))
    
    #Imagens
    imagem = pygame.image.load("ajuda.jpg")
    fundo = pygame.transform.scale(imagem,(600,600))
    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
        tela.fill((0,0,0))
        pygame.display.flip()
        
porta = "menu"

while porta == "menu":
    porta = menu(True)
    if porta == "sair":
        pygame.quit()
        sys.exit()
    while porta == "ajuda":
        porta = ajuda(True)
    while porta == "jogo":
        porta = jogo(True)
