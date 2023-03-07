# Additional Exercices Day 2

# Exercices : Loops

# Exercice 1 : Formatting a 10*10 multiplication table

# Format
print(f'{"1":>7} {"2":>3} {"3":>3} {"4":>3} {"5":>3} {"6":>3} {"7":>3} {"8":>3} {"9":>3} {"10":>3}')
print(f'{" ":>4}{"-"*41:>34}')
# Use nested loops to print out a 10*10 multiplication table
for i in range(1, 11): # outer loop is for rows
    print(f'{i:<2} |', end = "")
    for x in range(1, 11): # inner loop is for columns
        if x != 10:
            print(f'{i*x:>3}', end = " ")
        else:
            print(f'{" "}{i*x:<3}')
print()


# Exercice 2 : Lists

# Write python code to read in 5 numbers (on separate lines) from the user and store in a list
numbers = []
for i in range(5):
    number = int(input("Please enter a number: "))
    numbers.append(number)

# Iterate over the list and print out each number in turn (on the same line but separated with a comma
#  If a negative number is encountered in the list, then print the number followed by 'Negative! exiting!'  
# and exit the loop immediately.
for num in range(len(numbers)):
    if numbers[num] > 0:
        print(numbers[num], end = ", ")
    else:
        print(numbers[num])
        print("Negative! exiting!")
        break
    
# Exercice 3 : List

# Write python code to read in a list of names and store in a list.
names = input("Please enter names separated by a space: ").split()

# Then iterate over the list printing out numbers from 1 onwards and the name.
for name in range(len(names)):
    print(f'{name + 1} {names[name]}')
    

# Exercice 4: Functions

# Write a function that is input a list and  returns a list which has some changes but leaves the original list 
# unchanged e.g. input a list of integers and an integer and returns a list with the integer appended. 
# Print out the original and the new list at the end to show the original list is unchanged
def change_list(user_list, user_integer):
     new_list = user_list.copy()
     new_list.append(user_integer)
     return new_list
 
# main code
# get the list from the user
numbers = []
for i in range(5):
    num = int(input())
    numbers.append(num)
    
# get the integer to be added
integer = int(input("Enter a number to be added to the list: "))

numbers_changed = change_list(numbers, integer)
print("Numbers:", numbers)
print("Numbers changed:", numbers_changed)


# Exercice 5: 
# Implement the Python function change_string(in_string: str, change_char: str, replace_char: str) -> str: 
# as follows

# it is input a in_string,  a change_char (str of length 1) and a replace_char
# it replaces all occurrences of change_char in in_string with replace_char
# it returns the resulting string

def change_string(in_string, change_char, replace_char):
    for letter in in_string:
        if letter == change_char:
            in_string = in_string.replace(change_char, replace_char)
    return in_string

# main code
user_string = input()
user_change_char = input()
user_replace_char = input()
new_string = change_string(user_string, user_change_char, user_replace_char)
print(new_string)


#  Amend your Python function change_string(in_string: str, change_char: str, replace_char: str) -> str: 
# as follows
# it replaces the first occurrence of change_char in in_string with replace_char
def change_string(in_string, change_char, replace_char):
    string_list = in_string.split()
    changed_string =''
    for word in string_list:
        for letter in range(len(word)):
            if word[letter] != change_char:
                changed_string += word[letter]
            elif word[letter] == change_char:
                changed_string += replace_char + word[letter + 1:] + " "
                break
    return changed_string
    
user_string = input()
user_change_char = input()
user_replace_char = input()
new_string = change_string(user_string, user_change_char, user_replace_char)
print(new_string)



# Exercice 6 

# Create a Python function that accepts a string 
# counts the number of Xs and the number of Os in the string 
# returns a boolean value of either True or False. 
# If the count of Xs and Os are equal, then the function should return True.
# If the count isn't the same, it should return False. 
# If there are no Xs or Os in the string, it should also return True because 0 equals 0. 
# The string can contain any type and number of characters.

def count_characters(user_string):
    counter_x = 0
    counter_o = 0
    for char in user_string:
        if char == 'x':
            counter_x += 1
        elif char == 'o':
            counter_o += 1
    
    if counter_x == counter_o:
        return True
    else:
        return False
    
# Main code
user_input = input("Please enter a string: ")

boolean_value = count_characters(user_input)

if boolean_value == True:
    print("There are as many x as o in the string")
