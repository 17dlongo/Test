import random
number = random.randint(1,100)
player1 = input('Name of Player 1')
player2 = input('Name of Player 2')
def is_it(number):
    guess = input('guess a number')
    if type(guess) is int:
        if guess > number:
            print('A tad to high')
            is_it(number)
        if guess < number:
            print('A tad to low')
            is_it(number)
        if guess == number:
                  print('You got it')
                  return number
                  print(guess)
    if type(guess) is str:
        print('Invalid input')
        is_it(number)

is_it(number)
