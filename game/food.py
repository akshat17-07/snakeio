import random
import pygame


class Food:
    def __init__(
        self,
        config,
        x=None,
        y=None,
    ):
        self.config = config

        self.x = (
            x
            if x is not None
            else random.randint(
                0,
                config.WIDTH
            )
        )

        self.y = (
            y
            if y is not None
            else random.randint(
                0,
                config.HEIGHT
            )
        )

        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

    # =========================
    # DRAW
    # =========================
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (
                int(self.x),
                int(self.y),
            ),
            self.config.FOOD_RADIUS,
        )