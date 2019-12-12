#coding: utf-8
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import time
from pygame.mixer import *

sounds = pygame.mixer
sounds.init()

s = sounds.Sound("audios/Beach.ogg")
arombado = sounds.Sound("audios/arombado.ogg")

pygame.init()
pygame.font.init()
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
screen = pygame.display.set_mode((1280, 720), 0, 32)
background_filename = 'imagens/floresta.jpg'
background = pygame.image.load(background_filename).convert()
arara = {
    'superficie': pygame.image.load('imagens/arara.png').convert_alpha(),
    'position': [620, 500],
    'velocidade': {
        'x': 0,
        'y': 0
        }
    }
pygame.display.set_caption('JOGO DA ARARA!')
clock = pygame.time.Clock()

def criar_dino():
    return {
        'superficie': pygame.image.load('imagens/dinossauro.png').convert_alpha(),
        'position': [randrange(1200), -35],
        'velocidade': randrange(20, 30)
        }
dinossauros = []
def mover_dino():
    for dinossauro in dinossauros:
        dinossauro['position'][1] += dinossauro['velocidade']
def remover_dino():
    for dinossauro in dinossauros:
        if dinossauro['position'][1] > 720:
            dinossauros.remove(dinossauro)
            dinossauros.append(criar_dino())
def get_rect(obj):
    return Rect(obj['position'] [0],
                obj['position'] [1],
                obj['superficie'].get_width(),
                obj['superficie'].get_height())
permissao = True
def arara_colisao():
    arara_rect = get_rect(arara)
    for dinossauro in dinossauros:
        if arara_rect.colliderect(get_rect(dinossauro)):
            dinossauros.remove(dinossauro)
            return True
            arombado.play()
    return False
collided = False
tempo1 = time.time()
contador = True
segundos = 0
s.play(-1)
a = False
recordereal = 0
primeiro_dino = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    tecla_pressionada = pygame.key.get_pressed()
    if tecla_pressionada[K_q]:
        exit()
    if tecla_pressionada[K_UP] or tecla_pressionada[K_w]:
        arara['superficie'] = pygame.image.load('imagens/arara_cima.png').convert_alpha()
        arara['velocidade'] ['y'] = -10
    elif tecla_pressionada[K_DOWN] or tecla_pressionada[K_s]:
        arara['superficie'] = pygame.image.load('imagens/arara_baixo.png').convert_alpha()
        arara['velocidade'] ['y'] = 10
    if tecla_pressionada[K_RIGHT] or tecla_pressionada[K_d]:
        arara['superficie'] = pygame.image.load('imagens/arara_direita.png').convert_alpha()
        arara['velocidade'] ['x'] = 10
    elif tecla_pressionada[K_LEFT] or tecla_pressionada[K_a]:
        arara['superficie'] = pygame.image.load('imagens/arara.png').convert_alpha()
        arara['velocidade'] ['x'] = -10
    screen.blit(background, (0, 0))
    if not collided:
            collided = arara_colisao()
            arara['position'] [0] = arara['position'] [0] + arara['velocidade'] ['x']
            arara['position'] [1] = arara['position'] [1] + arara['velocidade'] ['y']
            if (arara['position'] [0] > 1190):
                arara['position'] [0] = arara['position'] [0] - 11
            if (arara['position'] [0] < -30):
                arara['position'] [0] = arara['position'] [0] + 11
            if (arara['position'] [1] > 620):
                arara['position'] [1] = arara['position'] [1] - 11
            if (arara['position'] [1] < -20):
                arara['position'] [1] = arara['position'] [1] + 11
            screen.blit(arara['superficie'], arara['position'])
            msgr = game_font.render('Recorde: ', 1, (0, 0, 156))
            msgs = game_font.render('Tempo: ', 1, (0, 0, 156))
            segundos = round(segundos, 2)
            recorde = game_font.render(str(recordereal), 1, (0, 0, 0))
            segundosmsg = game_font.render(str(segundos), 1, (0, 0, 0))
            screen.blit(msgs, (880, 20))
            screen.blit(segundosmsg, (1100, 20))
            screen.blit(msgr, (850, 70))
            screen.blit(recorde, (1100, 70))
            if (permissao == True):
                mover_dino()
                for dinossauro in dinossauros:
                    screen.blit(dinossauro['superficie'], dinossauro['position'])
                remover_dino()
            tempo = time.time()
            segundos = tempo - tempo1
            if (segundos > recordereal):
                recordereal = segundos
                recordereal = round(recordereal, 2)
    else:
        segundos = 0
        permissao = False
        s.stop()
        if a == False:
            arombado.play()
            a = True
        texto = game_font.render('SEU INÚTIL! VOCE MATOU A ARARA...', 1, (255, 0, 0))
        texto3 = game_font.render('TEMPO DE SOBREVIVÊNCIA (s):', 1, (0, 0, 156))
        texto2 = game_font.render('Pressione Enter para continuar ou Q, para sair', 1, (255, 0, 0))
        texto4 = game_font.render('Recorde: ', 1, (0, 0, 156))
        screen.blit(texto4, (500, 500))
        screen.blit(recorde, (720, 500))
        screen.blit(texto, (235, 300))
        screen.blit(texto3, (20, 400))
        screen.blit(segundosmsg, (820, 400))
        screen.blit(texto2, (100, 600))
        collided = True
        if tecla_pressionada[K_RETURN]:
            a = False
            primeiro_dino = True
            arara['position'][0] = 650
            arara['position'][1] = 350
            s.play(-1)
            collided = False
            contador = True
            tempo1 = time.time()
    arara['velocidade'] = {
                            'x': 0,
                            'y': 0
                           }
    if (segundos > 1):
        if (primeiro_dino):
            dinossauros.append(criar_dino())
            primeiro_dino = False
        permissao = True
    pygame.display.update()
    time_passed = clock.tick(50)
