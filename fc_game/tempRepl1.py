from fc_card_New import Card
from fc_card_New import Deck
from fc_io_New   import PrintItBBU
from fc_io_New   import SQLiteIO
from fc_tableau_New import New_Tableau_dataclass
BLANKCARD = '__'
tabloDC = New_Tableau_dataclass()
#class pop(tabloDC):
def convertSQL2Tablo    (tabloDC):
    sql3=SQLiteIO(tabloDC)
    bprt=PrintItBBU(tabloDC)    
    #dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
    lTblRows =['4Cxxxxxxxxxxxxxx', '8CTC5S9C6SAC3DAS', '8H7H7CJS8D6H4DQD', '7SJDQS7D2DKH3C4S', '9D8SKD2C3SAD2S5H', '2HJCQHAH6CxxJHTD', 'TS5D9SKSKCxx3H4H', '6D9HTHQCxxxxxxxx', '5Cxxxxxxxxxxxxxx']
    suit1=Card.suit_list; rank1=Card.rank_list
    tablow=[]
    selflTblRows = lTblRows
    #with closing(sql3class.cursorSQL3) as cursor3:
    #gamer=game()
    selftablow=[]
    qq=[BLANKCARD for zz in range(8)]
    selftablow.append(qq)
    running=True#selflTblRows=sql3class.readlast record()
    cardi=[]    
    if selflTblRows !=None and len(selflTblRows) < 2:
        selfgameid,selfmoveid,selflTblRows = sql3.readlastrecord()
    #selfgameid+=1    #selfmoveid+=1        #tablow = fromsql2tablo
    for ir,listoflists in enumerate(selflTblRows):
        if len(listoflists) != 16: 
            selfinvalidTabloLen = True
            sql3.closeconn()
            raise Exception(f'len(listoflists) != 16({len(listoflists)}): Have a blessed...')
        cardh= [listoflists[i:i+2] for i in range(0, len(listoflists), 2)]
        cardi.append(cardh) 
        ww=[]
        for ic,yy in enumerate(cardh):
            if yy == 'xx':
                ww.append('__')
            else:
                ww.append(Card(rank1.index(yy[0]),suit1.index(yy[1]),ir,ic))
                tabloDC.posdict.update({yy:[ir,ic]})
        tabloDC.tablown.append(ww)
    while len(tabloDC.tablown) < 23:
        tabloDC.tablown.append(['__' for w in range(8)])
    bprt.printTableau(tabloDC)
    """for idxm,rown in enumerate(tabloDC.tablown):
        for idxn, itemn in enumerate(rown):
            if str(itemn) == 'xx':
                tabloDC.tablown[idxm][idxn] = '__'    #Tableau.gamePrintTableau(tablow)"""
    return
'''[["4Cxxxxxxxxxxxxxx"],["8CTC5S9C6SAC3DAS"]]
      to['5C', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx'],
        ['8C', 'TC', '5S', '9C', '6S', 'AC', '3D', 'AS'], 
        len = 8'''
'''
    suit1=Card.suit_list; rank1=Card.rank_list
    selftablown=[]
    for ir,xx in enumerate(cardi):
        ww=[]
        for ic,yy in enumerate(xx):
            if yy == 'xx':
                ww.append(yy)
            else:
                ww.append(Card(rank1.index(yy[0]),suit1.index(yy[1]),ir,ic))
                selfposdict.update({yy:[ir,ic]})
        selftablown.append(ww)
    while len(selftablown) < 23:
        selftablown.append(['__' for w in range(8)])
    for idxm,rown in enumerate(selftablown):
        for idxn, itemn in enumerate(rown):
            if str(itemn) == 'xx':
                selftablown[idxm][idxn] = '__'    #Tableau.gamePrintTableau(tablow)'''
if __name__ == '__main__':
    #tabloDC = New_Tableau_dataclass()
    #ooo=pop(tabloDC)
    
    convertSQL2Tablo(tabloDC)
    for ii,zz in enumerate(tabloDC.tablown):
        #if ii%8 == 0:
        #    print()
        if zz != ['__' for zz in range(8)] and ii > 0:
            print(f'{zz}')