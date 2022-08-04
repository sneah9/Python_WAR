""" 1. I will be creating the basic card game War; it is the first game that I learned to play with a 52 card deck and teaches about the basic ranking of cards.  

2. I am unsure as of yet, which data structures I will be using for the deck of cards and the two players hands.  I will need to create a hierarchy of cards but will also need to disregard the suits in terms of value ranking.  I thought that a dictionary could work for the "deck" of cards in order to give the value of each card as the value in the dictionary for the game to compare logic.  The players hand will likely be a list so that we can keep it ordered and when the player wins a hand it will go at the "bottom" and they will play from the "top".

3. the game should begin by allowing the player to enter their name, then welcome the player and prompt them to begin the game by pressing a start button, this will "shuffle and deal" the cards.

-the player will be prompted to start the hand by pressing a button and see the results

-each hand will be declared as a win, loss or draw which will create the special example of dealing the next 4 cards; next three "face down(value of these cards doesn't matter in game logic)" and the forth card "face up" in comparison to the computer player's card value.

-the game will end and the winner announced on screen when all the cards are in a single player's hand. """


import random

print("WAR: There is only so much within your control!")
#user = input("Welcome, enter your name to begin:")
play = input("Shuffle and deal? y/n") 
#create shuffled deck
deck= []
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
    for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        deck.append(value+suit)


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
    b=0
    while (len(userHand)>0) and (len(cpuHand)>0):
        userPlay.append(userHand.pop(0))
        cpuPlay.append(cpuHand.pop(0))
        print(userPlay)
        print(cpuPlay)
        if userPlay > cpuPlay:
            userHand.append(userPlay)
            userHand.append(cpuPlay)
            userPlay.pop
            cpuPlay.pop
        elif userPlay < cpuPlay:
            cpuHand.append(userPlay)
            cpuHand.append(cpuPlay)
            userPlay.pop
            cpuPlay.pop
        else:
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
        b+=1    
    print(cpuPlay, userPlay, b)
        






else:
    print("Have a great day, come back when you are ready to engage in WAR")
    exit


