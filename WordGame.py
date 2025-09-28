import random

def inWord(letter, word):
    """Returns True if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns True if letter is in the given spot in the word"""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns feedback:
    - Capital letter if the letter is in the right spot
    - Lowercase letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all
    """
    result = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result += myGuess[i].lower()
        else:
            result += "*"
    return result

def main():
    # Load word list and choose a random word
    with open("words.txt", 'r') as wordFile:
        wordList = wordFile.read().splitlines()
    todayWord = random.choice(wordList).strip().lower()

    print("Welcome to Word Game!")
    print(f"Guess the {len(todayWord)}-letter word. You have 6 tries.\n")

    for attempt in range(6):
        guess = input(f"Attempt {attempt + 1}: ").strip().lower()

        if len(guess) != len(todayWord):
            print(f"Please enter a {len(todayWord)}-letter word.\n")
            continue

        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if guess == todayWord:
            print("You guessed the word correctly!")
            break
    else:
        print(f"Out of tries! The word was: {todayWord}")

if __name__ == '__main__':
    main()

