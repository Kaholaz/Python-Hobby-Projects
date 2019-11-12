import random, os
os.system('title Guessing Game')
def intcheck(str):
    i = input(str)
    while True:
        try:
            i = int(i)
            return i
        except:
            i = input('*ERROR* YOU HAVE TO ENTER AN INTEGER\n' + str)
def guess():
    x = 0
    while True:
        x += 1
        guess = intcheck('Take a guess!\n')
        if guess < num:
            print('¨You need to go higer!')
        elif guess > num:
            print('You need to go lower!')
        elif guess == num:
            return x
def minmax(str):
    return(str + ': ')
def restart():
    while True:
        restart = input('Would you like to play again? [y/n]:\n')
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print('Oops! Please type only a y or an n...')
while True:
    print('Between what two numbers would you like the random number to be chosen?')
    while True:
        min = intcheck(minmax('min'))
        max = intcheck(minmax('max'))
        if min < max:
            break
        else:
            print('*ERROR* THE LOWEST VALUE HAS TO BE LOWER THAN THE HIGHEST')
    num = random.randint(min,max)
    numofGuesses = guess()
    print('You got it right after only %d guesses!' % (numofGuesses))
    if not restart():
        break
            
