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

        # FITNESS
        self.fitness = 0

        # SURVIVAL
        self.frames_alive = 0

        # FOOD
        self.food_eaten = 0

        # DAMAGE
        self.damage_taken = 0

        # GENERATION
        self.generation = 0

        # BOOST
        # BOOST
        self.is_boosting = False

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
    # =========================
    # MOVE FORWARD
    # =========================
    def move_forward(self):
        speed = self.speed

        # BOOST SPEED
        if self.is_boosting:
            speed *= (
                self.config
                .BOOST_SPEED_MULTIPLIER
            )

            # LOSE LENGTH
            self.length -= (
                self.config
                .BOOST_LOSS_AMOUNT
            )

            # STOP BOOST IF TOO SMALL
            if (
                self.length
                <= self.config.MIN_BOOST_LENGTH
            ):
                self.length = (
                    self.config.MIN_BOOST_LENGTH
                )

                self.is_boosting = False

        rad = math.radians(self.angle)

        self.x += math.cos(rad) * speed
        self.y += math.sin(rad) * speed
    # =========================
    # UPDATE
    # =========================
    def update(self):
        if not self.alive:
            return
        
        # SURVIVAL TIME
        self.frames_alive += 1

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

        self.food_eaten += 1

    # =========================
    # DRAW BODY
    # =========================
    def draw_body(
        self,
        screen,
        camera_x,
        camera_y,
    ):
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
                    int(segment[0] - camera_x),
                    int(segment[1] - camera_y),
                ),
                size,
            )

    # =========================
    # DRAW HEAD
    # =========================
    def draw_head(
        self,
        screen,
        camera_x,
        camera_y,
    ):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                int(self.x - camera_x),
                int(self.y - camera_y),
            ),
            self.radius,
        )

    # =========================
    # BOOST
    # =========================
    def start_boost(self):
        if self.length > self.config.MIN_BOOST_LENGTH:
            self.is_boosting = True


    def stop_boost(self):
        self.is_boosting = False

    # =========================
    # DRAW EYES
    # =========================
    def draw_eyes(
        self,
        screen,
        camera_x,
        camera_y,
    ):
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
                int(left_eye_x - camera_x),
                int(left_eye_y - camera_y),
            ),
            eye_radius,
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (
                int(right_eye_x - camera_x),
                int(right_eye_y - camera_y),
            ),
            eye_radius,
        )

    # =========================
    # CALCULATE FITNESS
    # =========================
    def calculate_fitness(self):

        if self.fitness != 0:
            return self.fitness

        self.fitness = (

            # SURVIVAL
            self.frames_alive
            * self.config.FITNESS[2]

            +

            # LENGTH
            self.length
            * self.config.FITNESS[0]

            +

            # KILLS
            self.kills
            * self.config.FITNESS[1]

            +

            # FOOD
            self.food_eaten
            * self.config.FITNESS[4]
        )

        # DEATH PENALTY
        if not self.alive:

            self.fitness += (
                self.config.FITNESS[3]
            )

        return self.fitness

    # =========================
    # DRAW
    # =========================
    def draw(
        self,
        screen,
        camera_x,
        camera_y,
    ):
        if not self.alive:
            return
        self.draw_body(
            screen,
            camera_x,
            camera_y,
        )

        self.draw_head(
            screen,
            camera_x,
            camera_y,
        )

        self.draw_eyes(
            screen,
            camera_x,
            camera_y,
        )

    