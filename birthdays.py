import json
import time
import os
import datetime
from functools import reduce

def init():
    with open("json/birthdates.json", "r") as f:
        birthdates = json.load(f)
    for person in birthdates:
        birthdates[person] = datetime.date.fromisoformat(birthdates[person])
    os.system('color 0b')
    today = datetime.date.today()
    main(birthdates, today)


def main(birthdates, today):
    people = sorted(list(birthdates.keys()), key=lambda a: a.split()[-1])
    nextbday = [people[0]]
    distbday = get_distbday(today, birthdates[people[0]])
    for person in people[1:]:
        if get_distbday(today, birthdates[person]) == distbday:
            nextbday.append(person)
        if get_distbday(today, birthdates[person]) < distbday:
            nextbday = [person]
            distbday = get_distbday(today, birthdates[person])
            
    if len(nextbday) == 1:
        bday_str = f'{nextbday[0]} sin bursdag'
        pronomen = 'vedkommende'
    else:
        bday_str = f'{", ".join(nextbday[:-1])} og {nextbday[-1]} sin bursdag'
        pronomen = 'de'
    dates = [birthdates[person] for person in nextbday]
    if (today.month, today.day) == (birthdates[nextbday[0]].month, birthdates[nextbday[0]].day):
        print(f'I dag er det {bday_str}!\nI dag er {pronomen} {format_age(today, dates)} år gammel!')
    else:
        print(f'Den neste bursdagen er {bday_str} som er den {decode_bday(birthdates[nextbday[0]])[:-5]}.\nDa blir {pronomen} {format_age(today, dates)} år gammel!\n')
    print(''.join(['-' for i in range(0,60)]))
    
    while True:
        inp = ''
        names = people[:]
        print('Personene jeg vet bursdagen til:\n')
        for a in names:
            print(a)
        inp = input('\nHvem sin bursdag vil du vite?\n').casefold()
        if inp == 'add':
            json_add()
            continue
        compare = {}
        while True:
            names_split = [name.casefold().split() for name in names]      
            os.system('cls')
            inp_split = inp.split()
            for i in range(len(inp_split)):
                compare_list = [0 for a in range(0, len(names))]
                for j in range(len(names)):
                    if inp_split[i] in names_split[j]:
                        compare_list[j] = 1
                compare[i] = compare_list
            
            search = [reduce(lambda a, b: a * b, (compare[j][i] for j in range(len(compare)))) for i in range(len(names))]
            names = [names[i] for i in range(len(names)) if names[i] * search[i]]
            
            if not names:
                print('Denne personen finnes ikke i databasen...\n')
            elif len(names) > 1:
                out_str = f'{", ".join(names[:-1])} eller {names[-1]}'
                inp = input(f'Mente du {out_str}?\n')
                continue
            else:
                print(f'{names[0]} ble født {decode_bday(birthdates[names[0]])}\n')
            time.sleep(1.5)
            break

def get_distbday(now, then):
    return (then.month - now.month) % 12, then.day - then.day

def get_age(today, born):
    return today.year - born.year - ((today.month, today.day - 1) < (born.month, born.day))

def days_passed(today):
    days_passed = today[0] - 1
    for i in range(0, today[1]):
        if i in range(1,8,2) or i in range(8, 13, 2):
            days_passed += 31
        elif i in [4, 6] or i in range(9, 12, 2):
            days_passed += 30
        elif i == 2:
            days_passed += 28
            if int(str(datetime.datetime.now()).split()[0].split('-')[0]) % 4 == 0:
                days_passed += 1
    return days_passed

def format_age(today, dates):
    if (today.month, today.day) != (dates[0].month, dates[0].day):
        currDay = today.replace(year=today.year + 1)
        print(currDay)

    if all(date.year == dates[0] for date in dates):
        return get_age(currDay, dates[0])
    else:
        return f"{', '.join(str(get_age(currDay, date)) for date in dates[:-1])} og {get_age(currDay, dates[-1])}"

def decode_bday(bday):
    months = ['januar', 'februar', 'mars',
              'april', 'mai', 'juni', 'juli',
              'august', 'september', 'oktober',
              'november', 'desember']
    return f'{bday.day}. {months[bday.month]} {bday.year}'

def json_add():
    with open('json/birthdates.json', 'r') as f:
        birthdays = json.load(f)
    try:
        while True:
            name = input('Name: ')
            while True: 
                date = input('Date: ')
                try:
                    datetime.date.fromisoformat(date)
                    break
                except ValueError as e:
                    print(e)             
            birthdays[name] = [date]
    except:
        with open('json/birthdays.json', 'w') as f:
            json.dump(birthdays,f)

if __name__ == '__main__':
    init()