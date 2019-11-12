import string
import random
def need(str):
    while True:
        need = input(str + ' [y/n]\n')
        if need == 'y':
            return True
        elif need == 'n':
            return False
        else:
            print('Please submit either n for no or y for yes.')
def intcheck(str):
    i = input(str)
    while True:
        try:
            i = int(i)
            return i
        except:
            i = input('*ERROR* YOU HAVE TO ENTER AN INTEGER\n' + str)
def randpass(length,list):
    outlist = []
    for i in range(0,length):
        outlist.append(list[random.randint(0, len(list) - 1)])
    return outlist
def plsreset():
    while True:
        reset = input(': ')
        if reset == 'new' or reset == 'restart' or reset == 'exit':
            return reset
        print('*ERROR*\nTo generate a new password type [new], to change the settings type [restart], to exit the program type [exit]')
def checklist(lis):
    for i in range(0 , len(lis) - 1):
        if lis[i] in password:
            return True
    return False
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
number = list(string.digits)
special = list('!#$%&()*+,-./:;<=>?@[]^_`{|}~')
while True:
    possible = lower + upper + number
    length = intcheck('How many characters do you want your password to contain?\n')
    if need('Do you want your password to contain special characters [!, _, @ ect...)?'):
        possible += special
    needupper = need('Does your password require atleast one uppercase letter?')
    neednumber = need('Does your password require atleast one number?')
    while True:
        password = randpass(length,possible)
        if needupper and neednumber:
            while True:
                if checklist(upper) and checklist(number):
                    break
                password = randpass(length,possible)
        elif needupper:
            while True:
                if checklist(upper):
                    break
                password = randpass(length,possible)
        elif neednumber:
            while True:
                if checklist(number):
                    break
                password = randpass(length,possible)
        password = ''.join(password)
        print('Your random password is: ' + password)
        reset = plsreset()
        if reset == 'new':
            continue
        else:
            break
    if reset == 'exit':
        print('Thanks for using this password generator')
        break
        
                            
    
        
    
