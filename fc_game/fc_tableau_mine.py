from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck    #import cardsfrommsucse    #from cardsfrommsucse import Card as card  #from cardsfrommsucse import Deck as deck
from          rich import print as rp
from rich.table    import Table
from rich.console  import Console
from fc_rules_mine import Rules as rule
from fc_io_mine    import PrintItBBU as brichprt
from fc_io_mine    import SQLiteIO   as bsqlite3
from dataclasses   import dataclass
from fc_cons_New1  import *
#    def total_cost(self) -> float:
#        return self.unit_price * self.quantity_on_hand
#will add, among other things, a __init__() that looks like:

#def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
#    self.name = name
#    self.unit_price = unit_price
#    self.quantity_on_hand = quantity_on_hand
#from minimum_rows import getidx4lastcards

cardA=card()
validt = rule()
brichp=brichprt()
bsqlt3=bsqlite3()

@dataclass
class StateFlags:
    """Class for keeping track of state."""

class Tableau(object):
    """Class for keeping track of Game status."""
    running: bool = True
    newGame: bool = False
    restart: bool = False
    moveing: bool = True 
    noAbend: bool = False
    winning: bool = False
    verbose: bool = True


    #allMoveSQLFwdBack = []
    CLRSYM={'C':['[blue]','♣'],'D':['[bright_magenta]','♦'],\
                 'H':['[red]','♥'], 'S':['[bright_green]','♠']}
    
    
    #verbose=True; running = True

    if verbose:    
        brichp.printConst();verbose=False
    
    def __init__(self) -> None:
        ''' bsqlt3.readFirstGamesRec();
            self.gameid,self.moveid,self.lTblRows=bsqlt3.readlastrecord()'''
        #flag=StateFlags()#porew=self.nextCards['3H']
        #if flag.running:
        #    pass
        self.tablow=[]
        qq=[BLANKCARD for _ in range(8)]
        self.tablow.append(qq)

        self.gameid=bsqlt3.readFirstGamesRec()
        self.gameid,self.moveid,self.lTblRows=bsqlt3.readlastrecord()
        if bsqlt3.allMoveSQLFwdBack == []:
            self.allMoveSQLFwdBack = []
        else:
            for i in bsqlt3.allMoveSQLFwdBack:
                self.allMoveSQLFwdBack.append(i)
        self.reason=[]
        #self.running: bool = True
        #self.newGame = newGame
        #self.restart = restart
        #self.moveing = moveing
        #self.noAbend = noAbend
        #self.winning = winning
        #self.verbose = verbose
    def NewGame(self, testDeck=None):
        """used to be able to test the same game over and over..."""
        running=True
        flagNewGame=True
        self.newGame = True
        self.restart = False
        self.moveing = True
        self.noAbend = False
        self.winning = False
        self.verbose = False
        dek = deck(); dek.shuffle()

        if testDeck==None:
            deckA,deckB=dek.turnTestdeckIntoDeck()            #tablow1=dek.newGame()            
        else:
            deckA,deckB=dek.turnTestdeckIntoDeck(testDeck)            #tablow1=deckE.newGame()        #deckE=dek
        validt.initPositionDict()
        zz=0
        self.originaltablow=[]
        self.originaltablow.append([BLANKCARD for _ in range(8)])
        self.tablow=[]
        self.tablow.append([BLANKCARD for _ in range(8)])
        for xx in range(22):
            zlistd=[]
            for yy in range(8):
                if zz < 52:   
                    zlistd.append(deckA[zz])
                    deckA[zz].set_position(xx,yy)
                    validt.posdic.update({str(deckA[zz]):[xx,yy]})
                else:
                    zlistd.append(BLANKCARD)
                zz+=1                
            self.tablow.append(zlistd)
            self.originaltablow.append(zlistd)
        self.gameid+=1;self.moveid=0
        dek.display(8)
        self.newGameflag=True
        bsqlt3.gamePrintTableau(self.tablow, self.reason, self.newGameflag)
        #imdjs=self.tablow[2][2].suit()
        return True,deckA,self.tablow
        # 
    def GGCard(self, tablow, minp):
        #self.validGG=False
        listsuit=list(self.SYMBOL.keys())
        if minp[1] in listsuit:
        #if minp[1] in list(SYMBOL.keys()):    rank=A t[0][f]=BLANKCARD
            foundation =  listsuit.index(minp[1]) + 4     #-1 for the x in listsuit
            if self.verbose and not self.winning:
                rp(f'{foundation=} = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit')
            moveCard   = self.VALID_RANK.index(minp[0])
            if (moveCard == 0 and tablow[0][foundation]==BLANKCARD) or \
                str(tablow[0][foundation])[0] == self.VALID_RANK[moveCard -1]:

                for xxx,www in enumerate(tablow):
                    uuu=[str(qqq) for qqq in www]
                    if xxx==0: 
                        if minp in uuu[:4]:
                            tablow[xxx][uuu.index(minp)] = BLANKCARD
                            break
                    elif minp in uuu: 
                        tablow[xxx][uuu.index(minp)] = BLANKCARD
                        break
                
                #tempcard=cardA.stringToCard(minp)
