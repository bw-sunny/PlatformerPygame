# Окно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

GRAVITY = 0.55

# Уровни
LEVELS = {
    1: {
        "ground": [
            (0, 550, 700),      # Первый участок земли (y=550)
            (1000, 550, 800),     # Второй участок
            (2600, 550, 1000),    # Третий участок
            (3500, 550, 600)      # Четвертый участок
        ],
        "platforms": [
            # Платформы над землей (y < 550)
            (200, 450, 100),     # Над первым участком
            (400, 350, 100),
            (600, 250, 200),
            (1400, 425, 150),    # Между первым и вторым участком
            (1850, 350, 150),
            (2200, 450, 100),
            (2500, 350, 150),    # Над третьим участком
            (3000, 400, 200),
            (3850, 280, 150)
        ],
        "speed_potions": [
            (550, 430),  # Над первой платформой (y=450-20)
        ],
        "holes": [
            (700, 550, 300),  # Яма между первым и вторым участком
            (1800, 550, 800)   # Яма между вторым и третьим участком
        ]
    }
}
#Background #1
BACKGROUND_IMAGE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/background1.png"
GROUND_TEXTURE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/ground.png"  # Текстура земли
PLATFORM_TEXTURE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/platfrom.png"  # Текстура платформ



# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 100, 255)
RED = (255, 0, 0)