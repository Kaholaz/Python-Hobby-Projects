import math
import os


def prime_(i):
    sqrt = math.sqrt(i)
    for x in prime:
        if i % x == 0:
            return False
        if x > sqrt:
            return True


def intcheck(str):
    i = input(str)
    while True:
        try:
            i = int(i)
            return i
        except:
            i = input('*ERROR* YOU HAVE TO ENTER AN INTEGER\n' + str)
    while True:
        restart = input('Would you like to play again? [y/n]:\n')
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print('*ERROR* Please write only a y or an n...')


def output_check(output):
    checklist = ['save', 'print', 'exit']
    if output in checklist:
        return True
    else:
        return False


def output_func():
    while True:
        output = input('Would you like to [save] them to a file, [print] them so you can copy them, or just [exit]?\n')
        if not output_check(output):
            print('Please use only the commands save, print, or exit')
        else:
            return output


def yesno():
    while True:
        restart = input('It looks like you have previous primes saved, would you like to import them?\n[y/n]:\n')
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print('*ERROR* Please write only a y or an n...')


x = True
with open('data/primes.txt', mode='r') as primes:
    if int(primes.readline()) == 2 and yesno():
        prime_test = primes.readlines()
        prime = [2]
        for prime_num in prime_test:
            prime_num = int(prime_num)
            prime.append(prime_num)
        j = (prime[-1] + 1) % 6
        i = prime[-1] - j
        print(j)
        print(i)
    else:
        prime = [2, 3]
        i = 5
print('imported!')
try:
    print(
        'This is a program designed to find primes\n'
        'You can at any time stop the process by pressint ctrl + c\n'
        'Press any key to start the calculation...')
    os.system('pause >nul')
    while True:
        if prime_(i):
            print('Found a prime!' + str(i))
            prime.append(i)
        i += 2
        if prime_(i):
            print('Found a prime!' + str(i))
            prime.append(i)
        i += 4
except:
    length = len(prime)
    print('You found %d primes!' % (length))
    output = output_func()
    if not output == 'exit':
        if output == 'save':
            with open('data/primes.txt', mode='w') as primes:
                primes.writelines('%d\n' % prim for prim in prime)
            print('Primes saved to primes.txt')
        if output == 'print':
            print(prime)
        print('Press any key to exit the program...')
        os.system('pause >nul')
    else:
        print('Good bye!')
