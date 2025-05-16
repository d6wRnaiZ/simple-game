import pygame

from simple_game.game.settings import HEIGHT, PLAYER_COLOR, PLAYER_SIZE, WIDTH


class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 画面外に出ないように制限
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)
