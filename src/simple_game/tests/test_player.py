import pygame

from simple_game.game.player import Player

# ─── ここにダミーキーオブジェクトを定義 ───


class DummyKeys:
    def __init__(self, pressed_keys):
        # pressed_keys: set of pygame のキー定数
        self.pressed = pressed_keys

    def __getitem__(self, key):
        # key が押されていれば 1、そうでなければ 0 を返す
        return 1 if key in self.pressed else 0

# ─────────────────────────────────────────


def test_player_initial_position():
    player = Player()
    assert (player.rect.x, player.rect.y) == (100, 100)


def test_player_moves_right(monkeypatch):
    # 右キーのみ押された状態をシミュレート
    dummy = DummyKeys({pygame.K_RIGHT})
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: dummy)

    player = Player()
    player.update()
    assert player.rect.x == 100 + player.speed


def test_player_clamp(monkeypatch):
    # 左上キーを押しっぱなしで何度か update しておく
    dummy = DummyKeys({pygame.K_LEFT, pygame.K_UP})
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: dummy)

    player = Player()
    for _ in range(50):
        player.update()

    # clamp によって画面外に出ない
    assert player.rect.x >= 0
    assert player.rect.y >= 0
    assert player.rect.y >= 0
