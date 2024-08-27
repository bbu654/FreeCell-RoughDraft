from copy import deepcopy as dpcopy
from dataclasses import dataclass, field
from tabnanny import check
import webbrowser

from rich import print as rp
from rich.console import Console
from rich.table import Table

from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck  # import cardsfrommsucse    #from cardsfrommsucse import Card as card  #from cardsfrommsucse import Deck as deck
from fc_cons_New1 import *
from fc_io_mine import PrintItBBU as brichprt
from fc_io_mine import SQLiteIO as bsqlite3
from fc_rules_mine import Rules

#    def total_cost(self) -> float:
#        return self.unit_price * self.quantity_on_hand
#will add, among other things, a __init__() that looks like:

#def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
#    self.name = name
#    self.unit_price = unit_price
#    self.quantity_on_hand = quantity_on_hand
#from minimum_rows import getidx4lastcards

cardA=card()    
rules = Rules()
brichp=brichprt()
bsqlt3=bsqlite3()

@dataclass
class StateFlags(object):
    """Class for keeping track of state flags."""
    running: bool = True
    newGame: bool = False
    restart: bool = False
    moveing: bool = True 
    noAbend: bool = False
    winning: bool = False
    verbose: bool = False
    isdirty: bool = False
    backfwd: bool = False
    print(f'exit: StateFlags')
    def restoreFlagDefaults(self):
        if self.running  != True:    self.running  = True
        if self.newGame  != False:   self.newGame  = False
        if self.restart  != False:   self.restart  = False
        if self.moveing  != True:    self.moveing  = True 
        if self.noAbend  != False:   self.noAbend  = False
        if self.winning  != False:   self.winning  = False
        if self.verbose  != False:   self.verbose  = False
        if self.isdirty  != False:   self.isdirty  = False
        if self.backfwd  != False:   self.backfwd  = False
@dataclass
class Tableau_dataclass(StateFlags):
    """Class for keeping track of Game variables (not flags)."""
    print(f'entr: Tableau_dataclass')
    maxmvid: int  = -1
    gameid:  int  = -1
    moveid:  int  = -1
    answall: str  = ''
    tablown: list = field(default_factory=list) 
    sbckN4h: list = field(default_factory=list)    #in fc_io_mine: sqlite3 
    reasonx: list = field(default_factory=list)   
    posdict: dict = field(default_factory=dict)
    ogtablo: list = field(default_factory=list)

    EMPTYROW=[BLANKCARD for _ in range(8)]
    #allMoveSQLFwdBack = []
    CLRSYM={'C':['[blue]','♣'],'D':['[bright_magenta]','♦'],\
                 'H':['[red]','♥'], 'S':['[bright_green]','♠']}
    
    def __post_init__(self):            #print(f'before makep osdict{self.posdict=}')
        self.makeposdict()                   
        print(f'exit: __post_init__')                                                                                                                                                                                                                                                       #print(f'after  makep osdict{self.p osdic=}')
        ''' bsqlt3.readFirstGamesRec();
            self.gameid,self.moveid,self.lTblRows=bsqlt3.readlastrecord()'''
        #flag=StateFlags()#porew=self.nextCards['3H']
        #if flag.running:
        #    pass
        self.tablown=[]
        qq=[BLANKCARD for _ in range(8)]
        self.tablown.append(qq)
    
    #verbose=True; running = True

    if StateFlags.verbose:    
        brichp.printConst();StateFlags.verbose=False
    
    def makeposdict( self ):
        '''return {k+l:[-1,-1] for k in validcard}'''
        self.posdict = {k:[-1,-1] for k in validcard}
        print(f'exit: Tableau_dataclass.makeposdict')

    def convertSQL2Tablo(self, chk1strow=False):
        #dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list
        #tablow=[]
        #with closing(sql3class.cursorSQL3) as cursor3:
        #gamer=game()
        self.tablown=[]
        qq=[BLANKCARD for zz in range(8)]
        #if not self.backfwd:#chk1strow:
        #    self.tablown.append(qq)
        self.backfwd = False
        running=True#self.lTblRows=sql3class.readlast record()
        cardi=[]
        if self.lTblRows !=None and len(self.lTblRows) < 2:
            self.gameid,self.moveid,self.answall,self.lTblRows = bsqlt3.readlastrecord()
        #self.gameid+=1     #self.moveid+=1    #tablow = fromsql2tablo
        for listoflists in self.lTblRows:
            if len(listoflists) != 16: 
                self.invalidTabloLen = True
                bsqlt3.closeconn()
                raise Exception(f'{len(listoflists)=} AND != 16') 
            lof2char= [listoflists[i:i+2] for i in range(0, len(listoflists), 2)]
            cardi.append(lof2char)
        suit1=card.suit_list; rank1=card.rank_list
        self.rowx=-1;self.coly=-1
        for ir,xx in enumerate(cardi):
            ww=[];self.rowx += 1
            if self.rowx > 22: raise Exception(f"rowx Index[[{self.rowx}] out of range")
            for ic,yy in enumerate(xx):
                self.coly += 1                        #if self.coly > 7: raise Exception(f"coly Index[[{self.coly}] out of range") 
                if yy == 'xx' or yy == '__':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1]),ir,ic))
                    self.posdict.update({yy:[ir,ic]})
            self.tablown.append(ww)
        while len(self.tablown)<23:
            self.tablown.append([BLANKCARD for w in range(8)])
        for idxm,rown in enumerate(self.tablown):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    self.tablown[idxm][idxn] = BLANKCARD    #Tableau.gamePrintTableau(self.answall,self.tablown)
        
        return 

