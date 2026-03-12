import random
from typing import Optional

import random
from typing import Optional

MIN_ETINY = 1
MAX_ETINY_SIMPLE = 10
MAX_ETINY_MEDIUM = 50
MAX_ETINY_HARD = 100

LEVELS = ["Simple", "Medium", "Hard"]

LEVEL_TO_MAX = {
    "Simple": MAX_ETINY_SIMPLE,
    "Medium": MAX_ETINY_MEDIUM,
    "Hard": MAX_ETINY_HARD,
}


def request_user_input(max_entry: int) -> Optional[int]:
    try:
        return int(input(f'Guess a number ({MIN_ETINY}-{max_entry}): '))
    except ValueError:
        return None


def request_num_of_attempts() -> Optional[int]:
    try:
        return int(input('How many attempts do you want? '))
    except ValueError:
        return None


def select_level() -> Optional[str]:
    print("Select difficulty level:")

    for i, level in enumerate(LEVELS, start=1):
        print(f"{i}. {level}")

    try:
        choice = int(input("Enter your choice (1-3): "))
        if 1 <= choice <= len(LEVELS):
            return LEVELS[choice - 1]
    except ValueError:
        pass

    print("Invalid selection!")
    return None


def guess_number(magic_number: int, guess: int) -> bool:
    if guess == magic_number:
        print('Correct! 🎉')
        return True
    elif guess > magic_number:
        print('Your guess is too high!')
    else:
        print('Your guess is too low!')
    return False


def guess():
    print('🎮 Welcome to the Number Guessing Game!')

    selected_level = select_level()
    if selected_level is None:
        return

    max_entry = LEVEL_TO_MAX[selected_level]

    attempts = request_num_of_attempts()
    if not attempts or attempts <= 0:
        print('Invalid number of attempts!')
        return

    magic_number = random.randint(MIN_ETINY, max_entry)

    for _ in range(attempts):
        guess_input = request_user_input(max_entry)

        if guess_input is None:
            print('Please enter a valid number!')
            continue

        if guess_number(magic_number, guess_input):
            return

    print(f'Sorry! The correct number was {magic_number}')


if __name__ == '__main__':
    guess()
