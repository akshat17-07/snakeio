import json
import os


class SaveSystem:

    def __init__(self):

        # ROOT
        self.data_folder = "data"

        # GENERATIONS
        self.generations_folder = (
            os.path.join(
                self.data_folder,
                "generations",
            )
        )

        # CREATE FOLDERS
        os.makedirs(
            self.generations_folder,
            exist_ok=True,
        )

    # =====================================
    # SAVE GENERATION
    # =====================================
    def save_generation(
        self,
        snakes,
        generation,
    ):

        generation_data = []

        for snake in snakes:

            genome = {}

            if snake.ai_controller:

                genome = (
                    snake.ai_controller.genome
                )

            snake_data = {

                # GENERATION
                "generation": generation,

                # FITNESS
                "fitness": snake.fitness,

                # STATS
                "length": snake.length,
                "kills": snake.kills,
                "food_eaten": (
                    snake.food_eaten
                ),
                "frames_alive": (
                    snake.frames_alive
                ),

                # GENOME
                "genome": genome,
            }

            generation_data.append(
                snake_data
            )

        filename = os.path.join(
            self.generations_folder,
            f"generation_{generation}.json",
        )

        with open(
            filename,
            "w",
        ) as f:

            json.dump(
                generation_data,
                f,
                indent=4,
            )

    # =====================================
    # SAVE BEST GENOME
    # =====================================
    def save_best_genome(
        self,
        snake,
        generation,
    ):

        if not snake.ai_controller:
            return

        data = {

            "generation": generation,

            "fitness": snake.fitness,

            "genome": (
                snake.ai_controller.genome
            ),
        }

        with open(
            os.path.join(
                self.data_folder,
                "best_genome.json",
            ),
            "w",
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
            )

    # =====================================
    # LOAD BEST GENOME
    # =====================================
    def load_best_genome(self):

        filename = os.path.join(
            self.data_folder,
            "best_genome.json",
        )

        if not os.path.exists(
            filename
        ):
            return None

        with open(
            filename,
            "r",
        ) as f:

            data = json.load(f)

        return data
    
    # =====================================
    # GET LATEST GENERATION
    # =====================================
    def get_latest_generation(self):

        files = os.listdir(
            self.generations_folder
        )

        generations = []

        for file in files:

            if not file.startswith(
                "generation_"
            ):
                continue

            number = (
                file.replace(
                    "generation_",
                    ""
                )
                .replace(".json", "")
            )

            try:
                generations.append(
                    int(number)
                )

            except:
                pass

        if len(generations) == 0:
            return 1

        return max(generations)