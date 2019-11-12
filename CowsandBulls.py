import random, time, json, os
os.system('title Cows and Bulls')
def intcheck(imp):
    try:
        int(imp)
        return True
    except:
        return False
def digit(lenght):
    dig = []
    for _ in range(0,lenght):
        dig.append(random.randint(0,9))
    return dig
def inputcheck(imp):
    if intcheck(imp) and len(imp) == length:
        return True
    else:
        return False
def cowbull_func():
    cowbull = [0,0]
    numcheck = [1 for i in range(0,length)]
    guesscheck = [1 for i in range(0,length)]
    for i in range(0,length):
        if guess[i] == num[i]:
            cowbull[1] += 1
            numcheck[i] = 0
            guesscheck[i] = 0
        else:
            continue
    numlist = [(a + 1) * b for a,b in zip(num, numcheck)]
    guesslist = [(a + 1) * b for a,b in zip(guess, guesscheck)]
    for i in range(0,length):
        if guesslist[i] != 0 and (guess[i] + 1) in numlist:
            cowbull[0] +=1
            numlist[numlist.index(guesslist[i])] = 0
    return cowbull
def yesno(str):
    while True:
        restart = input(str)
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print('*ERROR* Please write only a y or an n...')
def open_high():
    try:
        with open('text/CowBull.json') as f:
            high = json.load(f)
            if not len(high) > 10:
                return high
    except:
        pass
    return {}
length = 4
print('This is a game called cows and bulls\nThe computer will generate a random %d digit number and your job is to guess it\nFor every digit you guess right and in the right place, you get a bull\nFor every digit you guess right, but in the wrong place, you get a cow\nThe game ends when you guess all the right digit in the right places\nGood luck!' % (length))
high = open_high()
if len(high) > 0:
    name_lengths = []
    for a in high:
        name_lengths.append(len(high[a][0]))
    name_lengths.sort()
    high_str = ''
    for i in range(1, len(high) + 1):
        high_str += str(i).rjust(2, ' ') + '.' + high[str(i)][0].rjust(name_lengths[len(name_lengths) - 1] + 1, ' ') + str(high[str(i)][1]).rjust(3, ' ') + '\n'
    print('\nHere are the highscores:\n' + high_str)
while True:
    tries = 1
    num = digit(length)
    print('You can at any time type "resign" to give up...\n')
    try:
        while True:
            while True:
                guess = input('Enter a %d digit number to take a guess: ' % (length))
                if guess == 'resign':
                    if tries == 1:
                        print('Atleast give it one shot, wanker!')
                    else:
                        print(f'You gave up after {tries} tries...')
                        time.sleep(0.6)
                        break
                elif inputcheck(guess):
                    guess = [int(a) for a in guess]
                    break
                else:
                    print('*ERROR*')
            if guess == 'resign':
                win = 0
                break
            else:
                cowbull_list = cowbull_func()
                if cowbull_list == [0,4]:
                    print(f'Congratulations! You won after only {tries} tries!!!')
                    time.sleep(0.6)
                    win = 1
                    break
                print('%d bull(s), %d cow(s)' % (cowbull_list[1],cowbull_list[0]))
                tries += 1
        os.system('cls')
        if win:
            high = open_high()
            if len(high) < 10 or tries < high["10"][1]:
                if yesno("You've made the highscores!\nWould you like to save your score? [y/n]:\n"):
                        name = input('\nWhat is you name?\n')
                        i = 0
                        j = 0
                        for i in range(len(high), 0, -1):
                            if tries >= high[str(i)][1]:
                                print('>')
                                j = i
                                break
                            print('continue')
                            j = 0
                        if j != len(high):
                            for k in range(len(high) + 1,i , -1):
                                high[str(k)] = high[str(k - 1)]
                        high[str(j + 1)] = [name, tries]
                        try:
                            del high['11']
                        except:
                            pass
                        with open('text/CowBull.json', 'w') as f:
                            json.dump(high, f)
        if not yesno('Would you like to play again? [y/n]:\n'):
            print('See you soon!')
            time.sleep(1.5)
            break
##        while True:
##            length = input('This time, you can try to make it a little harder for yourself by chosing how many digits you need to guess\nHow many digits long do you want the randomly generated number to be?')
##            if intcheck(length):
##                length = int(length)
##                break
##            else:
##                print('*ERROR* please enter an integer..')
        os.system('cls')
    except:
        print('*EXECUTION ERROR* ERRORCODES:')
        print(num,guess)
        input()
    
    
                  







