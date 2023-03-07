#
# File     : elyjy009_encryptor.py
# Author   : Joy El-Hayek
# Email ID : elyjy009@mymail.unisa.edu.au
# Description: Programming Assignment 2 - Caesar Cipher
# This is my own work as defined by the University's
# Academic Misconduct Policy.
#

# Create a function to display details
def display_details():
    print('File     : elyjy009_encryptor.py')
    print('Author   : Joy El-Hayek')
    print('Stud ID  : 110372250')
    print('Email ID : elyjy009')
    print('Description: Programming Assignment 2 - Caesar Cipher')
    print('This is my own work as defined by the University\'s Academic Misconduct Policy.')

# Create a function to display the menu to the screen, prompt for, read, validate the
# menu command entered by the user, and return the command entered by the user
def get_menu_choice():
    # Display menu to the screen
    print('*** Menu ***')
    print('')
    print('1. Encrypt string')
    print('2. Decrypt string')
    print('3. Brute force decryption')
    print('4. Quit')
    print('')
    # Prompt for and read the command entered by user
    command = input('What would you like to do [1,2,3,4]? ')
    # Validate user input
    while not command.isdigit():
        print('Invalid choice, please enter either 1, 2, 3 or 4.')
        print('')
        command = input('What would you like to do [1,2,3,4]? ')
    while command != '1' and command != '2' and command != '3' and command != '4':
        print('Invalid choice, please enter either 1, 2, 3 or 4.')
        print('')
        command = input('What would you like to do [1,2,3,4]? ')
    # Return command entered by user
    return int(command)
        
# Create a function that prompts for, reads and validates the offset value entered by user
# The function takes no parameters and returns the offset entered by the user.
def get_offset():
    # Prompt for and read offset value
    offset_value = input('Please enter offset value (1 to 94): ')
    # Validate offset value
    while not offset_value.isdigit()or int(offset_value) < 1 or int(offset_value) > 94:
        offset_value = input('Please enter offset value (1 to 94): ')
    # Return the offset value entered by user
    return int(offset_value)

# Create a function to encrypt a string
def encrypt_string(string, offset):
    # Create a list to store encrypted string
    encrypted_string_list = []
    # Go through the letters of the string one by one
    for letter in string:
       # Get the ASCII of the letter
       ord_of_letter = ord(letter)
       # Add offset value to the ASCII of the letter
       new_ord = ord_of_letter + offset
       # Keep the new ASCII within the range of available ASCIIs
       if new_ord > 126:
           new_ord -= 95
       # Get equivalent letter for new ASCII
       equivalent_letter = chr(new_ord)
       # Store equivalent letters in a list
       encrypted_string_list.append(equivalent_letter)
    # Display the encrypted string
    print('')
    print('Encrypted string:')
    for item in encrypted_string_list:
        print(item, end= "")

# Create a function to decrypt a string
def decrypt_string(string, offset):
    # Create a list to store decrypted string
    decrypted_string_list = []
    # Go through the letters of the string one by one
    for letter in string:
        # Get the ASCII of the letter
        ord_of_letter = ord(letter)
        # Substract offset value from the ASCII of the letter
        new_ord = ord_of_letter - offset
        # Keep the new ASCII within the range of available ASCIIs
        if new_ord < 32:
            new_ord += 95
        # Get equivalent letter for new ASCII
        equivalent_letter = chr(new_ord)
        # Store equivalent letters in a list
        decrypted_string_list.append(equivalent_letter)
    # Display the decrypted string
    print('')
    print('Decrypted string:')
    for item in decrypted_string_list:
        print(item, end= "")

# Create a function for the brute force decryption
def brute_force_decryption(string):
    # Create a variable to store offset value
    offset_value = 1
    # Add a while loop to go through the offset values one by one
    while 1 <= offset_value <= 94:
        # Create a list to store decrypted string
        brute_force_decrypted_string_list = []
        # Go through the letters of the string one by one
        for letter in string:
            # Get the ASCII of the letter
            ord_of_letter = ord(letter)
            # Substract offset value from the ASCII of the letter
            new_ord = ord_of_letter - offset_value
            # Keep the new ASCII within the range of available ASCIIs
            if new_ord < 32:
                new_ord += 95
            # Get equivalent letter for new ASCII
            equivalent_letter = chr(new_ord)
            # Store equivalent letters in a list
            brute_force_decrypted_string_list.append(equivalent_letter)
        # Display the decrypted strings corresponding to each offset value
        print('Offset:', offset_value, '= Decrypted string: ', end= "")
        for item in brute_force_decrypted_string_list:
            print(item, end= "")
        print('')
        # Increment offset value by one
        offset_value += 1

# Call a function to display the details
display_details()
print('')

# Create a variable to store the value of the command
command = 0

# Start the encryption / decryption game
while command != 4:
    # Call the get menu choice function to display menu
    command = get_menu_choice()
    # Display corresponding output if user chooses to encrypt a string
    if command == 1:
        print('')
        # Ask user to enter a string
        user_string = input('Please enter string to encrypt: ')
        # Call a function to get offset value
        offset_value = get_offset()
        # Display the encrypted string by calling the function
        encrypted_string = encrypt_string(user_string, offset_value)
        print('')
        print('')
    # Display corresponding output if user chooses to decrypt a string
    elif command == 2:
        print('')
        # Ask user to enter a string
        user_string = input('Please enter string to decrypt: ')
        # Call a function to get offset value
        offset_value = get_offset()
        # Display the decrypted string by calling the function
        decrypted_string = decrypt_string(user_string, offset_value)
        print('')
        print('')
    # Display corresponding output if user chooses brute force decryption
    elif command == 3:
        print('')
        # Ask user to enter a string
        user_string = input('Please enter a string to decrypt: ')
        print('')
        # Display the brute force decrypted string by calling the function
        brute_force_decrypted_string = brute_force_decryption(user_string)
        print('')
# Display gooodbye message if user decides to quit
if command == 4:
    print('')
    print('Goodbye.')
