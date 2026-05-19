import numpy as np


class ObservationSystem:
    def __init__(self, config):
        self.config = config

    # =====================================
    # BUILD OBSERVATION
    # =====================================
    def build_observation(
        self,
        snake,
        foods,
        snakes,
    ):
        size = (
            self.config
            .OBSERVATION_GRID_SIZE
        )

        # =====================================
        # EMPTY GRID
        # =====================================
        grid = np.full(
            (
                size,
                size,
            ),
            self.config.OBSERVATION_VALUES[0],
            dtype=np.float32,
        )

        # =====================================
        # CAMERA
        # =====================================
        camera_x = (
            snake.x
            - self.config.SCREEN_WIDTH / 2
        )

        camera_y = (
            snake.y
            - self.config.SCREEN_HEIGHT / 2
        )

        # =====================================
        # WALLS
        # =====================================

        # LEFT WALL
        if camera_x < 0:

            wall_ratio = (
                abs(camera_x)
                / self.config.SCREEN_WIDTH
            )

            wall_cells = int(
                wall_ratio * size
            )

            grid[
                :,
                :wall_cells
            ] = (
                self.config
                .OBSERVATION_VALUES[3]
            )

        # RIGHT WALL
        right_overflow = (
            camera_x
            + self.config.SCREEN_WIDTH
            - self.config.WORLD_WIDTH
        )

        if right_overflow > 0:

            wall_ratio = (
                right_overflow
                / self.config.SCREEN_WIDTH
            )

            wall_cells = int(
                wall_ratio * size
            )

            grid[
                :,
                size-wall_cells:
            ] = (
                self.config
                .OBSERVATION_VALUES[3]
            )

        # TOP WALL
        if camera_y < 0:

            wall_ratio = (
                abs(camera_y)
                / self.config.SCREEN_HEIGHT
            )

            wall_cells = int(
                wall_ratio * size
            )

            grid[
                :wall_cells,
                :
            ] = (
                self.config
                .OBSERVATION_VALUES[3]
            )

        # BOTTOM WALL
        bottom_overflow = (
            camera_y
            + self.config.SCREEN_HEIGHT
            - self.config.WORLD_HEIGHT
        )

        if bottom_overflow > 0:

            wall_ratio = (
                bottom_overflow
                / self.config.SCREEN_HEIGHT
            )

            wall_cells = int(
                wall_ratio * size
            )

            grid[
                size-wall_cells:,
                :
            ] = (
                self.config
                .OBSERVATION_VALUES[3]
            )

        # =====================================
        # FOOD
        # =====================================
        for food in foods:

            screen_x = (
                food.x
                - camera_x
            )

            screen_y = (
                food.y
                - camera_y
            )

            # OUTSIDE SCREEN
            if (
                screen_x < 0
                or
                screen_x >= self.config.SCREEN_WIDTH
                or
                screen_y < 0
                or
                screen_y >= self.config.SCREEN_HEIGHT
            ):
                continue

            grid_x = int(
                (
                    screen_x
                    / self.config.SCREEN_WIDTH
                )
                * size
            )

            grid_y = int(
                (
                    screen_y
                    / self.config.SCREEN_HEIGHT
                )
                * size
            )

            # CLAMP
            grid_x = max(
                0,
                min(size - 1, grid_x)
            )

            grid_y = max(
                0,
                min(size - 1, grid_y)
            )

            grid[
                grid_y,
                grid_x,
            ] += (
                self.config
                .OBSERVATION_VALUES[1]
            )

        # =====================================
        # SNAKES
        # =====================================
        for other in snakes:

            if not other.alive:
                continue

            # =========================
            # BODY
            # =========================
            for segment in other.body:

                screen_x = (
                    segment[0]
                    - camera_x
                )

                screen_y = (
                    segment[1]
                    - camera_y
                )

                # OUTSIDE SCREEN
                if (
                    screen_x < 0
                    or
                    screen_x >= self.config.SCREEN_WIDTH
                    or
                    screen_y < 0
                    or
                    screen_y >= self.config.SCREEN_HEIGHT
                ):
                    continue

                grid_x = int(
                    (
                        screen_x
                        / self.config.SCREEN_WIDTH
                    )
                    * size
                )

                grid_y = int(
                    (
                        screen_y
                        / self.config.SCREEN_HEIGHT
                    )
                    * size
                )

                # CLAMP
                grid_x = max(
                    0,
                    min(size - 1, grid_x)
                )

                grid_y = max(
                    0,
                    min(size - 1, grid_y)
                )

                grid[
                    grid_y,
                    grid_x,
                ] += (
                    self.config
                    .OBSERVATION_VALUES[2]
                )

            # =========================
            # HEAD
            # =========================
            screen_x = (
                other.x
                - camera_x
            )

            screen_y = (
                other.y
                - camera_y
            )

            if (
                screen_x < 0
                or
                screen_x >= self.config.SCREEN_WIDTH
                or
                screen_y < 0
                or
                screen_y >= self.config.SCREEN_HEIGHT
            ):
                continue

            grid_x = int(
                (
                    screen_x
                    / self.config.SCREEN_WIDTH
                )
                * size
            )

            grid_y = int(
                (
                    screen_y
                    / self.config.SCREEN_HEIGHT
                )
                * size
            )

            # CLAMP
            grid_x = max(
                0,
                min(size - 1, grid_x)
            )

            grid_y = max(
                0,
                min(size - 1, grid_y)
            )

            # NORMALIZED HEAD VALUE
            head_value = (
                self.config
                .OBSERVATION_VALUES[4]
                + other.length
            )

            head_value /= (
                self.config
                .OBSERVATION_VALUES[5]
            )

            head_value = min(
                head_value,
                self.config
                .OBSERVATION_VALUES[6]
            )

            grid[
                grid_y,
                grid_x,
            ] += head_value

        return grid