class Tableau(Tableau_dataclass):
    print(f'entr: class Tableau')
    def __init__(self):
        Tableau_dataclass.__init__(self)#return super().__post_init__()
        print(f'entr: Tableau.__init__')
        self.gameid=bsqlt3.readFirstGamesRec()
        self.gameid,self.moveid,self.answall,self.lTblRows=bsqlt3.readlastrecord()
        if bsqlt3.allMoveSQLFwdBack == []:
            self.allMoveSQLFwdBack = []
            self.sbckN4h = []
        else:
            for i in bsqlt3.allMoveSQLFwdBack:
                self.allMoveSQLFwdBack.append(i)
                self.sbckN4h.append(i)
        self.reasonx=[]

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
        self.gtabl1 = dpcopy(self.posdict)
        self.answall = 'O   '
        dek = deck(); dek.shuffle()
        if testDeck==None:
            deckA,deckB=dek.turnTestdeckIntoDeck()            #tablow1=dek.newGame()            
        else:
            deckA,deckB=dek.turnTestdeckIntoDeck(testDeck)            #tablow1=deckE.newGame()        #deckE=dek
        #rules.initPositionDict()
        self.makeposdict()
        zz=0
        self.ogtablo=[]
        self.ogtablo.append([BLANKCARD for _ in range(8)])
        self.tablown=[]
        self.tablown.append([BLANKCARD for _ in range(8)])
        for xx in range(22):
            zlistd=[]
            for yy in range(8):
                if zz < 52:   
                    zlistd.append(deckA[zz])
                    deckA[zz].set_position(xx,yy)
                    self.posdict.update({str(deckA[zz]):[xx,yy]})
                else:
                    zlistd.append(BLANKCARD)
                zz+=1                
            self.tablown.append(zlistd)
            self.ogtablo.append(zlistd)
        self.gameid+=1;self.moveid=0
        dek.display(8)
        self.newGameflag=True
        bsqlt3.gamePrintTableau(self.answall[-4:],self.tablown, self.reasonx, self.newGameflag)
        self.reasonx = []
        #imdjs=self.tablown[2][2].suit()

        return True,deckA
        # 
    
    def findNoOf0FC(self):
        numOf0InFC=0; first0InFC=-1
        for ll in range(4):
            if str(self.tablown[0][ll]) == BLANKCARD or str(self.tablown[0][ll]) == 'xx':
                numOf0InFC += 1
                if first0InFC == -1:
                    first0InFC = ll
    
        return numOf0InFC, first0InFC
    
    def findNoOf0Cols(self, tablow):
        ''' Fixed bug: 1 used self.tablown[1:] the other didnt\n
                if you call me use self.tablown[1:]'''
        blankcolumns=0; first0Col=-1
        EMPTYCOL=[BLANKCARD for idxs in range(len(tablow))]
        
        colv = list(zip(*tablow))   
        
        for idc,colu in enumerate(colv):    #        all0=True
            colo = []
            colp=[str(w) for w in colu]  # fixed bug:
            for valk in colp:     # 1used self.tablown[1:] the other didnt
                colo.append(valk) 
            if colo == EMPTYCOL:            #for ids,colt in enumerate(colu[1:]):            #    if colt == ':            #        all0=False            #        break            #if all0:
                blankcolumns+=1
                if first0Col == -1:
                    first0Col = idc
        return blankcolumns, first0Col

    def FFCard(self, minp):
        moapt=0,0;doapt=0,0
        if minp[1] in list(SYMBOL.keys()):
            numOf0InFC, first0InFC = self.findNoOf0FC()
            if first0InFC > -1:
                moapt, doapt = self.getCardLocation(minp, 'dinp')
                doapt = [0,first0InFC]#; mou=0; moo=0
                if str(self.tablown[moapt[0]+1][moapt[1]]) != BLANKCARD and\
                                    moapt[0] != 0:
                    self.moveing = False
                    self.reasonx.append('moapt+1!BLANK')
                elif self.moveing:
                    self.moveCCCard(moapt, doapt, f_or_gf=True)
                '''
                mou,moo=card(card.rank_list.index(minp[0]),card.suit_list.index(minp[1])).get_position()
                newCard=card(mou,moo).set_position(0,first0InFC)
                self.tablown[0][first0InFC]=newCard
                for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        self.posdictNEtablo(minp, mou, moo, moapt)
                        self.tablown[doapt[0]][doapt[1]]=self.tablown[mou][moo]
                        self.tablown[mou][moo]=BLANKCARD
                        self.posdict.update({minp:[0,first0InFC]})
                        break'''
            else:
                self.moveing = False
        else:
            self.moveing = False

           # moapt,doapt

    def GGCard(self, minp):
        #self.validGG=False
        listsuit=list(SYMBOL.keys())
        if minp[1] in listsuit:
        #if minp[1] in list(SYMBOL.keys()):    rank=A t[0][f]=BLANKCARD
            foundation =  listsuit.index(minp[1]) + 4     #-1 for the x in listsuit
            if self.verbose and not self.winning:
                rp(f'{foundation=} = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit')
            moveCard   = validrank.index(minp[0])
            if (moveCard == 0 and self.tablown[0][foundation]==BLANKCARD) or \
                str(self.tablown[0][foundation])[0] == validrank[moveCard -1]:
                moapt, doapt = self.getCardLocation(minp,'dinp')
                doapt = [0,foundation]
                if moapt[0] == 0 and moapt[1] in range(4,8):
                    self.moveing = False
                    self.reasonx.append('moapt=foundation')
                #valid 0-4 or +1 blank
                elif str(self.tablown[moapt[0]+1][moapt[1]]) != BLANKCARD and\
                                      moapt[0] != 0:
                    self.moveing = False
                    self.reasonx.append('moapt+1!BLANK')
                elif self.moveing:
                    self.moveCCCard(moapt, doapt, f_or_gf=True)
                '''
                for xxx,www in enumerate(self.tablown):
                    uuu=[str(qqq) for qqq in www]
                    if xxx==0: 
                        if minp in uuu[:4]:
                            yyy=uuu.index(minp)
                            self.posdictNEtablo(minp, xxx, yyy, [xxx,yyy])
                            self.tablown[xxx][yyy] = BLANKCARD
                            break
                    elif minp in uuu: 
                        yyy=uuu.index(minp)
                        self.posdictNEtablo(minp, xxx, yyy, [xxx,yyy])
                        self.tablown[xxx][yyy] = BLANKCARD
                        break
                
                #tempcard=cardA.stringToCard(minp)
#                if foundation not in range(4,8):
#                    raise Exception(f'{foundation=} Out of range(s/b 4-7)')
                self.moveCCCard(moapt, doapt, f_or_gf=True)
                
                self.tablown[0][foundation] = minp
                self.tablown[0][foundation] = card(card.rank_list.index(minp[0]),card.suit_list.index(minp[1]),0,foundation)
                self.posdict.update({minp:[0,foundation]})'''#self.validGG=True
        
    def ZZCard(self, minp):
        moapt=0,0;doapt=0,0        #nofoundation
        if minp[1] in list(SYMBOL.keys()):
            self.copytavl = dpcopy(self.tablown[1:])
            blankcolumns, first0Col = self.findNoOf0Cols(self.copytavl)
            if first0Col > -1:
                moapt, doapt = self.getCardLocation(minp,'dinp')
                doapt = [0, first0Col]#;    mou=0; moo=0
                '''
                for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=[mou,moo]'''
                if str(self.tablown[moapt[0]+1][moapt[1]]) != BLANKCARD and\
                                    moapt[0] != 0:
                    doapt = [0, first0Col]
                    moapt, doapt = self.handlemultimove(moapt, doapt)
                    '''break'''
