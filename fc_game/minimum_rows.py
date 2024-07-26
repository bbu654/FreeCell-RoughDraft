from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck
from rich          import print as rp 
from fc_io_mine    import PrintItBBU as printclass
from fc_io_mine    import SQLiteIO as sql3cls
from contextlib    import closing
from fc_game_mine  import Game as game
#conn = sqlite3.connect(location)


    # Do anything that may raise an exception here
##from fc_rules_mine import Rules as rulesA

#rules=rulesA()
prtit =printclass()
deckA=deck()
sql3class=sql3cls()
deckA.shuffle();#self=0
#realdeal

#def putUpLastRowsOfCards( running, dek, tablow, idx4lastcards, rowidx):
#    '''we might not need idxlastcards'''
#    for column in range(8):
#        if idx4lastcards[column] > -1 and tablow[rowidx][column]!='0':
#            reason=rules.validLastRowsOfCards(tablow, rowidx, column)
#            if rules.validMove:
#                pass
#
#    pass
#    return running, dek, tablow
#
#def testhandleWeWon(self, running, dek,tablow):
#    strtemp='0';lentablow=len(tablow)
#    for errchk in range(4):
#        if type(tablow[0][errchk]) != type(strtemp):
#            return False, dek, tablow
#    #############################################
#    #running, dek, tablow, idx4lastcards, maxidxoflc = getidx4lastcards(\
#    #running, dek, tablow)
#    maxidxoflc+=1
#    for rowidx in range(maxidxoflc,1,-1):
#        running, dek, tablow = putUpLastRowsOfCards(\
#        running, dek, tablow, idx4lastcards, rowidx)
#    return running, dek,tablow
def restartfromdb():
    #with closing(sql3class.cursorSQL3) as cursor3:
    gamer=game()
    gamer.tablClass.tablow=[]
    qq=gamer.tablClass.EMPTYROW
    gamer.tablClass.tablow.append(qq)
    gamer.tablClass.gameid=sql3class.readFirstGamesRec()
    gamer.tablClass.moveid, gamer.tablClass.lresult = sql3class.readlastrecord()
    cardj = ['xx8Cxxxx2C6D3H5S', 
             '7HKSKDxxxxxx4CKH', 
             '9HKCQCxx9Cxx4HQS', 
             '3CxxJDxx8HxxJCJH', 
             'QDxxTSxxxxxxxxTC', 
             '7Sxxxxxxxxxxxx9D', 
             '6Sxxxxxxxxxxxx8S', 
             'QHxxxxxxxxxxxx7D', 
             'JSxxxxxxxxxxxx6C', 
             'TDxxxxxxxxxxxx5H', 
             '9Sxxxxxxxxxxxxxx', 
             '8Dxxxxxxxxxxxxxx', 
             '7Cxxxxxxxxxxxxxx', 
             '6Hxxxxxxxxxxxxxx', 
             '5Cxxxxxxxxxxxxxx']        # 3, 67,
    cardk = [ '8H8C5Cxx2C6D3H5S',        
             '7HKSKDxxTDxx4CKH', 
             '9HKCQCxx9Cxx4HQS', 
             '3CxxJDxxxxxxJCJH', 
             'QDxxTSxxxxxxxxTC', 
             '7Sxxxxxxxxxxxx9D', 
             '6Sxxxxxxxxxxxx8S', 
             'QHxxxxxxxxxxxx7D', 
             'JSxxxxxxxxxxxx6C', 
             'THxxxxxxxxxxxx5H', 
             '9Sxxxxxxxxxxxxxx', 
             '8Dxxxxxxxxxxxxxx', 
             '7Cxxxxxxxxxxxxxx', 
             '6Hxxxxxxxxxxxxxx']
    sqld="INSERT INTO 'Game' ('gameid', 'moveid', 'row0', 'row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8', 'row9', 'row10', 'row11', 'row12', 'row13')  VALUES (3, 67, '8H8C5Cxx2C6D3H5S', '7HKSKDxxTDxx4CKH', '9HKCQCxx9Cxx4HQS', '3CxxJDxxxxxxJCJH', 'QDxxTSxxxxxxxxTC', '7Sxxxxxxxxxxxx9D', '6Sxxxxxxxxxxxx8S', 'QHxxxxxxxxxxxx7D', 'JSxxxxxxxxxxxx6C', 'THxxxxxxxxxxxx5H', '9Sxxxxxxxxxxxxxx', '8Dxxxxxxxxxxxxxx', '7Cxxxxxxxxxxxxxx', '6Hxxxxxxxxxxxxxx');"
    cardi=[]    
    for listoflists in gamer.tablClass.lresult:
        cardg='';cardh=[]
        for idxchar,chara in enumerate(listoflists):
            cardg+=chara
            if idxchar%2!=0 and idxchar>0:
                cardh.append(cardg)
                cardg=''                        #else:
        cardi.append(cardh)        

    suit1=card.suit_list; rank1=card.rank_list;tablow=[]
    for xx in cardi:
        ww=[]
        for yy in xx:
            if yy == 'xx':
                ww.append('0')
            else:
                ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
        tablow.append(ww)
        while len(tablow)<23:
            tablow.append(['0' for w in range(8)])
    return tablow
