#from cards_msu_cse import Card as acard, Deck as adeck
import rich.prompt
from fc_card_New1   import Card
from fc_card_New1   import Deck
#from fc_cons_New import Constants 
from more_itertools import quantify
from fc_cons_New1   import *
#import fc_cons_New1
import rich
testtablow = ['8C', 'TD', 'KD', 'QD', 'TH', 'QC', '9H', '8S', '5S', 
'4H', '2C', 'QS', '8H', '3C', 'JS', '6H', 'KH', 'JC', 'JH', '2D', '3S', '6C', '7S', '2S', 'KC', '7D', '6D', '5D', '4D', 'KS', '3D', 'AC',  
'2H', '5C', '6S', '7C', '3H', 'QH', '9C', '9S', '5H', 'AS', '9D', 'JD', '4C', 'AD', 'AH', '8D', 'TC', '7H', '4S', 'TS']

deckh=Deck();deckc=[];rest=False
if rest:
    deckb,deckd=deckh.turnTestdeckIntoDeck(testtablow)
else:
    deckh.shuffle()
    deckb,deckd=deckh.turnTestdeckIntoDeck()
#C=Constants()    
zs=BLANKCARD
print('\nBLANK=',BLANKCARD)
print();zo=None
for i,c in enumerate(deckb):    #for j,d in enumerate(str(c)):    #if i%8==0:    #    print()    
    deckc.append(f'{c.rank_list[c.rank()]}{c.suit_list[c.suit()]}')
    if i<5:#print(f'{c}',sep='',end='')    #popp=deckh.__deck    #deckh.display(deckh.__deck,8)#,8
        print(f'{type(c)=}{c=}',end='  ')
        if type(c) != type(zo):
            print(f'didnt abend on type check{type(zo)=}')
if len(deckc)> -1:
    print(f'{len(deckc)=}')
ix=0
for cd,cx in deckc:
    if ix%8==0:
        print()
    ix+=1
    print(f'{cd}{cx}',end=' ')
print(f'\n{zs=}{type(zs)=}{type(ix)}')
deckh.display(8)
q=0;ans='q'
while ans != 'q':
    ans=rich.prompt.Prompt.ask(f'giveme giveme some lovin')
    if ans==q: break
    raise Exception('BBU end of program: temp_repl.py')   

