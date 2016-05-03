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
def log_in(users):
    username = input('Enter Your Username')
    if username is in users:
        password = input('Enter Uour Password')
        if password = users[username][0]:
            return users[username][0:]
    if username is not in users:
        choice = input('This username does not exist in the data bases. Would you like to (retry) or (create user)')
        if choice == 'retry' or 'Retry'
            return log_in(users)
        if choice == 'create user' or 'Create user' or Create User':
            retrun create_user

def make(number):
    guess = input('Guess a number 1 to 100')
    if guess > number:
        print(guess)('Is too large guess a smaller number')
        return 1
    elif guess < number:
        print(guess)('Is too small guess a larger number')
        return 1
    elif guess == number:
        print('You guessed it!!!!!)
        return 2


def play():
    number = random.randint(1,100)
    P1tn = False
    P2th = True
    Guesses = 0
    While P1tn == True:

        if guess > 6:
            print('you are out of guesses')
            retrun play()
        if make(number) == 2:
            P1pt += Guesses* 10
        if make(number) == 1:
            Guesses += 1
    
   