def getFieldNamesfromPRAGMAtable_info(tablow):
    #sql3class.cusorSQL3=self.conn.cursor()
    with closing(sql3class.cursorSQL3) as cursor3:
        cursor3.execute('PRAGMA table_info(Game)')
        namesResult=cursor3.fetchall()
    '''This script will print out each column’s name from the users table. The PRAGMA statement returns a list of tuples, where each tuple represents a column. The second element in each tuple (index 1) is the column name.
    While this method is more verbose than the basic example, it also provides additional details about each column, such as data type, whether the column can hold NULL values, and the default value for the column, among others.
    Exploring Metadata with PRAGMA
    If you’re interested in fetching more than just the column names, like the data type or whether the column is a primary key, you can adjust the aforementioned code to suit your needs. Here is how you can do it:'''
    table_info4Games=[];ti4gRow=[];litlist=['','Name:','Type:','NULL:','Dfalt:','IsPK:']
    for idx,row in enumerate(namesResult):
        ti4gRow=[]
        for idy in range(1,6):
            ti4gRow.append(row[idy])#;ti4gRow.append(litlist[idy])
        table_info4Games.append(ti4gRow)
    sql3class.fieldNames4games=[table_info4Games[idz][0] for idz in range(len(table_info4Games))]
    sql3class.row0Index=sql3class.fieldNames4games.index('row0')
    rp(f'{sql3class.fieldNames4games[sql3class.row0Index:11]=}||||{sql3class.row0Index=}',sep=', ')
    """ self.fieldNames4games[:10]=['dbid', 'gameid', 'moveid', 
        'row0', 'row1', 'row2', 'row3', 'row4', 'row5', 
        'row6']||||self.row0Index=3"""
    snames=sql3class.fieldNames4games;srowidx=sql3class.row0Index
    sql3class.gameid=3#gameid
    sql3class.moveid=1#moveid
    sql3class.moveid+=1;sql3class.sep=', '# Create a new record
    sqlb=[sql3class.gameid,sql3class.moveid]
    for sqlridx,sqlrow in enumerate(tablow):
        sqlc=''
        """ DONT SKIP THE FIRST ROW IF ITS EMPTY (skip the rest of them)"""
        if sqlridx ==0 or sqlrow != ['' for _ in range(8)]:
            for sqlcol in sqlrow:
                sqlcol2=str(sqlcol)
                if sqlcol2 != '': 
                    sqlc+=sqlcol2
                else:
                    sqlc+='xx'
            sqlb.append(sqlc)
        else:
            continue
        #

    sql3class.rowstring= f" VALUES {tuple(sqlb[idxcv] for idxcv in range(len(sqlb)))}; "
    numbers = [1, 2, 3, 4, 5];    squares = tuple(x**2 for x in numbers)
    print(squares)  # Output: (1, 4, 9, 16, 25)
    sql3class.valuestr = f"INSERT INTO 'Game' {tuple(snames[idz] for idz in range(1,len(sqlb)))} "
    #for idx,rowf in enumerate(sqlb):
    #    if idx == len(sqlb)-1:
    #        sql3class.rowstring += f"'{str(rowf)}');"
    #        sql3class.valuestr  += f"'{snames[idx+srowidx]}')"
    #    else:
    #        sql3class.rowstring += f"'{str(rowf)}', "
    #        sql3class.valuestr  += f"'{snames[idx+srowidx]}', "
    sqld = f"{sql3class.valuestr}{sql3class.rowstring}"
                
    print(f'{sqlb=}{sqld=}',sep=',') 
    #try:
    cursor3.execute(sqld)#, ('john@example.com', 'mypassword'))
    #except
    #################################################################   


outc=[[ '0', '0', '0', '0', '0', '0', '0', '0'],     #0
      ['4S','JD','3S','QH','7D','4C','2S','3C'],     #1
      ['7S','9C','7H','JS','5H','AC','8C','AD'],     #2
      ['KS','3D','TH','2C','6C','AS','QC','9D'],     #3
      ['3H','AH','9H','4D','8D','KH','8H','8S'],     #4
      ['KC','6D','5S','KD','6S','7C','5D','5C'],     #5
      ['6H','QS','2D','TD','TS','4H','JH','2H'],     #6
      ['TC','QD','JC','9S', '0', '0', '0', '0'],     #7
      [ '0', '0', '0', '0', '0', '0', '0', '0'],     #8
      [ '0', '0', '0', '0', '0', '0', '0', '0'],     #9
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #10
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #11
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #12
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #13
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #14
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #15
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #16
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #17
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #18
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #19
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #20
      [ '0', '0', '0', '0', '0', '0', '0', '0'],    #21
      [ '0', '0', '0', '0', '0', '0', '0', '0']]    #22   
