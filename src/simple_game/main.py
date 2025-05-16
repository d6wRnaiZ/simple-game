# main.py
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
pygame.quit()
