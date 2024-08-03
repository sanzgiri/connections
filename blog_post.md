# Building a Connections Game: A Step-by-Step Journey

In this blog post, I'll walk you through the process of creating a web-based Connections Game, inspired by the popular New York Times word puzzle. This project combines Python backend development with Flask, and frontend development using HTML, CSS, and JavaScript. Let's dive in!

## 1. Setting Up the Project

We started by creating a new Python project and setting up a virtual environment. Our initial requirements included Flask for the web framework.

```bash
mkdir connections-game
cd connections-game
python -m venv venv
source venv/bin/activate
pip install Flask
```

## 2. Creating the Game Logic

The core of our game is the Python script `connections_game.py`. Here's a breakdown of its main components:

1. **Loading Categories**: We created a function to load categories and words from a text file.
2. **Generating a Game**: This function randomly selects categories and words for each game.
3. **Shuffling Words**: We shuffle the words to display them randomly on the game board.
4. **Checking Groups**: This function verifies if a group of selected words belongs to the same category.

## 3. Building the Flask Application

We used Flask to create our web application. Here's a simplified version of our main Flask routes:

```python
@app.route('/')
def index():
    return start_new_game()

@app.route('/check', methods=['POST'])
def check():
    # Logic to check submitted words
    pass

@app.route('/new_game', methods=['POST'])
def new_game():
    return start_new_game()
```

## 4. Designing the Frontend

We created an HTML template (`game.html`) with embedded JavaScript for interactivity. The design focuses on a clean, responsive layout inspired by the NYT Connections game.

Key features of our frontend include:
- A 4x4 grid of word buttons
- A submit button for checking selected words
- An info bar showing game progress
- Animations for correct and incorrect guesses

## 5. Styling with CSS

We used custom CSS to style our game, giving it a modern, minimalist look. We chose a color scheme and typography that's easy on the eyes and maintains readability.

## 6. Adding Interactivity with JavaScript

JavaScript plays a crucial role in our game's interactivity. We implemented functions for:
- Selecting and deselecting words
- Submitting groups for checking
- Updating the game state based on server responses
- Starting a new game

## 7. Handling Game State

We used Flask's session management to maintain game state between requests. This allows us to keep track of:
- Remaining categories
- Number of submissions
- Current words on the board

## 8. Implementing Game Over Logic

We added logic to end the game when all categories are found or when the maximum number of submissions is reached. At game over, we display all categories and their words, and offer a "New Game" button.

## 9. Testing and Debugging

Throughout the development process, we continuously tested our application, both manually and by logging key information. We used Flask's debug mode during development for easier troubleshooting.

## 10. Deployment

Finally, we prepared our application for deployment. We created a `requirements.txt` file and a `vercel.json` configuration file for deploying to Vercel.

```json
{
    "version": 2,
    "builds": [
        {
            "src": "connections_game.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "connections_game.py"
        }
    ]
}
```

## Conclusion

Building this Connections Game was an exciting journey that combined various aspects of web development. From backend logic to frontend design and interactivity, this project showcases how Python and JavaScript can work together to create an engaging web application.

The final product is a fun, interactive game that challenges players to find connections between words, much like the NYT original. Feel free to clone the repository, make your own modifications, and enjoy playing!

Happy coding!
