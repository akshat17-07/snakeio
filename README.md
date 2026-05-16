# Snake.io AI Simulation

A Snake.io-style multiplayer simulation built with Python and Pygame.

This project is designed with a machine-learning-ready architecture, allowing future integration of:
- Reinforcement Learning
- Neural Networks
- Genetic Algorithms
- PPO / DQN Agents
- Evolutionary Simulations

---

# Features

## Gameplay
- Smooth Snake.io-style movement
- Boost mechanic
- Food collection
- Snake growth
- Snake death system
- Food drops on death
- Kill tracking
- Large scrolling world
- Camera system
- AI-controlled snakes

## AI System
- Random AI movement
- Random boosting
- Modular AI controller architecture
- ML-ready environment structure

## Engine Architecture
- World-space rendering
- Camera-space rendering
- Config-driven setup
- Expandable game engine structure

---

# Controls

## Player
| Key | Action |
|---|---|
| A | Turn Left |
| D | Turn Right |
| W | Boost |

---

# Project Structure

```text
snakeio/
│
├── main.py
├── config.py
├── README.md
│
└── game/
    ├── __init__.py
    ├── game.py
    ├── snake.py
    ├── food.py
    └── ai_controller.py
```

---

# Installation

## 1. Create Virtual Environment

```bash
python -m venv .venv
```

## 2. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install pygame-ce
```

---

# Run Project

```bash
python main.py
```

---

# Configuration Settings

All game settings are located in:

```python
config.py
```

---

## Screen Settings

### `SCREEN_WIDTH`

```python
self.SCREEN_WIDTH = width
```

Controls the visible game window width.

---

### `SCREEN_HEIGHT`

```python
self.SCREEN_HEIGHT = height
```

Controls visible game window height.

---

## World Settings

### `WORLD_WIDTH`

```python
self.WORLD_WIDTH = 6000
```

Controls total world width.

---

### `WORLD_HEIGHT`

```python
self.WORLD_HEIGHT = 6000
```

Controls total world height.

---

## Performance

### `FPS`

```python
self.FPS = 60
```

Controls game update/render speed.

Higher FPS:
- smoother movement
- more CPU usage

---

## Grid Settings

### `GRID_SPACING`

```python
self.GRID_SPACING = 80
```

Distance between background grid lines.

---

## Player Settings

### `PLAYER_ENABLED`

```python
self.PLAYER_ENABLED = True
```

### `True`
- player controlled snake
- keyboard input enabled

### `False`
- AI-only simulation
- useful for ML training

---

## Snake Settings

### `SNAKE_COUNT`

```python
self.SNAKE_COUNT = 10
```

Number of AI snakes.

---

### `INITIAL_LENGTH`

```python
self.INITIAL_LENGTH = 30
```

Starting snake body length.

---

### `SNAKE_SPEED`

```python
self.SNAKE_SPEED = 4
```

Base snake movement speed.

---

### `TURN_SPEED`

```python
self.TURN_SPEED = 4
```

How quickly snake rotates.

---

### `SNAKE_RADIUS`

```python
self.SNAKE_RADIUS = 12
```

Snake head size.

---

## Boost Settings

### `BOOST_SPEED_MULTIPLIER`

```python
self.BOOST_SPEED_MULTIPLIER = 2
```

Multiplier applied during boost.

---

### `BOOST_LOSS_AMOUNT`

```python
self.BOOST_LOSS_AMOUNT = 0.08
```

Amount of snake length lost each frame while boosting.

---

### `MIN_BOOST_LENGTH`

```python
self.MIN_BOOST_LENGTH = 20
```

Minimum length required for boosting.

---

## Food Settings

### `FOOD_COUNT`

```python
self.FOOD_COUNT = 300
```

Number of food pellets in world.

---

### `FOOD_RADIUS`

```python
self.FOOD_RADIUS = 4
```

Visual food size.

---

## Death Settings

### `FOOD_DROP_DIVISOR`

```python
self.FOOD_DROP_DIVISOR = 5
```

Controls food dropped on death.

Formula:

```python
food_dropped = snake_length / FOOD_DROP_DIVISOR
```

---

# AI Architecture

Main AI file:

```text
game/ai_controller.py
```

This allows easy replacement of:
- Random AI
- Neural Networks
- Reinforcement Learning
- Genetic Algorithms

without changing rendering or engine logic.

---

# Current AI

Current AI behavior:
- Random turning
- Random boosting
- Wall collision
- Food collection
- Respawning

---

# Planned Features

## Gameplay
- Leaderboard
- Minimap
- Boost particles
- Smooth interpolation
- Zoom system
- Better collisions

## AI
- Food-seeking AI
- Wall avoidance
- Tail avoidance
- Enemy targeting
- Neural-network agents
- Reinforcement learning training

## Performance
- Spatial partitioning
- Chunk loading
- Headless simulation mode
- Faster training environment

---

# Example Competitive Configuration

```python
self.SNAKE_COUNT = 40

self.WORLD_WIDTH = 12000
self.WORLD_HEIGHT = 12000

self.FOOD_COUNT = 1000

self.SNAKE_SPEED = 5

