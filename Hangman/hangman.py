import random
import cozmo
import os
from collections import defaultdict

player_names = []
player_scores = []
# word_to_guess = None
letters_missed = []

def players(robot):
    print("----------------------")
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabChatty).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    robot.say_text("Welcome to Hangman", False, False, 0.5).wait_for_completed()
    print("Welcome to Hangman!")
    print("Please wait for me to finish talking before typing anything.")
    robot.say_text("Please wait for me to finish talking before typing anything.", False, False, 0.5).wait_for_completed()
    print("----------------------") 

    while(True):
        try:
            robot.say_text("How many humans are going to play", False, False, 0.5).wait_for_completed()
            players = int(input("\nHow many humans are going to play? ")) 
        except ValueError:
            action1 = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
            action2 = robot.say_text("That's not a number. Please input a number", False, False, 0.5, in_parallel=True).wait_for_completed()
            print("That's not a number. Please input a number")
            continue
        else:
            print()
            break
            
    add_player_to_list(players, robot)

    more_players = None

    while(True):
        robot.say_text("There are currently " + str(len(player_names)) + " human players. Is that correct? Yes or no?", False, False, 0.5).wait_for_completed()
        more_players = input("\nThere are currently " + str(len(player_names)) + " human players. Is that correct? (Yes/No) ").lower()
        
        if (more_players != "yes" and more_players != "no"):
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
            robot.say_text("Wrong input. please input yes or no", False, False, 0.5).wait_for_completed()
            print("Wrong input. Please input yes or no")
        elif (more_players == "no"): 
            robot.say_text("How many more human players will join?", False, False, 0.5).wait_for_completed()
            how_many = int(input("How many more human players will join? "))
            add_player_to_list(how_many, robot)
            continue
        elif (more_players == "yes"):
            break
    
    print_player_names(len(player_names), robot)
    hangman(robot)
    # print("The current players are: {}".format(player_names))
    
def hangman(robot):
    word_to_guess = random_words()
    # robot.say_text("Word to guess: {}".format(word_to_guess), False, False, 0.5).wait_for_completed()
    # print("Word to guess: {}" .format(word_to_guess))
    word_length = len(word_to_guess)
    guess = ['_' for i in range(word_length)]
    lives = 6
    flag = None
    number_of_players = len(player_names)
    current_player = 0

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabPartyTime).wait_for_completed()
    print("====================================================")
    robot.say_text("Let us begin the game", False, False, 0.5).wait_for_completed()
    print("\nLet us begin the game!")
    robot.say_text("You will have six tries as a group to guess the word", False, False, 0.5).wait_for_completed()
    print("You will have 6 lives as a group to guess the word.")
    robot.say_text("The current word is {} letters long".format(word_length), False, False, 0.5).wait_for_completed()
    print("The current word is {} letters long" .format(word_length))
    robot.say_text("If you would like to check the scores, type in score.", False, False, 0.5).wait_for_completed()
    print("If you would like to check the scores, type in score.\n")
    print("Please only input 1 letter at a time.")
    robot.say_text("Please only input 1 letter at a time.", False, False, 0.5).wait_for_completed()
    print("Please wait for me to finish talking before typing anything.")
    robot.say_text("Please wait for me to finish talking before typing anything.", False, False, 0.5).wait_for_completed()
    
    while(True):        
        check_win_condition(lives, guess, word_to_guess,robot)

        print("Word: ", end='')
        for i in guess:
            print(i,' ', end='')
        
        print("")

        print("Lives: {}" .format(lives))
        print("Misses: ", end = '')
        for i in letters_missed:
            print(i,' ',end='')

        robot.say_text("What is your guess: {}? " .format(player_names[current_player]), False, False, 0.5).wait_for_completed()
        input_guess = input("\nWhat is your guess {}? " .format(player_names[current_player]))
        print("")
        if (len(input_guess) > 1 or input_guess == "score"):
            if(input_guess == "score"):
                print_scores(len(player_names), robot)
                continue
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
            robot.say_text("Please only input one letter", False, False, 0.5).wait_for_completed()
            print("Please only input 1 letter")
            continue
        elif (input_guess.isalpha()):
            flag = check_letter(input_guess.upper(), word_to_guess.upper(), robot)

        if (flag == 1):
            for i in range(word_length):
                if(word_to_guess[i] == input_guess):
                    guess[i] = input_guess.upper()
                    player_scores[current_player] += 1
        elif (flag == 0):
            lives = lives - 1

        # print("===============")
        # robot.say_text("Current Scores").wait_for_completed()
        # print("Current Scores")
        # print_player_names(len(player_names), robot)
        # print("===============")

        # print_scores(robot)

        if (current_player >= (number_of_players - 1)):
            current_player = 0
        elif (current_player <= (number_of_players - 1)):
            current_player += 1
  
def add_player_to_list(players, robot):
    for name in range(players):
        robot.say_text("What is your name human? ", False, False, 0.5 ).wait_for_completed()
        name = (input("What is your name human? "))
        robot.say_text("{} has been integrated into the game" .format(name), False, False, 0.5).wait_for_completed()
        print("{} has been integrated" .format(name))
        player_names.append(name)
        player_scores.append(0)

def check_letter(letter, word_to_guess, robot):
    flag = 0
    
    if (letter in word_to_guess): 
            robot.say_text("That is correct", False, False, 0.5).wait_for_completed()
            flag = 1
    if (flag == 0):
        if (not letter in letters_missed):
            robot.say_text("That is incorrect", False, False, 0.5).wait_for_completed()
            letters_missed.append(letter.upper())
    
    return flag

