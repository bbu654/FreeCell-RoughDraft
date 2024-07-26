from dataclasses import dataclass, field
from fc_card_mineNew import Card as card
from fc_card_mineNew import Deck as deck
from          rich import print as rp
from rich.table    import Table
from rich.console  import Console
from fc_rules_mine import Rules as rule
from fc_io_mine    import PrintItBBU as brichprt
from fc_io_mine    import SQLiteIO   as bsqlite3

BLANKCARD = '0'
VALID_RANK = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
@dataclass
class New_Tableau_dataclass( object ):
    running: bool = True
    newGame: bool = False
    restart: bool = False
    moveing: bool = True 
    noAbend: bool = False
    winning: bool = False
    verbose: bool = True

    tablow:  list = field(default_factory=list) 
    #allMoveSQLFwdBack = []    #in fc_io_mine: sqlite3 
    reason:  list = field(default_factory=list)   
    posdic:  list = field(default_factory=list)   
    EMPTYROW=[BLANKCARD for _ in range(8)]

    def restoreFlagDefaults(self):
        if self.running  != True:    self.running  = True
        if self.newGame  != False:   self.newGame  = False
        if self.restart  != False:   self.restart  = False
        if self.moveing  != True:    self.moveing  = True 
        if self.noAbend  != False:   self.noAbend  = False
        if self.winning  != False:   self.winning  = False
        if self.verbose  != True:    self.verbose  = True

    def updatePosition( self, destCard, doapt=None ):
        if doapt==None or (doapt[0] == -1 or doapt[1] == -1):
            if destCard in self.validcard:
            dou, doo = self.findPositionofW(destCard)