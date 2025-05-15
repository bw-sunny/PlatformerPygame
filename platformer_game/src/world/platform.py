import pygame
from pygame.sprite import Sprite
from settings import BLUE, RED

class Platform(Sprite):
    def __init__(self, x, y, width, height, group, is_hole=False):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED if is_hole else BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_hole = is_hole
        if not is_hole:  # Ямы не добавляем в группу коллизий
            group.add(self)