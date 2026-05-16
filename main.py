from CONFIG import GameConfig
from game.game import Game


def main():
    config = GameConfig(
        width=1800,
        height=1000,
        fps=60,
    )

    game = Game(config)
    game.run()


if __name__ == "__main__":
    main()