# Окно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

GRAVITY = 0.55

# Уровни
LEVELS = {
    1: {
        "ground": [
            (0, 550, 700),
            (1000, 550, 800),
            (2600, 550, 1000),
            (3500, 550, 600)
        ],
        "platforms": [
            (200, 450, 100),
            (400, 350, 100),
            (600, 250, 200),
            (1400, 425, 150),
            (1700, 350, 150),
            (2100, 450, 150),
            (2450, 350, 150),
            (2900, 400, 100),
            (3400, 320, 100),
            (3850, 300, 150)
        ],
        "holes": [
            (700, 550, 300),
            (1800, 550, 800)
        ],
        "speed_potions": [
            (1700, 500)
        ]
    }
}

# Пути к изображениям
BACKGROUND_IMAGE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/background1.png"
GROUND_TEXTURE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/ground.png"
PLATFORM_TEXTURE = "/Users/bezenov_v/Desktop/PlatformerPygame/platformer_game/assets/backgrounds/platfrom.png"

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 100, 255)
RED = (255, 0, 0)