#                else:
                    '''self.posdictNEtablo(minp, mou, moo, moapt)'''
                elif self.moveing:
                    self.moveCCCard(moapt, doapt)  
                    '''              
                    self.tablown[doapt[0]][doapt[1]]=self.tablown[mou][moo]
                    self.tablown[mou][moo]=BLANKCARD
                    self.posdict.update({minp:[0,first0Col]})
                    break'''
            else:
                self.moveing = False
        else:
            self.moveing = False

        # moapt,doapt
    
    def CCCard(self, minp, dinp):
        moapt=-1,0;    doapt=-1,0#;    dou=-1;    mou=-1
        test = False; errmsg=''    #        rules = rule()
        #if rules.validMove: '''# remove?!?!?!?!?!?!?!??!?!'''
        self.reasonx = rules.validNextCCCard(self.tablown,minp,dinp,test)
        if rules.movnotdifcolr_1 and self.verbose:
            rp(f'[red]{rules.movnotdifcolr_1Lit}[/]')
        if rules.validMove:
            self.moveing = True
            moapt, doapt = self.getCardLocation( \
            minp,  dinp)
            if str(self.tablown[doapt[0]+1][doapt[1]]) != BLANKCARD:
                self.moveing = False            
                errmsg = errmsg + (f'Dest!_: tablow[{doapt[0]+1}][{doapt[1]}]{str(self.tablown[doapt[0]+1][doapt[1]])}')
            elif str(self.tablown[moapt[0]+1][moapt[1]]) != BLANKCARD and\
                                  moapt[0] != 0:
                moapt, doapt = self.handlemultimove(moapt, doapt)
            elif self.moveing:
                self.moveCCCard(moapt, doapt)
        if len(self.reasonx)>0:
            rp(f'{[y for y in self.reasonx]}',sep='\n')
        if rules.noAbend: self.noAbend=True
        else:                self.noAbend=False
        return    self.moveing, self.noAbend
    
    def handlemultimove(self, moapt, doapt):
        self.cpytblwn = dpcopy(self.tablown)
        self.moapt = moapt; self.doapt = doapt; running = True
        '''YES!'''#test the firstone again???? 
        running, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
        running) #moapt[0] is row changing moapt[1] col !chg!
        #see if there ar enough empty spaces do first
        #we need lastofcol - firstocol empty spaces
        numOf0InFC, first0InFC = self.findNoOf0FC()
        blankcolumns, first0Col=self.findNoOf0Cols(dpcopy(self.tablown[1:]))
        firstorow = moapt[0]
        lastofrow = idx4lastcards[moapt[1]]
        if blankcolumns>1 and numOf0InFC >1: # 3                     2     4
            self.movnum = numOf0InFC+(numOf0InFC*blankcolumns)-1
        else: 
            self.movnum = numOf0InFC+blankcolumns + 1
        if lastofrow + 1 - firstorow > self.movnum:
            self.moveing = False
            self.reasonx.append(f'undermove!blank')
        for coltst in range(firstorow+1,lastofrow+1):
            if str(self.cpytblwn[coltst][moapt[1]]) not in nextCard[str(self.cpytblwn[coltst-1][moapt[1]])]:
                self.moveing = False
                self.reasonx.append(f'{str(self.cpytblwn[coltst][moapt[1]])} not in nextCard{self.cpytblwn[coltst-1][moapt[1]]}[{nextCard[str(self.cpytblwn[coltst-1][moapt[1]])]}]')
                break
        if self.moveing:
            zz=0
            for coltst in range(firstorow,lastofrow + 1):
                self.moveCCCard([coltst,moapt[1]],[doapt[0]+zz,doapt[1]])
                zz += 1
            pass#see if there ar enough empty spaces do first
        
        return  moapt, doapt
    def moveCCCard(self, moapt, doapt, f_or_gf=False):
        mou,moo=moapt;dou,doo=doapt
        if f_or_gf:
            self.tablown[dou][doo]=self.tablown[mou][moo]
            #if type(self.tablown[dou][doo]) != str:
            #    self.tablown[dou][doo].set_position(doapt[0],doapt[1])
            self.posdict.update({str(self.tablown[mou][moo]):[doapt[0],doapt[1]]})
            self.tablown[mou][moo]=BLANKCARD    #break  # moapt,doapt
            f_or_gf = False
        elif dou > -1 and mou > -1:
            self.tablown[dou+1][doo]=self.tablown[mou][moo]
            self.posdict.update({str(self.tablown[mou][moo]):[doapt[0]+1,doapt[1]]})
            self.tablown[mou][moo]=BLANKCARD    #break  # moapt,doapt
        
    def getCardLocation(self, minp, dinp):
        mou=-1;moo=0;dou=-1;doo=0;moapt=mou,moo;doapt=dou,doo
        self.cpytblwn1= dpcopy(self.tablown)
        for ii,qq in enumerate(self.cpytblwn1):# if minp in qq else 0]
            rr=[str(ss) for ss in qq]
            if minp in rr: 
                mou=ii; moo=rr.index(minp);moapt=mou,moo
                #sliceddict = { key: self.posdict[key] for key in self.posdict.keys() if key in ['AC', '2C', '3C', '4C', '5C', '6C', '7C']}
                #self.posdictNEtablo(minp, mou, moo, moapt)
                if dinp == 'dinp':        break    

            if dinp in rr and dinp != 'dinp': 
                dou=ii; doo=rr.index(dinp);doapt=dou,doo
                #self.posdictNEtablo(dinp, dou, doo, doapt)            #if dou > -1 and mou > -1:
            #    self.tablown[doapt[0]+1][doapt[1]]=self.tablown[mou][moo]
            #    self.tablown[mou][moo]=BLANKCARD
            #    break  # moapt,doapt
        return moapt, doapt

    def posdictNEtablo(self, minp, mou, moo, moapt):
        if self.posdict[minp][0] != mou or self.posdict[minp][1] != moo:
            rp(f'!?{minp=}: {self.posdict[minp]=}!={moapt=}',end=',        ')
            self.posdict.update({minp:[mou,moo]})
    

    def getidx4lastcards(self, running):
    #def getidx4lastcards( running):
        idx4lastcards=[-1,-1,-1,-1,-1,-1,-1,-1]
        cpyrow=[];cpytbl=[];strtemp=BLANKCARD
        for idxrow,rowLocked in enumerate(self.tablown):
            cpyrow=[]
            for idxcell,cell in enumerate(rowLocked):
                cpyrow.append(self.tablown[idxrow][idxcell])
                tablowtype= type(self.tablown[idxrow][idxcell]);cardtype = type(card)
                if type(self.tablown[idxrow][idxcell]) != type(strtemp)and idxrow!=0:
                    idx4lastcards[idxcell]=idxrow
            cpytbl.append(cpyrow)
        maxidxoflc = max(idx4lastcards)
        pass
        return running, idx4lastcards, maxidxoflc
    
