import itertools
import random
from fc_card_New1   import Card as card
from fc_card_New1   import Deck
from fc_io_mine     import PrintItBBU
from more_itertools import quantify
from fc_cons_New1   import *
brichp = PrintItBBU()
dek=Deck();dek.shuffle();dek.turnTestdeckIntoDeck()
nminp='';minp='3d'
nminp = ''.join(minp[i].upper() if str(minp[i]).isalpha() else minp[i] for i in range(2) )
print(nminp)
validrank=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
vsuita=['C','D','H','S']
validsuit={'C':['D','H'],'D':['C','S'],\
                         'H':['C','S'],'S':['D','H']}
valcrds=itertools.product(validrank,vsuita)
vk = ['{}'.format(''.join(s)) for s in itertools.product(validrank,vsuita)]
validcards=[rg+sg for sg in vsuita for rg in validrank ]
print(f'{validcards=}'); random.shuffle(validcards);print('validcards=',validcards)
nextCard = {}
for vsuit in validsuit:
    for idx, vrank in enumerate(validrank[2:]):
        nextCard[vrank+vsuit]=[validrank[idx+1]+validsuit[vsuit][0],validrank[idx+1]+validsuit[vsuit][1]]
        print(f'{vrank+vsuit}: {nextCard[vrank+vsuit]}',sep='',end=' ')
    print()  
nextcrds = {}
for idxr, vr1 in enumerate(validrank[2:]):
    for vsz in validsuit:
        nextcrds[vr1+vsz]=[validrank[idxr+1]+validsuit[vsz][0],validrank[idxr+1]+validsuit[vsz][1]]
        print(f'{vr1+vsz}:{nextcrds[vr1+vsz]}',sep='',end='  ')
    print()
print(f'{nextCard['5C']=}{len(nextCard.keys())=}')
{
'3C': ['2D', '2H'], 
'4C': ['3D', '3H'], 
'5C': ['4D', '4H'], 
'6C': ['5D', '5H'], 
'7C': ['6D', '6H'], 
'8C': ['7D', '7H'], 
'9C': ['8D', '8H'], 
'TC': ['9D', '9H'], 
'JC': ['TD', 'TH'], 
'QC': ['JD', 'JH'], 
'KC': ['QD', 'QH'], 

'3D': ['2C', '2S'], 
'4D': ['3C', '3S'], 
'5D': ['4C', '4S'], 
'6D': ['5C', '5S'], 
'7D': ['6C', '6S'], 
'8D': ['7C', '7S'], 
'9D': ['8C', '8S'], 
'TD': ['9C', '9S'], 
'JD': ['TC', 'TS'], 
'QD': ['JC', 'JS'], 
'KD': ['QC', 'QS'], 

'3H': ['2C', '2S'], 
'4H': ['3C', '3S'], 
'5H': ['4C', '4S'], 
'6H': ['5C', '5S'], 
'7H': ['6C', '6S'], 
'8H': ['7C', '7S'], 
'9H': ['8C', '8S'], 
'TH': ['9C', '9S'], 
'JH': ['TC', 'TS'], 
'QH': ['JC', 'JS'], 
'KH': ['QC', 'QS'], 

'3S': ['2D', '2H'], 
'4S': ['3D', '3H'], 
'5S': ['4D', '4H'], 
'6S': ['5D', '5H'], 
'7S': ['6D', '6H'], 
'8S': ['7D', '7H'], 
'9S': ['8D', '8H'], 
'TS': ['9D', '9H'], 
'JS': ['TD', 'TH'], 
'QS': ['JD', 'JH'], 
'KS': ['QD', 'QH']}
def getlensubstr(z):
    return len(z) == 16
listofstr = ['xxxxxxxxxxxxxxxx', '6H9DKD3S4S9C6SQH', 
             '4HTDAS8D9HKC7C2C', '5CQSJD3D7SQDAC3C', 
             '7D5D2H6DTC8H7H6C', 'JS5HJHAH2DAD3H4C', 
             '2SQC4DTHTSKS8S8C', '9SKH5SJCxxxxxxxx'] 
lenlistofstr = [ 1 if len(listofstr[x])==16 else 0 for x in range(len(listofstr)) ]
countoflenlist= sum(x for x in lenlistofstr)
if (countOf16:=sum([1 if len(listofstr[x]) == 16 else 0 for x in range(len(listofstr))])) !=                          len(listofstr):  
    raise Exception(f'{countOf16=} != {len(listofstr)=}')
if countoflenlist != len(listofstr): 
    raise Exception(f'{countoflenlist=} != {len(listofstr)=}')
if countnum16:=quantify(listofstr, getlensubstr) != len(listofstr):raise Exception(f'{countnum16=} != {len(listofstr)=}')
#(seq[pos:pos + size] for pos in range(0, len(seq), size))
newliststr=[['__' if yy[xr:xr+2] == 'xx' else yy[xr:xr+2]] for yy in listofstr for xr in range(0,16,2) ]
print('newliststr:',end='')
for idxz,zz in enumerate(newliststr):
    if idxz%8==0:
        print()
    print(str(zz),sep=',',end='')
#print(f'{[str(zz)+"\n" for zz in newliststr]}')
#xr=0;irow=0
tablow1=[];print(f'\ntablow1')
for ww in listofstr:
    if len(ww) == 16:
        cd=[]
        for xr in range(0,16,2):
            #if ww[xr:xr+2] == 'xx':
            cd.append(card(ww[xr:xr+2][0],ww[xr:xr+2][1]))
        tablow1.append(cd)
        print(cd)
#print(f'{[tablow1[vv] for vv in range(len(tablow1))]}',sep='\n')
run=False
suit1=suit_list; rank1=rank_list
if run:
    tablow=[]
    for xx in tablow1:
        ww=[]
        for yy in xx:
            if yy == 'xx':
                ww.append('__') 
            else:
                ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
        tablow.append(ww)
    while len(tablow)<23:
        tablow.append(['__' for w in range(8)])
    for idxm,rown in enumerate(tablow):
        for idxn, itemn in enumerate(rown):
            if str(itemn) == 'xx':
                tablow[idxm][idxn] = '__'    #Tableau.gamePrintTableau(tablow)
    
    #print(f'tablow=\n{[tablow[vv] for vv in range(len(tablow))]}\ntablow=\n{tablow}',sep='\n')

print('\ntablow=')
for rr in range(len(tablow1)):
    if tablow1[rr] != ['__' for w in range(8)] or rr == 0:
        print(tablow1[rr])
brichp.printTableau(tablow1)