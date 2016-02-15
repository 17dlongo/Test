import math

def is_prime(number):
    for n in range(2,int(math.sqrt(number))):
        if number%n == 0:
            return False
    return True
    
 
     
            

def numbers(numbervariable):
    for x in range(0,100):
        if x%(numbervariable) == 0:
            print((x))
    print("hello")
def nxprime(number):
    x = number + 1
    while is_prime(x) == False:
        x = x + 1
    return x
#for x in range(1,10):
#    print(nxprime(x))                    


print(is_prime(5915587277))
