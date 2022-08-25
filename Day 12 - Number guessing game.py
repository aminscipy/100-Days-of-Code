import random


def guess_the_number():
    print("Welcome to the number guessing game.\nI am thinking about number between 1 to 100.")
    difficulty_level = input("Choose difficulty level. type 'easy' or 'hard': ").lower()

    def number_of_attempts():
        if difficulty_level == 'easy':
            print("You have 10 attempts left to guess the number")
        elif difficulty_level == 'hard':
            print("You have 5 attempts left to guess the number")
        else:
            print("wrong input. choose again")
            number_of_attempts()

    number_of_attempts()

    guessed_number = random.choice(range(1, 100))

    if difficulty_level == 'easy':
        should_continue = True
        attempts_left = 10
        while should_continue:
            make_guess = int(input('Make guess: '))
            if make_guess < guessed_number:
                print("too low")
                attempts_left -= 1
                print(f"You have {attempts_left} attempt left to guess the correct number")
                if attempts_left == 0:
                    print("You run out of guesses. You lost")
                    should_continue = False
            elif make_guess > guessed_number:
                print("too high")
                attempts_left -= 1
                print(f"You have {attempts_left} attempt left to guess the correct number")
                if attempts_left == 0:
                    print("You run out of guesses. You lost")
                    should_continue = False
            elif make_guess == guessed_number:
                print("congratulations! it's correct number. you won")
                should_continue = False
            else:
                print('invalid input, guess again')

    if difficulty_level == 'hard':
        should_continue = True
        attempts_left = 5
        while should_continue:
            make_guess = int(input('Make guess: '))
            if make_guess < guessed_number:
                print("too low")
                attempts_left -= 1
                print(f"You have {attempts_left} attempt left to guess the correct number")
                if attempts_left == 0:
                    print("You run out of guesses. You lost")
                    should_continue = False
            elif make_guess > guessed_number:
                print("too high")
                attempts_left -= 1
                print(f"You have {attempts_left} attempt left to guess the correct number")
                if attempts_left == 0:
                    print("You run out of guesses. You lost")
                    should_continue = False
            elif make_guess == guessed_number:
                print("congratulations! it's correct number. you won")
                should_continue = False
            else:
                print('invalid input, guess again')

    def keep_playing():
        want_to_continue = input("type 'Yes' to continue playing or type 'No' to stop the game: ").lower()
        if want_to_continue == 'yes':
            guess_the_number()
        elif want_to_continue == 'no':
            print("Thank you")
        else:
            print("invalid input.")
            keep_playing()
    keep_playing()


guess_the_number()
