from dataclasses   import dataclass, field
from fc_card_New   import Card 
from fc_card_New   import Deck 
from        rich   import print as rp
from rich.table    import Table
from rich.console  import Console
from fc_rules_mine import Rules 
from fc_io_New    import PrintItBBU as brichprt
from fc_io_New    import SQLiteIO   as bsqlite3
BLANKCARD = '__'
VALID_RANK = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
VALID_SUIT = ['C','D','H','S']
validcard=[]
for suitB in VALID_SUIT:
    for rankB in VALID_RANK:
        validcard.append(f'{rankB}{suitB}')

@dataclass
class Flags(object):
    running: bool = True
    newGame: bool = False
    restart: bool = False
    moveing: bool = True 
    noAbend: bool = False
    winning: bool = False
    verbose: bool = False
    isdirty: bool = False

    def restoreFlagDefaults(self):
        if self.running  != True:    self.running  = True
        if self.newGame  != False:   self.newGame  = False
        if self.restart  != False:   self.restart  = False
        if self.moveing  != True:    self.moveing  = True 
        if self.noAbend  != False:   self.noAbend  = False
        if self.winning  != False:   self.winning  = False
        if self.verbose  != False:   self.verbose  = False
        if self.isdirty  != False:   self.isdirty  = False


@dataclass
class New_Tableau_dataclass( Flags ):
    maxmvid: int  = -1
    gameid:  int  = -1
    moveid:  int  = -1
    tablown: list = field(default_factory=list) 
    sbckN4h: list = field(default_factory=list)    #in fc_io_mine: sqlite3 
    reasonx: list = field(default_factory=list)   
    posdict: dict = field(default_factory=dict)
    ogtablo: list = field(default_factory=list)

    EMPTYROW=[BLANKCARD for _ in range(8)]
    def __post_init__(self):            #print(f'before makep osdict{self.posdict=}')
        self.makeposdict()                                                                                                                                                                                                                                                                          #print(f'after  makep osdict{self.p osdic=}')
    
    def makeposdict( self ):
        '''return {k+l:[-1,-1] for k in validcard}'''
        self.posdict = {k:[-1,-1] for k in validcard}
    def findPosition( self, destCard):
        return 3,4
    def updatePosition( self, destCard, doapt=None ):
        if doapt!=None:
            if (doapt[0] > -1 and doapt[1] > -1):
                if destCard in validcard:
                    self.posdict.update({destCard:doapt})    
            elif destCard in validcard:
                dou, doo = self.findPosition(destCard)
                self.posdict.update({destCard:[dou,doo]})
        elif destCard in validcard:
            dou, doo = self.findPosition(destCard)
            self.posdict.update({destCard:[dou,doo]})
    def newTablowFromDeck( self, deck1, brichp):
        deck,deckA = deck1.turnTestdeckIntoDeck()
        zz=0
        self.ogtablo = [];self.tablown=[]
        self.ogtablo.append([BLANKCARD for z in range(8)])
        self.tablown.append([BLANKCARD for ii in range(8)])
        for xx in range(22):
            zlist=[]
            for yy in range(8):
                if zz < 52:
                    zlist.append(deck[zz])
                    deck[zz].set_position(xx,yy)
                    self.posdict.update({str(deck[zz]):[xx,yy]})
                else:
                    zlist.append(BLANKCARD)
                zz += 1
            self.tablown.append(zlist)
            self.ogtablo.append(zlist)
        self.gameid += 1; self.moveid = 0; self.newGame = True
        deck1.display(8);#sql3.gamePrintTableau(self,self.reason,True)
        brichp.printTableau(self)

    def getTablownFromLite3(self, sql3, brichp):
        answer='b5'
        self.gameid, self.moveid, self.lTblRows = \
            sql3.handlebackfwd(answer)
        self.convertSQL2Tablo( )
        brichp.printTableau(self)#pass

        
    def convertSQL2Tablo    (self):        #dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=Card.suit_list; rank1=Card.rank_list        #tablow=[]    #with closing(sql3class.cursorSQL3) as cursor3:    #gamer=game()
        self.tablown=[];running=True;cardi=[]
        qq=[BLANKCARD for zz in range(8)]
        self.tablown.append(qq)        #self.lTblRows=sql3class.readlast record()

        if self.lTblRows !=None and len(self.lTblRows) < 2:
            self.gameid,self.moveid,self.lTblRows = sql3.readlastrecord()        #self.gameid+=1    #self.moveid+=1        #tablow = fromsql2tablo

        for ir,listoflists in enumerate(self.lTblRows):
            if len(listoflists) != 16: 
                self.invalidTabloLen = True
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
                    self.posdict.update({yy:[ir,ic]})
            self.tablown.append(ww)

        while len(self.tablown) < 23:
            self.tablown.append(['__' for w in range(8)])

        '''[["4Cxxxxxxxxxxxxxx"],["8CTC5S9C6SAC3DAS"]]
          to['5C', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx'],
            ['8C', 'TC', '5S', '9C', '6S', 'AC', '3D', 'AS'], 
            len = 8'''
        '''
        suit1=Card.suit_list; rank1=Card.rank_list
        self.tablown=[]
        for ir,xx in enumerate(cardi):
            ww=[]
            for ic,yy in enumerate(xx):
                if yy == 'xx':
                    ww.append(yy)
                else:
                    ww.append(Card(rank1.index(yy[0]),suit1.index(yy[1]),ir,ic))
                    self.posdict.update({yy:[ir,ic]})
            self.tablown.append(ww)

        while len(self.tablown) < 23:
            self.tablown.append(['__' for w in range(8)])

        for idxm,rown in enumerate(self.tablown):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    self.tablown[idxm][idxn] = '__'    #Tableau.gamePrintTableau(tablow)
        '''


if __name__ == '__main__':             #    dek=deck();dek.shuffle();dek.turnTestdeckIntoDeck()
    tabloDC=New_Tableau_dataclass()    #    tabloDC.makep osdict    ()
    tabloDC.posdict.update({'AC':[5,5]}) ;doapt=[6,6]               
    tabloDC.updatePosition('AD',doapt)
    print(tabloDC.posdict)
    brichp=brichprt(tabloDC)
    sql3=bsqlite3(tabloDC)
    deck1=Deck();deck1.shuffle()
    tabloDC.newTablowFromDeck(deck1, brichp)
    tabloDC.getTablownFromLite3(sql3, brichp)