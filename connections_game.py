import random
import os
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

MAX_SUBMISSIONS = 4

def load_categories(filename='categories.txt'):
    all_categories = {}
    with open(filename, 'r') as f:
        for line in f:
            category, *words = line.strip().split('|')
            all_categories[category] = words
    return all_categories

all_categories = load_categories()

def generate_game():
    categories = random.sample(list(all_categories.keys()), 4)
    game_categories = {}
    
    for category in categories:
        game_categories[category] = random.sample(all_categories[category], 4)
    
    return game_categories

def shuffle_words(categories):
    all_words = [word for category in categories.values() for word in category]
    random.shuffle(all_words)
    return all_words

def check_group(group, categories):
    for category, words in categories.items():
        if set(group).issubset(set(words)):
            return category
    return None

@app.route('/')
def index():
    return start_new_game()

def start_new_game():
    session['categories'] = generate_game()
    session['words'] = shuffle_words(session['categories'])
    session['remaining_categories'] = list(session['categories'].keys())
    session['submissions'] = 0
    return render_template('game.html', words=session['words'], remaining=len(session['remaining_categories']), max_submissions=MAX_SUBMISSIONS)

@app.route('/new_game', methods=['POST'])
def new_game():
    return start_new_game()

@app.route('/check', methods=['POST'])
def check():
    selected_words = request.json['words']
    app.logger.info(f"Selected words: {selected_words}")  # Log the selected words
    category = check_group(selected_words, session['categories'])
    
    session['submissions'] += 1
    game_over = session['submissions'] >= MAX_SUBMISSIONS or len(session['remaining_categories']) == 0
    
    if category:
        session['remaining_categories'].remove(category)
        session['words'] = [word for word in session['words'] if word not in selected_words]
        app.logger.info(f"Correct group found: {category}")  # Log the correct category
        
        return jsonify({
            'correct': True,
            'category': category,
            'remaining_words': session['words'],
            'remaining_categories': len(session['remaining_categories']),
            'submissions': session['submissions'],
            'game_over': game_over,
            'all_categories': session['categories'] if game_over else None
        })
    else:
        app.logger.info("Incorrect group submitted")  # Log incorrect submission
        return jsonify({
            'correct': False,
            'submissions': session['submissions'],
            'game_over': game_over,
            'all_categories': session['categories'] if game_over else None
        })

if __name__ == "__main__":
    app.run(debug=True)
