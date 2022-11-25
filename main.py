import random
from words import word_list


def levels():
    diff = input("Choose a difficulty. Type 'easy' or 'medium' or 'hard': ")
    if diff == "easy":
        easy()

    elif diff == "medium":
        medium()

    elif diff == "hard":
        hard()

    else:
        print("Invalid input.")
        levels()


def easy():
    tries = 10
    print("You have chosen 'easy'.")
    print("You have {} guesses left.".format(tries))
    word = random.choice(word_list)
    guessed_letters = []
    progress = "_" * len(word)
    print("{} is the length of the word.".format(len(word)))
    print(word)

    while progress != word and tries > 0:
        guess = input("Enter a letter: ")
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            print("The guessed letters are: {}".format(guessed_letters))

        elif guess in word:
            if progress == word:
                break
            else:
                for i in range(len(word)):
                    if word[i] == guess:
                        progress = progress[:i] + guess + progress[i + 1:]
                tries -= 1
                print("You guessed {} so far.".format(progress))

        else:
            tries -= 1
            print("That letter is not in the word. You have {} guesses left.".format(tries))
            print("You guessed {} so far.".format(progress))

        if tries == 0:
            print("You have run out of guesses. You lose.")
            break

    if progress == word:
        print("You guessed the word! You win!")

    else:
        print("Such a failure. You lose.")


def medium():
    tries = 8
    count = 0
    print("You have chosen 'medium'.")
    print("You have {} guesses left.".format(tries))
    word = random.choice(word_list)
    guessed_letters = []
    progress = "_" * len(word)
    print("{} is the length of the word.".format(len(word)))

    while progress != word and tries > 0:
        guess = input("Enter a letter: ")
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            print("The guessed letters are: {}".format(guessed_letters))

        elif guess == word[count]:
            if progress == word:
                break
            else:
                progress = progress[:count] + guess + progress[count + 1:]
                count += 1
                tries -= 1
                print("You guessed {} so far.".format(progress))

        elif guess in word:
            tries -= 1
            print("That letter is not in the correct position. You have {} guesses left.".format(tries))

        else:
            tries -= 1
            print("That letter is not in the word. You have {} guesses left.".format(tries))
            print("You guessed {} so far.".format(progress))

        if tries == 0:
            print("You have run out of guesses. You lose.")
            break

    if progress == word:
        print("You guessed the word! You win!")

    else:
        last_chance = input("You have one last chance. Enter the word: ")

        if last_chance == word:
            print("You guessed the word! You win!")
        else:
            print("Such a failure. You lose.")


def hard():
    tries = 6
    hint = 2
    count_list = []
    print("You have chosen 'hard'.")
    print("You have {} guesses left.".format(tries))
    word = random.choice(word_list)
    guessed_words = []
    print("{} is the length of the word.".format(len(word)))
    print(word)
    guess = ""

    while guess != word and tries > 0:
        guess = input("Enter the word: ")
        if guess in guessed_words:
            print("You have already guessed that word.")
            print("The guessed words are: {}".format(guessed_words))

        elif guess == word:
            break

        else:
            tries -= 1
            print("That letter is not in the word. You have {} guesses left.".format(tries))
            if hint > 0:
                hint_aggred = input("Do you want a hint? Type 'yes' or 'no': ").upper()
                if hint_aggred == "YES":
                    count = random.randint(0, len(word) - 1)
                    while count in count_list:
                        count = random.randint(0, len(word) - 1)
                    print("{} is in word.".format(word[count]))
                    hint -= 1

        if tries == 0:
            print("You have run out of guesses. You lose.")
            break

    if guess == word:
        print("You guessed the word! You win!")

    else:
        print("Such a failure. You lose.")


if __name__ == '__main__':
    levels()