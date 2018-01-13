import random

player_names = []
# word_to_guess = None
letters_missed = []

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
    print("Word to guess: {}" .format(word_to_guess))
    word_length = len(word_to_guess)
    guess = ['_' for i in range(word_length)]
    lives = 6
    flag = None

    print("====================================================")
    print("\nLet us begin the game!")
    print("You will have 6 lives as a group to guess the word.")
    print("The current word is {} letters long\n" .format(word_length))
    
    while(True):
        print("Word: ", end='')
        for i in guess:
            print(i,' ', end='')
            
        print()

        if (lives == 0):
            print("\nYou have run out of lives. Better luck next time!")
            print("The correct word was {}\n" .format(word_to_guess.upper()))
            exit()
        if (not '_' in guess):
            print("\nCongratulations! You figured out the word.")
            exit()

        print("Lives: {}" .format(lives))
        print("Misses: ", end = '')
        for i in letters_missed:
            print(i,' ',end='')

        input_guess = input("\nWhat is your guess? ")

        if (len(input_guess) > 1):
            print("Please only input 1 letter")
            continue
        elif (input_guess.isalpha()):
            flag = check_letter(input_guess.upper(), word_to_guess.upper())

        if (flag == 1):
            for i in range(word_length):
                if(word_to_guess[i] == input_guess):
                    guess[i] = input_guess.upper()
        elif (flag == 0):
            lives = lives - 1
  
def add_player_to_list(players):
    for name in range(players):
        name = (input("What is your name Player: "))
        player_names.append(name)

def random_words():
    words = ["headline", "soup", "filter", "command", "mass", "truck", "tumble", "flourish", "squash", "mouth"]
    return random.choice(words)

def check_letter(letter, word_to_guess):
    flag = 0
    
    if (letter in word_to_guess): 
            flag = 1
    if (flag == 0):
        if (not letter in letters_missed):
            letters_missed.append(letter.upper())
    
    return flag
    
def print_player_names():
    print("\nThe current players are: ")
    for name in player_names:
        print(name)

def game():
    players()

game()

