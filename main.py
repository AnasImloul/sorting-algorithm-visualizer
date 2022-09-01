import pygame
from Bars import Bars
from random import *
from sort import *


WIDTH = 800
HEIGHT = 600
FPS = 120

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
clock.tick(FPS)

array = choices(range(1, 1024), k=400)
bars = Bars(array, x=0, y=100, width=WIDTH, height=HEIGHT - 100, screen=screen)


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


count_sort(bars)
loop()