#def putUpLastRowsOfCards( running, dek, tablow, idx4lastcards, rowidx):
#    '''we might not need idxlastcards'''
#    for column in range(8):
#        if idx4lastcards[column] > -1 and self.tablown[rowidx][column]!=BLANK_CARD:
#            reasonx=rules.validLastRowsOfCards(self.tablown, rowidx, column)
#            if rules.validMove:
#                pass
#
#    pass
#    return running, dek, tablow


    def testhandleWeWon(self, running):
        strtemp=BLANKCARD;lentablow=len(self.tablown)
        self.minplist=[];self.winning=True
        for errchk in range(4):
            if str(self.tablown[0][errchk]) != BLANKCARD:
                return True
        #addans = dpcopy(self.tablown)
        bsqlt3.insertCurrentTablownAsMoveid2(self.answall,dpcopy(self.tablown),tempmoveid=1)
        #############################################
        running, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
        running)
        maxidxoflc+=1 
        reversed11to1=reversed(range(1,maxidxoflc))   
        for rowidx in reversed(range(1,maxidxoflc)):
                for column in range(8):
                    if idx4lastcards[column] > -1 and \
                       str(self.tablown[idx4lastcards[column]][column])!=BLANKCARD:
                        self.minplist.append(str(self.tablown[idx4lastcards[column]][column]))
                        self.GGCard(str(self.tablown[idx4lastcards[column]][column]))
                running, idx4lastcards, maxidxoflc = self.getidx4lastcards(\
                running)
                bsqlt3.gamePrintTableau(self.answall[-4:], self.tablown, self.reasonx)
                self.reasonx = []
                self.handleWeWon()
                        #if self.validGG:
                        #    return False, tablow
 #          running, dek, tablow, idx4lastcards = self.getidx4lastcards(\
 #          running, dek, tablow)
        return running
    
    def handle_Re_Start(self, running, gameinit=False, restartLit=''):    
        '''self.gameinit=gameinit        
        if not gameinit:
            Tableau_dataclass.__init__()
            Tableau_dataclass.__post_init__()
            gameinit=True;self.gameinit=True
            pass'''
        print();print();reason=[]
        answer = brichp.getAnswer(question=f'Enter  Q|uit N|ewGame{restartLit}: ', reason=self.reasonx)
        lenAns=len(answer)
        self.typeposdict = type(self.posdict)
        if lenAns==1:
            answer=answer.upper()
            if answer in ["N","R","H","Q"]:
                if answer == "N":
                    running, dek = self.NewGame()
                if answer == "R":
                    dek = self.restartfromdb()
                if answer == "H":
                    webbrowser.open_new_tab('fc_help_mine.html')
                if answer == "Q":
                    running = False; dek = None; self.tablown = []
                if answer not in ['N','R','Q']:
                    running = True; dek = None; self.tablown = []
                #def restartFromSQLite3DB(self):    #    tablow=self.restart_fromdb()        #bsqlt3.gamePrintTableau(self.answall[-4:],tablow, self.reasonx)        
            '''for xx in outd:        
            ww=[]
            for yy in xx:
                if yy == BLANK_CARD:
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            self.tablown.append(ww)'''
        self.answall += answer.ljust(4)    
        try:
            if type(running)      == bool: pass
        except:            running = True
        try:
            if type(dek)          == list: pass
        except:            dek=[]
        try:
            if type(self.tablown) == list: pass
        except:            self.tablown = []
    
        return running, dek, self.tablown
    
    
    
    def handleWeWon(self):
        if self.tablown[1] == [BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD]:
            rp('minplist=')
            for ii,zz in enumerate(self.minplist):
                if ii%12 == 0 and ii > 0: 
                    print()
                rp(f'{COLORS[zz[1]]}{zz}[/]',end=', ')
            self.minplist=[];self.winning=False
            rp(f'{COLORS["C"]}WON![/] {COLORS['D']}WON![/] {COLORS["H"]}WON![/] {COLORS["S"]}WON![/] {COLORS["C"]}WON![/] {COLORS["D"]}WON![/] {COLORS["H"]}WON![/] {COLORS["S"]}WON![/]')    
            self.norow2leave = 3
            bsqlt3.deleteMostOfDbRowsAfterWin(self.gameid,self.norow2leave)
            running, dek, self.tmptablown = self.handle_Re_Start(True, True, restartLit='')



    def handleAnswer(self, running, dek, tablown):
        self.gtabl = dpcopy(tablown)
        self.posdicttype = str(type(self.posdict))
        answer = brichp.getAnswer( f'card, dest|FF,GG,Q: ',self.reasonx);lenAns=len(answer)
        self.moveing=True#try:    
        if lenAns < 1 or lenAns > 5:
            self.moveing = False
            self.reasonx.append("!<1|>5 input 2 short/long!")
            return True, dek, dpcopy(self.tablown)
        else:
            if lenAns == 1: #and answer == 'q':  running=False;rp('[gra]QUIT')
                running =self.handle1char(\
                running, answer)
                return running, dek, dpcopy(self.tablown)
            elif lenAns  >1 and lenAns<4:
                self.handle23char(answer, self.moveid)
                return running, dek, dpcopy(self.tablown)                
            elif lenAns == 4:
                minp=answer[:2];    dinp=answer[2:]
            elif lenAns == 5:
                minp=answer[:2];    dinp=answer[3:]
        
        if (lenAns == 4 or lenAns == 5) and self.moveing:
            running = self.handle4char(\
            running, minp, dinp)
        
        self.handleWeWon()

        if not running:
            bsqlt3.closeconn()
        
        return running, dek, dpcopy(self.tablown)

    def copyrow1ontbl(self):
        cpytbl=[]
        for irow,drow in enumerate(self.tablown):
            if irow > 0:
                cpytbl.append(drow)
        return cpytbl


    def handle1char(self, running, answer):
        '''handle Q(uit), \n
                  W(on),  \n
                  H(elp), \n
                  R(estart)\n
                  N(ew) GAME from scratch'''
        
        running                            = True
        answer=answer.upper()  if str(answer).isalpha() else answer
        self.answall += answer.ljust(4)    
        if answer == 'Q':
            running = False
        if answer == 'W':
            running =self.testhandleWeWon(\
            running)
        if answer == 'H':
            webbrowser.open_new_tab('fc_help_mine.html')
        if answer == 'N':
            self.restartCurrentGameFromScratch = False
            self.beginANewGame                 = True
        if answer == 'R':
            self.restartCurrentGameFromScratch = True
            self.beginANewGame                 = False
        return running
    def handle4char(self, running, minp, dinp):
        validMove=True;noAbend=False
        minp, dinp = self.makeInputUppercase(str(minp), str(dinp))
        self.answall += minp + dinp
        copytabl = dpcopy(self.tablown)
        errmsg = rules.noFoundationAsMover(copytabl, minp)
        if not rules.moveing:    self.moveing=False
        if dinp[1] == 'G' and self.moveing:
            dinp = 'GG';   self.GGCard(minp)
        elif dinp[1] == 'F' and self.moveing:
            dinp = 'FF';   self.FFCard(minp) 
        elif dinp[1] == 'Z' and self.moveing:
            dinp = 'ZZ';   self.ZZCard(minp) 
        elif self.moveing:
            validMove, noAbend = self.CCCard(minp, dinp) 
        #if dinp == 'GG' or dinp == 'FF' or dinp == 'ZZ':
        #tablow1, moapt1, doapt1 = dek.position(tablow1, minp, dinp)
        #rp(f'From cardsfrommsucse:{moapt1=}, {doapt1=}')
        #dek.richPrintTablow()
        #except:    rp('if len(answer) not in [1,4,5]:')
        self.reasonx.append(errmsg)
        if validMove and self.moveing and not noAbend:
            
            bsqlt3.gamePrintTableau(self.answall[-4:],self.tablown, self.reasonx)  #tablow = self.handleWeWon(tablow)
            self.reasonx = []    
        return running

    def handle23char(self, answer, currentMoveId):
        answer=answer[0].upper()+answer[1:]  if str(answer)[0].isalpha() else answer
        self.currentMoveId = currentMoveId
        self.noOfRows2Move=0; self.needAnswer=True
        self.answall += answer
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
        running=True
        if self.needAnswer:    #                    self.currentMoveId = currentMoveId
            running, self.moveing, self.tablown, self.reasonx, self.lTblRows = bsqlt3.handlebackfwd(running,self.tablown, answer,self.reasonx)
            if self.moveing:
                self.backfwd = True
                self.convertSQL2Tablo()
                bsqlt3.gamePrintTableau(self.answall[-4:], self.tablown, self.reasonx, False)
                self.reasonx = []

        return

    # def handlePost23char(self, running, self.tablown,  answer):
    #     return running, self.tablown

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
        dek = deck()
        self.convertSQL2Tablo(True)   
        bsqlt3.readAllRowsOnRestart()
        bsqlt3.gamePrintTableau(self.answall[-4:],self.tablown, self.reasonx)
        self.reasonx = []
        return dek

    '''def convertSQL2 Tablo(self):
        dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list;self.tablown=[]
        #with closing(sql3class.cursorSQL3) as cursor3:
        #gamer=game()
        self.tablown=[]
        qq=self.EMPTYROW
        self.tablown.append(qq)
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
            self.gameid,self.moveid,self.answall,self.lTblRows = bsqlt3.readlastrecord()
        #self.gameid+=1
        #self.moveid+=1
        #self.tablown = fromsql2tablo
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
    
        suit1=card.suit_list; rank1=card.rank_list;self.tablown=[]
        for xx in cardi:
            ww=[]
            for yy in xx:
                if yy == 'xx':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            self.tablown.append(ww)
        while len(self.tablown)<23:
            self.tablown.append([BLANKCARD for w in range(8)])
        for idxm,rown in enumerate(self.tablown):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    self.tablown[idxm][idxn] = BLANKCARD
        bsqlt3.gamePrintTableau(self.answall[-4:],self.tablown, self.reasonx)
        return dek,self.tablown,running'''

    def validdestempty(self):


        pass

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
        """ #rp(f'{len(self.tablown)=}')  
        nminp='';ndinp=''
        #nminp=minp[i].upper()  if str(minp[i]).isalpha() else minp[i] for i in range(2)
            
        ndinp = ''.join(dinp[i].upper() if str(dinp[i]).isalpha() else dinp[i] for i in range(2) )
        if self.verbose:
            rp(f'{minp=}==>{nminp=}    and   {dinp=}==>{ndinp=}')
        minp=minp[0].upper()+minp[1] if str(minp[0]).isalpha() else minp
        minp=minp[0]+minp[1].upper() if str(minp[1]).isalpha() else minp
        dinp=dinp[0].upper()+dinp[1] if str(dinp[0]).isalpha() else dinp 
        dinp=dinp[0]+dinp[1].upper() if str(dinp[1]).isalpha() else dinp
        return str(minp),str(dinp)
         
    