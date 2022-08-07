import random

word_list = ['amin', 'asif', 'afsar']
chosen_word = random.choice(word_list)
print('It is a', len(chosen_word), 'letter word\nYou have', len(chosen_word), 'lives')

# create an empty list using '_' to show how many letters are there

display = []
for letter in chosen_word:
    display.append('_')
print(''.join(display))

# while loop for receiving user input until all empty index positions filled

lives = len(chosen_word)
while '_' in display:
    letter_index = -1  # letter index for adding letter at specific index no in list
    guess_letter = input('guess the letter: ')
    guess_letter.lower()
    for letter in chosen_word:
        letter_index += 1
        if letter == guess_letter:
            display[letter_index] = guess_letter
            print("That's right")
    print(''.join(display))
    if guess_letter not in chosen_word:
        lives -= 1
        print(f'Wrong guess. You have {lives} more lives.')
        if lives == 0:
            print('You lost')
            break
else:
    print('You won')
