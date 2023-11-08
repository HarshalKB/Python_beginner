# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

pass_list = []

for i in range(nr_letters):
    pass_list.append(letters[random.randint(0, len(letters) - 1)])

for i in range(nr_numbers):
    pass_list.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(nr_symbols):
    pass_list.append(symbols[random.randint(0, len(symbols) - 1)])

pass_len = nr_letters + nr_numbers + nr_symbols
password = ''

for i in range(pass_len):
    password += pass_list.pop(random.randint(0, len(pass_list) - 1))

print(password)
