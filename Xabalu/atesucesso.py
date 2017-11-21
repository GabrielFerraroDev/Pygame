# importa a biblioteca pygame
import pygame
import os
import math
import random
import sys

# FUNÇÕES PARA O ALIEN
def criar_alien():
    pontos = [[1, 0], [-1, 0], [-0.7, 0],
            [-0.5, 0.4], [0.5, 0.4],
            [0.7, 0],
            [0.5, -0.4], [-0.5, -0.4],
            [-0.7, 0]]
    escala = 16
    return { 'x': largura_tela, 
             'y': random.randint(20,altura_tela-20), 
             'pontos': pontos, 
             'escala': escala,
             'largura': 2*escala,
             'altura': escala}

def atualizar_avanco_alien():
    if alien != None:
        alien['x'] -= 8

def tiro_acertou_alien(tiro):
    if tiro['x'] >= alien['x'] and tiro['x'] < alien['x'] + alien['largura']:
        if tiro['y'] >= alien['y'] and tiro['y'] < alien['y'] + alien['altura']:
            return True
    return False
        
def desenhar_alien_na_tela():
    if alien != None:
        pontos_abs = []
        for ponto_rel in alien['pontos']:
            ponto_abs = (alien['x'] + alien['escala']*ponto_rel[0], 
                         alien['y'] + alien['escala']*ponto_rel[1])
            pontos_abs.append(ponto_abs)
        pygame.draw.polygon(screen, (255,255,0), pontos_abs, 2)
        
# FUNÇÕES PARA ASTERÓIDES
def deve_criar_novo_asteroide():
    if len(asteroides) < 20:
        return True
    return False

def criar_asteroide():
    escala = random.randint(5,50)
    numero_pontos = random.randint(5, 10)
    pontos = []
    for i in range(numero_pontos):
        angulo = i * 360 / numero_pontos + random.randint(-20, 20)
        distancia = random.random() / 4.0 + 0.75
        pontos.append([distancia * math.cos(angulo * math.pi/180), 
                       distancia * math.sin(angulo * math.pi/180)])

    angulo_deslocamento = random.randint(0,359)
    if angulo_deslocamento < 45 or angulo_deslocamento >= 315:
        x = 0
        y = random.randint(0,altura_tela-1)
    elif angulo_deslocamento >= 45 and angulo_deslocamento < 135:
        y = altura_tela - 1
        x = random.randint(0,largura_tela-1)
    elif angulo_deslocamento >=135 and angulo_deslocamento < 225:
        x = largura_tela - 1
        y = random.randint(0,altura_tela-1)
    else:
        y = 0
        x = random.randint(0,largura_tela-1)
        
    return {'x':x, 
            'y':y, 
            'escala':escala, 
            'pontos':pontos, 
            'deslocamento': 2, 
            'angulo_deslocamento': angulo_deslocamento}

def atualizar_avanco_asteroides():
    for asteroide in asteroides:
        asteroide['x'] += asteroide['deslocamento'] * math.cos(asteroide['angulo_deslocamento']*math.pi/180)
        asteroide['y'] -= asteroide['deslocamento'] * math.sin(asteroide['angulo_deslocamento']*math.pi/180)
        asteroide['x'] %= largura_tela
        asteroide['y'] %= altura_tela
        if asteroide['x'] < 0:
            asteroide['x'] = largura_tela - asteroide['x']
        if asteroide['y'] < 0:
            asteroide['y'] = altura_tela - asteroide['y']

def desenhar_asteroides_na_tela():
    for asteroide in asteroides:
        pontos_abs = []
        for ponto_rel in asteroide['pontos']:
            ponto_abs = (asteroide['x'] + asteroide['escala']*ponto_rel[0], 
                         asteroide['y'] + asteroide['escala']*ponto_rel[1])
            pontos_abs.append(ponto_abs)
        pygame.draw.polygon(screen, (255,255,255), pontos_abs, 2)

# FUNÇÕES PARA OS TIROS
def criar_tiro(atraso):
    return { 'x':nave['x'], 
             'y':nave['y'], 
             'angulo':nave['angulo'], 
             'atraso':atraso }

def atualizar_tiros():
    for tiro in tiros:
        if tiro['atraso'] >= 0:
            # decrementar atraso dos tiro
            tiro['atraso'] -= 1
        
        if tiro['atraso'] == 0:
            tiro['x'] = nave['x'] + 0.5 * largura_imagem_nave * math.cos(nave['angulo'] * math.pi/180)
            tiro['y'] = nave['y'] - 0.5 * largura_imagem_nave * math.sin(nave['angulo'] * math.pi/180)
            tiro['angulo'] = nave['angulo']
        elif tiro['atraso'] < 0:
            tiro['x'] += deslocamento_tiros * math.cos(tiro['angulo'] * math.pi/180)
            tiro['y'] -= deslocamento_tiros * math.sin(tiro['angulo'] * math.pi/180)
            if tiro['x'] > largura_tela or tiro['x'] < 0 or tiro['y'] > altura_tela or tiro['y'] < 0:
                tiros.remove(tiro)

