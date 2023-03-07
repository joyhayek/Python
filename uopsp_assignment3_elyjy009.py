# 
# File: uopsp_assignment3_elyjy009.py 
# Author: Joy El-Hayek
# Email ID: elyjy009
# Student ID: 110372250
# Description: Assignment 3 – Manage character (hero and villain) information
# This is my own work as defined by the University's
# Academic Misconduct policy. 
# 

# Import random module
import random

# Functions

# Create a function to display our details
def display_details():
    print('File     : elyjy009.py')
    print('Author   : Joy El-Hayek')
    print('Email ID : elyjy009')
    print('This is my own work as defined by the University\'s Academic Misconduct Policy.')

# Create function to read file content into a list of lists
def read_file(file_name):
    infile = open(file_name, 'r')
    # Create empty list to store all the information 
    file_list = []
    # Read content of file
    name = infile.readline()
    # Go through lines in file one by one to get information on characters
    while name != '':
        # Create a list to store information about one specific character
        one_character_list = []
        secret_id = infile.readline()
        battle_info = infile.readline()
        battle_info = battle_info.split()
        # Add character information to a list
        one_character_list.append(name.strip('\n'))
        one_character_list.append(secret_id.strip('\n'))
        for info in battle_info:
            if info.isalpha():
                one_character_list.append(info)
            else:
                one_character_list.append(int(info))
        # Add each character information to big list
        file_list.append(one_character_list)
        # Read the next line for next character
        name = infile.readline()
    # Return the list containing all information
    return file_list

# Create a function to output content of the list
def display_characters(character_list, display_type):
    print('===================================================')
    print('-     Character (heroes and villains) Summary     -')
    print('===================================================')
    print('-                             P  W  L  D  Health  -')
    print('===================================================')
    # If display type is 0 display all characters
    if display_type == 0:
        for character in character_list:
            print(format('-', '<3s') + format(character[0], '<25s') + format(character[3], '3d') + format(character[4], '3d') + format(character[5], '3d') + format(character[6], '3d') + format(character[7], '8d') + format('-', '>3s'))
            print('---------------------------------------------------')
    # If display type is 1 display only heroes
    elif display_type == 1:
        for character in character_list:
            if character[2] == 'h':
                print(format('-', '<3s') + format(character[0], '<25s') + format(character[3], '3d') + format(character[4], '3d') + format(character[5], '3d') + format(character[6], '3d') + format(character[7], '8d') + format('-', '>3s'))
                print('---------------------------------------------------')
    # If display type is 2 display only villains
    elif display_type == 2:
        for character in character_list:
            if character[2] == 'v':
                print('- ', format(character[0], '10s'), format(character[3], '17d'), format(character[4], '2d'), format(character[5], '2d'), format(character[6], '2d'), format(character[7], '7d'), format('-', '>2s'))
                print('---------------------------------------------------')

# Create a function to write to a new file
def write_to_file(filename, character_list):
    outfile = open(filename, 'w')
    # Iterate over character list
    for character in character_list:
        # Iterate over each character in list and write each information on the character in the file
        for element in character:
            outfile.write(str(element))
            # If character information is name or secret identity write newline character
            if element == character[0] or element == character[1]:
                outfile.write('\n')
            # If character information is battle information stay on the same line
            else:
                outfile.write(' ')
        # When done with information about one character write new line character
        outfile.write('\n')
    # Close the file
    outfile.close()

# Create a function to see if character in list
def find_character(character_list, name):
    # Create 2 variables to store result
    result = -1
    index = 0
    # Go over each character in the list
    for character in character_list:
        # If character name is the same as name parameter assign index value to result variable
        if character[0] == name:
            result = index
        # Increment index by 1
        index += 1
    # Return the result
    return result

