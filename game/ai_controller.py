import random
import numpy as np


# =====================================
# RANDOM AI
# =====================================
class RandomAIController:
    def __init__(self):

        self.turn_timer = 0

        self.boost_timer = 0

        self.direction = 0

    # =====================================
    # UPDATE
    # =====================================
    def update(self, snake):

        # RANDOM TURNING
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

        # RANDOM BOOSTING
        self.boost_timer -= 1

        if self.boost_timer <= 0:

            self.boost_timer = random.randint(
                40,
                150,
            )

            should_boost = (
                random.random() < 0.35
            )

            if should_boost:
                snake.start_boost()

            else:
                snake.stop_boost()


# =====================================
# ML CONTROLLER
# =====================================
class MLController:
    def __init__(
        self,
        genome=None,
    ):

        # =====================================
        # GENOME
        # =====================================
        self.genome = genome or {

            # TURNING
            "turn_threshold": random.uniform(
                0.2,
                0.8,
            ),

            # BOOSTING
            "boost_threshold": random.uniform(
                0.1,
                0.9,
            ),

            # FOOD PRIORITY
            "food_priority": random.uniform(
                0.0,
                1.0,
            ),

            # DANGER SENSITIVITY
            "danger_sensitivity": random.uniform(
                0.0,
                1.0,
            ),

            # RANDOMNESS
            "randomness": random.uniform(
                0.0,
                0.2,
            ),
        }

        # OBSERVATION GRID
        self.grid = None

    # =====================================
    # MUTATE GENOME
    # =====================================
    def mutate_genome(self):

        mutated = {}

        for key, value in (
            self.genome.items()
        ):

            mutation = random.uniform(
                -0.1,
                0.1,
            )

            new_value = (
                value + mutation
            )

            # CLAMP
            new_value = max(
                0.0,
                min(1.0, new_value)
            )

            mutated[key] = new_value

        return mutated

    # =====================================
    # PREDICT ACTION
    # =====================================
    def predict_action(
        self,
    ):

        if self.grid is None:
            return 0

        size = self.grid.shape[0]

        center = size // 2

        # =====================================
        # REGIONS
        # =====================================

        # FORWARD
        forward_region = (
            self.grid[
                center-8:center+8,
                center:center+20,
            ]
        )

        # LEFT
        left_region = (
            self.grid[
                center-20:center,
                center-8:center+8,
            ]
        )

        # RIGHT
        right_region = (
            self.grid[
                center:center+20,
                center-8:center+8,
            ]
        )

        # =====================================
        # SCORES
        # =====================================

        forward_score = np.sum(
            forward_region
        )

        left_score = np.sum(
            left_region
        )

        right_score = np.sum(
            right_region
        )

        # =====================================
        # DANGER
        # =====================================

        danger_weight = (
            self.genome[
                "danger_sensitivity"
            ]
        )

        left_score *= danger_weight
        right_score *= danger_weight

        # =====================================
        # RANDOMNESS
        # =====================================

        if (
            random.random()
            <
            self.genome[
                "randomness"
            ]
        ):
            return random.choice(
                [-1, 0, 1]
            )

        # =====================================
        # DECISION
        # =====================================

        if left_score > right_score:

            return -1

        elif right_score > left_score:

            return 1

        return 0

    # =====================================
    # UPDATE
    # =====================================
    def update(
        self,
        snake,
    ):

        action = (
            self.predict_action()
        )

        # LEFT
        if action == -1:
            snake.turn_left()

        # RIGHT
        elif action == 1:
            snake.turn_right()

        # =====================================
        # BOOST
        # =====================================

        boost_threshold = (
            self.genome[
                "boost_threshold"
            ]
        )

        if (
            random.random()
            < boost_threshold
        ):
            snake.start_boost()

        else:
            snake.stop_boost()