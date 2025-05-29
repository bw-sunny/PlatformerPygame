# Окно
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

GRAVITY = 0.55

# Уровни
LEVELS = {
    1: {
        "ground": [(0, 520, 700), (1050, 520, 850)],  # Было (0, 550, 700), (1050, 550, 850)
        "platforms": [
            (200, 450, 100),
            (400, 350, 100),
            (600, 250, 200),
            (1400, 425, 150),
            (1850, 350, 150),
            (1450, 275, 150)
        ],
        "speed_potions": [(300, 480)],
        "holes": [(1050, 520, 350)]  # Было (1050, 550, 350)
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