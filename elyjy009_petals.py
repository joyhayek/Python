#
# File     : elyjy009_petals.py
# Author   : Joy El-Hayek
# Student ID  : 110372250
# Email ID : elyjy009@mymail.unisa.edu.au
# Description: Programming Assignment 1 - Petals Around the Rose
# This is my own work as defined by the University's Academic Misconduct Policy.

# Display my details to the screen
print('File     : elyjy009_petals.py')
print('Author   : Joy El-Hayek')
print('Stud ID  : 110372250')
print('Email ID : elyjy009')
print('Description: Programming Assignment 1 - Petals Around the Rose')
print('This is my own work as defined by the University\'s Academic Misconduct Policy.')

# Leave an empty row between details and game header
print('')
# Display game name
print('Petals Around the Rose')
print('----------------------')
# Leave an empty row between game name and game rules
print('')
# Display game rules
print('The name of the game is \'Petals Around the Rose\'.  The name of the')
print('game is important.  The computer will roll five dice and ask you to')
print('guess the score for the roll.  The score will always be zero or an')
print('even number.  Your mission, should you choose to accept it, is to')
print('work out how the computer calculates the score.  If you succeed in')
print('working out the secret and guess correctly four times in a row, you')
print('become a Potentate of the Rose.')

# Create a variable to keep track of games played
games_played = 0
# Create a variable to keep track of correct guesses
correct_guesses = 0
# Create a variable to keep track of incorrect guesses
incorrect_guesses = 0
# Create a variable to keep track of correct guesses in a row
correct_guesses_in_a_row = 0
# Create a variable to keep track of incorrect guesses in a row
incorrect_guesses_in_a_row = 0

# Leave an empty line between game rules and user prompt
print('')
# Create a variable to ask the user if they want to play
play = input('Would you like to play Petals Around the Rose [y|n]? ')
# Validate user input
while play != 'y' and play != 'n':
    play = input('Please enter either "y" or "n":')
# Display a message if user says no the first time
if play == 'n':
    print('No worries... another time perhaps... :)')
# Create a loop to enable the user to play more than one game
while play == 'y':
    # Increment the number of games played
    games_played += 1
    # Import the dice.py file.
    import dice

    # Simulate the rolling of five dice.
    import random
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    die5 = random.randint(1, 6)

    # Store the dice values in a list
    values_of_rolls = [die1, die2, die3, die4, die5]
    # Create a variable to store the score
    score = 0
    # Create a for loop to calculate score based on dice roll values (game rules)
    for value in values_of_rolls:
        # For each die that displays 3, add 2 to the score
        if value == 3:
            score += 2
        # For each die that displays 5, add 4 to the score
        elif value == 5:
            score += 4
    # Display the randomly generated dice roll to the screen
    dice.display_dice(die1, die2, die3, die4, die5)

    # Prompt for and read the user’s score guess for the roll
    guess = int(input('Please enter your guess for the roll: '))

    # If the user guesses correctly, congratulate them
    if guess == score:
        print('Well done! You guessed it!')
        # Increment number of correct guesses
        correct_guesses += 1
        # Increment number of correct guesses in a row
        correct_guesses_in_a_row += 1
        # Reset counter of incorrect guesses in a row
        incorrect_guesses_in_a_row = 0
    # If the user enters an incorrect odd number, display a message saying that
    elif guess != score and guess%2 != 0:
        print('No sorry, it\'s', score, 'not', guess,'.','The score is always even.')
        # Increment number of incorrect guesses
        incorrect_guesses += 1
        # Increment number of incorrect guesses in a row
        incorrect_guesses_in_a_row += 1
        # Reset counter of correct guesses in a row
        correct_guesses_in_a_row = 0
    # If the user enters an incorrect even number, display a message saying that
    elif guess != score and guess%2 == 0:
        print('No sorry, it\'s', score, 'not', guess,'.')
        # Increment number of incorrect guesses
        incorrect_guesses += 1
        # Increment number of incorrect guesses in a row
        incorrect_guesses_in_a_row += 1
        # Reset counter of correct guesses in a row
        correct_guesses_in_a_row = 0
    # Display a message if user guesses correctly 4 times in a row
    if correct_guesses_in_a_row == 4:
        print('Congratulations! You have worked out the secret!')
        print('Make sure you don\'t tell anyone!')
        # Reset counter of correct guesses in a row
        correct_guesses_in_a_row = 0

    # Display a message if user guesses incorrectly 4 times in a row
    elif incorrect_guesses_in_a_row == 4:
        print('Hint: The name of the game is important... Petals around the Rose.')
        # Reset counter of incorrect guesses in a row
        incorrect_guesses_in_a_row = 0
    # Leave 1 empty line
    print('')
    # Ask user if they want to play again
    play = input('Roll dice again [y|n]?: ')
    # Validate user input
    while play != 'y' and play != 'n':
        play = input('Please enter either "y" or "n":')
    # Leave 1 empty line
    print('')
    # Display the game summary when the user doesn't want to play anymore
    if play == 'n':
        print('Game Summary')
        print('============')
        print('')
        # Display output according to number of games played
        if games_played == 1:
            print('You played', games_played, 'game:')
        elif games_played > 1:
            print('You played', games_played, 'games:')
        print('  |--> Number of correct guesses:',format(correct_guesses, '>10d'))
        print('  |--> Number of incorrect guesses:',format(incorrect_guesses, '>8d'))
        print('')
        print('Thanks for playing!')

