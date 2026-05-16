import math
import random
import pygame


class Snake:
    def __init__(
        self,
        config,
        x,
        y,
        color,
        ai_controller=None,
    ):
        self.config = config

        # POSITION
        self.x = x
        self.y = y

        # APPEARANCE
        self.color = color

        # MOVEMENT
        self.angle = random.randint(0, 360)

        self.speed = config.SNAKE_SPEED
        self.turn_speed = config.TURN_SPEED

        # SIZE
        self.radius = config.SNAKE_RADIUS

        # BODY
        self.body = []

        self.length = config.INITIAL_LENGTH

        # STATE
        self.alive = True

        # AI
        self.ai_controller = ai_controller

        # STATS
        self.kills = 0

    # =========================
    # CONTROLS
    # =========================
    def turn_left(self):
        self.angle -= self.turn_speed

    def turn_right(self):
        self.angle += self.turn_speed

    # =========================
    # MOVE FORWARD
    # =========================
    def move_forward(self):
        rad = math.radians(self.angle)

        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed

    # =========================
    # UPDATE
    # =========================
    def update(self):
        if not self.alive:
            return

        # AI CONTROLLER
        if self.ai_controller:
            self.ai_controller.update(self)

        # MOVE
        self.move_forward()

        # ADD HEAD POSITION
        self.body.insert(
            0,
            (self.x, self.y)
        )

        # LIMIT BODY SIZE
        if len(self.body) > self.length:
            self.body.pop()

    # =========================
    # GROW
    # =========================
    def grow(self, amount=8):
        self.length += amount

    # =========================
    # DRAW BODY
    # =========================
    def draw_body(self, screen):
        body_len = len(self.body)

        if body_len == 0:
            return

        for i, segment in enumerate(
            reversed(self.body)
        ):
            scale = i / body_len

            size = max(
                4,
                int(self.radius * scale)
            )

            pygame.draw.circle(
                screen,
                self.color,
                (
                    int(segment[0]),
                    int(segment[1]),
                ),
                size,
            )

    # =========================
    # DRAW HEAD
    # =========================
    def draw_head(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                int(self.x),
                int(self.y),
            ),
            self.radius,
        )

    # =========================
    # DRAW EYES
    # =========================
    def draw_eyes(self, screen):
        rad = math.radians(self.angle)

        eye_distance = 6
        eye_radius = 2

        forward_x = math.cos(rad)
        forward_y = math.sin(rad)

        left_x = -forward_y
        left_y = forward_x

        # LEFT EYE
        left_eye_x = (
            self.x
            + forward_x * eye_distance
            + left_x * 4
        )

        left_eye_y = (
            self.y
            + forward_y * eye_distance
            + left_y * 4
        )

        # RIGHT EYE
        right_eye_x = (
            self.x
            + forward_x * eye_distance
            - left_x * 4
        )

        right_eye_y = (
            self.y
            + forward_y * eye_distance
            - left_y * 4
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                int(left_eye_x),
                int(left_eye_y),
            ),
            eye_radius,
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                int(right_eye_x),
                int(right_eye_y),
            ),
            eye_radius,
        )

    # =========================
    # DRAW
    # =========================
    def draw(self, screen):
        if not self.alive:
            return

        self.draw_body(screen)

        self.draw_head(screen)

        self.draw_eyes(screen)