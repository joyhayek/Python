# Additional Exercices Day 1

# Exercices : Python Variables, Expressions and Built-in Types  

# Exercice 1: Strings

# write python code to read in a users first name and surname
first_name = input("Please enter your first  name: ")
surname = input("Please enter your surname: ")

# the number of characters in their first name, surname
char_first_name = len(first_name)
char_surname = len(surname)

# the total number of characters in both the first names and surname
total_char_name = char_first_name + char_surname

# their initials (first letter of the first name, followed by the first letter of the surname) 
first_name_initial = first_name[0]
surname_initial = surname[0]

print(f'Number of characters in first name: {char_first_name}')
print(f'Number of characters in surname: {char_surname}')
print(f'Number of characters in full name: {total_char_name}')
print(f'Name initials: {first_name_initial} {surname_initial}')

# Exercice 2: Tuples

# write python code that reads in 4 integers entered by a user and stores them in a tuple
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))
num4 = int(input("Please enter a last number: "))

numbers = (num1, num2, num3, num4)

# Print out: myTuple, the type of myTuple() and the sum of the integers in the tuple
# myTuple
print("My tuple:", numbers)
# Type of myTuple
print("Type of this variable is:", type(numbers))
# Sum of integers in the tuple
total = 0
for num in numbers:
    total += num

print("Total:", total)


# Exercices: Python Branching Basics 

# write code that reads in 2 lines of text from a user and saves them as string1 and string2 
string1 = input("Please enter a first string: ")
string2 = input("Please enter another string: ")
# then tests whether string2 is a substring of string1 and prints out the result
if string2 in string1:
    print("String 2 is a substring of String 1")
else:
    print("String 2 is not a substring of string 1")

# Last exercice: Bringing it all together

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
print( """OPTIONS:
1: Add Ice Cream Flavour
2: Update price of Ice Cream
3: Exit""")
option = int(input("Which option: "))

# Depending on user input
# 1: get the name of the new ice cream, the price for small and large and add to the dictionary
if option == 1:
    new_flavour = input("Enter a new flavour of ice cream: ")
    prices = []
    prices.append(float(input("Enter the price of a small ice cream (float): ")))
    prices.append(float(input("Enter the price of a large ice cream (float): ")))
    ice_creams[new_flavour] = prices
    
# 2 ask the user for name of ice cream and whether small/large, get the updated price and update the dictionary
elif option == 2:
    ice_cream_flavour = input("Enter the name of the ice cream: ")
    if ice_cream_flavour in ice_creams.keys():
        size = input("Choose a size: (small/large) ")
        new_price = float(input("Enter the new price (float): "))
        
        if size == 'small':
            ice_creams[ice_cream_flavour] = [new_price, 4.0]
        elif size == 'large':
            ice_creams[ice_cream_flavour] = [2.0, new_price]

print(ice_creams)