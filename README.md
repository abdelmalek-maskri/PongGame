# Pong Game

This is a classic Pong game implemented in Python using the Turtle graphics library. The game features two paddles and a ball, where the objective is to beat the opponent by being the first to score 10 points. Each player controls a paddle on either side of the screen, and the game speeds up as you score more points.

## Features

- Two-player gameplay: Control the paddles using keyboard commands.
- Scoring system: Tracks each player's score and updates it on the screen.
- Ball speed increases with each hit to add challenge.
- Collision detection: The ball bounces off paddles and walls.
- Game over condition when a player reaches 10 points.

## Prerequisites

To run this game, you need to have Python installed on your computer. Python can be downloaded from [here](https://www.python.org/downloads/).

## How to Play

1. **Starting the Game**: Run the `main.py` script to start the game.
2. **Player Controls**:
   - **Left Paddle**: Use 'W' to move up and 'S' to move down.
   - **Right Paddle**: Use 'Up Arrow' to move up and 'Down Arrow' to move down.

## Setup and Run

1. Clone this repository to your local machine or download the files.
2. Navigate to the directory containing the game files in your terminal or command prompt.
3. Run the command `python main.py` to start the game.

## Game Files

- `main.py`: Initializes the game, creates the window, and contains the game loop.
- `paddle.py`: Contains the `Paddle` class that creates and manages paddle behavior.
- `ball.py`: Contains the `Ball` class that handles ball movement and collision logic.
- `scoreboard.py`: Manages the score display and updates scores.

## Customizations

You can customize the game by modifying:
- Ball speed and paddle size for different difficulty levels.
- Scoring rules and game over conditions.
- Visuals and colors to change the game's theme.


