class GameConfig:
    def __init__(
        self,
        width=1400,
        height=900,
        fps=60,
    ):
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps

        # WORLD
        self.GRID_SPACING = 80

        # COLORS
        self.BACKGROUND_COLOR = (20, 20, 30)
        self.GRID_COLOR = (35, 35, 45)

        # SNAKES
        self.SNAKE_COUNT = 10
        self.INITIAL_LENGTH = 30
        self.FOOD_DROP_DIVISOR = 5

        self.SNAKE_SPEED = 4
        self.SNAKE_RADIUS = 12
        self.TURN_SPEED = 4

        # PLAYER ENABLE
        self.PLAYER_ENABLED = True

        # FOOD
        self.FOOD_COUNT = 300
        self.FOOD_RADIUS = 4

        # BOOST
        self.BOOST_SPEED_MULTIPLIER = 2
        self.BOOST_LOSS_AMOUNT = 0.08
        self.MIN_BOOST_LENGTH = 20