from wordList import words
import random
import string


#this function will return valid words from list of words
def get_valid_word(words):

    #randomly chooses the word from list of words
    word = random.choice(words)
    while word == ' ' or word == '-':
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    copyWord = word_letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #to track set of used letters
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left, You have used these letters: ",
              ' '.join(used_letters))

        #what current word is A_ID
        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print("Current word is: ", ' '.join(word_list))

        #getting user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # Take away a life for each wrong answer

        elif user_letter in used_letters:
            print("You have already guessed this letter , guess another \n")

        else:
            print("Wrong input \n")

    #reaches here if length of word_letters == 0 OR when lives = 0
    if lives == 0:
        print("Sorry, no Lives left")
        print("The word was: ", word)
    else:
        print("You have gussed the word: ", word, "!!")


if __name__ == "__main__":
    hangman()
