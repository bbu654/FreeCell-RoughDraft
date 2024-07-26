from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck
from          rich import print as rp
from rich.table    import Table
from rich.console  import Console
from fc_rules_mine import Rules as rule
from fc_io_mine    import PrintItBBU as brichprt
from fc_io_mine    import SQLiteIO   as bsqlite3
from dataclasses   import dataclass

#    def total_cost(self) -> float:
#        return self.unit_price * self.quantity_on_hand
#will add, among other things, a __init__() that looks like:

#def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
#    self.name = name
#    self.unit_price = unit_price
#    self.quantity_on_hand = quantity_on_hand
#from minimum_rows import getidx4lastcards
BLANKCARD = '0'
cardA=card()
validt = rule()
brichp=brichprt()
bsqlt3=bsqlite3()
BLANKCARD='0'
@dataclass
class DataTablow(object):
    '''This is a data only class no code
         (except to create destroy)
         (find out where a card is )'''
      
    
    running: bool = True  # User wants to QUIT playing and have a beer
    newGame: bool = False
    restart: bool = False
    moveing: bool = True  #Continue move or return to input()
    noAbend: bool = False
    winning: bool = False
    verbose: bool = True
    testing: bool = False
    print()
    stateFlags=[running,verbose,restart,moveing,noAbend,winning,verbose]
    
    
    keylist=[rr+ss for ss in card.suit_list[1:] for rr in card.rank_list[1:]]
    tabloq={k:[-1,-1] for k in keylist}    
    #        keylist.append(rr+ss) 
    mou=1;moo=1;dou=2;doo=2
    doapt=[dou,doo]
    toa=9,4
    tabloq.update({'AS':[mou,moo]})
    tabloq.update({'2S':doapt})
    tabloq.update({'3S':[3,3]})
    tabloq.update({'4S':[4,4]})
    tabloq.update({'4S':[0,0]})
    tabloq.update({'5S':[5,5]})
    tabloq.update({'6S':toa})
    mtt,mqq=tabloq['AS']
    rp(f'{mtt=},{mqq=}, {tabloq['AS'][0]=}, {tabloq['6S'][1]=}')
    cardstr='xx'
    tablo=[]; index4card=-1 
    for index4row in range(23):
        rowa=[]
        for index4col in range(8):
            index4card += 1
            rowa.append([{cardstr:[index4row,index4col]}])#deckA[index4card])
        tablo.append(rowa)
    
    tabloPosition=[{cardstr:[index4row,index4col]}]
    tblpos = ['0' for  _ in range(8)]
    dek=deck();dek.shuffle()
    deckA, deckB = dek.turnTestdeckIntoDeck()
    index4card = -1
    toploc=[]
    toploc.append([BLANKCARD for _ in range(8)])
    for idxrow in range(23):
        rowpos =[]
        for idxcol in range(8):
            index4card += 1
            if index4card < 52:
                deckA[index4card].set_position(idxrow,idxcol)
                rowpos.append({str(deckA[index4card]):[idxrow, idxcol]})
            else:
                rowpos.append('xx')
        toploc.append(rowpos)
    EMPTYROW=[BLANKCARD for _ in range(8)]
    
    # Example: Creating a list of lists of strings
    words = ["hello", "world", "python"]
    list_of_lists = [[char for char in word] for word in words]
    print()
    rp(f'{tabloq=}\n{toploc=}')
    for uu in range(len(tablo)):
        rp(f'{tablo[uu]}',sep='')

#rp("If your terminal supports links, the following text should be clickable:")
#rp("[link=https://www.willmcgugan.com][i]Visit [red]my[/red][/i] [yellow]Blog[/]")

