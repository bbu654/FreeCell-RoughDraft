import cardsfrommsucse 
from cardsfrommsucse import Card as card
from cardsfrommsucse import Deck as deck
from            rich import print as rp
from rich.table      import Table
from rich.console    import Console
from fc_rules_mine   import Rules as rule
from fc_io_mine      import PrintItBBU as brichprt, SQLiteIO as bsqlite3
import fc_tableau_mine


tablClass=fc_tableau_mine.Tableau()
brichp=brichprt()
bsqlt3=bsqlite3()
BLANKCARD = ''
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
rp(f'{suitlit=}',sep=' ',end=', ')
if True:    
    output={}#nextCards
    for j in range(3,13+1):
        for k in range(2):
            output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
            output[j+(13*(k+2))] = [j-1, j+12]

    j=0;k=0; validsuit={'C':['D','H'],'S':['D','H'],\
                        'H':['C','S'],'D':['C','S']}
    nextCard = {}
    for vsuit in validsuit:
        for idx, vrank in enumerate(VALID_RANK[2:]):
            nextCard[vrank+vsuit]=[VALID_RANK[idx+1]+validsuit[vsuit][0],VALID_RANK[idx+1]+validsuit[vsuit][1]]
    rp(f'{nextCard=}{output=}',sep=' ',end=' ')
    nextCards={'3H':['2C','2S'],'4H':['3C','3S'],\
               '5H':['4C','4S'],'6H':['5C','5S'],\
               '7H':['6C','6S'],'8H':['7C','7S']}
    
def NewGame(dek=None):
    running=True
    if dek==None:
        dek = cardsfrommsucse.Deck(); dek.shuffle()
        tablow1=dek.newGame()
        deckE=dek
    else:
        deckE= deck(dek)
        tablow1=deckE.newGame()
    
    deckF= deckE.lister()
    #deckh=[]
    #for cardj in deckE.__deck:
    #    deckh.append(str(cardj))
    deckE.richPrintTablow()
    rp(f'{type(deckF)}, {deckE.pretty_print(8)}{tablow1=}')
    #deckA=str(dek); deckB=deckA.split(','); deckC=list(deckB)
    #blb=list((str(dek)).split(","))
    #rp(f'blb=list((str(dek)).split(","))={blb[22]=}')
    #rp(f'{[l for l in dek]}',sep=' ');
    zz=0;yy=[BLANKCARD for _ in range(8)]
    tablow = [];tablow.append(yy);rp(tablow)
    for rowr in range(22):
        yy=[]
        for colr in range(8):
            yy.append(deckF[zz] if zz <52 else BLANKCARD);zz+=1
        tablow.append(yy)    #HDSC   = ('♥','♦','♠','♣')
    selfgameid=1;selfmoveid=1;selfsep=', '# Create a new record
    selfrowstring= f" VALUES ({selfgameid}, {selfmoveid}, "
    selfvaluestr = f"INSERT INTO 'game' ('gameid', 'moveid', "
    for idx,rowf in enumerate(tablow):
        if idx == 22:
            selfrowstring += f"'{rowf}'); "
            selfvaluestr  += f"'row{idx}')"
        else:
            selfrowstring += f"'{str(rowf)}', "
            selfvaluestr  += f"'row{idx}', "
    sql = f"{selfvaluestr}{selfrowstring}"
    sqla=''.join(str(item) if item !='' else 'xx' for innerlist in tablow for item in innerlist )
    sqlb=[]
    for sqlridx,sqlrow in enumerate(tablow):
        sqlc=''
        if sqlridx ==0 or sqlrow != ['' for _ in range(8)]:
            for sqlcol in sqlrow:
                if sqlcol != '': 
                    sqlc+=str(sqlcol)
                else:
                    sqlc+='xx'
            sqlb.append(sqlc)
        else:
            continue
    selfgameid=1;selfmoveid=1;selfsep=', '# Create a new record
    selfrowstring= f" VALUES ({selfgameid}, {selfmoveid}, "
    selfvaluestr = f"INSERT INTO 'game' ('gameid', 'moveid', "
    for idx,rowf in enumerate(sqlb):
        if idx == len(sqlb)-1:
            selfrowstring += f"'{str(rowf)}');"
            selfvaluestr  += f"'row{idx}')"
        else:
            selfrowstring += f"'{str(rowf)}', "
            selfvaluestr  += f"'row{idx}', "
    sqld = f"{selfvaluestr}{selfrowstring}"
                
    print(f'{sqla=}{sqlb=}{sqld=}',sep=',') 
    return running,dek,tablow,tablow1
