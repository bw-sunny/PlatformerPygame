import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, BACKGROUND_IMAGE
from entities.player import Player
from world.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True

        # Инициализация уровня
        self.level = Level(1)  # Только первый уровень
        self.platforms = self.level.platforms

        # Игрок
        self.player = Player(100, 300)
        self.all_sprites = pygame.sprite.Group(self.player, self.platforms)

        # Камера
        self.camera_offset = pygame.math.Vector2(0, 0)
        self.background = pygame.Surface((self.level.level_width, SCREEN_HEIGHT))
        self.background.fill((30, 30, 50))  # Темно-синий фон

        self.original_bg = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()

        # Рассчитываем новые размеры
        self.bg_width = int(self.original_bg.get_width() * 0.42)
        self.bg_height = int(self.original_bg.get_height() * 0.56)

        # Масштабируем
        self.background = pygame.transform.scale(
            self.original_bg,
            (self.bg_width, self.bg_height)
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_r:  # Рестарт
                    self.reset_level()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move(1)

    def update(self):
        # Камера следует за игроком
        self.camera_offset.x = self.player.rect.centerx - SCREEN_WIDTH // 2
        self.camera_offset.x = max(0, min(self.camera_offset.x,
                                          self.level.level_width - SCREEN_WIDTH))

        # Физика игрока
        self.player.update(self.platforms)
        # Падение за экран
        if self.player.rect.top > SCREEN_HEIGHT:
            self.reset_level()

    def reset_level(self):
        self.player.rect.x = 100
        self.player.rect.y = 300
        self.camera_offset.x = 0

    def render(self):
        self.screen.fill(BLACK)  # Фон подложка

        # Позиционируем по центру экрана
        bg_x = (SCREEN_WIDTH - self.bg_width) // 2
        bg_y = (SCREEN_HEIGHT - self.bg_height) // 2

        # Отрисовка фона
        self.screen.blit(self.background, (bg_x, bg_y))

        # Отрисовка игровых объектов (ваш код)
        for sprite in self.all_sprites:
            self.screen.blit(
                sprite.image,
                (sprite.rect.x - self.camera_offset.x, sprite.rect.y)
            )

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

        pygame.quit()