#                if foundation not in range(4,8):
#                    raise Exception(f'{foundation=} Out of range(s/b 4-7)')
                tablow[0][foundation] = minp
                tablow[0][foundation] = card(card.rank_list.index(minp[0]),card.suit_list.index(minp[1]),0,foundation)
                rule.posdic.update({minp:[0,foundation]})#self.validGG=True
        return tablow
    
    def findNoOf0FC(self,tablow):
        numOf0InFC=0; first0InFC=-1
        for ll in range(4):
            if str(tablow[0][ll]) == BLANKCARD or str(tablow[0][ll]) == 'xx':
                numOf0InFC += 1
                if first0InFC == -1:
                    first0InFC = ll
    
        return numOf0InFC, first0InFC
    
    def findNoOf0Cols(self, tablow):
        ''' Fixed bug: 1 used tablow[1:] the other didnt\n
                if you call me use tablow[1:]'''
        blankcolumns=0; first0Col=-1
        EMPTYCOL=[BLANKCARD for idxs in range(len(tablow))]

        colv = list(zip(*tablow))   
        
        for idc,colu in enumerate(colv):    #        all0=True
            colo = []
            colp=[str(w) for w in colu]  # fixed bug:
            for valk in colp:     # 1used tablow[1:] the other didnt
                colo.append(valk) 
            if colo == EMPTYCOL:            #for ids,colt in enumerate(colu[1:]):            #    if colt == ':            #        all0=False            #        break            #if all0:
                blankcolumns+=1
                if first0Col == -1:
                    first0Col = idc
        return blankcolumns, first0Col
    
    
    def FFCard(self, tablow, minp):
        moapt=0,0;doapt=0,0
        if minp[1] in list(self.SYMBOL.keys()):
            numOf0InFC, first0InFC = self.findNoOf0FC(tablow)
            if first0InFC > -1:
                doapt=0,first0InFC; mou=0; moo=0
                mou,moo=card(card.rank_list.index(minp[0]),card.suit_list.index(minp[1])).get_position()
                newCard=card(mou,moo).set_position(0,first0InFC)
                tablow[0][first0InFC]=newCard
                for ii,qq in enumerate(tablow):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        tablow[doapt[0]][doapt[1]]=tablow[mou][moo]
                        tablow[mou][moo]=BLANKCARD
                        rule.posdic.update({minp:[0,first0InFC]})
                        break
            else:
                self.moveing = False
        else:
            self.moveing = False

        return    tablow   # moapt,doapt
    
    def ZZCard(self, tablow, minp):
        moapt=0,0;doapt=0,0
        if minp[1] in (self.SYMBOL.keys()):
            blankcolumns, first0Col = self.findNoOf0Cols(tablow[1:])
            if first0Col > -1:
                doapt=1,first0Col; mou=0; moo=0
                for ii,qq in enumerate(tablow):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        tablow[doapt[0]][doapt[1]]=tablow[mou][moo]
                        tablow[mou][moo]=BLANKCARD
                        rule.posdic.update({minp:[0,first0Col]})
                        break
            else:
                self.moveing = False
        else:
            self.moveing = False

        return    tablow   # moapt,doapt
    
    def CCCard(self, tablow, minp, dinp):
        moapt=-1,0;    doapt=-1,0#;    dou=-1;    mou=-1
        test = False    #        validt = rule()
        #if validt.validMove: '''# remove?!?!?!?!?!?!?!??!?!'''
        self.reason = validt.validNextCCCard(tablow,minp,dinp,test)
        if validt.movnotdifcolr_1 and self.verbose:
            rp(f'[red]{validt.movnotdifcolr_1Lit}[/]')
        if validt.validMove:
            self.moveing = True
            tablow, moapt, doapt = self.getCardLocation( \
            tablow, minp,  dinp)
            if str(tablow[doapt[0]+1][doapt[1]]) != BLANKCARD:
                self.moveing = False            
                self.reason.append(f'Dest Not Empty: tablow[{doapt[0]+1}][{doapt[1]}]{str(tablow[doapt[0]+1][doapt[1]])}')
            else:
                tablow=self.moveCCCard(tablow, moapt, doapt)
        rp(f'{[y for y in self.reason]}',sep='\n')
        if validt.noAbend: self.noAbend=True
        else:                self.noAbend=False
        return    tablow, self.moveing, self.noAbend
    def moveCCCard(self, tablow, moapt, doapt):
        mou,moo=moapt;dou,doo=doapt
        if dou > -1 and mou > -1:
            tablow[dou+1][doo]=tablow[mou][moo]
            rule.posdic.update({str(tablow[mou][moo]):[doapt[0],doapt[1]]})
            tablow[mou][moo]=BLANKCARD    #break  # moapt,doapt
        return tablow
    def getCardLocation(self,tablow, minp, dinp):
        mou=-1;moo=0;dou=-1;doo=0;moapt=mou,moo;doapt=dou,doo
        for ii,qq in enumerate(tablow):# if minp in qq else 0]
            rr=[str(ss) for ss in qq]
            if minp in rr: 
                mou=ii; moo=rr.index(minp);moapt=mou,moo
            if dinp in rr: 
                dou=ii; doo=rr.index(dinp);doapt=dou,doo
            
            #if dou > -1 and mou > -1:
            #    tablow[doapt[0]+1][doapt[1]]=tablow[mou][moo]
            #    tablow[mou][moo]=BLANKCARD
            #    break  # moapt,doapt
        return tablow,moapt,doapt
    

    def getidx4lastcards(self, running, tablow):
    #def getidx4lastcards( running, tablow):
        idx4lastcards=[-1,-1,-1,-1,-1,-1,-1,-1]
        cpyrow=[];cpytbl=[];strtemp=BLANKCARD
        for idxrow,rowLocked in enumerate(tablow):
            cpyrow=[]
            for idxcell,cell in enumerate(rowLocked):
                cpyrow.append(tablow[idxrow][idxcell])
                tablowtype= type(tablow[idxrow][idxcell]);cardtype = type(card)
                if type(tablow[idxrow][idxcell]) != type(strtemp)and idxrow!=0:
                    idx4lastcards[idxcell]=idxrow
            cpytbl.append(cpyrow)
        maxidxoflc = max(idx4lastcards)
        pass
        return running, tablow, idx4lastcards, maxidxoflc
    
