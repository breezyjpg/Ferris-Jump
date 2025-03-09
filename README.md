# Ferris Jump

Ferris Jump is a simple 2D platformer game built with Pygame, where the player controls a crab that jumps on floating platforms to stay in the game and increase their score. If the crab falls off the screen, the game ends.

## How to Play
- Use the **Left Arrow Key** (`←`) to move left.
- Use the **Right Arrow Key** (`→`) to move right.
- The crab jumps automatically when landing on platforms.
- Keep jumping on platforms to increase your score.
- If the crab falls off the screen, the game is over.

## Features
- Randomly generated platforms.
- Smooth jumping mechanics.
- Score tracking.
- Game Over screen with final score display.

## Installation
1. Ensure you have **Python 3** installed on your system.
2. Install Pygame if you haven't already:
   ```sh
   pip install pygame
   ```
3. Clone or download the project files.

## Running the Game
1. Make sure the `images` folder contains the required assets:
   - `background.png`
   - `crab.png`
   - `plate.png`
2. Run the game script:
   ```sh
   python main.py
   ```

## Folder Structure
```
FerrisJump/
│── images/
│   ├── background.png
│   ├── crab.png
│   ├── plate.png
│── main.py
│── README.md
```

## Dependencies
- Python 3
- Pygame

## Notes
- The game window size is **500x700 pixels**.
- Platforms are randomly positioned each time the game starts.
- The crab's sprite flips when moving left or right.

## Future Improvements
- Add sound effects and background music.
- Improve graphics with animations.
- Implement a start menu and restart functionality.

Enjoy playing Ferris Jump!