self.BOOST_SPEED_MULTIPLIER = 2.5
```

---

# Example ML Training Configuration

```python
self.PLAYER_ENABLED = False

self.SNAKE_COUNT = 100

self.FPS = 240

self.WORLD_WIDTH = 20000
self.WORLD_HEIGHT = 20000
```

Used for:
- reinforcement learning
- large simulations
- evolutionary training

# Configuration Settings

All game settings are located in:

```python
config.py
```

Example:

```python
class GameConfig:
    def __init__(
        self,
        width=1400,
        height=900,
        fps=60,
    ):
```

---

# Screen Settings

## `SCREEN_WIDTH`

```python
self.SCREEN_WIDTH = width
```

Controls the visible game window width.

Example:

```python
self.SCREEN_WIDTH = 1920
```

Larger values:
- show more world
- increase rendering cost

---

## `SCREEN_HEIGHT`

```python
self.SCREEN_HEIGHT = height
```

Controls visible game window height.

Example:

```python
self.SCREEN_HEIGHT = 1080
```

---

# World Settings

## `WORLD_WIDTH`

```python
self.WORLD_WIDTH = 6000
```

Controls total world width.

This is the actual playable map size.

Larger values:
- more exploration
- snakes spread out more
- better for ML simulations

---

## `WORLD_HEIGHT`

```python
self.WORLD_HEIGHT = 6000
```

Controls total world height.

---

# Performance

## `FPS`

```python
self.FPS = 60
```

Controls game update/render speed.

Examples:

```python
30
```

Low performance mode

```python
60
```

Normal gameplay

```python
144
```

High refresh gameplay

Higher FPS:
- smoother movement
- more CPU usage

---

# Grid Settings

## `GRID_SPACING`

```python
self.GRID_SPACING = 80
```

Distance between background grid lines.

Smaller:
- dense grid

Larger:
- cleaner look

---

# Player Settings

## `PLAYER_ENABLED`

```python
self.PLAYER_ENABLED = True
```

Controls whether human player exists.

### `True`
- player controlled snake
- keyboard input enabled

### `False`
- AI-only simulation
- useful for ML training

---

# Snake Settings

## `SNAKE_COUNT`

```python
self.SNAKE_COUNT = 10
```

Number of AI snakes.

Higher values:
- more chaos
- more collisions
- harder AI training
- more CPU usage

---

## `INITIAL_LENGTH`

```python
self.INITIAL_LENGTH = 30
```

Starting snake body length.

Higher values:
- stronger starting snakes
- easier survival

---

## `SNAKE_SPEED`

```python
self.SNAKE_SPEED = 4
```

Base snake movement speed.

Higher:
- faster gameplay
- harder turning

Lower:
- slower strategy gameplay

---

## `TURN_SPEED`

```python
self.TURN_SPEED = 4
```

How quickly snake rotates.

Higher:
- sharper turning

Lower:
- smoother wider turns

---

## `SNAKE_RADIUS`

```python
self.SNAKE_RADIUS = 12
```

Snake head size.

Also affects:
- collision size
- body thickness

---

# Boost Settings

## `BOOST_SPEED_MULTIPLIER`

```python
self.BOOST_SPEED_MULTIPLIER = 2
```

Multiplier applied during boost.

Example:

```python
2
```

means:
- snake moves 2x faster

---

## `BOOST_LOSS_AMOUNT`

```python
self.BOOST_LOSS_AMOUNT = 0.08
```

Amount of snake length lost each frame while boosting.

Higher:
- expensive boost

Lower:
- easier boosting

---

## `MIN_BOOST_LENGTH`

```python
self.MIN_BOOST_LENGTH = 20
```

Minimum length required for boosting.

Prevents tiny snakes from boosting forever.

---

# Food Settings

## `FOOD_COUNT`

```python
self.FOOD_COUNT = 300
```

Number of food pellets in world.

Higher:
- easier growth
- more rendering cost

Lower:
- more competitive gameplay

---

## `FOOD_RADIUS`

```python
self.FOOD_RADIUS = 4
```

Visual food size.

Also affects:
- food collision area

---

# Death Settings

## `FOOD_DROP_DIVISOR`

```python
self.FOOD_DROP_DIVISOR = 5
```

Controls food dropped on death.

Formula:

```python
food_dropped = snake_length / FOOD_DROP_DIVISOR
```

Example:

Snake length = `100`

```python
100 / 5 = 20 food
```

Lower values:
- more food explosions

Higher values:
- less food on death

---

# Example Competitive Configuration

```python
self.SNAKE_COUNT = 40

self.WORLD_WIDTH = 12000
self.WORLD_HEIGHT = 12000

self.FOOD_COUNT = 1000

self.SNAKE_SPEED = 5

self.BOOST_SPEED_MULTIPLIER = 2.5
```

---

# Example ML Training Configuration

```python
self.PLAYER_ENABLED = False

self.SNAKE_COUNT = 100

self.FPS = 240

self.WORLD_WIDTH = 20000
self.WORLD_HEIGHT = 20000
```

Used for:
- reinforcement learning
- large simulations
- evolutionary training
