# Delera, Aritz B.

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; 
# the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

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
# Create the file even.txt and write all of the even integers that were extracted.
# Create the file oo.txt and write all of the odd integers that were extracted.
