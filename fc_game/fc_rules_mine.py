from cards_msu_cse import Card, Deck



class Rules(object):


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
    
    
    
    
    '''
    def __init__(self) -> None:
        self.validMove=True
        self.movnotdifcolr_1 =False
        self.reason=['']
        self.lenname=0
        self.initPositionDict()

    def initPositionDict(self):
        self.posdic={k:[-1,-1] for k in self.validcard}        

    def getValidAnswer(self, answer):
        self.validAnswer = True; lenAnswer = len(answer);reason=''
        if lenAnswer < 1 or lenAnswer > 4:
            self.validAnswer = False
            reason +=(f"{answer} 2 long/short")
        elif lenAnswer == 1:
            answer = str(answer).upper()  if str(answer).isalpha() else answer
            if answer not in ['N','R','W','Q']:
                self.validAnswer = False
                reason +=(f"{answer} Wrong Answer")
        return self.validAnswer, answer, self.reason
    def noFoundationAsMover(self, tablow, minp):
        self.moveing = True
        #try:
        
        if minp[1] in self.vsuita:
        #if minp[1] in list(self.validsuit.keys):
            suitminp = self.vsuita.index(minp[1]) + 4
            if str(tablow[0][suitminp]) == self.BLANK:
                pass#
                #strFoundation=str(tablow[0][suitminp])
                #svr=self.validrank
            elif minp in str(tablow[0][suitminp]) or \
                self.validrank.index(minp[0]) < self.validrank.index(str(tablow[0][suitminp])[0]): 
                print(f'CANT MOVE{str(tablow[0][suitminp])} FROM FOUNDATION!!!!{self.validrank.index(minp[0])=} < {self.validrank.index(str(tablow[0][suitminp])[0])=}{str(tablow[0][suitminp])=}')    
                self.moveing = False
        else:
            self.moveing = False
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
            if minp not in self.validcard or dinp not in self.validcard:
                self.reason.append(f'{str(self.__qualname__)} Invalid Card(s):        {minp=}, {dinp=}: {self.validMove}')
                self.validMove = False
        except:
            self.reason.append(f'{str(__name__)} Invalid Card(s):        {minp=}, {dinp=}: {self.validMove}')
            self.validMove = False
            self.noAbend = True

        try:
            if dinp in self.ACES_TWOS:    
                self.reason.append(f'{str(__name__)} A and 2 cant be dest:    {dinp=} cant be {dinp[1]=}: {self.validMove}')
                self.validMove = False
        except:
            self.reason.append(f'{str(__name__)} A and 2 cant be dest:    {dinp=} cant be {dinp[1]=}: {self.validMove}')
            self.validMove = False
            self.noAbend = True

        try:
            if dinp in list(self.nextCard):
                if minp not in self.nextCard[dinp]:
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
        self.reason=[];suitlist1=self.vsuita#list(Rules.validsuit.keys)
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
  