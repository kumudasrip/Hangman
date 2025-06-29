import random


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
        ("keyboard", "Used to type on a computer"),
        ("triangle", "Shape with 3 sides"),
        ("backpack", "Carried on the shoulders"),
        ("hangman", "This very game!"),
        ("difficult", "The opposite of easy"),
        ("calendar", "Keeps track of days and months"),
        ("elephant", "Largest land animal"),
        ("internet", "Connects the world digitally")
    ],
    "hard": [
        ("architecture", "Art of designing buildings"),
        ("psychology", "Study of the human mind"),
        ("encyclopedia", "Book containing lots of knowledge"),
        ("entrepreneur", "Starts and runs a business"),
        ("transformation", "Complete change in form"),
        ("mathematics", "The study of numbers and shapes"),
        ("constitution", "The basic laws of a country"),
        ("philosopher", "A person who studies big questions")
    ]
}

def choose_word_and_hint(level):
    word, hint = random.choice(word_bank[level])
    return word.strip(), hint.strip()

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
    max_attempts = 8 if level == "easy" else 6 if level == "medium" else 5

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


print("🎮 Welcome to Hangman with Score Tracking!")

score = 0
while True:
    score = play_game(score)
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print(f"\n👋 Thanks for playing! Your final score: {score}")
        break