# Create a function to display character information if found
def display_character_information(character_list, character_name):
    # Call the find character function to check if character in list
    is_in_list = find_character(character_list, character_name)
    # If character not in list display appropriate message
    if is_in_list == -1:
        print()
        print(character_name, 'is not found in character (heroes and villains) list.')
        print()
    # If character in list display all information about them
    elif is_in_list != -1:
        print()
        print('All about', character_list[is_in_list][0], '--> ', end='')
        # Check if character hero or villain and display accordingly
        if character_list[is_in_list][2] == 'h':
            print('HERO')
        elif character_list[is_in_list][2] == 'v':
            print('VILLIAN')
        # Display character details
        print()
        print('Secret identity: ', character_list[is_in_list][1])
        print()
        print('Battles fought:', character_list[is_in_list][3])
        print('  >No won:', format(character_list[is_in_list][4], '>4d'))
        print('  >No lost:', format(character_list[is_in_list][5], '>3d'))
        print('  >No drawn:', format(character_list[is_in_list][6], '>2d'))
        print()
        print('Current health: ', character_list[is_in_list][7], '%', sep='')
        print()

# Create a function to add charcter to the list
def add_character(character_list, name, secret_identity, hero):
    # Call the find character function to check if character name entered is already in list
    in_list = find_character(character_list, name)
    # If character already in list display error message
    if in_list != -1:
        print(name, 'already exists in character list.')
        print()
    # If character not in list, add name and secret identity as specified, initialise battle info as 0, and set health to 100.
    else:
        new_character = [name, secret_identity, hero, 0, 0, 0, 0, 100]
        # Add that character to the character list
        character_list.append(new_character)
        # Display message saying character was added
        print('Successfully added', name, 'to character list.')
        print()
    return character_list

# Create a function to remove character from list
def remove_character(character_list, name):
    # Create a new list to store characters still present in character list
    character = []
    # Check if character entered by user is in the list by calling find character function
    find_in_list = find_character(character_list, name)
    # If character not in list display error message
    if find_in_list == -1:
        print(name, 'is not found in characters.')
        print()
        return character_list
    # If character name is in list, add all other character to the new list 
    else:
        for x in range(len(character_list)):
            if x != find_in_list:
                character.append(character_list[x])
        # Display message saying that character was removed
        print('Successfully removed', name, 'from character list.')
        print()
        return character

# Create a function to help sort health by adding all characters except chosen one to new list
def remove_character_for_health(character_list, name):
    # Create a new list to store characters still present in character list
    character = []
    # Check if character is in list by calling the find character function
    find_in_list = find_character(character_list, name)
    # If character name is in list, add all other character to the new list
    for x in range(len(character_list)):
        if x != find_in_list:
            character.append(character_list[x])
    # Return new list
    return character

# Create a function to find the highest number of battles won
def display_highest_battles_won(character_list):
    # Create 2 variables representing highest number of battles faught by a character, and that character
    # Assign random values to these variables
    highest = 0
    highest_character = character_list[0]
    # Check which character has the highest number of battles fought and assign new values to both variables
    for character in character_list:
        if character[4] > highest:
            highest = character[4]
            highest_character = character
        elif character[4] == highest:
            if character[3] < highest_character[3]:
                highest = character[4]
                highest_character = character
    # If no characters are stored in the list or a character with the highest number of battles won cannot be found display error message
    if highest == 0:
        print('Error')
    # If character is found display information
    else:
        print('Highest number of battles won =>' , highest_character[0], 'with', highest_character[4], 'opponents defeated!')

