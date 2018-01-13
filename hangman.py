import random

player_names = []
# word_to_guess = None
lives = 6
letters_missed = []
guess = None

def players():
    print("----------------------")
    print("Welcome to Hangman!")
    print("----------------------") 

    players = int(input("\nHow many players are going to play?")) 

    add_player_to_list(players)

    more_players = None

    while(True):
        more_players = input("\nThere are currently " + str(players) + " players. Is that correct? (Yes/No) ").lower()
        
        if (more_players != "yes" and more_players != "no"):
            print("Wrong input. Please input yes or no")
        elif (more_players == "no"): 
            how_many = int(input("How many more players will join? "))
            add_player_to_list(how_many)
            break
        elif (more_players == "yes"):
            break

    print_player_names()
    hangman()
    # print("The current players are: {}".format(player_names))
    
def hangman():
    word_to_guess = random_words()
    word_length = len(word_to_guess)
    guess = ['_' for i in range(word_length)]

    print("====================================================")
    print("\nLet us begin the game!")
    print("You will have 6 lives as a group to guess the word.")
    print("The current word is {} letters long\n" .format(word_length))
    
    while(True):
        print("Word: ", end='')
        for i in guess:
            print(i,' ', end='')
            
        print()

        print("Lives: {}" .format(lives))
        print("Misses: ", end = '')
        for i in letters_missed:
            print(i,' ',end='')

        input_guess = input("What is your guess? ")

        if (len(input) > 1):
            print("Please only input 1 letter")
            continue
        elif (input.isalpha()):
            check_letter(input, word_length, word_to_guess)
        
        
    


def add_player_to_list(players):
    for name in range(players):
        name = (input("What is your name Player: "))
        player_names.append(name)

def random_words():
    words = ["headline", "soup", "filter", "command", "mass", "truck", "tumble", "flourish", "squash", "mouth"]
    return random.choice(words)

def check_letter(letter, word_length, word_to_guess):
    for i in range(word_length):


def print_player_names():
    print("\nThe current players are: ")
    for name in player_names:
        print(name)

def game():
    players()

game()

