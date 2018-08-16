__author__ = "Adeyoriju Olabode Wilson."
__email__ = "whilson03@gmail.com"
#  created 30 - 8 - 2017
# last modified 24 july 2018
#  python version 3
# word game that displays incomplete words and user is required to type in the complete word to win.
import random


def banner():
    """
     This is the games welcome screen and also accepts the players name as input
    :return: players name.
    """
    name = input("please enter your name: ")
    print("|*********************************" + "*" * len(name) + "|")
    print("|*HELLO {} welcome to word frenzy".upper().format(name), "* |")
    print("|*********************************" + "*" * len(name) + "|")
    print()
    return name


def get_word():
    """
    read a file containing series of words to be used in the game.
    :return: A list of all five letter words and above.
    """
    word_list = []
    try:
        file = open("words_file.txt", "r")
        texts = file.read()
        text_list = texts.split()  # split at blank spaces
        for words in text_list:
            if len(words) >= 5:
                word_list.append(words)
        file.close()
    except IOError as e:
        print("**TEXT FILE FOR WORDS NOT FOUND:** ", e)
    return word_list


def random_word(word_list):
    """
    This functions selects a single random word from a list of words and shuffles the list afterwards.
    :param word_list: list of all the words imported from the txt file.
    :return: A single random word.
    """
    for words in range(len(word_list)):
        word = random.choice(word_list)
        random.shuffle(word_list)
        return word


def give_blank(word):
    """
    :param word: A single word, to be made incomplete.
    :return: Same word but now incomplete, removed letters are replaced with underscores.
    """
    output = list(word)  # create a list of all letters in the word.
    # control statements to set the no of underscores in each word.
    if len(word) <= 7:
        no_of_blank = 2
    else:
        no_of_blank = 3
    index_list = []  # get list of unique indexes to change
    counter = 0
    while len(index_list) < no_of_blank:  # no of indexes to be changed depending on word length.
        position = random.randrange(len(word))  # get random indexes
        if position not in index_list:  # ensure that indexes do not repeat in d list.
            index_list.append(position)
            counter += 1
        else:
            counter += 1
    # print(indexList)
    # print(word)
    for index, letter in enumerate(word):
        # print(index,letter)
        if index in index_list:
            output[index] = "_"  # slot in underscores to the random indexes.

    blank = " ".join(output)
    return blank


def show_word(blank):
    """
    this function is to display the blank word to the user.
    :param blank: the chosen word ,but now with underscores ..
    :return: nothing
    """
    print("##==> ", blank)


def get_input(word, name):
    """
    :param word: takes in the word to check if the user input is correct.
    :param name: for reference in the congratulatory message .
    :return: users answer.
    """
    user_input = input("Type In The complete word HERE :>>  ".upper())
    #  list of random congratulatory messages .
    celeb_list = ["FANTASTIC", "AWESOME", "WONDERFUL", "SUPERB", "EXCELLENT", "GREAT"]
    celebrate = random.choice(celeb_list)
    if user_input == word:
        print("{} YOU WERE CORRECT..".format(celebrate))
        print()
    else:
        print("OOPS , TRY AGAIN {}".format(name.upper()))
        print("\t\t\t\t==> the correct word is ** {} **".format(word))
        print()
    return user_input


def main():
    # load all words to be used from the the text.
    load_word = get_word()
    # initialize game screen
    display_screen = banner()
    # no of times the game should run, can be increased if need be.
    attempts = 0
    score = 0
    while attempts <= 10:  # default of ten attempts.
        attempts += 1
        # randomly pick  one word at a time.
        computer_choice = random_word(load_word)
        # place underscores in the selected words randomly
        get_blank = give_blank(computer_choice)
        # shows the incomplete words
        show_word(get_blank)
        # get the players input and cross check if correct with the incomplete words.
        player = get_input(computer_choice, display_screen)
        if computer_choice == player:  # score player for correct answers
            score += 10
        else:
            score += 0
    print("YOUR TOTAL POINT IS {}".format(score))


if __name__ == '__main__':
    main()
