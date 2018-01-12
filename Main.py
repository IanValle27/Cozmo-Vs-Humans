'''Cozmo Hangman
Files: Main, Player, Wordbank, Game, Input, Display

Make Cozmo spin and count up how many players with facial recognition, name and points for each.
	Player.py
Cozmo will then start a game of hangman with a random word
	Wordbank.py
	Game.py
Player have 6 letter guesses for the word if wrong the lose a guess and cozmo is sad with an X
	Input.py
	Main.py
After all lives are lost Cozmo will reset the game and ask for players once again
	Player.py
If all letters are guess correctly Cozmo will congratulate the player with a picture
	Display.py
	Wordbank.py
	

'''

import cozmo, Player, Wordbank, Game, Input, Display


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("I'll be back").wait_for_completed()


cozmo.run_program(cozmo_program)
