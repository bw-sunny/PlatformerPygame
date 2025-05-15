from abc import ABC, abstractmethod
from pygame.sprite import Sprite


class Entity(Sprite, ABC):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.health = 100

    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def draw(self, surface):
        pass