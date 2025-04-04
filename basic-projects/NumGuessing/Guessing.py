import random

guess = random.randrange(100)

chances = 7

count = 0

print("NUMBER guessing game")
print("=============================")
while count < chances:

    count += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {count} attempt')
        break

    elif count >= chances and my_guess != guess:
        print(f'Oops sorry, The number is {guess} better luck next time')

    elif my_guess > guess:
        print('Your guess is higher ')

    elif my_guess < guess:
        print('Your guess is lesser')

