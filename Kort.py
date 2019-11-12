import random, os, math, json

def main():
    printInterval = 100000
    deck = [1 for i in range(0, 4)] + [0 for i in range(4, 52)]
    results = []
    print("How many iterations do you want to run?")
    while True:
        inp = input(" >    ")
        try:
            j = int(inp)
            math.sqrt(j)
            break
        except Exception as err:
            print(err)
            print("\nPlease enter an integer larger or equal to 0...")
    try:
        if j == 0:
            while True:
                appendAceNr(deck, results, printInterval)
        else: 
            for _ in range(0, j):
                appendAceNr(deck, results, printInterval)
    except KeyboardInterrupt:
        pass
    if len(results) % printInterval != 0:
        printResults(results, len(results))
    print("\n{0}".format(''.join(["-" for l in range(0,39)])))
    os.system("pause")
    saveToJson("kortData", results)

def appendAceNr(deck, results, printInterval):
    aceNr = getAceNr(deck)
    results.append(aceNr)
    reslen = len(results)
    if reslen % printInterval == 0:
        printResults(results, reslen)

def printResults(res, i):
    print("\n\nResults after {0} tries:\n\n".format(i))
    for j in range(0,5):
        printAceStat(res, j)


def getRandomDeck(deckLocal):
    randDeck = deckLocal[:]
    random.shuffle(randDeck)
    return randDeck

def getAces(cards):
    aceNr = 0
    for card in cards:
        aceNr += card
    return aceNr

def printAceStat(resloc, nr):
    count = resloc.count(nr)
    presentage = (count / len(resloc)) * 100
    formatedPres = round(presentage, 3)
    print(" >   {0} ACES: {1} -- {2}%".format(nr, count, formatedPres))

def inpCheck(inpLocal):
    try:
        inpLocal = int(inpLocal)
        if inpLocal > 0:
            return True
        else:
            return False
    except:
        return False

def getAceNr(deck):
    deck = deck[:]
    randDeck = getRandomDeck(deck)
    sample = randDeck[:13]
    aceNr = getAces(sample)
    return aceNr
    # print(deck)
    # print("Length: " + str(len(deck)))

def saveToJson(name, result):
    print("Saving... \n")
    data = {}
    try:
         with open("data\\{0}.json".format(name), "r") as f:
            data = json.load(f) 
    except FileNotFoundError:
        print("'data\\{0}.json' does not exist..\nWriting to new file...")
    except ValueError:
        print("File at path 'data\\{0}.json' is not a valid json file..")
        print("Would you like to overwrite the file? [y/n]")
        if not YorN():
            name += "(1)"
    data[len(data.keys())] = result
    while True:
        try:
            with open("data\\{0}.json".format(name), "w") as f:
                json.dump(data, f)
                print("\nSaved data to data\\{0}.json".format(name))
                break
        except Exception as err:
            print("\nError saving data to file [ {0} ]".format(err))
            print("Would you like to retry?")
            if not YorN():
                break
    print("Press any key to exit the program...")
    os.system("pause >nul")
    
            
def YorN():
    while True:
        inp = input(" >    ").casefold()
        if inp == "y":
            return True
        if inp == "n":
            return False
        else:
            print("\nPlese type 'y' for yes, and 'n' for no..")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
main()

