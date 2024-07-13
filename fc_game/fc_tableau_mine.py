from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck
#import cardsfrommsucse 
#from cardsfrommsucse import Card as card
#from cardsfrommsucse import Deck as deck
from          rich import print as rp
from rich.table    import Table
from rich.console  import Console
from fc_rules_mine import Rules as rule
from fc_io_mine    import PrintItBBU as brichprt
from fc_io_mine    import SQLiteIO   as bsqlite3
#from minimum_rows import getidx4lastcards
BLANKCARD = '0'
cardA=card()
brichp=brichprt()
bsqlt3=bsqlite3()
class Tableau(object):

    EMPTYROW=[BLANKCARD for _ in range(8)]
    suitlit = ['[white]0[/]']
    SYMBOL={'C':'♣','D':'♦','H':'♥','S':'♠'}
    COLORS={'C':'[blue]','D':'[bright_magenta]','H':'[red]','S':'[bright_green]'}
    VALID_RANK = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    CLRSYM={'C':['[blue]','♣'],'D':['[bright_magenta]','♦'],\
                 'H':['[red]','♥'], 'S':['[bright_green]','♠']}
    
    
    startOver=False; running = True
    for at in SYMBOL:
        for au in range(1,14):
            if au == 1:
                suitlit.append(f'{CLRSYM[at][0]}A{CLRSYM[at][1]}[/]')    
            elif au == 10:
                suitlit.append(f'{CLRSYM[at][0]}T{CLRSYM[at][1]}[/]')
            elif au == 11:
                suitlit.append(f'{CLRSYM[at][0]}J{CLRSYM[at][1]}[/]')
            elif au == 12:
                suitlit.append(f'{CLRSYM[at][0]}Q{CLRSYM[at][1]}[/]')
            elif au == 13:
                suitlit.append(f'{CLRSYM[at][0]}K{CLRSYM[at][1]}[/]')
            else:
                suitlit.append(f'{CLRSYM[at][0]}{str(au)}{CLRSYM[at][0]}[/]')
    #rp(f'{suitlit=}',sep=' ',end=', ')
    if True:    
        brichp.printConst()
        #output={}#nextCards
        #for j in range(3,13+1):
        #    for k in range(2):
        #        output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
        #        output[j+(13*(k+2))] = [j-1, j+12]
    
        j=0;k=0; validsuit={'C':['D','H'],'S':['D','H'],\
                            'H':['C','S'],'D':['C','S']}
        #nextCard = {}
        #for vsuit in validsuit:
        #    for idx, vrank in enumerate(VALID_RANK[2:]):
        #        nextCard[vrank+vsuit]=[VALID_RANK[idx+1]+validsuit[vsuit][0],VALID_RANK[idx+1]+validsuit[vsuit][1]]
        ##rp(f'{nextCard=}{output=}',sep=' ',end=' ')
        #nextCards={'3H':['2C','2S'],'4H':['3C','3S'],\
        #           '5H':['4C','4S'],'6H':['5C','5S'],\
        #           '7H':['6C','6S'],'8H':['7C','7S']}
    

    def __init__(self) -> None:
        #porew=self.nextCards['3H']
        self.tablow=[]
        qq=[BLANKCARD for _ in range(8)]
        self.tablow.append(qq)

        self.gameid=bsqlt3.readFirstGamesRec()
        self.gameid,self.moveid,self.lTblRows=bsqlt3.readlastrecord()

    def NewGame(self, testDeck=None):
        running=True
        dek = deck(); dek.shuffle()
        if testDeck==None:
            deckA,deckB=dek.turnTestdeckIntoDeck()
            #tablow1=dek.newGame()
            
        else:
            deckA,deckB=dek.turnTestdeckIntoDeck(testDeck)
            #tablow1=deckE.newGame()
        #deckE=dek
        zz=0;self.originaltablow=[]
        for xx in range(22):
            zlistd=[]
            for yy in range(8):
                zlistd.append(deckA[zz] if zz < 52 else BLANKCARD)
                zz+=1
            self.tablow.append(zlistd)
            self.originaltablow.append(zlistd)
        self.gameid+=1;self.moveid=0
        dek.display(8)
        
        self.gamePrintTableau(self.tablow)
        imdjs=self.tablow[2][2].suit()
        return True,deckA,self.tablow
    
    def GGCard(self, tablow, minp):
        #self.validGG=False
        listsuit=list(self.SYMBOL.keys())
        if minp[1] in listsuit:
        #if minp[1] in list(SYMBOL.keys()):    rank=A t[0][f]=BLANKCARD
            foundation =  listsuit.index(minp[1]) + 4     #-1 for the x in listsuit
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
                tablow[0][foundation] = minp
                #self.validGG=True
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
                for ii,qq in enumerate(tablow):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        tablow[doapt[0]][doapt[1]]=tablow[mou][moo]
                        tablow[mou][moo]=BLANKCARD
                        break
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
                        break
        return    tablow   # moapt,doapt
    
    def CCCard(self, tablow, minp, dinp):
        moapt=-1,0;    doapt=-1,0#;    dou=-1;    mou=-1
        test = True
        validCC = rule()
        if validCC.validMove:
            reason = validCC.validNextCCCard(tablow,minp,dinp,test)
            if validCC.movnotdifcolr_1:
                rp(f'[red]{validCC.movnotdifcolr_1Lit}[/]')
            if validCC.validMove:
                tablow,moapt,doapt = self.getCardLocation( \
                tablow, minp, dinp)
                tablow=self.moveCCCard(tablow, moapt, doapt)
            rp(f'{[y for y in reason]}',sep='\n')
        return    tablow 
    def moveCCCard(self, tablow, moapt, doapt):
        mou,moo=moapt;dou,doo=doapt
        if dou > -1 and mou > -1:
            tablow[dou+1][doo]=tablow[mou][moo]
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
        cpyrow=[];cpytbl=[];strtemp='0'
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
#        if idx4lastcards[column] > -1 and tablow[rowidx][column]!='0':
#            reason=rules.validLastRowsOfCards(tablow, rowidx, column)
#            if rules.validMove:
#                pass
#
#    pass
#    return running, dek, tablow


    def testhandleWeWon(self, running, tablow):
        strtemp='0';lentablow=len(tablow)
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
                        tablow=self.GGCard(tablow,str(tablow[idx4lastcards[column]][column]))
                running, tablow, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
                running, tablow)
                self.gamePrintTableau(tablow)
                tablow = self.handleWeWon(tablow)
                        #if self.validGG:
                        #    return False, tablow
 #          running, dek, tablow, idx4lastcards = self.getidx4lastcards(\
 #          running, dek, tablow)
        return running, tablow
    
    def handle_Re_Start(self, running):    
        answer = brichp.getAnswer(f'\nnEnter N|ewGame R|estartLastGameFromDB or Q|uit: ')
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

                #def restartFromSQLite3DB(self):    #    tablow=self.restartfromdb()        #self.gamePrintTableau(tablow)        
            '''for xx in outd:        
            ww=[]
            for yy in xx:
                if yy == '0':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            tablow.append(ww)'''
        return running, dek, tablow   
    
    def handleWeWon(self, tablow):
        if tablow[1] == ['0','0','0','0','0','0','0','0']:
            rp(f'{self.COLORS["C"]}WON![/] {self.COLORS['D']}WON![/] {self.COLORS["H"]}WON![/] {self.COLORS["S"]}WON![/] {self.COLORS["C"]}WON![/] {self.COLORS["D"]}WON![/] {self.COLORS["H"]}WON![/] {self.COLORS["S"]}WON![/]')    
            self.norow2leave =3
            bsqlt3.deleteMostOfDbRowsAfterWin(self.gameid,self.norow2leave)
        return tablow


    def handleAnswer(self, running, dek, tablow):
        answer = brichp.getAnswer();lenAns=len(answer)
    #try:    
        if lenAns not in [1,4,5]:
            rp("invalid input: return False, BLANKCARD, BLANKCARD")
            return True, dek, tablow
        else:
            if lenAns == 1: #and answer == 'q':  running=False;rp('[gra]QUIT')
                running, tablow =self.handle1char(\
                running, tablow, answer)
                return running, dek, tablow
            elif lenAns == 4:
                minp=answer[:2];    dinp=answer[2:]
            elif lenAns == 5:
                minp=answer[:2];    dinp=answer[3:]
        
        running,tablow = self.handle4char(\
        running,tablow,minp,dinp)
        #    return running,tablow,tablow1,dek
        #if tablow[0] == ['0','0','0','0','KC','KD','KH','KS']:
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
        self.restartCurrentGameFromScratch = False
        self.beginANewGame                 = True
        running                            = True
        answer=answer.upper()  if str(answer).isalpha() else answer
        if answer == 'Q':
            running = False
        if answer == 'W':
            running,tablow =self.testhandleWeWon(\
            running, tablow)
        if answer == 'N':
            pass
        if answer == 'R':
            self.restartCurrentGameFromScratch = True
            self.beginANewGame                 = False
            running                            = True
        return running,tablow
    def putSomeUp(self,running,tablow):
        winning=True;numOfMove2Foundation=0
        self.backuptbl=[rows for rows in tablow]
        self.zackuptbk=[rows for rows in tablow]
        yackuptbj=[rows for rows in tablow]
            
        while winning:    #colh = list(zip(*tablow))
            lastnon0 = 0;rankl=self.VALID_RANK;suitl=list(self.SYMBOL.keys())
            
            for idx,colj in enumerate(list(zip(*yackuptbj))):   #0is0
                self.cpytbl =[rows for rows in yackuptbj]
                blankcolumns, first0Col = self.findNoOf0Cols(self.cpytbl[1:])
                if blankcolumns == 8:
                    winning=False
                    break
                lastnon0=BLANKCARD;lastidx=-1        #find the last non-zero !! Does it Foundation???
                #check if FCs will go up       #object of type 'reversed' has no len()
                reversedcolj = []
                for xx in reversed(colj):
                    reversedcolj.append(str(xx))            
                if reversedcolj == [BLANKCARD for poiu in range(len(reversedcolj))]:
                    pass
                else:
                    for iey,xcv in enumerate(reversedcolj):
                        xxx=str(xcv)
                        lln0=len(lastnon0)
                        if lastidx == -1 and xxx != BLANKCARD:
                            if xxx[0] in rankl and xxx[1] in suitl:
                                lastnon0 = xxx
                                lastidx  = iey
                    if len(lastnon0) == 2 and lastidx<22:#if 2h
                        if lastnon0[0] == 'A':    
                            winning=False
                            break
                        sidx = suitl.index(lastnon0[1])+4
                        ridx = rankl.index(lastnon0[0])
                        foundation=yackuptbj[0][sidx]
                        movecard=f'{rankl[ridx-1]}{lastnon0[1]}'
                        if movecard == foundation:
                            yackuptbj[0][sidx]=lastnon0
                            yackuptbj[22-lastidx][idx]=0
                            self.gamePrintTableau(yackuptbj)

        return    running,tablow
    def handle4char(self, running, tablow,minp,dinp):
    
        minp, dinp = self.makeInputUppercase(str(minp), str(dinp))
                   
        if dinp[1] == 'G':
            dinp = 'GG';   tablow = self.GGCard(tablow, minp)
        elif dinp[1] == 'F':
            dinp = 'FF';   tablow = self.FFCard(tablow, minp) 
        elif dinp[1] == 'Z':
            dinp = 'ZZ';   tablow = self.ZZCard(tablow, minp) 
        else:
                           tablow = self.CCCard(tablow, minp, dinp) 
        #if dinp == 'GG' or dinp == 'FF' or dinp == 'ZZ':
        #tablow1, moapt1, doapt1 = dek.position(tablow1, minp, dinp)
        #rp(f'From cardsfrommsucse:{moapt1=}, {doapt1=}')
        #dek.richPrintTablow()
        #except:    rp('if len(answer) not in [1,4,5]:')
        self.gamePrintTableau(tablow)  #tablow = self.handleWeWon(tablow)
    
        return running, tablow
    
    def gamePrintTableau(self, tablow):
        tablow,self.gameid,self.moveid = bsqlt3.insertTablow(tablow,self.gameid,self.moveid)
        brichp.printTableau(tablow)                    

    def restartfromdb(self):
        #def restartCurrentGame(self):
        ranklist=['K','Q','J','T','9','8','7','6','5','4','3','2','A']
        testdeck=[r+s for r in ['C','D','H','S'] for s in (ranklist)]
        outa = [[ '0', '0', '0', '0','2C','2D','5H','5S'],       #00
                [ '0','KS','KD', '0', '0','KC', '0','KH'],       #01
                [ '0','QD','QC', '0', '0','QH', '0','QS'],       #02 
                [ '0','JS','JD', '0', '0','JC', '0','JH'],       #03
                [ '0','TH','TC', '0', '0','TD', '0','TS'],       #04 
                [ '0','9C','9H', '0', '0','9S', '0','9D'],       #05
                [ '0','8D','8C', '0', '0','8H', '0','8S'],       #06
                [ '0','7C','7D', '0', '0','7S', '0','7H'],       #07
                [ '0','6H','6S', '0', '0','6D', '0','6C'],       #08
                [ '0','5C', '0', '0', '0', '0', '0','5D'],       #09
                [ '0','4D', '0', '0', '0', '0', '0','4C'],       #10
                [ '0','3C', '0', '0', '0', '0', '0','3D'],       #11
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #12
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #13
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #14
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #15
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #16
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #17
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #18
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #19
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #20
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #21
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22
        outb = [['QS', '0', '0', '0','AC','2D','4H','4S'],          
                ['JH','KS','KD','8H','5S','3D','TD','KH'],
                ['TS','QD','QC','7S','5H','KC','2C','4C'],
                ['9D','JS','JD','6D', '0','5D','QH', '0'],
                ['8S','TH','TC', '0', '0','JC','9S', '0'],
                ['7H','9C','9H', '0', '0', '0','8C', '0'],
                ['6C','8D', '0', '0', '0', '0','7D', '0'],
                [ '0','7C', '0', '0', '0', '0','6S', '0'],
                [ '0','6H', '0', '0', '0', '0', '0', '0'],     
                [ '0','5C', '0', '0', '0', '0', '0', '0'],     
                [ '0','4D', '0', '0', '0', '0', '0', '0'],     
                [ '0','3C', '0', '0', '0', '0', '0', '0'],        #11
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #12
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #13
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #14
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #15
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #16
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #17
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #18
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #19
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #20
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #21
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22
        outc = [[ '0', '0', '0', '0','2C','2D','4H','4S'],       #0  
                ['JH','KS','KD','8H','KC','3D', '0','KH'],       #1  
                ['TS','QD','QC','7S','QH', '0', '0','QS'],       #2   
                ['9D','JS','JD','6D','JC', '0', '0', '0'],       #3   
                ['8S','TH','TC','5S','TD', '0', '0', '0'],       #4   
                ['7H','9C','9H', '0','9S', '0', '0', '0'],       #5   
                ['6C','8D','8C', '0', '0', '0', '0', '0'],       #6   
                ['5H','7C','7D', '0', '0', '0', '0', '0'],       #7   
                ['4C','6H','6S', '0', '0', '0', '0', '0'],       #8   
                [ '0','5C','5D', '0', '0', '0', '0', '0'],       #9   
                [ '0','4D', '0', '0', '0', '0', '0', '0'],       #10   
                [ '0','3C', '0', '0', '0', '0', '0', '0'],       #11 
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #12
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #13
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #14
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #15
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #16
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #17
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #18
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #19
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #20
                [ '0', '0', '0', '0', '0', '0', '0', '0'],       #21
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22
        outd = [[ '0', '0', '0', '0', '0', '0', '0', '0'],     #0
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
        """Create a card for each strLit"""
        dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list;tablow=[]
        #with closing(sql3class.cursorSQL3) as cursor3:
        #gamer=game()
        self.tablow=[]
        qq=self.EMPTYROW
        self.tablow.append(qq)
        running=True#self.lTblRows=sql3class.readlastrecord()
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
        for listoflists in self.lTblRows:
            cardg='';cardh=[]
            for idxchar,chara in enumerate(listoflists):
                cardg+=chara
                if idxchar%2!=0 and idxchar>0:
                    #if cardg=='xx':
                    #    cardg='0'
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
            tablow.append(['0' for w in range(8)])
        for idxm,rown in enumerate(tablow):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    tablow[idxm][idxn] = '0'
        self.gamePrintTableau(tablow)   

        return running, dek, tablow 


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
        minp=minp[0].upper()+minp[1] if str(minp[0]).isalpha() else minp
        minp=minp[0]+minp[1].upper() if str(minp[1]).isalpha() else minp
        dinp=dinp[0].upper()+dinp[1] if str(dinp[0]).isalpha() else dinp 
        dinp=dinp[0]+dinp[1].upper() if str(dinp[1]).isalpha() else dinp
        return str(minp),str(dinp)
         
    