from wordslist import words
from hangmanart import hangman_art
import random

def display_hint(hint):
    print(" ".join(hint))
def display_man(nr_guesses):
    print("******************")
    for line in hangman_art[nr_guesses]:
        print(line)
    print("******************")
def display_answer(answer):
    print(" ".join(answer))


def main():
    wrong_guesses = 0
    guessed_letters = set()
    answer = random.choice(words)
    len_of_word = len(answer)
    hints = ["_"] * len_of_word
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hints)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue
        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}!")
            continue
        elif guess in answer:
            for i in range(len_of_word):
                if answer[i] == guess:
                    hints[i] = guess
        else:
            wrong_guesses+=1
        # print(dir(guessed_letters))
        guessed_letters.add(guess)
        if "_" not in hints:
            display_man(wrong_guesses)
            display_answer(answer)
            print("=============")
            print("  YOU WIN!  ")
            print("=============")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("=============")
            print("  YOU LOSE!  ")
            print("=============")
            is_running = False

if __name__ == "__main__":
    main()