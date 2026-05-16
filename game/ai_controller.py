import random
import math


import random
import math


class RandomAIController:
    def __init__(self):
        # TURN TIMER
        self.turn_timer = 0

        # BOOST TIMER
        self.boost_timer = 0

        # -1 LEFT
        #  0 FORWARD
        #  1 RIGHT
        self.direction = 0

    # =========================
    # UPDATE
    # =========================
    def update(self, snake):
        # =========================
        # RANDOM TURNING
        # =========================
        self.turn_timer -= 1

        if self.turn_timer <= 0:
            self.turn_timer = random.randint(
                10,
                50,
            )

            self.direction = random.choice(
                [-1, 0, 1]
            )

        # APPLY TURN
        if self.direction == -1:
            snake.turn_left()

        elif self.direction == 1:
            snake.turn_right()

        # =========================
        # RANDOM BOOSTING
        # =========================
        self.boost_timer -= 1

        if self.boost_timer <= 0:
            self.boost_timer = random.randint(
                40,
                150,
            )

            should_boost = random.random() < 0.35

            if should_boost:
                snake.start_boost()
            else:
                snake.stop_boost()

# =====================================
# FUTURE ML CONTROLLER
# =====================================
class MLController:
    def __init__(self, model=None):
        self.model = model

    # =========================
    # GET GAME STATE
    # =========================
    def get_state(
        self,
        snake,
        foods,
        snakes,
    ):
        """
        Convert world into ML inputs.
        """

        nearest_food = None
        nearest_distance = float("inf")

        for food in foods:
            dist = math.hypot(
                snake.x - food.x,
                snake.y - food.y,
            )

            if dist < nearest_distance:
                nearest_distance = dist
                nearest_food = food

        state = {
            "snake_x": snake.x,
            "snake_y": snake.y,
            "angle": snake.angle,
            "length": snake.length,
            "nearest_food_x": (
                nearest_food.x
                if nearest_food
                else 0
            ),
            "nearest_food_y": (
                nearest_food.y
                if nearest_food
                else 0
            ),
            "nearest_food_distance": (
                nearest_distance
            ),
        }

        return state

    # =========================
    # PREDICT ACTION
    # =========================
    def predict_action(self, state):
        """
        Placeholder for ML model.

        Return:
        -1 = LEFT
         0 = FORWARD
         1 = RIGHT
        """

        return random.choice([-1, 0, 1])

    # =========================
    # UPDATE
    # =========================
    def update(
        self,
        snake,
        foods=None,
        snakes=None,
    ):
        state = self.get_state(
            snake,
            foods or [],
            snakes or [],
        )

        action = self.predict_action(
            state
        )

        if action == -1:
            snake.turn_left()

        elif action == 1:
            snake.turn_right()