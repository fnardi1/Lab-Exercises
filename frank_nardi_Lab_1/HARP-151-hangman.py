CORRECT = "swoop"
guesses = 6
GAMEOVER = False
letters_guessed = []
word = []

def blanks_and_letters():
    for i in CORRECT:
        word.append("_ ")

def print_word_so_far():
    string_word = ""
    for i in word:
        string_word += i
    print(string_word)

def show_letters_guessed():
    letters = ""
    for letter in letters_guessed:
        letters += f"{letter} "
    return(letters)

blanks_and_letters()

while not GAMEOVER:
    print(f"The word has {len(CORRECT)} letters")
    print_word_so_far()
    print(f"You have {guesses} guesses left.")
    previous_guesses = show_letters_guessed()
    print(f"So far, you have guessed: {previous_guesses}")
    player_guess = input("Guess a letter ")
    print("_______________________________")

    if player_guess in letters_guessed:
        print("You already guessed that, guess again.")


    elif player_guess in CORRECT:
        letters_guessed.append(player_guess)
        for char in range(len(CORRECT)):
            if CORRECT[char] == player_guess:
                word[char] = player_guess + " "
        print(f"The letter {player_guess} is in the word!")
        if "_ " not in word:
            GAMEOVER = True
            print("You win!")
            print_word_so_far()
            print(f"You win! The word was {CORRECT}")

    elif player_guess not in CORRECT:
        guesses -= 1
        letters_guessed.append(player_guess)
        print(player_guess + " is not in the word.")
        if guesses == 0:
            GAMEOVER = True
            print(f"You lose. The correct word was {CORRECT}")
    print("_______________________________")
