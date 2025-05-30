import pygame
from pygame.sprite import Sprite
import math


class HintArrow(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_x = x
        self.original_y = y
        self.animation_offset = 0
        self.animation_speed = 0.01
        self.animation_range = 10

        try:
            self.original_image = pygame.image.load(
                "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/items/arrow_up.png"
            ).convert_alpha()
            self.image = self.original_image
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect(center=(x, y))
        except Exception as e:
            print(f"Ошибка загрузки изображения стрелки: {e}")
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, (255, 0, 0),
                                [(15, 0), (0, 30), (30, 30)])
            self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        # Плавное движение вверх-вниз с использованием синуса
        self.animation_offset = math.sin(pygame.time.get_ticks() * self.animation_speed) * self.animation_range
        self.rect.y = self.original_y + self.animation_offset