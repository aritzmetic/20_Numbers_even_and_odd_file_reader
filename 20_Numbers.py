# Delera, Aritz B.

import pyfiglet
import random

opening = pyfiglet.figlet_format("= O.O.P =", font = "lean")
print(opening)


# Create an introduction
print("=" * 61)
print(" Welcome to AritzMetic's Number Sorter! ".center(60, "+"))
print("=" * 61)

 # Ask the name of the user to create a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print("\033[40mHi", name, "! AritzMetic is here to help you in Sorting 20 Numbers!\033[0m")

# Open the numbers.txt 
with open("numbers.txt", "r") as input_file:
    numbers = input_file.readlines()
    # numbers.txt needs to have its character data converted into integers.
    numbers = [int(line.strip()) for line in numbers]
# Create separate blank lists for the even and odd integers.
even_numbers = []
odd_numbers = []
# Use for loops to separate the even and odd integers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"\033[46mIn the list, We found {len(even_numbers)} even numbers and {len(odd_numbers)} odd numbers!\033[0m")

# Shuffle the even and odd numbers at random.
random.shuffle(even_numbers)
random.shuffle(odd_numbers)

# Create the file even.txt and write all of the even integers that were extracted.
with open("even.txt", "w") as even_file:
    for n in even_numbers:
        even_file.write("We collected a list of all even numbers:\n")
        even_file.write(str(n) + "\n")

print("\033[31mWe created a new file named 'even.txt' and printed out the even integers there.\033[0m")

# Create the file oo.txt and write all of the odd integers that were extracted.
with open("odd.txt", "w") as odd_file:
    for n in odd_numbers:
        odd_file.write("We collected a list of all odd numbers:\n")
        odd_file.write(str(n) + "\n")

print("\033[31mWe created a new file named 'odd.txt' and printed out the odd integers there.\033[0m")

closing = pyfiglet.figlet_format("Thank you for utilizing Aritzmetic's Number Sorter! We hope that the information was helpful to you.", font="puffy")
print(closing)