#deckB,deckC = deckA.turnTestdeckIntoDeck()
outa=[[ '0', '0', '0','0','2C','2D','5H','5S'],          
      [ '0','KS','KD','0', '0','KC', '0','KH'],    
      [ '0','QD','QC','0', '0','QH', '0','QS'],    
      [ '0','JS','JD','0', '0','JC', '0','JH'],    
      [ '0','TH','TC','0', '0','TD', '0','TS'],    
      [ '0','9C','9H','0', '0','9S', '0','9D'],    
      [ '0','8D','8C','0', '0','8H', '0','8S'],    
      [ '0','7C','7D','0', '0','7S', '0','7H'],    
      [ '0','6H','6S','0', '0','6D', '0','6C'],    
      [ '0','5C', '0','0', '0', '0', '0','5D'],    
      [ '0','4D', '0','0', '0', '0', '0','4C'],    
      [ '0','3C', '0','0', '0', '0', '0','3D'] ]      
"""Create a card for each strLit"""
#for i,z in enumerate(tablow):    #if i%8==0:    #    print()
#    rp(f'{z}')
suit1=card.suit_list; rank1=card.rank_list;tablow=[]
#tablow=restartfromdb()
#print();prtit.printTableau(tablow)
mou=1;w2=card(rank1.index('2'),suit1.index('D'))
qq=['00' if p != mou else str(w2) for p in range(8)]
nminp='';minp='3d'
nminp = ''.join(minp[i] if str(minp[i]).isalpha() else minp[i] for i in range(2) )
#nminp+=minp[i].upper()  if str(minp[i]).isalpha() else minp[i] for i in range(2)
#tablow.append(qq)
#for po in tablow:
#    rp(f'{po }',end=', ')
love='Love';running=False;dek=0;   
#running, dek, tablow, idx4lastcards = getidx4lastcards(running, dek, tablow)
rp(f'{love}{qq}')#{idx4lastcards=}
#print();prtit.printTableau(tablow)
#getFieldNamesfromPRAGMAtable_info(tablow)
strlove='''
________________________________________
| Q♠ ┃ 0  ┃ 0  ┃ 0  ┃ A♣ ┃ 2♦ ┃ 4♥ ┃ 4♠ ┃
┡━━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━┩
│    │    │    │    │    │    │    │    │
│ J♥ │ K♠ │ K♦ │ 8♥ │ 5♠ │ 3♦ │ T♦ │ K♥ │
│ T♠ │ Q♦ │ Q♣ │ 7♠ │ 5♥ │ K♣ │ 2♣ │ 4♣ │
│ 9♦ │ J♠ │ J♦ │ 6♦ │ 0  │ 5♦ │ Q♥ │ 0  │
│ 8♠ │ T♥ │ T♣ │ 0  │ 0  │ J♣ │ 9♠ │ 0  │
│ 7♥ │ 9♣ │ 9♥ │ 0  │ 0  │ 0  │ 8♣ │ 0  │
│ 6♣ │ 8♦ │ 0  │ 0  │ 0  │ 0  │ 7♦ │ 0  │
│ 0  │ 7♣ │ 0  │ 0  │ 0  │ 0  │ 6♠ │ 0  │
│ 0  │ 6♥ │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │
│ 0  │ 5♣ │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │
│ 0  │ 4♦ │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │
│ 0  │ 3♣ │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │
└────┴────┴────┴────┴────┴────┴────┴────┘'''
outb=[['QS', '0', '0', '0','2C','2D','5H','5S'],          
      ['J♥','K♠','K♦','8♥','5♠','3♦','T♦','K♥'],
      ['T♠','Q♦','Q♣','7♠','5♥','K♣','2♣','4♣'],
      ['9♦','J♠','J♦','6♦', '0','5♦','Q♥', '0'],
      ['8♠','T♥','T♣', '0', '0','J♣','9♠', '0'],
      ['7♥','9♣','9♥', '0', '0', '0','8♣', '0'],
      ['6♣','8♦', '0', '0', '0', '0','7♦', '0'],
      [ '0','7♣', '0', '0', '0', '0','6♠', '0'],
      [ '0','6♥', '0', '0', '0', '0', '0', '0'],     
      [ '0','5♣', '0', '0', '0', '0', '0', '0'],     
      [ '0','4♦', '0', '0', '0', '0', '0', '0'],     
      [ '0','3♣', '0', '0', '0', '0', '0', '0']  ]      #11