def getAnswer():
    question = f'card, dest|FF,GG,Q:'
    return input(question)
def testPrint(tablow):
    tview = Table(title='My FreeCell')
    for idy,row1 in enumerate(tablow):
        strRow=[BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD,BLANKCARD] #str4=zip(row1)        #str5=str4        str0=''
                    #0        1         2         3         4         5         6         7         8  
        for idx,col1 in enumerate(row1):
            if col1 == BLANKCARD:
                stra=f'[white]0[/]'                
            else:
                stra=f'{CLRSYM[col1[1]][0]}{col1[0]}{CLRSYM[col1[1]][1]}[/]'
            if idy==0:#strx=str(col1)    if col1 == BLANKCARD:    tview.add_column(f'[white]0[/]')    else:    tview.add_column(f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]')                    # tview.add_column(suitlit[idx])
                tview.add_column(stra)
            else:
                strRow[idx] += stra #    if col1 == BLANKCARD:    strRow[idx] += f'[white]0[/]'       else:    strRow[idx] += f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'  
        if row1 != EMPTYROW:
            tview.add_row(strRow[0],strRow[1],strRow[2],strRow[3],\
                          strRow[4],strRow[5],strRow[6],strRow[7])
    consol=Console()    
    consol.print(tview)
    return tablow

def GGCard(tablow, minp):
    listsuit=list(SYMBOL.keys())
    if minp[1] in listsuit:
    #if minp[1] in list(SYMBOL.keys()):    rank=A t[0][f]=BLANKCARD
        foundation =  listsuit.index(minp[1]) + 4     #-1 for the x in listsuit
        rp(f'{foundation=} = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit')
        moveCard   = VALID_RANK.index(minp[0])
        if (moveCard == 0 and tablow[0][foundation]==BLANKCARD) or \
            tablow[0][foundation][0] == VALID_RANK[moveCard -1]:
            for xxx,www in enumerate(tablow):
                if xxx==0: 
                    if minp in www[:4]:
                        tablow[xxx][www.index(minp)] = BLANKCARD
                        break
                elif minp in www: 
                    tablow[xxx][www.index(minp)] = BLANKCARD
                    break
            tablow[0][foundation] = minp
    return tablow

def findNoOf0FC():
    numOf0InFC=0; first0InFC=-1
    for ll in range(4):
        if tablow[0][ll] == BLANKCARD: 
            numOf0InFC += 1
            if first0InFC == -1:
                first0InFC = ll

    return numOf0InFC, first0InFC

def findNoOf0Cols(tablow):
    blankcolumns=0; first0Col=-1
    EMPTYCOL=[BLANKCARD for idxs in range(len(tablow)-1)]
    colv = list(zip(*tablow))   
    
    for idc,colu in enumerate(colv):    #        all0=True
        colo = []
        for valk in colu[1:]:
            colo.append(valk) 
        if colo == EMPTYCOL:            #for ids,colt in enumerate(colu[1:]):            #    if colt == ':            #        all0=False            #        break            #if all0:
            blankcolumns+=1
            if first0Col == -1:
                first0Col = idc
    return blankcolumns, first0Col


def FFCard(tablow,minp):
    moapt=0,0;doapt=0,0
    if minp[1] in list(SYMBOL.keys()):
        numOf0InFC, first0InFC = findNoOf0FC()
        if first0InFC > -1:
            doapt=0,first0InFC; mou=0; moo=0
            for ii,qq in enumerate(tablow):# if minp in qq else 0]
                if minp in qq: 
                    mou=ii; moo=qq.index(minp);moapt=mou,moo
                    tablow[doapt[0]][doapt[1]]=tablow[mou][moo]
                    tablow[mou][moo]=BLANKCARD
                    break
    return    tablow   # moapt,doapt

