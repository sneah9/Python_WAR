import random

print("WAR: There is only so much within your control!")
user = input("Welcome warrior, enter your name to begin:")
play = input("Shuffle and deal? y/n") 

#create shuffled deck
deck= []
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
    for card in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:  
        deck.append(card+suit)

#create dictionary of values for each card
values= []
for x in range(4):
    for value in range(2,15):
        values.append(value)
key = dict(zip(deck, values))

#create lists for each player's hand and the cards in play
userHand= []
userPlay= []
cpuHand= []
cpuPlay= []

if play == "y":
    print("Your cards are being shuffled and dealt")
    random.shuffle(deck)
    for i in range(0,len(deck)-1,2):  
        userHand.append(deck[i])
        cpuHand.append(deck[i+1])
    print(userHand, "\n",cpuHand)
    count=0
    while (len(userHand)>0) and (len(cpuHand)>0):
        if (len(userPlay) == 0) & (len(cpuPlay) ==0):
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
            print(userPlay)
            print(cpuPlay)

        userValue = key.get(userPlay[0])
        cpuValue = key.get(cpuPlay[0])
        print (userValue)
        print (cpuValue)

        if userValue > cpuValue:
            for x in range(len(userPlay)):
                userHand.append(userPlay.pop(0))
                userHand.append(cpuPlay.pop(0))

        elif userValue < cpuValue:
            for y in range(len(userPlay)):
                cpuHand.append(userPlay.pop(0))
                cpuHand.append(cpuPlay.pop(0))

        else:
            for z in range(4):
                if (len(userHand) != 0) & (len(cpuHand) !=0):
                    userPlay.insert(0, userHand.pop(0))
                    cpuPlay.insert(0, cpuHand.pop(0))
            print(userPlay)
            print(cpuPlay)
            
        count+=1
        print(userPlay)
        print(cpuPlay)    
        print('You have', len(userHand), 'cards in your hand')
        print('the computer has', len(cpuHand), 'cards in its hand')
        print('end of round', count)
    if cpuHand == 0:
        print(user + ', you have won the WAR!')
    else:
        print(user + ', you have lost the WAR!')
    print(cpuPlay, userPlay, count)

        
else:
    print("Have a great day, come back when you are ready to engage in WAR")
    exit