# Snake.io AI Simulation

A Snake.io-style multiplayer simulation built with Python and Pygame.

The project is built with a machine-learning-ready architecture so AI systems can later be integrated without changing the game engine.

Supported future AI systems:
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
- Random AI boosting
- Modular AI controller architecture
- ML-ready environment structure

## Engine Architecture
- World-space rendering
- Camera-space rendering
- Config-driven setup
- Expandable game engine structure

---

# Controls

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

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install pygame-ce
```

---

# Run Project

```bash
python main.py
```

---

# Configuration

All settings are located in:

```python
config.py
```

---

## Screen Settings

### `SCREEN_WIDTH`

Controls visible game window width.

### `SCREEN_HEIGHT`

Controls visible game window height.

---

## World Settings

### `WORLD_WIDTH`

Controls total playable world width.

### `WORLD_HEIGHT`

Controls total playable world height.

Larger worlds:
- increase exploration
- spread snakes further apart
- improve ML simulations

---

## Performance

### `FPS`

Controls game update/render speed.

Higher FPS:
- smoother gameplay
- more CPU usage

---

## Grid Settings

### `GRID_SPACING`

Controls spacing between background grid lines.

---

## Player Settings

### `PLAYER_ENABLED`

```python
self.PLAYER_ENABLED = True
```

### True
- human player enabled

### False
- AI-only simulation
- useful for ML training

---

## Snake Settings

### `SNAKE_COUNT`

Number of AI snakes.

### `INITIAL_LENGTH`

Starting snake body length.

### `SNAKE_SPEED`

Base snake movement speed.

### `TURN_SPEED`

Snake turning speed.

### `SNAKE_RADIUS`

Snake head/body size.

---

## Boost Settings

### `BOOST_SPEED_MULTIPLIER`

Boost movement speed multiplier.

### `BOOST_LOSS_AMOUNT`

Length lost per frame while boosting.

### `MIN_BOOST_LENGTH`

Minimum snake length required for boosting.

---

## Food Settings

### `FOOD_COUNT`

Total food pellets in the world.

### `FOOD_RADIUS`

Visual food size and collision size.

---

## Death Settings

### `FOOD_DROP_DIVISOR`

Controls how much food drops when snakes die.

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

The AI system is completely separated from rendering and game logic.

This allows easy replacement of:
- Random AI
- Neural Networks
- Reinforcement Learning
- Genetic Algorithms

without modifying the engine.

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
