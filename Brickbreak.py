import pygame
import sys
import time

pygame.init()

screen_width = 1200
screen_height = 650


screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Brick Breaker")


tamanho_bola = 20
bola = pygame.Rect(390, 320, tamanho_bola, tamanho_bola)
bola_velocidade = [4, 4]


tamanho_jogador = 100
jogador = pygame.Rect(350, 585, tamanho_jogador, 15)
jogador_velocidade = 7


def criar_blocos():
    blocos = []
    linha_blocos = 10
    coluna_blocos = 17
    largura_bloco = 60
    altura_bloco = 20
    espaco_bloco = 10
    
    for linha in range(linha_blocos):
        for coluna in range(coluna_blocos):
            x = coluna * (largura_bloco + espaco_bloco) + espaco_bloco
            y = linha * (altura_bloco + espaco_bloco) + espaco_bloco
            bloco = pygame.Rect(x, y, largura_bloco, altura_bloco)
            blocos.append(bloco)
    
    return blocos

blocos = criar_blocos()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(1/85)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jogador.left > 0:
        jogador.move_ip(-jogador_velocidade, 0)
    if keys[pygame.K_RIGHT] and jogador.right < screen_width:
        jogador.move_ip(jogador_velocidade, 0)

   
    bola.move_ip(bola_velocidade)

    if bola.left <= 0 or bola.right >= screen_width:
        bola_velocidade[0] = -bola_velocidade[0]
    if bola.top <= 0:
        bola_velocidade[1] = -bola_velocidade[1]
    if bola.bottom >= screen_height:
        print("Game Over")
        pygame.quit()
        sys.exit()

  
    if bola.colliderect(jogador):
        bola_velocidade[1] = -bola_velocidade[1]

    
    for bloco in blocos[:]:
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            bola_velocidade[1] = -bola_velocidade[1]
            break

    
    screen.fill((0, 0, 0))

  
    pygame.draw.rect(screen, (255, 255, 255), bola)


    pygame.draw.rect(screen, (255, 0, 0), jogador)

    
    for bloco in blocos:
        pygame.draw.rect(screen, (0, 0, 255), bloco)

   
    pygame.display.flip()

pygame.quit()

