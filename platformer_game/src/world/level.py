import pygame
from .platform import Platform
from settings import LEVELS


class Level:
    def __init__(self, level_num=1):  # По умолчанию 1 уровень
        self.platforms = pygame.sprite.Group()
        self.level_width = 2000  # Фиксированная ширина для первого уровня
        self.load_level(level_num)

    def load_level(self, level_num):
          # И другие зелья

        level_data = LEVELS.get(level_num, {})

        # Генерация земли
        for x, y, width in level_data.get("ground", []):
            Platform(x, y, width, 80, self.platforms)  # 5 параметров

        # Воздушные платформы
        for x, y, width in level_data.get("platforms", []):
            Platform(x, y, width, 20, self.platforms)  # 5 параметров

        # Ямы
        for x, y, width in level_data.get("holes", []):
            Platform(x, y, width, 50, self.platforms, is_hole=True)  # 6 параметров