def check_win_condition(lives, guess, word_to_guess, robot):

        if (lives == 0):
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabUnhappy).wait_for_completed()
            robot.say_text("You have run out of lives better luck next time", False, False, 0.5).wait_for_completed()
            print("You have run out of lives. Better luck next time!")
            robot.say_text("The correct word was {}" .format(word_to_guess.upper()), False, False, 0.5).wait_for_completed()
            print("The correct word was {}\n" .format(word_to_guess.upper()))
            
            while(True):
                robot.say_text("Would you like to play again yes or no", False, False, 0.5).wait_for_completed()
                play_again = input("Would you like to play again? (Yes/No) ").lower()
                if (play_again != "yes" and play_again != "no"):
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
                    robot.say_text("Wrong input. Please input yes or no", False, False, 0.5).wait_for_completed()
                    print("Wrong input. Please input yes or no")
                elif (play_again == "yes"):
                    print("\n")
                    
                    del player_names[:]
                    del player_scores[:]
                    del letters_missed[:]

                    os.system("cls")
                    game(robot)
                elif (play_again == "no"):
                    print("Thank you for playing Cozmo Hangman")
                    robot.say_text("Thank you for playing Cozmo Hangman", False, False, 0.5).wait_for_completed()
                    robot.play_anim_trigger(cozmo.anim.Triggers.GoToSleepOff).wait_for_completed()
                    os.system("cls")
                    exit()
        
        if (not '_' in guess):
            print("")
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabVictory).wait_for_completed()
            robot.say_text("Congratulations! You figured out the word", False, False, 0.5).wait_for_completed()
            print("Congratulations! You figured out the word.")
            robot.say_text("The word was {}".format(word_to_guess.upper()), False, False, 0.5).wait_for_completed()
			#DISPLAY IMAGE
            print("The word was {}" .format(word_to_guess.upper()))
            check_higher_score(robot)
            print("")

            while(True):
                robot.say_text("Would you like to play again? Yes or no", False, False, 0.5).wait_for_completed()
                play_again = input("Would you like to play again? (Yes/No) ").lower()
                if (play_again != "yes" and play_again != "no"):
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
                    robot.say_text("Wrong input. Please input yes or no", False, False, 0.5).wait_for_completed()
                    print("Wrong input. Please input yes or no")
                elif (play_again == "yes"):
                    print("\n")
                    
                    del player_names[:]
                    del player_scores[:]
                    del letters_missed[:]
                    os.system("cls")
                    game(robot)
                elif (play_again == "no"):
                    print("Thank you for playing Cozmo Hangman")
                    robot.say_text("Thank you for playing Cozmo Hangman", False, False, 0.5).wait_for_completed()
                    robot.play_anim_trigger(cozmo.anim.Triggers.GoToSleepOff).wait_for_completed()  
                    os.system("cls")
                    exit()

def check_higher_score(robot):
    # if (len(player_scores != len(set(player_scores)))):
    #     print("More than 1 person ")

    duplicates = defaultdict(list)
    for i,item in enumerate(player_scores):
        duplicates[item].append(i)
    duplicates = {k:v for k,v in duplicates.items() if len(v)>1}

    if not duplicates:
        max_score = max(player_scores)
        max_score_index = player_scores.index(max_score)

        print_scores(len(player_names), robot)

        robot.say_text("{} got the highest score with {} points!" .format(player_names[max_score_index], max_score), False, False, 0.5).wait_for_completed()
        print("{} got the highest score with {} points!" .format(player_names[max_score_index], max_score))
    else:
        max_score = max(player_scores)
        
        print_scores(len(player_names), robot)
        
        robot.say_text("Multiple players achieved a high score of {}" .format(max_score), False, False, 0.5).wait_for_completed()
        print("Multiple players achieved a high score of {}!" .format(max_score))

    # dups = defaultdict(list)
    # for i, e in enumerate(player_scores):
    #     dups[e].append(i)
    # for k, v in sorted(dups.items()):
    #     if len(v) >= 2:
    #         print('K:%s: V:%r' % (k, v))
    #     for values in v:
    #         print("Players {} " .format(player_names[values]), end='')

    #         print("got: ", end='')

def print_player_names(players, robot):
    robot.say_text("The current human players are", False, False, 0.5).wait_for_completed()
    print("\nThe current human players are: ")
    for item in range(players):
        robot.say_text(player_names[item], False, False, 0.5).wait_for_completed()
        print(player_names[item],end=': ') 
        print(player_scores[item])

def print_scores(player, robot):
        print("===============")
        robot.say_text("Current Scores", False, False, 0.5).wait_for_completed()
        print("Current Scores")
        # print_player_names(len(player_names), robot)
        for item in range(len(player_names)):
            # robot.say_text(player_names[item] + "with " + player_scores[item] + "points.", False, False, 0.5).wait_for_completed()
            robot.say_text("{} with {} points.".format(player_names[item], player_scores[item]), False, False, 0.5).wait_for_completed()
            print(player_names[item],end=': ') 
            print(player_scores[item])
        print("===============")

def random_words():
    words = ["headline", "soup", "filter", "command", "mass", "truck", "tumble", "flourish", "squash", "mouth", "drill","Inn", "atmosphere", "Anki", "cosmo", "universe", "protest", "fiction", "robot","intelligence", "school", " ranch","hangman", "game", "ancestor", "prescription"]
    return random.choice(words)

def game(robot):
    os.system("cls")
    players(robot)

def cozmo_program(robot: cozmo.robot.Robot):
    game(robot)

cozmo.run_program(cozmo_program)

