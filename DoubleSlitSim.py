import pygame
import numpy as np
import random

L = 100.0
lam = 1.0
d = 1.0
a = 0.2

width, height = 800, 600

y_vals = np.arange(height) - height/2
pdf = (np.cos(np.pi * d * y_vals / (lam * L))**2) * (np.sinc(a * y_vals / (lam * L))**2)
pdf = pdf.clip(min=0)
cdf = np.cumsum(pdf)
cdf = cdf / cdf[-1]

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
pygame.display.set_caption("Interferência de Dupla Fenda")
clock = pygame.time.Clock()

dot = pygame.Surface((1, 1))
dot.fill((10, 10, 10))

photons_per_frame = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(photons_per_frame):
        r = random.random()
        index = np.searchsorted(cdf, r)
        y = index
        x = random.randrange(width)
        screen.blit(dot, (x, y), special_flags=pygame.BLEND_ADD)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
