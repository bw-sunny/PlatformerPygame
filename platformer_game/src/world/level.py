import pygame
from .platform import Platform


class Level:
    def __init__(self, level_num=1):  # По умолчанию 1 уровень
        self.platforms = pygame.sprite.Group()
        self.level_width = 2000  # Фиксированная ширина для первого уровня
        self.load_level(level_num)

    def load_level(self, level_num):
        from settings import LEVELS
        level_data = LEVELS.get(level_num, {})

        # Основная земля
        for x, y, width in level_data.get("ground", []):
            Platform(x, y, width, 50, self.platforms)

        # Платформы в воздухе
        for x, y, width in level_data.get("platforms", []):
            Platform(x, y, width, 20, self.platforms)

        # Ямы (визуализация)
        for x, y, width in level_data.get("holes", []):
            Platform(x, y, width, 50, self.platforms, is_hole=True)