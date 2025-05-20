# src/simple_game/tests/conftest.py

import pygame
import pytest


@pytest.fixture(autouse=True)
def sdl_dummy(monkeypatch):
    # ヘッドレス環境用にダミーSDLドライバを指定
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")
    # pygameのディスプレイだけ初期化
    pygame.display.init()
    yield
    # テスト後に表示をクリーンアップ
    pygame.display.quit()
