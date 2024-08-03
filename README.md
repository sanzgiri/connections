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
   pip install -r requirements.txt
   ```

## Configuration

The game categories and words are stored in the `categories.txt` file. Each line in this file represents a category and its words, separated by the `|` character. The format is:

```
Category Name|Word1|Word2|Word3|Word4
```

You can edit this file to add, remove, or modify categories and words.

## How to Run Locally

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000`

## Deployment to Vercel

1. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

2. Login to your Vercel account:
   ```
   vercel login
   ```

3. Deploy the app:
   ```
   vercel
   ```

4. Follow the prompts to complete the deployment.

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
