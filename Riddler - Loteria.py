from random import *
file = open('Riddler - Loteria.txt', 'w')
file.write('Game,Winner,CardsLeft,Draws\n')

mainDeck = []
mainDeck.extend(range(1,55))

for game in range (1,5000300):
    myDeck = sample(mainDeck,16)
    yourDeck = sample(mainDeck,16)
    drawOrder = sample(mainDeck,54)
    draws = 0
    winner = ''
    remaining = 0
    
    for i in drawOrder:
        draws += 1
        while i in myDeck:
            myDeck.remove(i)
        while i in yourDeck:
            yourDeck.remove(i)
        if len(myDeck) == 0 and len(yourDeck) == 0:
            winner = "Tie"
            remaining = 0
            break        
        if len(myDeck) == 0:
            winner = "Me"
            remaining = len(yourDeck)
            break
        if len(yourDeck) == 0:
            winner = "Christina"
            remaining = len(myDeck)
            break
                
   
#    print game, winner, remaining, draws        

    if game%100000==0:
        print game
    file.write(str(game)+','+winner+','+str(remaining)+','+str(draws)+'\n')

file.close