def ZZCard(tablow,minp):
    moapt=0,0;doapt=0,0
    if minp[1] in (SYMBOL.keys()):
        blankcolumns, first0Col = findNoOf0Cols(tablow)
        if first0Col > -1:
            doapt=1,first0Col; mou=0; moo=0
            for ii,qq in enumerate(tablow):# if minp in qq else 0]
                if minp in qq: 
                    mou=ii; moo=qq.index(minp);moapt=mou,moo
                    tablow[doapt[0]][doapt[1]]=tablow[mou][moo]
                    tablow[mou][moo]=BLANKCARD
                    break
    return    tablow   # moapt,doapt

def CCCard(tablow,minp,dinp):
    moapt=-1,0;    doapt=-1,0#;    dou=-1;    mou=-1
    test = True
    validCC = rule()
    if validCC.validMove:
        reason = validCC.validNextCCCard(tablow,minp,dinp,test)
        if validCC.movnotdifcolr_1:
            rp(f'[red]{validCC.movnotdifcolr_1Lit}[/]')
        if validCC.validMove:
            tablow,moapt,doapt = getCardLocation( \
            tablow, minp, dinp)
            tablow=moveCCCard(tablow, moapt, doapt)
        rp(f'{[y for y in reason]}',sep='\n')
    return    tablow 
def moveCCCard(tablow,moapt,doapt):
    mou,moo=moapt;dou,doo=doapt
    if dou > -1 and mou > -1:
        tablow[dou+1][doo]=tablow[mou][moo]
        tablow[mou][moo]=BLANKCARD    #break  # moapt,doapt
    return tablow
def getCardLocation(tablow, minp, dinp):
    mou=-1;moo=0;dou=-1;doo=0;moapt=mou,moo;doapt=dou,doo
    for ii,qq in enumerate(tablow):# if minp in qq else 0]
        if minp in qq: 
            mou=ii; moo=qq.index(minp);moapt=mou,moo
        if dinp in qq: 
            dou=ii; doo=qq.index(dinp);doapt=dou,doo
        
        #if dou > -1 and mou > -1:
        #    tablow[doapt[0]+1][doapt[1]]=tablow[mou][moo]
        #    tablow[mou][moo]=BLANKCARD
        #    break  # moapt,doapt
    return tablow,moapt,doapt
def handleAnswer(running,tablow,tablow1,dek):
    answer = getAnswer();lenAns=len(answer)
    #try:
    
    if lenAns not in [1,4,5]:
        rp("return False, BLANKCARD, BLANKCARD");running=False
    else:
        if lenAns == 1: #and answer == 'q':  running=False;rp('[gra]QUIT')
            running, tablow, tablow1, dek=handle1char(\
            running, tablow, tablow1, dek, answer)
            return running,tablow,tablow1,dek
        elif lenAns == 4:
            minp=answer[:2];    dinp=answer[2:]
        elif lenAns == 5:
            minp=answer[:2];    dinp=answer[3:]
    running,tablow,tablow1,dek = handle4char(\
    running,tablow,tablow1,dek,minp,dinp)
    return running,tablow,tablow1,dek
 
def handle1char(running,tablow,tablow1,dek,answer):
    '''handle Q(uit), \n
              W(on),  \n
              S(tart) this Game from scratch'''
    answer=answer.upper()  if str(answer).isalpha() else answer
    if answer == 'Q':
        running = False
    if answer == 'W':
        running,tablow,tablow1,dek=putSomeUp(\
        running,tablow,tablow1,dek)
    return running,tablow,tablow1,dek