def desenhar_tiros_na_tela():
    for tiro in tiros:
        if tiro['atraso'] <= 0:
            pygame.draw.circle(screen, (0,255,255), (int(tiro['x']),int(tiro['y'])), 2)

# FUNÇÕES PARA A NAVE
def criar_nave():
    return {'imagem':imagem_nave, 
        'x':x_nave_inicial, 
        'y':y_nave_inicial, 
        'angulo':angulo_nave_inicial,
        'deslocamento': 0,
        'angulo_deslocamento': 0 }

def girar_nave(delta):
    nave['angulo'] += delta
    nave['angulo'] %= 360

def atualizar_avanco_nave():
    nave['x'] += nave['deslocamento'] * math.cos(nave['angulo_deslocamento']*math.pi/180)
    nave['y'] -= nave['deslocamento'] * math.sin(nave['angulo_deslocamento']*math.pi/180)
    nave['x'] %= largura_tela
    nave['y'] %= altura_tela
    if nave['x'] < 0:
        nave['x'] = largura_tela - nave['x']
    if nave['y'] < 0:
        nave['y'] = altura_tela - nave['y']
    
def ativar_avanco_nave():
    if nave['deslocamento'] == 0:
        nave['deslocamento'] = 5
        nave['angulo_deslocamento'] = nave['angulo']

def desativar_avanco_nave():
    nave['deslocamento'] = 0    
    
def desenhar_nave_na_tela():
    imagem = nave['imagem']
    x_nave_centro = nave['x']
    y_nave_centro = nave['y']
    angulo = nave['angulo']
    
    # rotaciona a imagem
    imagem_rot = pygame.transform.rotate(imagem, angulo)
    
    # obtém as dimensões da imagem rotacionada
    largura_imagem_rot, altura_imagem_rot = imagem_rot.get_rect().size
    
    # calcula coordenadas x e y de forma que a imagem rotacionada fique no centro da tela
    x_nave_rect = int(x_nave_centro - largura_imagem_rot/2)
    y_nave_rect = int(y_nave_centro - altura_imagem_rot/2)
    
    screen.blit(imagem_rot, (x_nave_rect,y_nave_rect))  

    
# inicializa as módulos dessa biblioteca.
pygame.init()

# cria uma janela em modo gráfico; cria e devolve uma tela
largura_tela = 600
altura_tela = 400
screen = pygame.display.set_mode((largura_tela,altura_tela))

# define um título na janela.
pygame.display.set_caption("Exemplo 1")

folder = "img"                # subdiretorio onde a imagem se encontra

# os.path.join é o separador de diretórios (independente de SO) 
imagem_nave = pygame.image.load(os.path.join(folder, "nave.bmp"))

# obtém as dimensões da imagem da nave
largura_imagem_nave, altura_imagem_nave = imagem_nave.get_rect().size

# definição de uma cor da imagem para que fique transparente
imagem_nave.set_colorkey((255,255,255),1)

# definição de uma lista com as informações da nave
# coordenadas x e y do centro da nave
x_nave_inicial = int(largura_tela/2)
y_nave_inicial = int(altura_tela/2)
angulo_nave_inicial = 0

nave = criar_nave()

# número de graus que a nave será rotacionada a cada iteração
delta_angulo_nave = 3

tiros = []
deslocamento_tiros = 10

asteroides = []

sair = False

clock = pygame.time.Clock()

alien = None
alien_intervalo = 150
alien_timer = alien_intervalo

while not sair:
    

    for tiro in tiros:
        if alien != None:
            if tiro_acertou_alien(tiro):
                tiros.remove(tiro)
                alien = None
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        girar_nave(delta_angulo_nave)
    if keys[pygame.K_RIGHT]:
        girar_nave(-delta_angulo_nave)
    if keys[pygame.K_SPACE]:
        if len(tiros) == 0:
            for i in range(0,11,5):
                tiro = criar_tiro(i)
                tiros.append(tiro)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ativar_avanco_nave()
            if event.key == pygame.K_DOWN:
                desativar_avanco_nave()

    if alien == None:
        if alien_timer > 0:
            alien_timer -= 1
        else:
            alien = criar_alien()
            alien_timer = alien_intervalo
    else:
        if alien['x'] < 0:
            alien = None

    
    if deve_criar_novo_asteroide():
        asteroide = criar_asteroide()
        asteroides.append(asteroide);
        
    atualizar_avanco_nave()
    atualizar_avanco_alien()
    atualizar_tiros()
    atualizar_avanco_asteroides()
    
    # preenche o fundo da tela
    screen.fill((0,0,0))

    desenhar_nave_na_tela() 
    desenhar_tiros_na_tela()
    desenhar_asteroides_na_tela()
    desenhar_alien_na_tela()
    
    # mostra a tela
    pygame.display.flip() 

    # aguarda o tempo para gerar uma taxa de aproximadamente 30 quadros por segundo 
    clock.tick(30)

# finaliza o pygame e descarrega os recursos alocados
pygame.quit()

