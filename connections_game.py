import random
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

all_categories = {
    "Ends in 'ER'": ["CORNER", "ANSWER", "BLISTER", "PLUMBER"],
    "Mythical Creatures": ["PHOENIX", "GRIFFIN", "UNICORN", "KRAKEN"],
    "Anagrams of 'TAME'": ["MATE", "TEAM", "MEAT", "TAME"],
    "Poker Terms": ["FLUSH", "RIVER", "BLIND", "FOLD"],
    "Shades of Blue": ["AZURE", "NAVY", "COBALT", "TEAL"],
    "Greek Letters": ["ALPHA", "OMEGA", "DELTA", "SIGMA"],
    "Types of Rocks": ["IGNEOUS", "SEDIMENTARY", "METAMORPHIC", "BASALT"],
    "Musical Symbols": ["SHARP", "FLAT", "CLEF", "FERMATA"],
    "Lakers Legends": ["KOBE", "SHAQ", "MAGIC", "KAREEM"],
    "Warriors' Splash Bros Era": ["CURRY", "THOMPSON", "DURANT", "GREEN"],
    "Bulls' 90s Dynasty": ["JORDAN", "PIPPEN", "RODMAN", "KUKOC"],
    "Celtics' Big Three": ["PIERCE", "GARNETT", "ALLEN", "RONDO"],
    "Inception Cast": ["DICAPRIO", "HARDY", "PAGE", "WATANABE"],
    "The Avengers Cast": ["DOWNEY", "EVANS", "HEMSWORTH", "JOHANSSON"],
    "Pulp Fiction Cast": ["TRAVOLTA", "JACKSON", "THURMAN", "WILLIS"],
    "The Godfather Cast": ["BRANDO", "PACINO", "CAAN", "DUVALL"]
}

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
    session['categories'] = generate_game()
    session['words'] = shuffle_words(session['categories'])
    session['remaining_categories'] = list(session['categories'].keys())
    return render_template('game.html', words=session['words'], remaining=len(session['remaining_categories']))

@app.route('/check', methods=['POST'])
def check():
    selected_words = request.json['words']
    category = check_group(selected_words, session['categories'])
    
    if category:
        session['remaining_categories'].remove(category)
        session['words'] = [word for word in session['words'] if word not in selected_words]
        
        return jsonify({
            'correct': True,
            'category': category,
            'remaining_words': session['words'],
            'remaining_categories': len(session['remaining_categories'])
        })
    else:
        return jsonify({'correct': False})

if __name__ == "__main__":
    app.run(debug=True)
