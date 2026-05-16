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
                config.WORLD_WIDTH
            )
        )

        self.y = (
            y
            if y is not None
            else random.randint(
                0,
                config.WORLD_HEIGHT
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
    def draw(
        self,
        screen,
        camera_x,
        camera_y,
    ):
        pygame.draw.circle(
            screen,
            self.color,
            (
                int(self.x - camera_x),
                int(self.y - camera_y),
            ),
            self.config.FOOD_RADIUS,
        )