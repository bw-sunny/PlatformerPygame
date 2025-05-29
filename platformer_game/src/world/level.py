import pygame
from .platform import Platform
from settings import LEVELS

class Level:
    def __init__(self, level_num=1):
        self.platforms = pygame.sprite.Group()
        self.holes = pygame.sprite.Group()  # Отдельная группа для ям
        self.level_width = 4000  # 3400 + 600 = 4000
        self.load_level(level_num)

    def load_level(self, level_num):
        level_data = LEVELS.get(level_num, {})

        # Загрузка земли (толщина 50px)
        for x, y, width in level_data.get("ground", []):
            Platform(x, y, width, 50, self.platforms)

        # Загрузка обычных видимых платформ (толщина 20px)
        for x, y, width in level_data.get("platforms", []):
            Platform(x, y, width, 20, self.platforms)

        # Загрузка ям (высота как у земли)
        for x, y, width in level_data.get("holes", []):
            Platform(x, y, width, 50, self.holes, is_hole=True)

        # Добавление специальной невидимой платформы (вручную)
        Platform(3700, 400, 100, 20, self.platforms, is_invisible=True)
