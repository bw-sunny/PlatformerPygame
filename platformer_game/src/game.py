import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, BACKGROUND_IMAGE
from entities.player import Player
from world.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Best team in the world")
        self.clock = pygame.time.Clock()
        self.running = True

        # Инициализация уровня
        self.level = Level(1)
        self.platforms = self.level.platforms
        self.holes = self.level.holes
        self.potions = self.level.potions

        # Игрок
        self.player = Player(100, 300)

        # Группа всех спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(*self.platforms)
        self.all_sprites.add(*self.holes)
        self.all_sprites.add(*self.potions)
        self.all_sprites.add(*self.level.hints)

        # Камера
        self.camera_offset = pygame.math.Vector2(0, 0)

        # Фон
        self.original_bg = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
        self.bg_width = int(self.original_bg.get_width() * 0.42)
        self.bg_height = int(self.original_bg.get_height() * 0.56)
        self.background = pygame.transform.scale(
            self.original_bg,
            (self.bg_width, self.bg_height)
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.jump()
                if event.key == pygame.K_r:
                    self.reset_level()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.move(-1)
        if keys[pygame.K_d]:
            self.player.move(1)

    def reset_level(self):
        """Полный сброс уровня"""
        # Сбрасываем игрока
        self.player.rect.x = 100
        self.player.rect.y = 300
        self.camera_offset.x = 0
        self.player.speed = self.player.base_speed
        self.player.has_speed_boost = False

        # Восстанавливаем зелья
        self.level.reset_potions()
        print("Уровень сброшен, зелья восстановлены")

    def update(self):
        self.camera_offset.x = self.player.rect.centerx - SCREEN_WIDTH // 2
        self.camera_offset.x = max(0, min(self.camera_offset.x,
                                          self.level.level_width - SCREEN_WIDTH))
        self.player.update(self.platforms, self.holes, self.potions)

        if self.player.rect.top > SCREEN_HEIGHT:
            self.reset_level()
        self.level.hints.update()


    def render(self):
        self.screen.fill(BLACK)
        bg_x = (SCREEN_WIDTH - self.bg_width) // 2
        bg_y = (SCREEN_HEIGHT - self.bg_height) // 2
        self.screen.blit(self.background, (bg_x, bg_y))

        for sprite in self.all_sprites:
            self.screen.blit(
                sprite.image,
                (sprite.rect.x - self.camera_offset.x, sprite.rect.y)
            )

        font = pygame.font.SysFont(None, 30)
        debug_text = [
            f"Player pos: ({self.player.rect.x}, {abs(self.player.rect.y)})",
            f"Camera offset: {self.camera_offset.x}",
            f"Speed: {self.player.speed}"
        ]
        debug_text.append(f"Зельев: {len(self.level.potions)}")

        for i, text in enumerate(debug_text):
            text_surface = font.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 10 + i * 30))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

        pygame.quit()