# Create a function to battle 2 opponents
def do_battle(character_list, opponent1_pos, opponent2_pos):
    # Get number of battle rounds to be fought by characters
    battle_number = input('Please enter number of battle rounds: ')
    # Create a variable to store current round value
    current_round = 1
    # Validate user input
    while not battle_number.isdigit() or int(battle_number) < 1 or int(battle_number) > 5:
        print('Must be between 1-5 inclusive.')
        print()
        battle_number = input('Please enter number of battle rounds: ')
    # Make battle_number an integer
    battle_number = int(battle_number)
    # Display battle header
    print()
    print()
    print('-- Battle --')
    print()
    print(character_list[opponent1_pos][0], 'versus', character_list[opponent2_pos][0], '-', battle_number, 'rounds')
    print()
    # While number of battle rounds have not been completed and both opponents are still alive
    while current_round <= battle_number and character_list[opponent1_pos][7] > 0 and character_list[opponent2_pos][7] > 0:
        # Randomly generate 2 damage values sustained from battle and update each opponent's health 
        damage_opponent1 = random.randint(0, 50)
        damage_opponent2 = random.randint(0, 50)
        # If damage sustained is bigger than health of character set health to 0
        if damage_opponent1 > character_list[opponent1_pos][7]:
            character_list[opponent1_pos][7] = 0
        # Otherwise remove damage sustained from character's health
        else:
            character_list[opponent1_pos][7] -= damage_opponent1
        # If damage sustained is bigger than health of character set health to 0
        if damage_opponent2 > character_list[opponent2_pos][7]:
            character_list[opponent2_pos][7] = 0
        #  Otherwise remove damage sustained from character's health
        else:
            character_list[opponent2_pos][7] -= damage_opponent2
        # Display each opponent's results
        print('Round:', current_round)
        print('  >', character_list[opponent1_pos][0], '-', 'Damage:', damage_opponent1, '-', 'Current health:', character_list[opponent1_pos][7])
        print('  >', character_list[opponent2_pos][0], '-', 'Damage:', damage_opponent2, '-', 'Current health:', character_list[opponent2_pos][7])
        print()
        # Increment number of current round
        current_round += 1
    # Display battle results
    print('-- End of battle --')
    print()
    # Check who died (if anyone) and display message accordingly
    if character_list[opponent1_pos][7] == 0:
        print('--', character_list[opponent1_pos][0], 'has died!  :(')
        print()
        print('**', character_list[opponent2_pos][0], 'wins! **')
        # Update battles won/lost for each character
        character_list[opponent2_pos][4] += 1
        character_list[opponent1_pos][5] += 1
    elif character_list[opponent2_pos][7] == 0:
        print('--', character_list[opponent2_pos][0], 'has died!  :(')
        print()
        print('**', character_list[opponent1_pos][0], 'wins! **')
        print()
        # Update battles won/lost for each character
        character_list[opponent1_pos][4] += 1
        character_list[opponent2_pos][5] += 1
    # Check who won and display message accordingly
    elif character_list[opponent1_pos][7] > character_list[opponent2_pos][7]:
        print('**', character_list[opponent1_pos][0], 'wins! **')
        print()
        # Update battles won/lost for each character
        character_list[opponent1_pos][4] += 1
        character_list[opponent2_pos][5] += 1
    # Check who won and display message accordingly
    elif character_list[opponent2_pos][7] > character_list[opponent1_pos][7]:
        print('**', character_list[opponent2_pos][0], 'wins! **')
        print()
        # Update battles won for character who won and battles lost for character who lost
        character_list[opponent2_pos][4] += 1
        character_list[opponent1_pos][5] += 1
    # If a battle results in a tie display appropriate message 
    else:
        print('-- A tie. Nobody wins.')
        print()
    # Increment numbers of battles for each character
    character_list[opponent1_pos][3] += 1
    character_list[opponent2_pos][3] += 1

# Create function to add elements from one list to another
def copy_list(character_list):
    new_list = []
    for character in character_list:
        new_list.append(character)
    return new_list

# Create a function to sort health by descending order
def sort_by_health(character_list):
    # Get a copy of character list
    character_list_copy = copy_list(character_list)
    # Create an empty list to store the character with highest health value
    new_character_list = []
    # Find the character with highest health value
    for x in range(len(character_list)):
        highest_health = 0
        highest_character = character_list[0]
        for i in range(len(character_list_copy)):
            if character_list_copy[i][7] > highest_health:
                highest_health = character_list_copy[i][7]
                highest_character = character_list_copy[i]
            elif character_list_copy[i][7] == highest_health:
                if character_list_copy[i][3] > highest_character[3]:
                    highest_health = character_list_copy[i][7]
                    highest_character = character_list_copy[i]
        # Remove that character from copy of character list
        character_list_copy = remove_character_for_health(character_list_copy, highest_character[0])
        # Add that character to new list
        new_character_list.append(highest_character)
    # Return new list
    return new_character_list

# General code          

# Create a list to store character information
character_list = []
# Fill the character list by calling the function and display it
character_list = read_file('characters.txt')

