import pygame
from pygame.sprite import Sprite
import math


class Key(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_x = x
        self.original_y = y
        self.load_image()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def load_image(self):
        try:
            self.original_image = pygame.image.load(
                "assets/items/key.png"
            ).convert_alpha()
            self.image = self.original_image
        except:
            self.image = pygame.Surface((30, 15), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (255, 215, 0), (0, 0, 30, 15))

    def update(self):
        # Плавное покачивание
        self.angle = math.sin(pygame.time.get_ticks() * 0.003) * 15
        y_offset = math.sin(pygame.time.get_ticks() * 0.005) * 5

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(
            self.original_x,
            self.original_y + y_offset
        ))