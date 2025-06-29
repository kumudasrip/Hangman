import random
import os

HANGMAN_PICS = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

word_bank = {
    "easy": [
        ("python", "A programming language and a snake"),
        ("banana", "A long yellow fruit"),
        ("planet", "Orbits a star"),
        ("bottle", "Used to hold liquids"),
        ("window", "Glass panel on a wall"),
        ("flower", "Grows in a garden, smells nice"),
        ("mirror", "Reflects your image"),
        ("button", "Used to fasten clothes")
    ],
    "medium": [
        ("architecture", "Art of designing buildings"),
        ("psychology", "Study of the human mind"),
        ("encyclopedia", "Book containing lots of knowledge"),
        ("entrepreneur", "Starts and runs a business"),
        ("transformation", "Complete change in form"),
        ("mathematics", "The study of numbers and shapes"),
        ("constitution", "The basic laws of a country"),
        ("philosopher", "A person who studies big questions")
    ],
    "hard": [
        ("abrogate", "To formally abolish or repeal a law"),
        ("anachronism", "Something out of place in time"),
        ("circumlocution", "The use of many words to say something simple"),
        ("conflagration", "A large destructive fire"),
        ("defenestration", "The act of throwing someone out of a window"),
        ("ephemeral", "Lasting for a very short time"),
        ("equanimity", "Mental calmness in a difficult situation"),
        ("grandiloquent", "Pompous or extravagant in speech"),
        ("impecunious", "Having little or no money"),
        ("inchoate", "Just begun and not fully developed"),
        ("intransigent", "Unwilling to change one's views or agree"),
        ("mellifluous", "Pleasant and musical to hear"),
        ("obfuscate", "To make unclear or confusing"),
        ("parsimonious", "Extremely unwilling to spend money"),
        ("pedantic", "Overly concerned with minor details"),
        ("perfidious", "Deceitful and untrustworthy"),
        ("recalcitrant", "Stubbornly uncooperative"),
        ("sesquipedalian", "Using long or complicated words"),
        ("vicissitude", "A change of circumstances or fortune"),
        ("zeitgeist", "The defining spirit of a particular era")
    ]
}

def choose_word_and_hint(level):
    word, hint = random.choice(word_bank[level])
    return word.strip(), hint.strip()

def update_leaderboard(name, score, filename="leaderboard.txt"):
    entries = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                try:
                    n, s = line.strip().rsplit(",", 1)
                    entries.append((n, int(s)))
                except:
                    continue

    entries.append((name, score))

    entries.sort(key=lambda x: x[1], reverse=True)
    entries = entries[:5]

    with open(filename, "w") as f:
        for n, s in entries:
            f.write(f"{n},{s}\n")

    return entries

def show_leaderboard(entries):
    print("\n🏆 Leaderboard (Top 5 Scores)")
    print("-" * 30)
    for i, (n, s) in enumerate(entries, 1):
        print(f"{i}. {n} - {s} points")
    print("-" * 30)

def play_game(score):
    print("\nChoose difficulty: Easy / Medium / Hard")
    while True:
        level = input("Enter difficulty: ").lower()
        if level in word_bank:
            break
        print("Invalid input. Please choose Easy, Medium, or Hard.")

    word, hint = choose_word_and_hint(level)
    word_letters = set(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 4 if level == "easy" else 5 if level == "medium" else 6

    print(f"\nHint: {hint}")
    print(f"You have {max_attempts} attempts to guess the word.")
    print("_ " * len(word))

    while wrong_guesses < len(HANGMAN_PICS) - 1 and word_letters:
        print(HANGMAN_PICS[wrong_guesses])
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print(f"Attempts left: {max_attempts - wrong_guesses}")

        current_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(current_word))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess.")

    if not word_letters:
        print(f"\n🎉 You guessed the word: {word}")
        score += 10
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\n💀 Game Over! The word was: {word}")
        score -= 5

    print(f"📊 Your current score: {score}")
    return score

print("🎮 Welcome to Hangman with Leaderboard!")
player_name = input("Enter your name: ").strip() or "Player"

score = 0
while True:
    score = play_game(score)
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print(f"\n👋 Thanks for playing, {player_name}! Your final score: {score}")
        leaderboard = update_leaderboard(player_name, score)
        show_leaderboard(leaderboard)
        break