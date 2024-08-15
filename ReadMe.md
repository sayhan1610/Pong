# Pong Game

A classic Pong game implemented using Pygame. Play against the CPU or a friend in this two-player game. Features include a home screen, game pausing, and sound effects for hits and scores.

## Features

- **Two Game Modes**: Play against the CPU or another human player.
- **Pause and Resume**: Pause the game and return to the home screen or resume playing.
- **Sound Effects**: Audio cues for hits and scoring.
- **Score Tracking**: Keeps track of the score and announces the winner when a player reaches the winning score.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sayhan1610/pong.git
   ```

2. **Navigate to the Project Directory**

   To get started with the Paper Airplane Game, simply run the installation files provided.

## Controls

- **Home Screen**

  - `1`: Play against CPU
  - `2`: Play against Human

- **In-Game**
  - `W`: Move Player 1's paddle up
  - `S`: Move Player 1's paddle down
  - `UP Arrow`: Move Player 2's paddle up (Human vs Human mode only)
  - `DOWN Arrow`: Move Player 2's paddle down (Human vs Human mode only)
  - `ESC`: Pause the game
  - `Q`: Quit to the Home Screen (when paused)
  - `R`: Restart the game (after a game over)

## Customization

- **Paddle Size & Speed**: Adjust the `PADDLE_WIDTH`, `PADDLE_HEIGHT`, and `PADDLE_SPEED` variables in the script.
- **Ball Size & Speed**: Modify the `BALL_SIZE` and `BALL_SPEED` variables.
- **Winning Score**: Change the winning score from 10 to any other number by modifying the `if score1 == 10` and `if score2 == 10` conditions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request.
