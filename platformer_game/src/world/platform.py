import pygame
from pygame.sprite import Sprite
from settings import BLUE, GROUND_TEXTURE, PLATFORM_TEXTURE


class Platform(Sprite):
    def __init__(self, x, y, width, height, group=None, is_hole=False):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_hole = is_hole
        self.width = width
        self.height = height

        # Загружаем текстуры только один раз при первом создании платформы
        if not hasattr(Platform, 'ground_texture'):
            Platform.ground_texture = pygame.image.load(GROUND_TEXTURE).convert_alpha()
            Platform.platform_texture = pygame.image.load(PLATFORM_TEXTURE).convert_alpha()

        if not is_hole:
            self.apply_texture()

        if group is not None:
            group.add(self)

    def apply_texture(self):
        """Накладывает текстуру на платформу"""
        if self.height > 30:  # Если это земля (толстая платформа)
            texture = Platform.ground_texture
        else:  # Если это воздушная платформа
            texture = Platform.platform_texture

        # Масштабируем текстуру под высоту платформы
        texture_height = texture.get_height()
        scale_factor = self.height / texture_height
        scaled_width = int(texture.get_width() * scale_factor)
        scaled_texture = pygame.transform.scale(texture, (scaled_width, self.height))

        # Заполняем поверхность повторяющейся текстурой
        for x_pos in range(0, self.width, scaled_width):
            self.image.blit(scaled_texture, (x_pos, 0))