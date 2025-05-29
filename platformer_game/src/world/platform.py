import pygame
from pygame.sprite import Sprite
from settings import BLUE, GROUND_TEXTURE, PLATFORM_TEXTURE


class Platform(Sprite):
    # Статические переменные для текстур (загружаются один раз)
    ground_texture = None
    platform_texture = None

    def __init__(self, x, y, width, height, group=None, is_hole=False, is_invisible=False):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_hole = is_hole
        self.is_invisible = is_invisible
        self.width = width
        self.height = height

        # Загрузка текстур при первом создании платформы
        if Platform.ground_texture is None:
            Platform.ground_texture = pygame.image.load(GROUND_TEXTURE).convert_alpha()
            Platform.platform_texture = pygame.image.load(PLATFORM_TEXTURE).convert_alpha()

        if not is_hole and not is_invisible:
            self.apply_texture()
        elif is_invisible:
            # Полностью прозрачная платформа
            self.image.fill((0, 0, 0, 0))

        if group is not None:
            group.add(self)

    def apply_texture(self):
        """Применяет соответствующую текстуру к платформе"""
        if self.height > 30:  # Земля
            texture = Platform.ground_texture
        else:  # Воздушная платформа
            texture = Platform.platform_texture

        # Масштабирование текстуры
        texture_height = texture.get_height()
        scale_factor = self.height / texture_height
        scaled_width = int(texture.get_width() * scale_factor)
        scaled_texture = pygame.transform.scale(texture, (scaled_width, self.height))

        # Заполнение поверхности текстурой
        for x_pos in range(0, self.width, scaled_width):
            self.image.blit(scaled_texture, (x_pos, 0))