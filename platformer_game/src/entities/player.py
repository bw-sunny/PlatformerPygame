import pygame
from pygame.sprite import Sprite
from settings import GRAVITY, WHITE

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.original_image = pygame.image.load(
                "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/sprites/player.png"
            ).convert_alpha()
            self.image = self.original_image
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
            self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.on_ground = False
        self.base_speed = 5
        self.speed = self.base_speed
        self.has_speed_boost = False
        self.pass_through = False
        self.pass_through_timer = 0
        self.alpha = 255

    def apply_speed_boost(self, new_speed):
        self.speed = new_speed
        self.has_speed_boost = True

    def update(self, platforms, holes, potions):
        if self.pass_through:
            self.pass_through_timer -= 1
            if self.pass_through_timer <= 0:
                self.pass_through = False
                self.alpha = 255
            else:
                self.alpha = 128
        else:
            self.alpha = 255

        if hasattr(self, 'original_image'):
            self.image = self.original_image.copy()
            self.image.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        self.process_collisions(platforms, holes, potions)

    def process_collisions(self, platforms, holes, potions):
        self.on_ground = False
        platform_hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in platform_hits:
            if self.velocity_y < 0 and not self.pass_through:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                    self.pass_through = True
                    self.pass_through_timer = 10
                    continue
            elif self.velocity_y > 0 and not self.pass_through:
                self.rect.bottom = platform.rect.top
                self.on_ground = True
                self.velocity_y = 0

        if potions:
            potion_hits = pygame.sprite.spritecollide(self, potions, False)
            for potion in potion_hits:
                if potion.active and not self.has_speed_boost:
                    self.apply_speed_boost(potion.new_speed)
                    print("Игрок получил ускорение!")

        if holes:
            hole_hits = pygame.sprite.spritecollide(self, holes, False)
            if hole_hits:
                self.reset_position()

        if potions and not self.has_speed_boost:
            potion_hits = pygame.sprite.spritecollide(self, potions, True)
            for potion in potion_hits:
                if hasattr(potion, 'new_speed'):
                    self.apply_speed_boost(potion.new_speed)

    def move(self, dx):
        if 0 <= self.rect.x <= 3970:
            self.rect.x += dx * self.speed
        elif self.rect.x < 0:
            self.rect.x += 10
        elif self.rect.x > 3970:
            self.rect.x -= 10

    def jump(self):
        if self.on_ground:
            self.velocity_y = -12
            self.pass_through = False

    def reset_position(self, potions_group=None):
        """Сброс позиции игрока с опциональным восстановлением зелий"""
        self.rect.x = 100
        self.rect.y = 300
        self.velocity_y = 0
        self.speed = self.base_speed
        self.has_speed_boost = False
        self.pass_through = False
        self.alpha = 255
