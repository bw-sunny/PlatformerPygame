import pygame
from pygame.sprite import Sprite

class SpeedPotion(Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Загрузка текстуры зелья (путь должен быть правильным)
        original_image = pygame.image.load("/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/poison.png").convert_alpha()

        # Масштабируем до 32x32
        self.image = pygame.transform.scale(original_image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_boost = 2.0  # Во сколько раз увеличиваем скорость
        self.duration = 5.0     # Длительность эффекта в секундах