import random

def guessing_game():
    random_number=random.randint(1,100)

    while True:
        number = input("Enter the number:")
        user_choice = int(number)
        if user_choice==random_number:
            print(f'you guessed the right number: {user_choice}')
            break;
        if user_choice<random_number:
            print(f'The {user_choice} is too low!')
        if user_choice > random_number:
            print(f'The {user_choice} is too high!')


guessing_game()
