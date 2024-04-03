import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(1, 8)
nr_symbols = random.randint(1, 8)
nr_numbers = random.randint(1, 8)

password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

# print(password_list)

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# print(password_list)

random.shuffle(password_list)
# print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")
