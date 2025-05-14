import pygame
import numpy as np
import random

# Parâmetros do experimento (unidades arbitrárias)
L = 100.0       # distância tela-fendas
lam = 1.0       # comprimento de onda
d = 1.0         # separação entre fendas
a = 0.2         # largura de cada fenda

# Tamanho da janela de visualização
width, height = 800, 600

# Pré-cálculo da distribuição de intensidade teórica
# Cria vetor y centrado; aqui, 1 pixel = 1 unidade de y
y_vals = np.arange(height) - height/2
# Calcula PDF proporcional a cos^2(...) * sinc^2(...)
pdf = (np.cos(np.pi * d * y_vals / (lam * L))**2) * ((np.sinc(a * y_vals / (lam * L)))**2)
# Normaliza PDF para obter distribuição de probabilidade
pdf = pdf.clip(min=0)  # garante não-negatividade
cdf = np.cumsum(pdf)
cdf = cdf / cdf[-1]    # normalização final

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
pygame.display.set_caption("Interferência de Dupla Fenda")
clock = pygame.time.Clock()

# Cria um pequeno pixel branco transparente para acumular brilho
dot = pygame.Surface((1, 1))
dot.fill((10, 10, 10))  # cada ponto adiciona +10 em cada canal RGB

# Parâmetro de controle de taxa de fótons por frame
photons_per_frame = 100  # aproximadamente 6000 fótons/segundo a 60 fps

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lança vários fótons por frame
    for _ in range(photons_per_frame):
        # Amostragem inversa da CDF para obter posição vertical y
        r = random.random()
        index = np.searchsorted(cdf, r)
        y = index
        # Escolhe posição horizontal aleatória (padrão uniforme em x)
        x = random.randrange(width)
        # Desenha o ponto na tela (soma valores RGB por BLEND_ADD)
        screen.blit(dot, (x, y), special_flags=pygame.BLEND_ADD)

    # Atualiza a tela e regula FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
