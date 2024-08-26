from cards_msu_cse import Card, Deck
from rich          import print as rp
from fc_cons_New1  import *
from copy          import deepcopy as dpcopy



class Rules(object):

    ''' 
    output={}#nextCards not any more
    for j in range(3,13+1):
        for k in range(2):
            output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
            output[j+(13*(k+2))] = [j-1, j+12]
    
    j=0;k=0; validsuit={'C':['D','H'],'S':['D','H'],\
                        'H':['C','S'],'D':['C','S']}
    
    validrank=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    vsuita=['C','D','H','S']
    validcard=[]
    for s in vsuita:
        for r in validrank:
            validcard.append(f'{r}{s}')
    
    posdic={k:[-1,-1] for k in validcard}    
    #posdic.update({'AS':[mou,moo]})
    #posdic.update({'2S':doapt})
    BLANK='__'
    nextCard = {}
    for vsuit in validsuit:
        for idx, vrank in enumerate(validrank[2:]):
            nextCard[vrank+vsuit]=[validrank[idx+1]+validsuit[vsuit][0],validrank[idx+1]+validsuit[vsuit][1]]
    ACES_TWOS = ('AC','2C','AS','2S','AH','2H','AD','2D')
   
    
    
    
    
    '''
    def __init__(self) -> None:
        self.validMove=True
        self.movnotdifcolr_1 =False
        self.reason=['']
        self.lenname=0
        self.initPositionDict()

    def initPositionDict(self):
        self.posdic={k:[-1,-1] for k in validcard}        

    def getValidAnswer(self, answer):
        self.validAnswer = True; lenAnswer = len(answer);errmsg=''
        if lenAnswer > 0:    
            answer = ''.join(answer[i].upper() if str(answer[i]).isalpha() else answer[i] for i in range(lenAnswer) )
        if lenAnswer < 1 or lenAnswer > 4:
            self.validAnswer = False
            errmsg +=(f"{answer} 2 long/short")
        elif lenAnswer == 1:
            answer = str(answer).upper()  if str(answer).isalpha() else answer
            if answer not in ['N','R','W','H','Q']:
                self.validAnswer = False
                errmsg +=(f"{answer} !in NRWHQ")
        elif lenAnswer > 1 and lenAnswer < 4:
            if answer[0] not in ['B', 'F']:
                self.validAnswer = False
                errmsg +=(f"{answer} ! B/F")
        elif lenAnswer in range(4,6):
            if answer[:2] not in validcard:
                self.validAnswer = False
                errmsg +=(f"{answer} 1st2 ! Card")
            elif answer[-1] not in ['F', 'G', 'Z'] and \
                 answer[-2:] not in validcard:# or last2     \
                 #self.noFoundationAsMover(Tableau.tablown,answer[-2:]):
                 self.validAnswer = False
                 errmsg +=(f"{answer} 1st2 ! Card")

        return self.validAnswer, answer, errmsg

    '''
    
        s1 = 'Geeksforgeeks'
        s2 = 'ksforgeeks'
        s3 = 'forgeeks'
        s4 = 'geeks'
          
        print(f'{s1 : >13}') 
        print(f'{s2 : >13}') 
        print(f'{s3 : >13}') 
        print(f'{s4 : >13}') 
        
        Output :
        
        Geeksforgeeks
           ksforgeeks
             forgeeks
                geeks
        
    def getFGZ_Dest(self, minp, dinp):
        doapt=[0,0]; self.moveing = False
        if dinp[1] == "F":
            FFnumOf0InFC, first0InFC = Tableau.findNoOf0FC()
            if first0InFC > -1:
                doapt = [0,first0InFC]
                self.moveing = True
        elif dinp[1] == "G":
            foundation =  vsuita.index(minp[1]) + 4     #-1 for the x in listsuit
            if self.verbose and not self.winning:
                rp(f'{foundation=} = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit')
            moveCard   = validrank.index(minp[0])
            if (moveCard == 0 and self.tablown[0][foundation]==BLANKCARD) or \
                str(self.tablown[0][foundation])[0] == validrank[moveCard -1]:
                doapt = [0, foundation]
                self.moveing = True
        elif dinp[1] == "Z":
            self.copytavl = dpcopy(self.tablown[1:])
            blankcolumns, first0Col = self.findNoOf0Cols(self.copytavl)
            if first0Col > -1:
                doapt = [1,first0Col]
                self.moveing = True


        return doapt
        '''


    def noFoundationAsMover(self, tablow, minp):
        self.moveing = True; global errmsg
        if len(errmsg) < 1: errmsg=''
        #try:
        
        if minp[1] in vsuita:
        #if minp[1] in list(self.validsuit.keys):
            suitminp = vsuita.index(minp[1]) + 4
            if str(tablow[0][suitminp]) == BLANKCARD:
                pass#
                #strFoundation=str(tablow[0][suitminp])
                #svr=self.validrank
            elif minp in str(tablow[0][suitminp]) or \
                validrank.index(minp[0]) < validrank.index(str(tablow[0][suitminp])[0]): 
                errmsg=f"CANT MOVE '{str(tablow[0][suitminp])}' FROM FOUNDATION!!!!"# Indexes{validrank.index(minp[0])} < {validrank.index(str(tablow[0][suitminp])[0])}"
                self.moveing = False
        else:
            self.moveing = False
        return errmsg
        #except:
        #    self.moveing = False#;self.noAbend=True;self.validMove=False
        #return self.moveing, self.noAbend, self.validMove
    def validNextCCCard(self,tablow,minp,dinp,test=False):
        self.reason=[]
        for char in str(__name__):
            self.lenname+=1
        #moapt=0,0;doapt=0,0
        self.validMove = True;self.noAbend = False
        self.CCvalidNextCCCardLit = [f'validNextCCCard is next card valid?']
        #self.reason.append(self.CCvalidNextCCCardLit)
        try:
            if dinp[1] == 'F' or dinp[1] == 'G' or dinp[1] == 'Z':
                self.reason.append(f'{str(__name__)} and dinp[1] cant be {dinp[1]}: {self.validMove}')
                self.validMove = False
                disl     = f'{Rules.validNextCCCard.__name__}'
        except:
                self.noAbend = True
                self.reason.append(f'{str(__name__)} and dinp[1] cant be {dinp[1]}: {self.validMove}')
                self.validMove = False
                disl     = f'{Rules.validNextCCCard.__name__}'

        try:
            if minp not in validcard or dinp not in validcard:
                self.reason.append(f'{str(self.__qualname__)} Invalid Card(s):        {minp=}, {dinp=}: {self.validMove}')
                self.validMove = False
        except:
            self.reason.append(f'{str(__name__)} Invalid Card(s):        {minp=}, {dinp=}: {self.validMove}')
            self.validMove = False
            self.noAbend = True

        try:
            if dinp in ACES_TWOS:    
                self.reason.append(f'{str(__name__)} A and 2 cant be dest:    {dinp=} cant be {dinp[1]=}: {self.validMove}')
                self.validMove = False
        except:
            self.reason.append(f'{str(__name__)} A and 2 cant be dest:    {dinp=} cant be {dinp[1]=}: {self.validMove}')
            self.validMove = False
            self.noAbend = True

        try:
            if dinp in list(nextCard):
                if minp not in nextCard[dinp]:
                    self.movnotdifcolr_1Lit = f'{str(__name__)} mover not diff color/-1  {dinp=} cant be {dinp[1]=}: {self.validMove}'
                    self.reason.append(self.movnotdifcolr_1Lit)
                    self.movnotdifcolr_1 =True
                    if not test:
                        self.validMove = False
        except:
            self.noAbend = True
            if not test:
                self.validMove = False
            self.movnotdifcolr_1Lit = f'{str(__name__)} mover not diff color/-1  {dinp=} cant be {dinp[1]=}: {self.validMove}'
            self.reason.append(self.movnotdifcolr_1Lit)
            self.movnotdifcolr_1 =True

        return self.reason

    def validLastRowsOfCards(self, tablow, rowidx, column):
        self.reason=[];suitlist1=vsuita#list(Rules.validsuit.keys)
        self.validMove = True
        self.validLastRowsOfCardsLit = [f'validLastRowsOfCards: put card into foundation?']
        self.reason.append(self.validLastRowsOfCardsLit)
        cell=str(tablow[rowidx][column]);aceidx=suitlist1.index(cell[1]) + 4
        str(tablow[0][aceidx])[0]
        if cell == '0' :
            pass  #cell1='C'
        elif cell[1]:#cell1=suit, need index of correct ACE and rank
           tablow[rowidx][column] 
        return tablow, rowidx, column
  