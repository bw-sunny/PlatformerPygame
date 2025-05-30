import pygame
from pygame.sprite import Sprite

class SpeedPotion(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_x = x
        self.original_y = y
        self.active = True
        self.load_image()
        self.new_speed = 7
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_image(self):
        try:
            self.image = pygame.image.load(
                "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/items/blue_portal.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
        except:
            self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
            self.image.fill((0, 255, 0))


    def reset(self):
        self.active = True
        self.load_image()
        self.rect.x = self.original_x
        self.rect.y = self.original_y
        print(f"Зелье восстановлено на ({self.original_x}, {self.original_y})")