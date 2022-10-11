import random


# ------------------------ Player guesses-----------------------
def guessing(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Try guessing a number from 1 to {x}: '))
        if guess < random_number:
            print('Too low, try again')
        elif guess > random_number:
            print('Too high, try again')
    print(f'You guessed {random_number} right!')


# guessing(20)


# ------------------------ Computer guesses-----------------------
def computer_turn(x):
    low_bound = 1
    high_bound = x
    comp_guess = ''
    while comp_guess != 'C':
        if low_bound != high_bound:
            guess = random.randint(low_bound, high_bound)
        else:
            guess = low_bound
        comp_guess = input(f'Is my {guess} too high (H), too low (L) or correct (C)?:  ').upper()
        if guess == 'H':
            high_bound = guess - 1
        elif guess == 'L':
            low_bound = guess + 1
    print(f'The computer guessed {guess} right!')


computer_turn(20)