users = {}
with  open("Users.txt") as f:
    for line in f:
        (key, val) = line.split
        users[str(key)] = val
        
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

def create_account(users):
    username = input('Enter Your Username')
    password = input('Enter Your Password')
    conferm = input(Please Conferm Your Password')
    if conferm == password:
        name = input('Name')
        email = input('Email')
        points = 0
        times_played = 0
        users[username] = [password, name, email, points, times_played]
        stf = open("Users.txt")
        stf = None
        stf = stf.append(users)
    if conferm != password;
        print("Values do not match")
        if input('Would you like to try again(Yes)' == yes or Yes:
            create_account(users)
        else:
            break





