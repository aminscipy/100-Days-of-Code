
# simple game base on conditional statements

print('welcome to treasure island')
door = input("to choose one door, type 'left' or 'right' : ").lower()

if door == 'left':
    swim = input("to swim type 'Y', or else type 'n' : ").lower()
    if swim == 'n':
        color_door = input("to choose color door type color of the door, 'blue', 'yellow', red' : ").lower()
        if color_door == 'yellow':
            print('you won')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('game over')
