import random
x = random.randint(1,100)
print (x)
p1 = input('Name of player 1')
p2 = input('Name of player 2')
def roll_die():
    d = random.randint(1,6)
    if d < 3:
        print (d)
        return True
    return False

roll_die()
if roll_die == False:
    print('false')
    
if roll_die == True:
    print('true')
    