def putSomeUp(running,tablow,tablow1,dek):
    winning=True;numOfMove2Foundation=0
    while winning:    #colh = list(zip(*tablow))
        lastnon0 = 0;rankl=VALID_RANK;suitl=list(SYMBOL.keys())
        for idx,colj in enumerate(list(zip(*tablow))):#0is0
            blankcolumns, first0Col = findNoOf0Cols(tablow[1:])
            if blankcolumns == 8:
                winning=False
                break
            lastnon0=BLANKCARD;lastidx=-1        #find the last non-zero !! Does it Foundation???
            #check if FCs will go up       #object of type 'reversed' has no len()
            reversedcolj = []
            for xx in reversed(colj):
                reversedcolj.append(xx)            
            if reversedcolj == [BLANKCARD for poiu in range(len(reversedcolj))]:
                pass
            else:
                for iey,xcv in enumerate(reversedcolj):
                    lln0=len(lastnon0)
                    if lastidx == -1 and xcv != BLANKCARD:
                        if xcv[0] in rankl and xcv[1] in suitl:
                            lastnon0 = xcv
                            lastidx  = iey
                if len(lastnon0) == 2 and lastidx<22:#if 2h
                    if lastnon0[0] == 'A':    
                        winning=False
                        break
                    sidx = suitl.index(lastnon0[1])
                    ridx = rankl.index(lastnon0[0])
                    foundation=tablow[0][sidx]
                    movecard=f'{rankl[ridx-1]}{lastnon0[1]}'
                    if movecard == foundation:
                        tablow[0][sidx]=lastnon0
                        tablow[22-lastidx][idx]=0
                        tablow=brichp.printTableau(tablow)

    return    running,tablow,tablow1,dek
def handle4char(running,tablow,tablow1,dek,minp,dinp):
    
    minp, dinp = makeInputUppercase(str(minp), str(dinp))
               
    if dinp[1] == 'G':
        dinp = 'GG';   tablow = GGCard(tablow, minp)
    elif dinp[1] == 'F':
        dinp = 'FF';   tablow = FFCard(tablow, minp) 
    elif dinp[1] == 'Z':
        dinp = 'ZZ';   tablow = ZZCard(tablow, minp) 
    else:
                       tablow = CCCard(tablow, minp, dinp) 
    #if dinp == 'GG' or dinp == 'FF' or dinp == 'ZZ':
    tablow1, moapt1, doapt1 = dek.position(tablow1, minp, dinp)
    rp(f'From cardsfrommsucse:{moapt1=}, {doapt1=}')
    dek.richPrintTablow()
    #except:    rp('if len(answer) not in [1,4,5]:')
    tablow = brichp.printTableau(tablow)                    
    rp(f'{CLRSYM["C"][0]}WON![/] {CLRSYM['D'][0]}WON![/] {CLRSYM["H"][0]}WON![/] {CLRSYM["S"][0]}WON![/] {CLRSYM["C"][0]}WON![/] {CLRSYM["D"][0]}WON![/] {CLRSYM["H"][0]}WON![/] {CLRSYM["S"][0]}WON![/]')

    return running,tablow,tablow1,dek

def makeInputUppercase(minp, dinp):
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
     
def runit(running,tablow,tablow1,dek):        
    '''run game logic'''
    testtablow = ['8C', 'TD', 'KD', 'QD', 'TH', 'QC', '9H', '8S', '5S', 
'4H', '2C', 'QS', '8H', '3C', 'JS', '6H', 'KH', 'JC', 'JH', '2D', '3S', '6C', '7S', '2S', 'KC', '7D', '6D', '5D', '4D', 'KS', '3D', 'AC',  
'2H', '5C', '6S', '7C', '3H', 'QH', '9C', '9S', '5H', 'AS', '9D', 'JD', '4C', 'AD', 'AH', '8D', 'TC', '7H', '4S', 'TS']
    if running:
        if dek == None or tablow == None or tablow1 == None:
            running,dek,tablow,tablow1 = NewGame(dek)
    #rp(f'{COLORS[tablow[2][2][-1]]}{tablow[2][2][:-1]}{SYMBOL[tablow[2][2][-1]]}[/]{tablow[2][2]}')
    #brichprt1=brichprt()
        tablow = brichp.printTableau(tablow)
        running,tablow,tablow1,dek = handleAnswer(running,tablow,tablow1,dek)
        return running,tablow,tablow1,dek
if __name__ == "__main__":
    running,dek,tablow,tablow1 = NewGame()
    while running:
        if startOver:
            running=True;dek=None;tablow=None;tablow1=None
            running,tablow,tablow1,dek = runit(running,tablow,tablow1,dek)
        running,tablow,tablow1,dek = runit(running,tablow,tablow1,dek)        