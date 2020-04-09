import random

def wannaPlay():
    while True:
        yes = input("Would you like to roll a die? Please type yes if so, please type no to exit\n")

        play = str("yes")
        dontPlay = str("no")

        while yes == play:
            roll()
        else

def roll():
#declaring a list named dice 
    dice = [1,2,3,4,5,6]
   
#randomizng list 
    roll = random.choice(dice)
# assigns the roled value to x

    x  = str(roll)
    print("You rolled a " + x)
    savedRoll = []
    # appends to list
    savedRoll = x.append()

def rollAgain():
    roll()

#def endGame():
    print("I hope rolling this die cured your Covid-19 boredom!!")

def rollHistory():
   print(savedRoll)


def main():
    wannaPlay()
    #print("Would you like to roll a die? Please type yes if so, please type no to exit")
    roll()
    print("Would you like to roll again?, Plese type again if so, please type stop to exit")


if __name__ == '__main__':
    main()


