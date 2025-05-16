import pygame
import pytest

from simple_game.game.player import Player
from simple_game.game.settings import HEIGHT, PLAYER_SIZE, WIDTH


@pytest.fixture(autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_player_init():
    p = Player()
    # Rect が生成され、サイズが PLAYER_SIZE になっている
    assert isinstance(p.rect, pygame.Rect)
    assert (p.rect.width, p.rect.height) == (PLAYER_SIZE, PLAYER_SIZE)


def test_player_clamp():
    p = Player()
    # 画面外に出す
    p.rect.x = WIDTH + 50
    p.rect.y = HEIGHT + 50
    p.update()
    # 端に収まっていること
    assert p.rect.right <= WIDTH
    assert p.rect.bottom <= HEIGHT
    assert p.rect.bottom <= HEIGHT