else:
    print("The number of x's is different to the number of o's in the string")


# Exercice 7:

# Write a function in Python that accepts a credit card number (length 12) 
# returns a string with all characters replaced with '*' apart from the last four 
# e.g. if the function is input "123456780000", then it should return "********0000".
def encrypt_credit_card(number):
    credit_card_number = str(number)
    encrypted_credit_card = ''
    for char in range(len(credit_card_number)):
        if char < 8:
            encrypted_credit_card += '*'
        else:
            encrypted_credit_card += credit_card_number[char]
    return encrypted_credit_card

# main code
# get credit card number from user
user_credit_card = int(input())
encrypted_number = encrypt_credit_card(user_credit_card)
print(encrypted_number)

# Exercice 8: String Formatting

# Placement of float, with specified number of decimal places, within field of specified size
import math
number = math.pi
print(f'{number:10.2f}') # :10.2f specifies a field of 10 characters and .2f prints 2 decimal places

# Filling string of specified length, with a specified character
my_str = 'Joy'
print(f'{my_str:/<10}') # / is the special character and 10 is the length and < specifies where the string is


# Last exercice: Bringing it all together

# Extend your code for the Ice Cream Dictionary exercise for Day 1 as follows:
# Separate the code into functions:
#     - Adding Ice Cream Flavour (option 1) 
#     - Updating Ice Cream Flavour (option 2)
# Add a loop, which loops until the menu/option selection until the user enters Exit


#  Create a dictionary where keys are flavours of ice cream (str) and corresponding values are a list of prices
# (float),  where there are 2 elements in the list and index position 0 is the price of a small ice cream and 
# index position 1 is the price of a large ice cream

# Create a function for adding an ice cream flavour
def add_flavour(dictionary):
    new_flavour = input("Enter a new flavour of ice cream: ")
    prices = []
    prices.append(float(input("Enter the price of a small ice cream (float): ")))
    prices.append(float(input("Enter the price of a large ice cream (float): ")))
    dictionary[new_flavour] = prices
    
# Create a function to update flavour price
def update_price(flavours):
    ice_cream_flavour = input("Enter the name of the ice cream: ")
    if ice_cream_flavour in ice_creams.keys():
        size = input("Choose a size: (small/large) ")
        new_price = float(input("Enter the new price (float): "))
        
        if size == 'small':
            flavours[ice_cream_flavour] = [new_price, 4.0]
        elif size == 'large':
            flavours[ice_cream_flavour] = [2.0, new_price]


#  Create a dictionary where keys are flavours of ice cream (str) and corresponding values are a list of prices
# (float),  where there are 2 elements in the list and index position 0 is the price of a small ice cream and 
# index position 1 is the price of a large ice cream
ice_creams = {
    'chocolate' : [2.0, 4.0],
    'vanilla' : [2.0, 4.0],
    'strawberry' : [2.0, 4.0],
    'salted caramel' : [2.0, 4.0],
    'cookies and cream' : [2.0, 4.0],
    'nutella' : [2.0, 4.0]
}

# 2. Get input from the user as follows: 
# What flavour of ice cream?
user_flavour = input("What flavour of ice cream? ")
# What size? small or large?
user_size = input("What size? small or large? ")
# How many ice creams?
num_ice_creams = int(input("How many ice creams? "))
# and calculate the total cost of their ice creams
total = 0

if user_size == 'small':
    total = ice_creams[user_flavour][0] * num_ice_creams
elif user_size == 'large':
    total = ice_creams[user_flavour][1] * num_ice_creams
    
# Concatenate strings to produce a single string to be printed to the user 
# (note: prices should be printed with 2 digits after decimal point). Such as:
# Total Cost: 2 large chocolate is $8.00
print(f'Total Cost: {num_ice_creams} {user_size} {user_flavour} is ${total:.2f}')

# Print a choice of options for the user
option = ''
while option != '3':
    print( """OPTIONS:
    1: Add Ice Cream Flavour
    2: Update price of Ice Cream
    3: Exit""")
    option = input("Which option: ")

    # Depending on user input
    # 1: get the name of the new ice cream, the price for small and large and add to the dictionary
    if option == '1':
        add_flavour(ice_creams)
        
    # 2 ask the user for name of ice cream and whether small/large, get the updated price and update the dictionary
    elif option == '2':
        update_price(ice_creams)
