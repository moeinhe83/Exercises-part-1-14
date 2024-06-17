# Practice_14

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 14', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value 
number = (3, 4, 5, 2, 1, 7, 8, 9, 6, 10)

# Convert Tuple To List
number = list(number)

# Display In Reverse Order
number.sort()
print(number)
number.sort(reverse=True)
print(number)


# Finish
# Create By Moein Heshmati
