string = input('Enter Word').lower()
def palindrome(word):
    for index in range(len(word)):
        if word[index] != word[len(word)-index-1]:
            print('This is not one')
            return
    print('This is one')
palindrome(string)


