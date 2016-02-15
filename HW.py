def allpb(base, letters, y):
    print(base)
    for letterInd in range(0, len(letters)):
        baseb = base + letters[letterInd]
        newLetters = letters[:letterInd] + letters[letterInd+1:]
        allpb(baseb, newLetters,y)
        y = y +1
print(allpb('','qwertyuiopasdfghjklzxcvbnm',0))
