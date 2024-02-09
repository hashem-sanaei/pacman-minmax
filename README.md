# Pacman MinMax

This project is a Python implementation of the classic Pacman game, using the MinMax algorithm for decision making.

## Files

- `Main.py`: This is the main entry point of the application. It contains the `run_game` function which starts the game, and the `minimax` function which implements the MinMax algorithm.
- `Gameboard.py`: This file defines the `Gameboard` class which represents the game board. It includes methods for setting obstacles and implementing the A* algorithm to find the shortest path to the foods.
- `Pacman_ghavi.py`: This file defines the `Pacman_ghavi` class which represents the Pacman character.
- `Ghost.py`: This file defines the `Ghost` class which represents the Ghost characters.

## Pacman Algorithm

The Pacman game in this project uses a combination of the MinMax algorithm and the A* algorithm to make decisions and find paths.

### MinMax Algorithm

The MinMax algorithm is used to make decisions for the Ghost characters. This algorithm simulates all possible game states up to a certain depth and evaluates them using a heuristic function. The Ghost characters then make the move that leads to the best possible outcome according to this evaluation.

The MinMax algorithm is implemented in the `minimax` function in the [`Main.py`](Main.py) file.

### A* Algorithm

The A* algorithm is used to find the shortest path from the Pacman character to the foods on the game board. This algorithm uses a heuristic function to estimate the cost of moving from one point to another, and it always chooses the path with the lowest estimated cost.

The A* algorithm is implemented in the `a_star_to_foods` method of the `Gameboard` class in the [`Gameboard.py`](Gameboard.py) file.

### Pacman Character

The Pacman character, represented by the `Pacman_ghavi` class in the [`Pacman_ghavi.py`](Pacman_ghavi.py) file, moves around the game board and eats food. The player controls the Pacman character.

## How to Run

To run the game, execute the `Main.py` file:

```sh
python Main.py