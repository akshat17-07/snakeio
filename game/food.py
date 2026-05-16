import random
import pygame


class Food:
    def __init__(self, config):
        self.config = config

        self.x = random.randint(0, config.WIDTH)
        self.y = random.randint(0, config.HEIGHT)

        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.config.FOOD_RADIUS,
        )