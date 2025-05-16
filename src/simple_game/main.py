import pygame
from game.player import Player
from game.settings import HEIGHT, WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

player = Player()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
pygame.quit()
