from random import randint
import time, os

os.system('title Hangman')


def draw(count):
    hangman = '                ________________\n' \
              '               /_______________ \\\n' \
              '              //               \\ |\n' \
              '              ||               |_|\n'
    if count > 0:
        hangman += '              ||              __|__\n' \
                   '              ||             / _ _ \\\n' \
                   '              ||            |  O O  |\n' \
                   '              ||            |   A   |\n' \
                   '              ||            |  ___  |\n' \
                   '              ||             \\_____/\n'
        if count > 4:
            hangman += '              ||              _| |_\n' \
                       '              ||             /     \\\n' \
                       '              ||            / /| |\\ \\\n' \
                       '              ||           / / | | \\ \\\n' \
                       '              ||           ||  | |  ||\n' \
                       '              ||          /TT¤ | | ¤TT\\\n'
            if count == 6:
                hangman += '              ||               / \\\n' \
                           '              ||              / _ \\\n' \
                           '              ||             / / \\ \\\n' \
                           '              ||            | |   | |\n' \
                           '              ||          __| |   | |__\n' \
                           '              ||         |_____| |_____|\n'
            if count == 5:
                hangman += '              ||               / |\n' \
                           '              ||              / /\n' \
                           '              ||             / /\n' \
                           '              ||            | |\n' \
                           '              ||          __| |\n' \
                           '              ||         |_____|\n'
        elif count == 4:
            hangman += '              ||              _| |_\n' \
                       '              ||             /     \\\n' \
                       '              ||            / /| |\\ \\\n' \
                       '              ||           / / | | \\ \\\n' \
                       '              ||           ||  | |  ||\n' \
                       '              ||          /TT¤ |_| ¤TT\\\n'
        elif count == 3:
            hangman += '              ||              _| |\n' \
                       '              ||             /   |\n' \
                       '              ||            / /| |\n' \
                       '              ||           / / | |\n' \
                       '              ||           ||  | |\n' \
                       '              ||          /TT¤ |_|\n'
        elif count == 2:
            hangman += '              ||               | |\n' \
                       '              ||               | |\n' \
                       '              ||               | |\n' \
                       '              ||               | |\n' \
                       '              ||               | |\n' \
                       '              ||               |_|\n'
    else:
        hangman += '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n'
    if count <= 1:
        hangman += '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n'
    if count <= 4:
        hangman += '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n' \
                   '              ||\n'
    hangman += ' _____________||_____________\n' \
               '/                            \\\n'
    return hangman


def helper(lis):
    if failed_guess:
        failed_str = ''
        for i in range(0, len(failed_guess) - 1):
            failed_str += failed_guess[i] + ', '
        failed_str += failed_guess[len(failed_guess) - 1]
        helper_str = '  You have already guessed\n  these letters and words:\n  %s\n' % failed_str
    else:
        helper_str = ''
    helper_str += '\n  Word: '
    for a in lis:
        helper_str += a + ' '
    return helper_str + '\n'


def restart_check():
    restart_str = input('Would you like to play again? [y/n]\n').casefold()
    if restart_str == 'y' or restart_str == 'n':
        return restart_str
    else:
        os.system('cls')
        time.sleep(0.1)
        print('Oops! Please type only a y or an n...')
        return False


while True:
    win = False
    failed_count = 0
    failed_guess = []
    with open('text/words.txt', mode='r') as file:
        word_list = file.readlines()
        correct = word_list[randint(0, len(word_list) - 1)].replace('\n', '').upper()
        if len(correct) == 1:
            continue
    correct_list = list(correct)
    word_helper = ['_' for a in range(0, len(correct))]
    os.system('cls')
    while True:
        print(draw(failed_count))
        if failed_count == 6:
            time.sleep(1.5)
            os.system('cls')
            print('\n' + draw(failed_count).replace('O', 'X'))
            win = False
            break
        print(helper(word_helper))
        while True:
            guess = input('Take a guess!\n')
            if guess.isalpha():
                break
            print('Please sumbit a letter or word containing only letters')
        guess = guess.casefold().upper()
        os.system('cls')
        time.sleep(0.3)
        if guess in failed_guess or guess in word_helper:
            print('You already guessed that!')
            continue
        elif len(guess) == 1:
            if guess in correct:
                print('You guessed correctly!')
                for i in range(0, len(correct)):
                    if guess == correct[i]:
                        word_helper[i] = guess
                if not '_' in word_helper:
                    win = True
                    break
                continue
        elif len(guess) == len(correct):
            if guess == correct:
                win = True
                break
        else:
            print('That phrase does not appear to have the right length...')
            continue
        print('You guessed wrong...')
        failed_guess.append(guess)
        failed_count += 1
    if win:
        print('                          _____\n'
              'Congratulations!         / _ _ \\\n'
              '                        |  O O  |\n'
              'You won, and your man   |   A   |\n'
              'walks free!             |  \\_/  |\n'
              '                         \\_____/\n'
              '                          _| |_\n'
              '                         /     \\\n'
              '                        / /| |\\ \\\n'
              '                       / / | | \\ \\\n'
              '                       ||  | |  ||\n'
              '                      /TT¤ | | ¤TT\\\n'
              '                           / \\\n'
              '                          / _ \\\n'
              '                         / / \\ \\\n'
              '                        | |   | |\n'
              '                      __| |   | |__\n'
              '                     |_____| |_____|\n')
        time.sleep(5)
    else:
        print('\nYou lost...\n')
        time.sleep(1)
        print('\nThe correct word was "%s" ...' % (correct))
    while True:
        restart = restart_check()
        if restart:
            break
    os.system('cls')
    time.sleep(0.25)
    if restart == 'n':
        print('exiting...')
        time.sleep(0.5)
        break
    else:
        print('restarting...')
        time.sleep(0.5)
        os.system('cls')