#def putUpLastRowsOfCards( running, dek, tablow, idx4lastcards, rowidx):
#    '''we might not need idxlastcards'''
#    for column in range(8):
#        if idx4lastcards[column] > -1 and tablow[rowidx][column]!=BLANK_CARD:
#            reason=rules.validLastRowsOfCards(tablow, rowidx, column)
#            if rules.validMove:
#                pass
#
#    pass
#    return running, dek, tablow


    def testhandleWeWon(self, running, tablow):
        strtemp=BLANKCARD;lentablow=len(tablow)
        minplist=[];self.winning=True
        for errchk in range(4):
            if str(tablow[0][errchk]) != BLANKCARD:
                return True, tablow
        #############################################
        running, tablow, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
        running, tablow)
        maxidxoflc+=1 
        reversed11to1=reversed(range(1,maxidxoflc))   
        for rowidx in reversed(range(1,maxidxoflc)):
                for column in range(8):
                    if idx4lastcards[column] > -1 and \
                       str(tablow[idx4lastcards[column]][column])!=BLANKCARD:
                        minplist.append(str(tablow[idx4lastcards[column]][column]))
                        tablow=self.GGCard(tablow,str(tablow[idx4lastcards[column]][column]))
                running, tablow, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
                running, tablow)
                bsqlt3.gamePrintTableau(tablow, self.reason)
                rp(minplist);minplist=[];self.winning=False
                tablow = self.handleWeWon(tablow)
                        #if self.validGG:
                        #    return False, tablow
 #          running, dek, tablow, idx4lastcards = self.getidx4lastcards(\
 #          running, dek, tablow)
        return running, tablow
    
    def handle_Re_Start(self, running, restartLit=''):    
        answer = brichp.getAnswer(f'\n\nEnter  Q|uit N|ewGame{restartLit}: ')
        lenAns=len(answer)
        if lenAns==1:
            answer=answer.capitalize()
            if answer in ["N","R","Q"]:
                if answer == "N":
                    running, dek, tablow = self.NewGame()
                if answer == "R":
                    running, dek, tablow = self.restartfromdb()
                if answer == "Q":
                    running = False; dek = None; tablow = None
                if answer not in ['N','R','Q']:
                    running = True; dek = None; tablow = None
                #def restartFromSQLite3DB(self):    #    tablow=self.restart_fromdb()        #bsqlt3.gamePrintTableau(tablow, self.reason)        
            '''for xx in outd:        
            ww=[]
            for yy in xx:
                if yy == BLANK_CARD:
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            tablow.append(ww)'''
        return running, dek, tablow   
    
    def handleWeWon(self, tablow):
        if tablow[1] == [BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD]:
            rp(f'{self.COLORS["C"]}WON![/] {self.COLORS['D']}WON![/] {self.COLORS["H"]}WON![/] {self.COLORS["S"]}WON![/] {self.COLORS["C"]}WON![/] {self.COLORS["D"]}WON![/] {self.COLORS["H"]}WON![/] {self.COLORS["S"]}WON![/]')    
            self.norow2leave = 3
            bsqlt3.deleteMostOfDbRowsAfterWin(self.gameid,self.norow2leave)
            
        return tablow


    def handleAnswer(self, running, dek, tablow):
        answer = brichp.getAnswer();lenAns=len(answer)
        self.moveing=True#try:    
        if lenAns < 1:
            self.moveing = False
            rp("invalid input: return False, BLANKCARD, BLANKCARD")
            return True, dek, tablow
        else:
            if lenAns == 1: #and answer == 'q':  running=False;rp('[gra]QUIT')
                running, tablow =self.handle1char(\
                running, tablow, answer)
                return running, dek, tablow
            elif lenAns  >1 and lenAns<4:
                self.currentMoveId = self.moveid
                running,self.moveing, tablow, self.reason = bsqlt3.handlebackfwd(running,tablow, answer,self.reason)
            elif lenAns == 4:
                minp=answer[:2];    dinp=answer[2:]
            elif lenAns == 5:
                minp=answer[:2];    dinp=answer[3:]
        if (lenAns == 4 or lenAns == 5) and self.moveing:
            running,tablow = self.handle4char(\
            running,tablow,minp,dinp)

        tablow = self.handleWeWon(tablow)

        if not running:
            bsqlt3.closeconn()
        
        return running, dek, tablow

    def copyrow1ontbl(self,tablow):
        cpytbl=[]
        for irow,drow in enumerate(tablow):
            if irow > 0:
                cpytbl.append(drow)
        return cpytbl


    def handle1char(self, running, tablow, answer):
        '''handle Q(uit), \n
                  W(on),  \n
                  S(tart) this Game from scratch
                  N(ew) GAME from scratch'''
        
        running                            = True
        answer=answer.upper()  if str(answer).isalpha() else answer
        if answer == 'Q':
            running = False
        if answer == 'W':
            running,tablow =self.testhandleWeWon(\
            running, tablow)
        if answer == 'N':
            self.restartCurrentGameFromScratch = False
            self.beginANewGame                 = True
        if answer == 'R':
            self.restartCurrentGameFromScratch = True
            self.beginANewGame                 = False
        return running,tablow
    def handle4char(self, running, tablow,minp,dinp):
        validMove=True;noAbend=False
        minp, dinp = self.makeInputUppercase(str(minp), str(dinp))
        validt.noFoundationAsMover(tablow, minp)
        if not validt.moveing:    self.moveing=False
        if dinp[1] == 'G' and self.moveing:
            dinp = 'GG';   tablow = self.GGCard(tablow, minp)
        elif dinp[1] == 'F' and self.moveing:
            dinp = 'FF';   tablow = self.FFCard(tablow, minp) 
        elif dinp[1] == 'Z' and self.moveing:
            dinp = 'ZZ';   tablow = self.ZZCard(tablow, minp) 
        elif self.moveing:
            tablow, validMove, noAbend = self.CCCard(tablow, minp, dinp) 
        #if dinp == 'GG' or dinp == 'FF' or dinp == 'ZZ':
        #tablow1, moapt1, doapt1 = dek.position(tablow1, minp, dinp)
        #rp(f'From cardsfrommsucse:{moapt1=}, {doapt1=}')
        #dek.richPrintTablow()
        #except:    rp('if len(answer) not in [1,4,5]:')
        if validMove and self.moveing and not noAbend:
            bsqlt3.gamePrintTableau(tablow, self.reason)  #tablow = self.handleWeWon(tablow)
    
        return running, tablow

    def handle23char(self, running, tablow, answer, currentMoveId):
        answer=answer[0].upper()+answer[1:]  if str(answer)[0].isalpha() else answer
        self.currentMoveId = currentMoveId
        self.noOfRows2Move=0; self.needAnswer=True
        if answer[0] == 'B' or answer[0] == 'F':
            try:
                if str(answer[1:]).isdigit():
                    self.noOfRows2Move=int(answer[1:])                    
            except:
                rp(f"invalid input: {answer}")
                self.needAnswer=False
        else:
            rp(f"invalid input: {answer}")
            self.needAnswer=False
        
        if answer[0] == 'B' and self.needAnswer:
            if self.currentMoveId - self.noOfRows2Move < 1:
                self.currentMoveId =1
            else:
                self.currentMoveId -= self.noOfRows2Move 
        elif answer[0] == 'F' and self.needAnswer:
            if self.currentMoveId + self.noOfRows2Move >= bsqlt3.maxmoveid:
                self.needAnswer=False
            else:
                self.currentMoveId += self.noOfRows2Move 

        if self.needAnswer:
            running, tablow = bsqlt3.getSpecificTablowDisplay(\
            running, tablow,  self.currentMoveId)
            bsqlt3.gamePrintTableau(tablow, self.reason)
        return running, tablow

    # def handlePost23char(self, running, tablow,  answer):
    #     return running, tablow

    def restartfromdb(self):
        #def restartCurrentGame(self):
        ranklist=['K','Q','J','T','9','8','7','6','5','4','3','2','A']
        testdeck=[r+s for s in ['C','D','H','S'] for r in (ranklist)]
        outa = [[ '__', '__', '__', '__','2C','2D','5H','5S'],       #00
                [ '__','KS','KD', '__', '__','KC', '__','KH'],       #01
                [ '__','QD','QC', '__', '__','QH', '__','QS'],       #02 
                [ '__','JS','JD', '__', '__','JC', '__','JH'],       #03
                [ '__','TH','TC', '__', '__','TD', '__','TS'],       #04 
                [ '__','9C','9H', '__', '__','9S', '__','9D'],       #05
                [ '__','8D','8C', '__', '__','8H', '__','8S'],       #06
                [ '__','7C','7D', '__', '__','7S', '__','7H'],       #07
                [ '__','6H','6S', '__', '__','6D', '__','6C'],       #08
                [ '__','5C', '__', '__', '__', '__', '__','5D'],       #09
                [ '__','4D', '__', '__', '__', '__', '__','4C'],       #10
                [ '__','3C', '__', '__', '__', '__', '__','3D'],       #11
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #12
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #13
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #14
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #15
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #16
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #17
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #18
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #19
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #20
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #21
                [ '__', '__', '__', '__', '__', '__', '__', '__']  ]     #22
        outb = [['QS', '__', '__', '__','AC','2D','4H','4S'],          
                ['JH','KS','KD','8H','5S','3D','TD','KH'],
                ['TS','QD','QC','7S','5H','KC','2C','4C'],
                ['9D','JS','JD','6D', '__','5D','QH', '__'],
                ['8S','TH','TC', '__', '__','JC','9S', '__'],
                ['7H','9C','9H', '__', '__', '__','8C', '__'],
                ['6C','8D', '__', '__', '__', '__','7D', '__'],
                [ '__','7C', '__', '__', '__', '__','6S', '__'],
                [ '__','6H', '__', '__', '__', '__', '__', '__'],     
                [ '__','5C', '__', '__', '__', '__', '__', '__'],     
                [ '__','4D', '__', '__', '__', '__', '__', '__'],     
                [ '__','3C', '__', '__', '__', '__', '__', '__'],        #11
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #12
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #13
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #14
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #15
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #16
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #17
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #18
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #19
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #20
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #21
                [ '__', '__', '__', '__', '__', '__', '__', '__']  ]     #22
        outc = [[ '__', '__', '__', '__','2C','2D','4H','4S'],       #0  
                ['JH','KS','KD','8H','KC','3D', '__','KH'],       #1  
                ['TS','QD','QC','7S','QH', '__', '__','QS'],       #2   
                ['9D','JS','JD','6D','JC', '__', '__', '__'],       #3   
                ['8S','TH','TC','5S','TD', '__', '__', '__'],       #4   
                ['7H','9C','9H', '__','9S', '__', '__', '__'],       #5   
                ['6C','8D','8C', '__', '__', '__', '__', '__'],       #6   
                ['5H','7C','7D', '__', '__', '__', '__', '__'],       #7   
                ['4C','6H','6S', '__', '__', '__', '__', '__'],       #8   
                [ '__','5C','5D', '__', '__', '__', '__', '__'],       #9   
                [ '__','4D', '__', '__', '__', '__', '__', '__'],       #10   
                [ '__','3C', '__', '__', '__', '__', '__', '__'],       #11 
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #12
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #13
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #14
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #15
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #16
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #17
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #18
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #19
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #20
                [ '__', '__', '__', '__', '__', '__', '__', '__'],       #21
                [ '__', '__', '__', '__', '__', '__', '__', '__']  ]     #22
        outd = [[ '__', '__', '__', '__', '__', '__', '__', '__'],     #0
                ['4S','JD','3S','QH','7D','4C','2S','3C'],     #1
                ['7S','9C','7H','JS','5H','AC','8C','AD'],     #2
                ['KS','3D','TH','2C','6C','AS','QC','9D'],     #3
                ['3H','AH','9H','4D','8D','KH','8H','8S'],     #4
                ['KC','6D','5S','KD','6S','7C','5D','5C'],     #5
                ['6H','QS','2D','TD','TS','4H','JH','2H'],     #6
                ['TC','QD','JC','9S', '__', '__', '__', '__'],     #7
                [ '__', '__', '__', '__', '__', '__', '__', '__'],     #8
                [ '__', '__', '__', '__', '__', '__', '__', '__'],     #9
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #10
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #11
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #12
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #13
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #14
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #15
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #16
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #17
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #18
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #19
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #20
                [ '__', '__', '__', '__', '__', '__', '__', '__'],    #21
                [ '__', '__', '__', '__', '__', '__', '__', '__']]    #22   
        """Create a card for each strLit"""
        dek=deck()
        running, tablow = bsqlt3.convertSQL2Tablo()   
        bsqlt3.readAllRowsOnRestart()
        bsqlt3.gamePrintTableau(tablow, self.reason)
        return running, dek, tablow 

    '''def convertSQL2 Tablo(self):
        dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list;tablow=[]
        #with closing(sql3class.cursorSQL3) as cursor3:
        #gamer=game()
        self.tablow=[]
        qq=self.EMPTYROW
        self.tablow.append(qq)
        running=True#self.lTblRows=sql3class.readlast record()
        cardj=[ 'xx8Cxxxx2C6D3H5S', 
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
                '5Cxxxxxxxxxxxxxx']
        cardi=[]    
        if self.lTblRows !=None and len(self.lTblRows) > 0:
            self.gameid,self.moveid,self.lTblRows = bsqlt3.readlastrecord()
        #self.gameid+=1
        #self.moveid+=1
        #tablow = fromsql2tablo
        for listoflists in self.lTblRows:
            cardg='';cardh=[]
            for idxchar,chara in enumerate(listoflists):
                cardg+=chara
                if idxchar%2!=0 and idxchar>0:
                    #if cardg=='xx':
                    #    cardg=BLANKCARD
                    cardh.append(cardg)
                    cardg=''                        #else:
            cardi.append(cardh)        
    
        suit1=card.suit_list; rank1=card.rank_list;tablow=[]
        for xx in cardi:
            ww=[]
            for yy in xx:
                if yy == 'xx':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            tablow.append(ww)
        while len(tablow)<23:
            tablow.append([BLANKCARD for w in range(8)])
        for idxm,rown in enumerate(tablow):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    tablow[idxm][idxn] = BLANKCARD
        bsqlt3.gamePrintTableau(tablow, self.reason)
        return dek,tablow,running'''


    def makeInputUppercase(self, minp, dinp):
        """if <b>InputAlphabetic</b> make uppercase:
        minp=minp[0].upper()+minp[1] \n
             if str(minp[0]).isalpha() else minp     
        minp=minp[0]+minp[1].upper() \n
             if str(minp[1]).isalpha() else minp     
        dinp=dinp[0].upper()+dinp[1] \n
             if str(dinp[0]).isalpha() else dinp     
        dinp=dinp[0]+dinp[1].upper() \n
             if str(dinp[1]).isalpha() else dinp     
        return minp,dinp
        """ #rp(f'{len(tablow)=}')  
        nminp='';ndinp=''
        #nminp=minp[i].upper()  if str(minp[i]).isalpha() else minp[i] for i in range(2)
        nminp = ''.join(minp[i].upper() if str(minp[i]).isalpha() else minp[i] for i in range(2) )
        ndinp = ''.join(dinp[i].upper() if str(dinp[i]).isalpha() else dinp[i] for i in range(2) )
        if self.verbose:
            rp(f'{minp=}==>{nminp=}    and   {dinp=}==>{ndinp=}')
        minp=minp[0].upper()+minp[1] if str(minp[0]).isalpha() else minp
        minp=minp[0]+minp[1].upper() if str(minp[1]).isalpha() else minp
        dinp=dinp[0].upper()+dinp[1] if str(dinp[0]).isalpha() else dinp 
        dinp=dinp[0]+dinp[1].upper() if str(dinp[1]).isalpha() else dinp
        return str(minp),str(dinp)
         
    