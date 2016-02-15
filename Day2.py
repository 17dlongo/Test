

def generate_numbers(top):
    x = []
    y = 0
    for y in range(0, top):
        y = y + 1
        x = x + [y]
    return (x)

def delete_odds(x):
    for y in range(1, 1000,2):
        x.remove(y)
    print(x)
    return x
#delete_odds(generate_numbers(1000))

def pstring(t):
    for x in range(len(t)):
        print (t[x])
pstring('HHBJHKBJHGHJGJKGJHGJHHYVYTVYTFRTUTTUYTi')
