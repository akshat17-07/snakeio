class GameConfig:
    def __init__(
        self,
        width=1400,
        height=900,
        fps=60,
    ):
        # SCREEN
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        # WORLD
        self.WORLD_WIDTH = 6000
        self.WORLD_HEIGHT = 6000
        self.FPS = fps

        # WORLD
        self.GRID_SPACING = 80

        # COLORS
        self.BACKGROUND_COLOR = (20, 20, 30)
        self.GRID_COLOR = (35, 35, 45)

        # SNAKES
        self.SNAKE_COUNT = 30
        self.INITIAL_LENGTH = 30
        self.FOOD_DROP_DIVISOR = 5

        self.SNAKE_SPEED = 3
        self.SNAKE_RADIUS = 12
        self.TURN_SPEED = 4

        # PLAYER ENABLE
        self.PLAYER_ENABLED = True

        # FOOD
        self.FOOD_COUNT = 800
        self.FOOD_RADIUS = 4
        self.FOOD_RANGE = 25

        # BOOST
        self.BOOST_SPEED_MULTIPLIER = 2
        self.BOOST_LOSS_AMOUNT = 0.08
        self.MIN_BOOST_LENGTH = 20


        # =====================================
    # OBSERVATION VALUES
    # =====================================

    OBSERVATION_VALUES = [

        # EMPTY CELL
        0.0,

        # FOOD VALUE
        0.05,

        # SNAKE BODY VALUE
        -0.03,

        # WALL VALUE
        -1.0,

        # HEAD BASE VALUE
        20.0,

        # HEAD NORMALIZATION DIVISOR
        100.0,

        # MAX HEAD VALUE
        1.0,

        # FOOD DENSITY SCALE
        1.0,

        # BODY DENSITY SCALE
        1.0,

        # HEAD DENSITY SCALE
        1.0,

        # OBSERVATION NOISE
        0.0,

        # FORWARD VISION BONUS
        0.5,

        # SIDE VISION SCALE
        1.0,

        # BACK VISION SCALE
        0.25,

        # ROTATION ENABLED
        1.0,

        # DENSITY ACCUMULATION ENABLED
        1.0,
    ]

    # =====================================
    # REWARDS
    # =====================================

    REWARDS = [

        # FOOD REWARD
        10.0,

        # KILL REWARD
        50.0,

        # SURVIVAL REWARD
        0.01,

        # DEATH PENALTY
        -100.0,

        # BOOST COST
        -0.001,

        # WALL HIT PENALTY
        -20.0,

        # GROWTH REWARD
        2.0,

        # DAMAGE TAKEN PENALTY
        -5.0,

        # CLOSE CALL REWARD
        1.0,

        # ESCAPE REWARD
        3.0,

        # CHASE REWARD
        2.0,

        # FOOD STREAK BONUS
        5.0,

        # IDLE PENALTY
        -0.01,

        # TURN SPAM PENALTY
        -0.001,

        # BOOST KILL BONUS
        20.0,

        # LARGE SNAKE KILL BONUS
        50.0,

        # SMALL SNAKE HUNT BONUS
        5.0,

        # SURROUND BONUS
        10.0,

        # TRAP ESCAPE BONUS
        15.0,

        # SUICIDE PENALTY
        -200.0,
    ]

    # =====================================
    # BEHAVIOR
    # =====================================

    BEHAVIOR = [

        # AGGRESSION
        0.5,

        # FOOD PRIORITY
        0.8,

        # DANGER SENSITIVITY
        0.9,

        # BOOST THRESHOLD
        0.4,

        # EXPLORATION RATE
        0.05,

        # RANDOM TURN CHANCE
        0.02,

        # RISK TAKING
        0.5,

        # CROWD AVOIDANCE
        0.8,

        # EDGE AVOIDANCE
        0.9,

        # TARGET LOCK STRENGTH
        0.7,

        # ESCAPE URGENCY
        0.9,

        # FOOD GREED
        0.8,

        # HUNTING DRIVE
        0.6,

        # BOOST AGGRESSION
        0.7,

        # BOOST CONSERVATION
        0.5,

        # LARGE SNAKE FEAR
        0.9,

        # SMALL SNAKE CONFIDENCE
        0.7,

        # PATH SMOOTHING
        0.6,

        # TURN RESPONSIVENESS
        0.8,

        # REACTION SPEED
        0.9,
    ]

    # =====================================
    # EVOLUTION
    # =====================================

    EVOLUTION = [

        # POPULATION SIZE
        100,

        # ELITE COUNT
        10,

        # MUTATION RATE
        0.05,

        # MUTATION STRENGTH
        0.1,

        # RANDOM AGENT COUNT
        5,

        # CROSSOVER RATE
        0.5,

        # PARAMETER MUTATION CHANCE
        0.2,

        # WEIGHT MUTATION CHANCE
        0.05,

        # HARD MUTATION CHANCE
        0.01,

        # SOFT MUTATION SCALE
        0.02,

        # GENERATION LENGTH
        3000,

        # FITNESS_DECAY
        0.99,

        # SPECIES THRESHOLD
        0.2,

        # MINIMUM DIVERSITY
        0.1,

        # MAX GENERATIONS
        100000,
    ]

    # =====================================
    # FITNESS
    # =====================================

    FITNESS = [

        # LENGTH WEIGHT
        1.0,

        # KILL WEIGHT
        25.0,

        # SURVIVAL WEIGHT
        0.01,

        # DEATH PENALTY
        -50.0,

        # FOOD EFFICIENCY
        2.0,

        # BOOST EFFICIENCY
        1.0,

        # ACCURACY BONUS
        1.0,

        # MOVEMENT SMOOTHNESS
        0.5,

        # TERRITORY CONTROL
        3.0,

        # AVERAGE POSITION BONUS
        1.0,

        # DOMINANCE BONUS
        10.0,

        # CONSISTENCY BONUS
        5.0,

        # WIN BONUS
        100.0,

        # TOP 10 BONUS
        20.0,

        # TOP 1 BONUS
        200.0,
    ]

    # =====================================
    # NETWORK
    # =====================================

    NETWORK = [

        # INPUT SIZE
        100,

        # HIDDEN SIZE
        128,

        # HIDDEN LAYERS
        2,

        # OUTPUT SIZE
        5,

        # LEARNING RATE
        0.001,

        # DROPOUT
        0.0,

        # ACTIVATION TYPE
        0,

        # MEMORY ENABLED
        0,

        # RECURRENT ENABLED
        0,

        # CNN ENABLED
        1,

        # ATTENTION ENABLED
        0,

        # TEMPORAL FRAMES
        4,
    ]

    OBSERVATION_GRID_SIZE = 100