player1 = str(input('Name of Player 1'))
pa = False
pb = False
import random 
player2 = str(input('Name of Player 2'))
number = random.randint(1,101)
print('' + player1 + ' guess a number')
pa = True
print(number)

while pa == True:
    guess = int(input('' + player1 + ' guess a number'))
    if guess > number:
        print(guess)
        print('is too high')
        pb = True
        pa = False
    if guess < number:
        print(guess)
        print('is too low')
        pb = True
        pa = False
    if guess == number:
        print(guess)
        print('is correct!!!!')

while pb == True:
    guess = int(input('' + player2 + ' guess a number'))
    if guess > number:
        print(guess)
        print('is too high')
        pa = True
        pb = False
    if guess < number:
        print(guess)
        print('is too low')
        pa = True
        pb = False

    if guess == number:
        print(guess)
        print('is correct!!!!')
        
              
    
