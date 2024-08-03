import random

def generate_game():
    all_categories = {
        "Ends in 'ER'": ["CORNER", "ANSWER", "BLISTER", "PLUMBER"],
        "Mythical Creatures": ["PHOENIX", "GRIFFIN", "UNICORN", "KRAKEN"],
        "Anagrams of 'TAME'": ["MATE", "TEAM", "MEAT", "TAME"],
        "Poker Terms": ["FLUSH", "RIVER", "BLIND", "FOLD"],
        "Shades of Blue": ["AZURE", "NAVY", "COBALT", "TEAL"],
        "Greek Letters": ["ALPHA", "OMEGA", "DELTA", "SIGMA"],
        "Types of Rocks": ["IGNEOUS", "SEDIMENTARY", "METAMORPHIC", "BASALT"],
        "Musical Symbols": ["SHARP", "FLAT", "CLEF", "FERMATA"]
    }
    
    categories = random.sample(list(all_categories.keys()), 4)
    game_categories = {}
    
    for category in categories:
        game_categories[category] = random.sample(all_categories[category], 4)
    
    return game_categories

def shuffle_words(categories):
    all_words = [word for category in categories.values() for word in category]
    random.shuffle(all_words)
    return all_words

def display_words(words):
    for i, word in enumerate(words, 1):
        print(f"{i}. {word}", end="  ")
        if i % 4 == 0:
            print()
    print()

def check_group(group, categories):
    for category, words in categories.items():
        if set(group).issubset(set(words)):
            return category
    return None

def play_game():
    print("Welcome to the Connections Game!")
    print("Group words into categories. Enter word numbers separated by spaces.")
    print("Enter 'q' to quit.")
    
    categories = generate_game()
    words = shuffle_words(categories)
    remaining_categories = list(categories.keys())
    
    while remaining_categories:
        print("\nRemaining categories:", len(remaining_categories))
        display_words(words)
        
        user_input = input("Enter your group (e.g., '1 5 9 13'): ").strip().lower()
        
        if user_input == 'q':
            print("Thanks for playing!")
            return
        
        try:
            indices = [int(i) - 1 for i in user_input.split()]
            if len(indices) != 4 or any(i < 0 or i >= len(words) for i in indices):
                raise ValueError
            
            group = [words[i] for i in indices]
            category = check_group(group, categories)
            
            if category:
                print(f"Correct! You found the '{category}' category.")
                remaining_categories.remove(category)
                words = [word for word in words if word not in group]
            else:
                print("Incorrect. Try again!")
        
        except ValueError:
            print("Invalid input. Please enter 4 valid numbers.")
    
    print("Congratulations! You've found all categories.")

if __name__ == "__main__":
    play_game()
