from random import *
file = open('Riddler - Loteria GRID.txt', 'w')
file.write('DeckSize,GridSize,Shutouts\n')

deckSizes = [22,26,30,34,38,42,46,50,54,58,62,66,70,74,78]
gridSizes = [4,9,16,25,36]

for x in deckSizes:
    for y in gridSizes:
        if x<y:
            break

        mainDeck = []
        mainDeck.extend(range(1,x+1))
        empty = 0
        
        for game in range (1,500001):
            myDeck = sample(mainDeck,y)
            yourDeck = sample(mainDeck,y)
            drawOrder = sample(mainDeck,x)
            remaining = 0
            
            for i in drawOrder:
                while i in myDeck:
                    myDeck.remove(i)
                while i in yourDeck:
                    yourDeck.remove(i)
                if len(myDeck) == 0 and len(yourDeck) == 0:
                    break        
                if len(myDeck) == 0:
                    remaining = len(yourDeck)
                    break
                if len(yourDeck) == 0:
                    remaining = len(myDeck)
                    break
            if remaining == y:
                empty += 1
        
        print x,y,empty
        file.write(str(x)+','+str(y)+','+str(empty)+'\n')

file.close


