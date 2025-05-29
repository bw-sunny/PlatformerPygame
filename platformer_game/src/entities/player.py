import pygame
from pygame.sprite import Sprite
from settings import GRAVITY, WHITE

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Загрузка спрайта (или заглушка)
        try:
            self.image = pygame.image.load("/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/sprites/player.png").convert_alpha()
        except:
            self.image = pygame.Surface((32, 32))
            self.image.fill('ffffff')  # Белый квадрат, если спрайт не найден

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.speed = 5  # Индивидуальная скорость игрока
        self.on_ground = False

    def update(self, platforms):
        # Гравитация
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Коллизии с платформами
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Падаем вниз
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                elif self.velocity_y < 0:  # Движемся вверх
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

    def move(self, dx):
        if 0 <= self.rect.x <= 1970:
            self.rect.x += dx * self.speed
        elif 0 > self.rect.x:
            self.rect.x += 10
        elif self.rect.x > 1970:
            self.rect.x -=10
        #print("x:",self.rect.x,"y:", self.rect.y)

    def jump(self):
        if self.on_ground:
            self.velocity_y = -12  # Сила прыжка

    def update(self, platforms):
        # Гравитация
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Проверка коллизий
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Падаем вниз
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0