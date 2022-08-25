import random
from replit import clear


def keep_playing():

    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print('Jack, Queen and king all count to 10 in this game.')

    your_cards = [random.choice(cards), random.choice(cards), random.choice(cards)]
    computers_cards = [random.choice(cards), random.choice(cards), random.choice(cards)]

    print(f"Your cards = {your_cards[0], your_cards[1]}")
    print(f"Computers card = {computers_cards[0]}")

    print(f"Your hand = {your_cards[0], your_cards[1]},"
          f" current score = {your_cards[0] + your_cards[1]}")

    your_score = your_cards[0] + your_cards[1]

    print(f"computers hand = {computers_cards[0], computers_cards[1]},"
          f" current score = {computers_cards[0] + computers_cards[1]} ")

    computers_score = computers_cards[0] + computers_cards[1]

    want_to_continue = input("Type 'Yes' if you want to get another card or type 'No' to pass: ").lower()
    if want_to_continue == 'yes':
        print(f"Your final hand = {your_cards[0], your_cards[1], your_cards[2]},"
              f" final score = {your_cards[0] + your_cards[1] + your_cards[2]}")

        your_score = your_cards[0] + your_cards[1] + your_cards[2]

    if computers_cards[0] + computers_cards[1] < 17:
        print('Computers score was less than 17 so it took another card')
        print(f"computers final hand = {computers_cards[0], computers_cards[1], computers_cards[2]},"
              f" final score = {computers_cards[0] + computers_cards[1] + computers_cards[2]}")

        computers_score = computers_cards[0] + computers_cards[1] + computers_cards[2]

    if 21 > your_score > computers_score:
        print('congratulations! you won!')
    elif 21 > computers_score > your_score:
        print('Computer won')
    elif your_score > 21 > computers_score:
        print('you went over, computer won')
    elif computers_score > 21 > your_score:
        print('computer went over, you won')
    elif computers_score and your_score > 21:
        print('both went over, try again')
    elif your_score == computers_score:
        print('both scored same. it a draw')

    want_to_keep_playing = input("type 'Yes' if you want to keep playing or type 'No' to stop ").lower()
    if want_to_keep_playing == 'yes':
        clear()
        keep_playing()
    elif want_to_keep_playing == 'no':
        print('Thank you!')


keep_playing()
