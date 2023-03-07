# Day 3 Additional Exercices: Lists and Dictionaries

# Part 1: Lists
# Exercice 1 : Lists and Loops

# Get number of numbers to be added
num_of_nums = int(input("Enter number of numbers you want to enter: "))
# Add them to list
numbers = []
for num in range(num_of_nums):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Print numbers separated by , except for the last one
for number in range(num_of_nums):
    if number < (num_of_nums - 1):
        print(numbers[number], end = ", ")
    else:
        print(numbers[number])
        
# Exercice 2: Lists and Strings

# Write a program that takes a string, representing a space delimited list of names and which stores them 
# as a list of strings. 
# For example, for the string 'Julie Geela Azadeh Axel' the output list is ['Julie', 'Geela', 'Azadeh', 'Axel']
user_string = input("Enter names separated by space: ").split()
print(user_string)

# Exercice 3: Strings

# Write a program that takes a list of strings and stores them as a string delimited with '-'
# e.g. for the list ['Julie', 'Geela', 'Azadeh', 'Axel'] the resulting string is 'Julie-Geela-Azadeh-Axel'
user_list = input("Please enter a list of names: ").split()
resulting_string = ''

for index in range(len(user_list)):
    if index < (len(user_list) - 1):
        resulting_string += user_list[index] + "-"
    else:
        resulting_string += user_list[index]

print(resulting_string)

# Part 2: Dictionaries
 
# Exercice 2: 
# Write a python program which prompts the user for a name and a list of numbers 
# (e.g. student and scores on tests) and saves this in a dictionary. 
# It will continue until a sentinel value is entered (e.g. 'q'). 
# Print out the dictionary. Then prompt the user for a name (key) and print out the highest number in the value associated with that key. 
# Make sure to handle user entering a name that isn't in the dictionary.

name = input("Enter a name: ")
# Create a dictionary
student_scores = {}
# Keep going until user enter 'q'
while name != 'q':
    # Get list of numbers
    numbers = input("Enter numbers separated by a space: ").split()
    # Add numbers to a list as integers
    scores = [int(i) for i in numbers]
    # Add values and names in dictionary
    student_scores[name] = scores
    # Get new name
    name = input("Enter a name: ")

print(student_scores)

# Ask user for a name
student = input("Enter a student's name: ")
# Make sure to handle user entering a name that isn't in the dictionary.
if student not in student_scores.keys():
    print("Student name entered not in the dictionary")
# If name in dictionary, print highest value
else:
    grades = student_scores[student]
    highest_grade = grades[0]
    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade
            
    print(f'{student}\'s highest grade is {highest_grade}')
    
    
# Exercice 3: Function keyword **kwargs

# Write a function that accepts a parameter of **kwargs (keyword arguments) 
# asks the user for input and checks whether the user input 'key' is in the keyword arguments dictionary. 
# Make sure it can handle user input that is not a key in the kwargs dictionary. For example for the following:
# myclass(group1='julie', group2='geela', group3='axel', group4='azadeh')
# Input 'group2' should output 'geela' and input 'group5' should output 'No such group'

def keywords(**kwargs):
    keyword_dict = {}
    # Add keywords and values to dictionary
    for keyword, value in kwargs.items():
        keyword_dict[keyword] = value
    # Ask the user for input and checks whether the user input 'key' is in the keyword arguments dictionary. 
    key = input("Enter a key: ")
    if key not in kwargs.keys():
        print("No such group")
    else:
        print(keyword_dict[key])
        
keywords(group1='julie', group2='geela', group3='axel', group4='azadeh')

# Last exercice: Rewrite the seasons exercice using a dictionary and a loop
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19
# Create a dictionary for seasons
seasons = { 'Spring' : {'March': [i for i in range(20, 32)], 
                        'April': [i for i in range(1, 31)],
                        'May': [i for i in range(1, 32)],
                        'June': [i for i in range(1, 21)]},
           'Summer' : {'June' : [i for i in range(21, 31)],
                       'July' : [i for i in range(1, 32)],
                       'August' : [i for i in range(1, 32)],
                       'September': [i for i in range(1, 22)]},
           'Autumn' : {'September': [i for i in range(22, 31)],
                       'October' : [i for i in range(1, 32)],
                       'November':[i for i in range(1, 31)],
                       'December' : [i for i in range(1, 21)]},
           'Winter' : {'December' : [i for i in range(21, 32)],
                       'January': [i for i in range(1, 32)],
                       'February' : [i for i in range(1, 30)],
                       'March' : [i for i in range(1, 20)]}
}

# Get user input
input_month = input("Enter a month: ")
input_day = int(input("Enter a day: "))
found_date = False

for season, months in seasons.items():
    for month, days in months.items():
        for day in days:
            if (input_month == month) and (input_day == day):
                print(season)
                found_date = True
                
if found_date == False:
    print("Invalid")