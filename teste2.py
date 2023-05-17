import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações da tela
largura_tela = 800
altura_tela = 600
tamanho_celula = 10

# Criando a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tron')

# Função para desenhar a moto
def desenhar_moto(posicoes, cor):
    for posicao in posicoes:
        pygame.draw.rect(tela, cor, (posicao[0], posicao[1], tamanho_celula, tamanho_celula))

# Função principal do jogo
def jogar():
    # Posições iniciais das motos
    moto1_posicao = [(largura_tela / 2, altura_tela / 4)]
    moto2_posicao = [(largura_tela / 2, 3 * altura_tela / 4)]

    # Direção inicial das motos
    moto1_direcao = 'cima'
    moto2_direcao = 'baixo'

    # Velocidade das motos
    velocidade = tamanho_celula

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Jogador 1 controla com as teclas WASD
                if event.key == pygame.K_w and moto1_direcao != 'baixo':
                    moto1_direcao = 'cima'
                elif event.key == pygame.K_s and moto1_direcao != 'cima':
                    moto1_direcao = 'baixo'
                elif event.key == pygame.K_a and moto1_direcao != 'direita':
                    moto1_direcao = 'esquerda'
                elif event.key == pygame.K_d and moto1_direcao != 'esquerda':
                    moto1_direcao = 'direita'

                # Jogador 2 controla com as teclas de seta
                if event.key == pygame.K_UP and moto2_direcao != 'baixo':
                    moto2_direcao = 'cima'
                elif event.key == pygame.K_DOWN and moto2_direcao != 'cima':
                    moto2_direcao = 'baixo'
                elif event.key == pygame.K_LEFT and moto2_direcao != 'direita':
                    moto2_direcao = 'esquerda'
                elif event.key == pygame.K_RIGHT and moto2_direcao != 'esquerda':
                    moto2_direcao = 'direita'

        # Movimentação das motos
        if moto1_direcao == 'cima':
            nova_posicao = (moto1_posicao[0][0], moto1_posicao[0][1] - velocidade)
        elif moto1_direcao == 'baixo':
            nova_posicao = (moto1_posicao[0][0], moto1_posicao[0][1] + velocidade)
        elif moto1_direcao == 'esquerda':
            nova_posicao = (moto1_posicao[0][0] - velocidade, moto1_posicao[0][1])
        elif moto1_direcao == 'direita':
            nova_posicao = (moto1_posicao[0][0] + velocidade, moto1_posicao[0][1])

        moto1_posicao.insert(0, nova_posicao)

        if moto2_direcao == 'cima':
            nova_posicao = (moto2_posicao[0][0], moto2_posicao[0][1] - velocidade)
        elif moto2_direcao == 'baixo':
            nova_posicao = (moto2_posicao[0][0], moto2_posicao[0][1] + velocidade)
        elif moto2_direcao == 'esquerda':
            nova_posicao = (moto2_posicao[0][0] - velocidade, moto2_posicao[0][1])
        elif moto2_direcao == 'direita':
            nova_posicao = (moto2_posicao[0][0] + velocidade, moto2_posicao[0][1])

        moto2_posicao.insert(0, nova_posicao)

        # Verifica colisões com as bordas da tela
        if (moto1_posicao[0][0] < 0 or moto1_posicao[0][0] >= largura_tela or
                moto1_posicao[0][1] < 0 or moto1_posicao[0][1] >= altura_tela):
            pygame.quit()
            sys.exit()

        if (moto2_posicao[0][0] < 0 or moto2_posicao[0][0] >= largura_tela or
                moto2_posicao[0][1] < 0 or moto2_posicao[0][1] >= altura_tela):
            pygame.quit()
            sys.exit()

        # Verifica colisões com os rastros
        if moto1_posicao[0] in moto1_posicao[1:] or moto1_posicao[0] in moto2_posicao:
            pygame.quit()
            sys.exit()

        if moto2_posicao[0] in moto2_posicao[1:] or moto2_posicao[0] in moto1_posicao:
            pygame.quit()
            sys.exit()

        # Limpa a tela
        tela.fill(PRETO)

        # Desenha as motos
        desenhar_moto(moto1_posicao, VERMELHO)
        desenhar_moto(moto2_posicao, AZUL)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a velocidade do jogo
        pygame.time.Clock().tick(15)