# Call function to display details
display_details()
print()
print()
# Prompt for and read menu commands.
print('Please enter choice')
choice = input('[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ')
print()
# Validate user input
while choice != 'list' and choice != 'heroes' and choice != 'villains' and choice != 'search' and choice != 'reset' and choice != 'add' and choice != 'remove' and choice != 'high' and choice != 'battle' and choice !='health' and choice != 'quit':
    print('Not a valid command - please try again.')
    print()
    print()
    print('Please enter choice')
    choice = input('[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ')
    print()

# Display output according to user choice
# Keep prompting user to choose commands until quit command is entered
while choice != 'quit':
    # If user chooses list display character list
    if choice == 'list':
        display_characters(character_list, 0)
    # If user chooses heroes display heroes information
    elif choice == 'heroes':
        display_characters(character_list, 1)
    # If user chooses villains display villain information
    elif choice == 'villains':
        display_characters(character_list, 2)
    # If user chooses search
    elif choice == 'search':
        # Prompt for and read character name
        character_name = input('Please enter name: ')
        # Check if the character is in list and if yes, display that character's information
        display_character_information(character_list, character_name)
    # If user chooses reset
    elif choice == 'reset':
        # Prompt for and read name of character
        name_of_character = input('Please enter character name: ')
        print()
        # Call the find character function to check if character is in list
        character_status = find_character(character_list, name_of_character)
        # If character not in list display error message
        if character_status == -1:
            print(name_of_character, 'is not found in character (heroes and villains) list.')
            print()
        # If character in list, reset character's health to 100
        else:
            character_list[character_status][7] = 100
            print('Successfully updated', name_of_character + '\'s', 'health to', character_list[character_status][7])
            print()
    # If user chooses add
    elif choice == 'add':
        # Prompt for and read character name, secret identity and if character is hero or villain
        name = input('Please enter name: ')
        secret_identity = input('Please enter secret_identity: ')
        hero = input('Is this character a hero or a villain [h|v]? ')
        print()
        # Validate user input for hero variable
        while hero != 'h' and hero != 'v':
            hero = input('Is this character a hero or a villain [h|v]? ')
            print()
        # Call the add character function to add character chosen to list
        character_list = add_character(character_list, name, secret_identity, hero)
    # If user chooses remove
    elif choice == 'remove':
        # Prompt for and read character's name to be removed
        name = input('Please enter name: ')
        print()
        # Call the remove character function to remove chosen character from list
        character_list = remove_character(character_list, name)
    # If user chooses high
    elif choice == 'high':
        # Call the display highest battles won to display character with highest number of battles won
        display_highest_battles_won(character_list)
        print()
    # If user chooses battle, show results of battle between two characters
    elif choice == 'battle':
        # Get first opponent
        opponent1 = input('Please enter opponent one\'s name: ')
        # Validate user input
        opponent1_position = find_character(character_list, opponent1)
        while opponent1_position == -1:
            print(opponent1, 'is not found in character list - please enter another opponent!')
            print()
            opponent1 = input('Please enter opponent one\'s name: ')
            opponent1_position = find_character(character_list, opponent1)
        # Get second opponent
        opponent2 = input('Please enter opponent two\'s name: ')
        # Validate user input
        opponent2_position = find_character(character_list, opponent2)
        while opponent2_position == -1 or opponent2_position == opponent1_position:
            print(opponent2, 'is not found in character list - please enter another opponent!')
            print()
            opponent2 = input('Please enter opponent two\'s name: ')
            opponent2_position = find_character(character_list, opponent2)
        # Start the battle
        do_battle(character_list, opponent1_position, opponent2_position)
    # If user chooses health, call the sort by health function to display characters' health in descending order
    elif choice == 'health':
        character_health = sort_by_health(character_list)
        display_characters(character_health, 0)
    # Ask user to enter another command
    print()
    print('Please enter choice')
    choice = input('[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ')
    print()
    # Validate user input
    while choice != 'list' and choice != 'heroes' and choice != 'villains' and choice != 'search' and choice != 'reset' and choice != 'add' and choice != 'remove' and choice != 'high' and choice != 'battle' and choice !='health' and choice != 'quit':
        print('Not a valid command - please try again.')
        print()
        print()
        print('Please enter choice')
        choice = input('[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ')
        print()
# If user chooses to quit display terminating message
print()
print('-- Program terminating --')

# Write character list content to a new file
write_to_file('new_characters.txt', character_list)
