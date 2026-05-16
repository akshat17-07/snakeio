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
            (
                config.SCREEN_WIDTH,
                config.SCREEN_HEIGHT,
            )
        )

        self.camera_x = 0
        self.camera_y = 0

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
                self.config.WORLD_WIDTH - 100
            ),
            random.randint(
                100,
                self.config.WORLD_HEIGHT - 100
            ),
            color,
            controller,
        )

        return snake
    
    # =========================
    # CAMERA
    # =========================
    def update_camera(self):
        if (
            not self.config.PLAYER_ENABLED
            or len(self.snakes) == 0
        ):
            return

        player = self.snakes[0]

        self.camera_x = (
            player.x
            - self.config.SCREEN_WIDTH // 2
        )

        self.camera_y = (
            player.y
            - self.config.SCREEN_HEIGHT // 2
        )

    # =========================
    # PLAYER SNAKES
    # =========================
    def spawn_player_snakes(self):
        if not self.config.PLAYER_ENABLED:
            return

        player = Snake(
            self.config,
            self.config.WORLD_WIDTH // 2,
            self.config.WORLD_HEIGHT // 2,
            (0, 255, 100),
        )

        player.angle = 0

        self.snakes.append(player)

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
        if not self.config.PLAYER_ENABLED:
            return

        if len(self.snakes) == 0:
            return

        player = self.snakes[0]

        keys = pygame.key.get_pressed()

        # TURN
        if keys[pygame.K_a]:
            player.turn_left()

        if keys[pygame.K_d]:
            player.turn_right()

        # BOOST
        if keys[pygame.K_w]:
            player.start_boost()
        else:
            player.stop_boost()

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
                or snake.x > self.config.WORLD_WIDTH
                or snake.y < 0
                or snake.y > self.config.WORLD_HEIGHT
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

            # PLAYER
            if (
                self.config.PLAYER_ENABLED
                and i == 0
                and not is_ai
            ):
                new_snake = Snake(
                    self.config,
                    self.config.WORLD_WIDTH // 2,
                    self.config.WORLD_HEIGHT // 2,
                    (0, 255, 100),
                )

                new_snake.angle = 0

            # AI
            else:
                new_snake = self.create_snake(
                    ai=True
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

        self.update_camera()

        # COLLISIONS
        self.check_snake_collisions()

        # RESPAWN
        self.respawn_dead_snakes()

    # =========================
    # GRID
    # =========================
    def draw_grid(self):
        spacing = self.config.GRID_SPACING

        start_x = int(
            self.camera_x // spacing
        ) * spacing

        end_x = (
            self.camera_x
            + self.config.SCREEN_WIDTH
        )

        start_y = int(
            self.camera_y // spacing
        ) * spacing

        end_y = (
            self.camera_y
            + self.config.SCREEN_HEIGHT
        )

        # VERTICAL
        for x in range(
            start_x,
            int(end_x),
            spacing,
        ):
            screen_x = x - self.camera_x

            pygame.draw.line(
                self.screen,
                self.config.GRID_COLOR,
                (screen_x, 0),
                (
                    screen_x,
                    self.config.SCREEN_HEIGHT,
                ),
            )

        # HORIZONTAL
        for y in range(
            start_y,
            int(end_y),
            spacing,
        ):
            screen_y = y - self.camera_y

            pygame.draw.line(
                self.screen,
                self.config.GRID_COLOR,
                (0, screen_y),
                (
                    self.config.SCREEN_WIDTH,
                    screen_y,
                ),
            )

    
    # =========================
    # UI
    # =========================
    def draw_stats(self):
        if not self.config.PLAYER_ENABLED:
            return

        if len(self.snakes) == 0:
            return

        player = self.snakes[0]

        text = (
            f"Length: {int(player.length)} | "
            f"Kills: {player.kills}"
        )

        surface = self.font.render(
            text,
            True,
            (255, 255, 255),
        )

        self.screen.blit(surface, (10, 10))
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
            food.draw(
                self.screen,
                self.camera_x,
                self.camera_y,
            )

        # SNAKES
        for snake in self.snakes:
            snake.draw(
                self.screen,
                self.camera_x,
                self.camera_y,
            )

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