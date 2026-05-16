import math
import random
import pygame

from game.snake import Snake
from game.food import Food
from game.ai_controller import RandomAIController


class Game:
    def __init__(self, config):
        self.config = config

        pygame.init()

        self.screen = pygame.display.set_mode(
            (config.WIDTH, config.HEIGHT)
        )

        pygame.display.set_caption("Snake.io")

        self.clock = pygame.time.Clock()

        self.running = True

        self.font = pygame.font.SysFont(None, 30)

        # =========================
        # SNAKES
        # =========================
        self.snakes = []

        self.spawn_player_snakes()
        self.spawn_ai_snakes()

        # =========================
        # FOOD
        # =========================
        self.foods = [
            Food(config)
            for _ in range(config.FOOD_COUNT)
        ]

    # =========================
    # CREATE SNAKE
    # =========================
    def create_snake(self, ai=False):
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

        controller = (
            RandomAIController()
            if ai
            else None
        )

        snake = Snake(
            self.config,
            random.randint(
                100,
                self.config.WIDTH - 100
            ),
            random.randint(
                100,
                self.config.HEIGHT - 100
            ),
            color,
            controller,
        )

        return snake

    # =========================
    # PLAYER SNAKES
    # =========================
    def spawn_player_snakes(self):
        player1 = Snake(
            self.config,
            300,
            300,
            (0, 255, 100),
        )

        player2 = Snake(
            self.config,
            1000,
            700,
            (255, 100, 100),
        )

        player1.angle = 0
        player2.angle = 180

        self.snakes.append(player1)
        self.snakes.append(player2)

    # =========================
    # AI SNAKES
    # =========================
    def spawn_ai_snakes(self):
        for _ in range(
            self.config.SNAKE_COUNT
        ):
            self.snakes.append(
                self.create_snake(ai=True)
            )

    # =========================
    # EVENTS
    # =========================
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # =========================
    # INPUT
    # =========================
    def handle_input(self):
        keys = pygame.key.get_pressed()

        # PLAYER 1
        if keys[pygame.K_a]:
            self.snakes[0].turn_left()

        if keys[pygame.K_d]:
            self.snakes[0].turn_right()

        # PLAYER 2
        if keys[pygame.K_LEFT]:
            self.snakes[1].turn_left()

        if keys[pygame.K_RIGHT]:
            self.snakes[1].turn_right()

    # =========================
    # FOOD COLLISION
    # =========================
    def check_food_collision(self, snake):
        eaten_food = []

        for food in self.foods:
            dist = math.hypot(
                snake.x - food.x,
                snake.y - food.y,
            )

            if (
                dist
                < snake.radius
                + self.config.FOOD_RADIUS
            ):
                snake.grow()

                eaten_food.append(food)

        for food in eaten_food:
            self.foods.remove(food)

            self.foods.append(
                Food(self.config)
            )

    # =========================
    # DROP FOOD ON DEATH
    # =========================
    def drop_food(self, snake):
        food_count = int(
            snake.length
            / self.config.FOOD_DROP_DIVISOR
        )

        if food_count <= 0:
            return

        step = max(
            1,
            len(snake.body) // food_count
        )

        for segment in snake.body[::step]:
            self.foods.append(
                Food(
                    self.config,
                    segment[0],
                    segment[1],
                )
            )

    # =========================
    # SNAKE COLLISIONS
    # =========================
    def check_snake_collisions(self):
        for snake in self.snakes:
            if not snake.alive:
                continue

            # WALL COLLISION
            if (
                snake.x < 0
                or snake.x > self.config.WIDTH
                or snake.y < 0
                or snake.y > self.config.HEIGHT
            ):
                snake.alive = False

                self.drop_food(snake)

                continue

            # OTHER SNAKE BODY COLLISION
            for other in self.snakes:
                if snake == other:
                    continue

                if not other.alive:
                    continue

                # Ignore head area
                for segment in other.body[10:]:
                    dist = math.hypot(
                        snake.x - segment[0],
                        snake.y - segment[1],
                    )

                    if dist < snake.radius:
                        snake.alive = False

                        other.kills += 1

                        self.drop_food(snake)

                        break

    # =========================
    # RESPAWN DEAD SNAKES
    # =========================
    def respawn_dead_snakes(self):
        for i, snake in enumerate(self.snakes):
            if snake.alive:
                continue

            is_ai = (
                snake.ai_controller
                is not None
            )

            # PLAYER 1
            if i == 0:
                new_snake = Snake(
                    self.config,
                    300,
                    300,
                    (0, 255, 100),
                )

                new_snake.angle = 0

            # PLAYER 2
            elif i == 1:
                new_snake = Snake(
                    self.config,
                    1000,
                    700,
                    (255, 100, 100),
                )

                new_snake.angle = 180

            # AI
            else:
                new_snake = self.create_snake(
                    ai=is_ai
                )

            self.snakes[i] = new_snake

    # =========================
    # UPDATE
    # =========================
    def update(self):
        self.handle_input()

        # MOVE
        for snake in self.snakes:
            snake.update()

        # FOOD
        for snake in self.snakes:
            if snake.alive:
                self.check_food_collision(
                    snake
                )

        # COLLISIONS
        self.check_snake_collisions()

        # RESPAWN
        self.respawn_dead_snakes()

    # =========================
    # GRID
    # =========================
    def draw_grid(self):
        spacing = (
            self.config.GRID_SPACING
        )

        for x in range(
            0,
            self.config.WIDTH,
            spacing
        ):
            pygame.draw.line(
                self.screen,
                self.config.GRID_COLOR,
                (x, 0),
                (x, self.config.HEIGHT),
            )

        for y in range(
            0,
            self.config.HEIGHT,
            spacing
        ):
            pygame.draw.line(
                self.screen,
                self.config.GRID_COLOR,
                (0, y),
                (self.config.WIDTH, y),
            )

    # =========================
    # UI
    # =========================
    def draw_stats(self):
        y = 10

        for i, snake in enumerate(
            self.snakes[:2]
        ):
            text = (
                f"P{i+1} | "
                f"Length: {snake.length} | "
                f"Kills: {snake.kills}"
            )

            surface = self.font.render(
                text,
                True,
                (255, 255, 255),
            )

            self.screen.blit(
                surface,
                (10, y),
            )

            y += 30

    # =========================
    # DRAW
    # =========================
    def draw(self):
        self.screen.fill(
            self.config.BACKGROUND_COLOR
        )

        self.draw_grid()

        # FOOD
        for food in self.foods:
            food.draw(self.screen)

        # SNAKES
        for snake in self.snakes:
            snake.draw(self.screen)

        # UI
        self.draw_stats()

        pygame.display.flip()

    # =========================
    # RUN
    # =========================
    def run(self):
        while self.running:
            self.clock.tick(
                self.config.FPS
            )

            self.handle_events()

            self.update()

            self.draw()

        pygame.quit()