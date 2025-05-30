import pygame
from .platform import Platform
from settings import LEVELS
from .speed_potion import SpeedPotion
from .hint_arrow import HintArrow


class Level:
    def __init__(self, level_num=1):
        self.platforms = pygame.sprite.Group()
        self.holes = pygame.sprite.Group()
        self.potions = pygame.sprite.Group()
        self.hints = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()  # Добавляем эту строку
        self.level_width = 4000
        self.level_num = level_num
        self.initial_potions = []  # Создаем ключ

        self.load_level(level_num)

    def load_level(self, level_num):
        level_data = LEVELS.get(level_num, {})

        # Сохраняем исходные данные зелий
        self.initial_potions = level_data.get("speed_potions", [])

        # Очищаем группы
        self.platforms.empty()
        self.holes.empty()
        self.potions.empty()

        # Загрузка платформ и ям (прежний код)
        for x, y, width in level_data.get("ground", []):
            Platform(x, y, width, 50, self.platforms)

        for x, y, width in level_data.get("platforms", []):
            Platform(x, y, width, 20, self.platforms)

        for x, y, width in level_data.get("holes", []):
            Platform(x, y, width, 50, self.holes, is_hole=True)

        # Загружаем зелья
        self.spawn_potions()

        arrow = HintArrow(3730, 500)  # Координаты как в задании
        self.hints.add(arrow)

        # Невидимая платформа
        Platform(3700, 400, 100, 20, self.platforms, is_invisible=True)



    def spawn_potions(self):
        """Создает новые зелья на начальных позициях"""
        self.potions.empty()  # Полностью очищаем группу

        for x, y in self.initial_potions:
            potion = SpeedPotion(x, y)
            self.potions.add(potion)
            print(f"Создано новое зелье на ({x}, {y})")  # Отладочный вывод

    def reset_level(self):
        """Полный сброс уровня с восстановлением зелий"""
        self.spawn_potions()




    def reset_potions(self):
        """Полное восстановление всех зелий"""
        self.potions.empty()  # Очищаем группу

        # Создаем новые зелья
        for x, y in self.initial_potions:
            potion = SpeedPotion(x, y)
            self.potions.add(potion)
            print(f"Создано зелье на ({x}, {y})")
