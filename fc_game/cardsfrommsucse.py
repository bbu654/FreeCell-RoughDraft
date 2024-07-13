import random    # required for shuffle method of Deck
from   rich         import print as rp
from   rich.table   import Table
from   rich.console import Console

class Card(object):
    ''' Suit and rank are ints, and index into suit_list and rank_list.
        Value is different from rank: for example face cards are equal in value (all 10)
    '''
    # Use these lists to map the ints of suit and rank to nice words.
    # The 'x' is a place holder so that index-2 maps to '2', etc.
    suit_list = ['0', 'C', 'D', 'H', 'S']
    rank_list = ['0', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
                 #0    1    2    3    4    5    6    7     
                           #3  
    def __init__(self, rank=0, suit=0):
        ''' Rank and suit must be ints.
            This checks that they are in the correct range.
            Blank card has rank and suit set to 0.
        '''
        self.__suit = 0
        self.__rank = 0
        if type(suit) == int and type(rank) == int:
            # only good indicies work
            if suit in range(1,5) and rank in range(1,15):
                self.__suit = suit
                self.__rank = rank

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit
    
##    These two "set" methods are for testing: turn them on for testing and
##    and then turn off.  These allow you to change a card's rand and suit so
##    you can test situations that might occur infrequently.
##
##    def set_rank(self, rank):
##        self.__rank = rank
##
##    def set_suit(self, suit):
##        self.__suit = suit

    def get_value(self):
        ''' Face cards return 10, the rest return their rank values. Aces are low.
        '''
        # ternary expression:
        return self.__rank if self.__rank < 10 else 10

    def equal_suit(self, other):
        '''Returns True if suits are equal.'''
        return self.__suit == other.__suit

    def equal_rank(self, other):
        '''Returns True if ranks are equal.'''
        return self.__rank == other.__rank

    def equal_value(self, other):
        '''Returns True if values are equal.'''
        return self.get_value() == other.get_value()

    def __str__(self):
        ''' Called by print() so you can print a card, just like any other data structure.
        '''
        # Uses rank to index into rank_list of names; uses suite to index into suit_list of names.
        return f'{(self.rank_list)[self.__rank]}{(self.suit_list)[self.__suit]}'
        #return "{:s}{:s}".format((self.rank_list)[self.__rank], (self.suit_list)[self.__suit])
        
    def __repr__(self):
        ''' This method is called if you simply enter a card name in the shell.
            It simply calls, the same method that prints a card.
        '''
        return self.__str__()

class Deck(object):
    ''' Deck of cards, implemented as a list of card objects.
        The last card in the deck (list) is the top of deck.
    '''
    EMPTYROW_=['0' for _ in range(8)]    
    SYMBOL_={'C':'♣','D':'♦','H':'♥','S':'♠'}
    COLORS_={'C':'[blue]','D':'[bright_magenta]','H':'[red]','S':'[bright_green]'}
    __suitlit= ['[white]0[/]']
    for __sidx in SYMBOL_:
        for __nidy in range(1,14):
            if __nidy == 1:
                __suitlit.append(f'{COLORS_[__sidx]}A{SYMBOL_[__sidx]}[/]')
            elif __nidy == 10:
                __suitlit.append(f'{COLORS_[__sidx]}T{SYMBOL_[__sidx]}[/]')
            elif __nidy == 11:
                __suitlit.append(f'{COLORS_[__sidx]}J{SYMBOL_[__sidx]}[/]')
            elif __nidy == 12:
                __suitlit.append(f'{COLORS_[__sidx]}Q{SYMBOL_[__sidx]}[/]')
            elif __nidy == 13:
                __suitlit.append(f'{COLORS_[__sidx]}K{SYMBOL_[__sidx]}[/]')
            else:
                __suitlit.append(f'{COLORS_[__sidx]}{str(__nidy)}{SYMBOL_[__sidx]}[/]')

    def __init__(self,dek=None):
        if dek ==None:
            self.__deck=[Card(rank,suit) for suit in range(1,5) for rank in range(1,14)]
        else:
            self.__deck=self.lister()
            self.__deck=[]
            #self.lister()
            for rs in dek:
                rank0= rs[0]
                suit1= rs[1]
                crl00=Card.rank_list
                csl11=Card.suit_list
                ranka=crl00.index(rank0)
                suita=csl11.index(suit1)
                self.__deck.append(Card(ranka,suita))
        if True: 
            pass    #self.__deck=[Card(Card.rank_list[Card.rank_list.index(crd[0])],Card.suit_list[Card.suit_list.index(crd[1])]) for crd in dek]
    def shuffle(self):
        '''Shuffle the deck using a call to random.'''
        random.shuffle(self.__deck)

    def newGame(self):
        __yy          = ['0' for _ in range(8)]
        __zz          = 0
        self.__tablow = []
        self.__tablow.append(__yy)
        for __rowr in range(23):
            __yy = []
            for __colr in range(8):
                __yy.append(str(self.__deck[__zz]) if __zz < 52 else '0' )
                __zz += 1
            self.__tablow.append(__yy)

        return self.__tablow
    def lister(self):
        self.listd=[]
        for cardj in self.__deck:
            self.listd.append(str(cardj))
        return self.listd
    def deal(self):
        '''Return the top card from the deck (only if the deck is not empty).'''
        # ternary expression
        return self.__deck.pop() if len(self.__deck) else None

    def cards_count(self):
        '''Returns the number of cards in the deck.'''
        return len(self.__deck)

    def findNoOf0FC(self):
        self.countOf0FC = 0;self.first0FC=0
        for ick in range(4):
            if self.__tablow[0][ick] == '0':
                self.countOf0FC += 1
                if self.first0FC==0:
                    self.first0FC=ick
        return self.countOf0FC,self.first0FC
    
    def position(self,tablow=[],minp='AC',dinp='GG'):
        if tablow != []:
            self.__tablow = tablow
        else:
            tablow = self.__tablow
        self.__moapt=0,0;self.__doapt=0,0
        if len(minp) != 2 \
            or minp[0] not in Card.rank_list[1:] \
            or minp[1] not in Card.suit_list[1:]:
            return self.__tablow, self.__moapt, self.__doapt
        if dinp[1] == 'G':
            __foundation = Card.suit_list.index(minp[1]) + 4 - 1
            __moveCard   = Card.rank_list.index(minp[0])     - 1 
            if self.__tablow[0][__foundation] != Card.rank_list[__moveCard]:
                return self.__tablow, self.__moapt, self.__doapt
            else:
                self.__doapt=0,__foundation
        elif dinp[1] == 'F':
            if __p:=self.findNoOf0FC()[1] > 0: self.__doapt = 0, __p
            self.findNoOf0FC()
            if self.first0FC > 0: 
                self.__doapt = 0, self.first0FC

        if str(self.__doapt) == '0,0':
            for __u, __v in enumerate(self.__tablow):
                if dinp in __v: 
                    self.__doapt=__u,__v.index(dinp)
        for __t, __w in enumerate(self.__tablow):
            if minp in __w:
                self.__moapt=__t,__w.index(minp)
        
        return self.__tablow, self.__moapt,self.__doapt

    def move(self,tablow,minp,dinp):
        pass

    def is_empty(self):
        '''Returns True if the deck is empty.'''
        return len(self.__deck) == 0

    def __str__(self):
        ''' Print a deck, simple but messy!
        '''
        return ','.join([str(card) for card in self.__deck])
            
    def __repr__(self):
        ''' Messy print deck, if you enter a deck's name in the shell.
        '''
        return self.__str__()

    def pretty_print(self, column_max=10):
        ''' Column-oriented printing of a deck.
        '''
        for index,card in enumerate(self.__deck):
            if index%column_max == 0:  # at final column so print a carriage return
                print()
            print(f"{card}", end=' ')
        print()
        print()

    def richPrintTablow(self):
        self.__tablowview = Table(title='FreeCell v0002')
        for __idy, __row1 in enumerate(self.__tablow):
            __strRow=['','','','','','','',''] #str4=zip(row1)        #str5=str4        str0=''
            for __idx,__col1 in enumerate(__row1):
                if __col1 == '0':
                    __stra=f'[white]0[/]'                
                else:
                    __stra=f'{self.COLORS_[__col1[1]]}{__col1[0]}{self.SYMBOL_[__col1[1]]}[/]'
                if __idy==0:    #strx=str(col1)    if col1 == '0':    tview.add_column(f'[white]0[/]')    else:    tview.add_column(f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]')                    # tview.add_column(suitlit1[idx])
                    self.__tablowview.add_column(__stra)
                else:
                    __strRow[__idx] += __stra #    if col1 == '0':    strRow[idx] += f'[white]0[/]'       else:    strRow[idx] += f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'  
            if __row1 != self.EMPTYROW_:
                self.__tablowview.add_row(__strRow[0],__strRow[1],__strRow[2],__strRow[3],\
                                      __strRow[4],__strRow[5],__strRow[6],__strRow[7])
        self.__consol=Console()    
        self.__consol.print(self.__tablowview)
        #return tablow