
import random

class Card( object ):
    """ Model a playing card. """

    # Rank is an int (1-13), where aces are 1 and kings are 13.
    # Suit is an int (1-4), where clubs are 1 and spades are 4.
    # Value is an int (1-10), where aces are 1 and face cards are 10.

    # List to map int rank to printable character (index 0 used for no rank)
    rank_list = ['x','A','2','3','4','5','6','7','8','9','T','J','Q','K']

    # List to map int suit to printable character (index 0 used for no suit)
    # 1 is clubs, 2 is diamonds, 3 is hearts, and 4 is spades
    #suit_list = ['x','\u2663','\u2666','\u2665','\u2660']
    suit_list = ['x','C','D','H','S']
    SUIT_LIST = {'x': 'x', 'C': '\u2663', 'D': '\u2666', 'H': '\u2665', 'S': '\u2660'}
    def __init__( self, rank=0, suit=0, rowx=-2, coly=-2 ):
        """ Initialize card to specified rank (1-13) and suit (1-4), \n
                       Tableau position  rowx (0-22) and coly (0-8)."""
        self.__rank = 0
        self.__suit = 0
        self.__face_up = None

        self.__rowx = -1
        self.__coly = -1
        self.__foundation = None
        # Verify that rank and suit are ints and that they are within
        # range (1-13 and 1-4), then update instance variables if valid.
        if type(rank) == int and type(suit) == int:
            if rank in range(1,14) and suit in range(1,5):
                self.__rank = rank
                self.__suit = suit
                self.__face_up = True
        self.set_rowx( rowx )
        self.set_coly( coly )
        self.enter_foundation( )

    def rank( self ):
        """ Return card's rank (1-13). """
        return self.__rank

    def value( self ):
        """ Return card's value (1 for aces, 2-9, 10 for face cards). """
        # Use ternary expression to determine value.
        return self.__rank if self.__rank < 10 else 10

    def suit( self ):
        """ Return card's suit (1-4). """
        return self.__suit
    
    def is_face_up( self ):
        """ Returns True if card is facing up."""
        return self.__face_up
    
    def rowx( self ):
        """ Returns Cards 'Row' position x."""
        return self.__rowx
    
    def coly( self ):
        """ Returns Cards 'Column' position y."""
        return self.__coly
    
    def set_rowx( self, rowx):
        """sets the row index when Tableau or moved"""
        if type(rowx) == int:
            if rowx in range(23):
                self.__rowx = rowx
    
    def set_coly( self, coly):
        """sets the column index when Tableau or moved"""
        if type(coly) == int:
            if coly in range(8):
                self.__coly = coly
  
    def is_in_foundation( self ):
        """ Returns True if card is in foundation."""
        return self.__foundation

    def enter_foundation( self ):
        """ Does card enter Foundation: then locked in"""
        if self.rowx() == 0 and self.coly() in range(4,8):
            self.__foundation = True

    def get_position( self ):
        """ Returns a list of rowx, coly """
        return [ self.rowx(), self.coly() ]

    def set_position( self, rowx, coly):
        """ Sets Both __rowx and __coly."""
        self.set_rowx( rowx )
        self.set_coly( coly )


    def flip_card( self ):
        """ Flips card between face-up and face-down"""
        self.__face_up = not self.__face_up

    def __str__( self ):
        """ Convert card into a string (usually for printing). """
        # Use rank to index into rank_list; use suit to index into suit_list.
        if self.__face_up:
            k=f"{self.rank_list[self.__rank]}"
            l=f"{self.suit_list[self.__suit]}"
            return f"{self.rank_list[self.__rank]+self.suit_list[self.__suit]}"
        else:
            return f"{'XX'}"

    def __repr__( self ):
        """ Convert card into a string for use in the shell. """
        return self.__str__()
        
    def __eq__( self, other ):
        """ Return True, if Cards of equal rank and suit; False, otherwise. """
        if not isinstance(other, Card):
            return False
            
        return self.rank() == other.rank() and self.suit() == other.suit()
    def stringToCard(self,minp='AC'):
        oldminp=minp
        self.minp=minp
        newminp=minp
        temprank=Card.rank_list.index(minp[0])
        tempsuit=Card.suit_list.index(minp[1])
        print(f'{oldminp=}{newminp=}{minp=}{temprank=}{tempsuit=}')
        return Card(Card.rank_list.index(minp[0],Card.suit_list.index(minp[1])))
        #pass
class Deck( object ):
    """ Model a deck of 52 playing cards. """

    # Implement the deck as a list of cards.  The last card in the list is
    # defined to be at the top of the deck.

    def __init__( self ):
        """ Initialize deck--Ace of clubs on bottom, King of spades on top. """
        #self.__deck = [Card(r,s) for s in range(1,5) for r in range(1,14)]
        self.__deck = [Card(r,s) for s in range(4,0,-1) for r in range(13,0,-1)]
        
    def shuffle( self ):
        """ Shuffle deck using shuffle method in random module. """
        random.shuffle(self.__deck)

    def deal( self ):
        """ Return top card from deck (return None if deck empty). """
        # Use ternary expression to guard against empty deck.
        return self.__deck.pop() if len(self.__deck) else None

    def is_empty( self ):
        """ Return True if deck is empty; False, otherwise """
        return len(self.__deck) == 0

    def __len__( self ):
        """ Return number of cards remaining in deck. """
        return len(self.__deck)
    
    def __str__( self ):
        """ Return string representing deck (usually for printing). """
        return "".join([str(card) for card in self.__deck])
            
    def __repr__( self ):
        """ Return string representing deck (for use in shell). """
        return self.__str__()

    def display( self, cols=13 ):
        """ Column-oriented display of deck. """
        for index, card in enumerate(self.__deck):
            if index%cols == 0:
                print()
            isii=str(card)
            print(f'{str(card)}',end=' ')
            #print(f"{str(card)} ", end="" )
        print()
        print()

    def turnTestdeckIntoDeck(self,testdeck=None):
        tempdeck=[]
        ranklist1=Card.rank_list
        suitlist1=['X','C','D','H','S']
        if testdeck==None:            #ydeck=Deck()
            #testdeck=self.__deck
            decki=[]
            for c in self.__deck:
                decki.append(f'{c.rank_list[c.rank()]}{c.suit_list[c.suit()]}')
            for i,c in enumerate(decki):       
                if i%8 == 0:
                    print()
                print(f'{c}',sep='',end='')
            
            return self.__deck,decki
        if type(testdeck)==type(list()):           
            for i,c in enumerate(testdeck):
                #self.__deck = [Card(r,s) 
                c=str(c)
                temprank=ranklist1.index(c[0])
                tempsuit=suitlist1.index(c[1])  
                tr = Card(temprank,tempsuit).rank()
                ts = Card(temprank,tempsuit).suit()
                if tr <10: 
                    trs=f'0{tr}'
                else:
                    trs=str(tr)
                if ts <10: 
                    tss=f'0{ts}'
                else:
                    tss=str(ts)
                
                #print(Card(temprank,tempsuit),end=', ')
                if i%8==0:
                    print()
                print(f'{trs},{tss}',end='  ')
                tempdeck.append([(ranklist1.index(c[0])),(suitlist1.index(c[1]))])
                # for s in range(1,5) 
                #     for r in range(1,14)]    
            self.__deck= [Card(c[0],c[1]) for c in tempdeck]
            self.display(8)
            print();print()
            decki=[]
            for c in self.__deck:
                decki.append(f'{c.rank_list[c.rank()]}{c.suit_list[c.suit()]}')
            print(decki)
            #print(f'{c.suit() for c in self.__deck}')
        return self.__deck,decki