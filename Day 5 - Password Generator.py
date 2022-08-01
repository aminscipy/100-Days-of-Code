import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print('Welcome to password generator')

num_letters = int(input('How many letters you want in your password? : '))
num_symbols = int(input('How many symbols you want in your password? : '))
num_numbers = int(input('How many numbers you want in your password? : '))

# combining random letters, numbers and symbols

password = str()
for i in range(num_letters):
    x = random.choice(letters)
    password += x
for j in range(num_symbols):
    y = random.choice(symbols)
    password += y
for k in range(num_numbers):
    z = random.choice(numbers)
    password += z

# generating random string(password) using combined string

password = list(password)
random.shuffle(password)
password = ''.join(password)
print('Your Password is :', password)
