from cards_msu_cse import Card as acard, Deck as adeck

testtablow = ['8C', 'TD', 'KD', 'QD', 'TH', 'QC', '9H', '8S', '5S', 
'4H', '2C', 'QS', '8H', '3C', 'JS', '6H', 'KH', 'JC', 'JH', '2D', '3S', '6C', '7S', '2S', 'KC', '7D', '6D', '5D', '4D', 'KS', '3D', 'AC',  
'2H', '5C', '6S', '7C', '3H', 'QH', '9C', '9S', '5H', 'AS', '9D', 'JD', '4C', 'AD', 'AH', '8D', 'TC', '7H', '4S', 'TS']

deckh=adeck();deckc=[];rest=False
if rest:
    deckb,deckd=deckh.turnTestdeckIntoDeck(testtablow)
else:
    deckh.shuffle()
    deckb,deckd=deckh.turnTestdeckIntoDeck()


for i,c in enumerate(deckb):    #for j,d in enumerate(str(c)):    #if i%8==0:    #    print()    
    deckc.append(f'{c.rank_list[c.rank()]}{c.suit_list[c.suit()]}')
    #print(f'{c}',sep='',end='')    #popp=deckh.__deck    #deckh.display(deckh.__deck,8)#,8
ix=0
for cd,cx in deckc:
    if ix%8==0:
        print()
    ix+=1
    print(f'{cd}{cx}',end=' ')
print('\nfrom',deckd)
q=0