# Connections Game

This is a web-based version of the Connections game, inspired by the NYT Connections game.

## Requirements

- Python 3.7+
- Flask
- Flask-Session

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/connections-game.git
   cd connections-game
   ```

2. Install the required packages:
   ```
   pip install flask flask-session
   ```

## How to Run

1. Start the Flask server:
   ```
   python connections_game.py
   ```

2. Open a web browser and go to `http://localhost:5000`

## How to Play

1. The game will display 16 words in a grid.

2. Your goal is to find groups of 4 words that belong to the same category.

3. Click on 4 words you think belong together.

4. Click the "Submit Group" button to check your guess.

5. If your guess is correct, those words will be removed and you'll be told which category you've found.

6. If your guess is incorrect, you can try again.

7. The game continues until you've found all categories.

## Game Rules

- There are 4 categories, each containing 4 words.
- You must find all 4 words in a category to complete it.
- The game ends when you've found all 4 categories.

Enjoy playing the Connections Game!
