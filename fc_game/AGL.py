import random,re
from rich import print as rp
import rich.prompt
from rich.table import Table
from rich.console import Console
colors = ('[red]','[bright_magenta]','[bright_green]','[blue]')
HDSC   = ('♥','♦','♠','♣')
validSuits = ['H','D','S','C','F','G','Z']
validAceMove = ['HH','DD','SS','CC']
startOver = False
def pop(sdeck=[]):
    output={}
    for j in range(3,13+1):
        for k in range(2):
            output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
            rp(f'output[{j+(13*k)}] == {j+(13*2)-1}, {j+(13*3)-1}',end=',        ')
            output[j+(13*(k+2))] = [j-1, j+12]
            print(f'output[{j+(13*(k+2))}] == {j-1}, {j+12}',end=',        ')
        print()        
    #print(sorted(output))
    for t,i in enumerate(sorted(output)):
            if t%8 == 0 and t != 0:
                 print()
            rp(f"{i}: {output[i]}",end=', ')
    
    
    q=(1,2,14,15,27,28,40,41);print()
    for z in range(1,53):
         if z not in q:
              print(f'{z}: {output[z]}',end=", ")
         if z%10 == 0 and z != 0:
              print()   
    
    suitlit = ['[white]0[/]']; suitlit1 = ['[white]0[/]']
    heart= [hy for hy in range(1,14)];print()      #♥
    diamond = [dy for dy in range(14,27)];print()  #
    spade = [sy for sy in range(27,40)];print()    #
    club = [cy for cy in range(40,53)];print()     #♣
    c0 = colors[0]; c1 = colors[1]; c2 = colors[2]; c3 = colors[3]
    s0 = HDSC[0];   s1 = HDSC[1];   s2 = HDSC[2];   s3 = HDSC[3]
    for at in range(4):
        for au in range(1,14):
            if au == 1:
                rp(f"{colors[at]}A{HDSC[at]}[/]:0{au}",end=', ')
                suitlit1.append(f'{colors[at]}A{HDSC[at]}[/]')    
            elif au == 10:
                rp(f"{colors[at]}T{HDSC[at]}[/]:{au}",end=', ')
                suitlit1.append(f'{colors[at]}T{HDSC[at]}[/]')
            elif au == 11:
                rp(f"{colors[at]}J{HDSC[at]}[/]:{au}",end=', ')
                suitlit1.append(f'{colors[at]}J{HDSC[at]}[/]')
            elif au == 12:
                rp(f"{colors[at]}Q{HDSC[at]}[/]:{au}",end=', ')
                suitlit1.append(f'{colors[at]}Q{HDSC[at]}[/]')
            elif au == 13:
                rp(f"{colors[at]}K{HDSC[at]}[/]:{au}",end=', ')
                suitlit1.append(f'{colors[at]}K{HDSC[at]}[/]')
            else:
                rp(f"{colors[at]}{au}{HDSC[at]}[/]:0{str(au)}",end=', ')
                suitlit1.append(f'{colors[at]}{str(au)}{HDSC[at]}[/]')
        print()
    for hu,hv in enumerate(heart):
        if hv == 1:       #01,14,27,40
            rp(f"{c0}A{s0}[/]:0{hv}",end=', ');suitlit.append(f'{c0}A♥[/]')
        elif hv == 10:    #10.23,36,49
            rp(f"{c0}T{s0}[/]:{hv}",end=', ');suitlit.append(f'{c0}T♥[/]')
        elif hv == 11:    #11.24,37,50
            rp(f"{c0}J{s0}[/]:{hv}",end=', ');suitlit.append(f'{c0}J♥[/]')
        elif hv == 12:    #12.25,38,51
            rp(f"{c0}Q{s0}[/]:{hv}",end=', ');suitlit.append(f'{c0}Q♥[/]')
        elif hv == 13:    #13.26,39,52
            rp(f"{c0}K{s0}[/]:{hv}",end=', ');suitlit.append(f'{c0}K♥[/]')
        else:
            rp(f"{c0}{hu+1}♥[/]:0{hv}",end=', ');suitlit.append(f'{c0}'+str(hu+1)+'♥[/]')
    #print(suitlit)    
    for du,dv in enumerate(diamond):
        if dv == 14:
            rp(f"[red]A♦[/]:{dv}",end=', ');suitlit.append('[red]A♦[/]')
        elif dv == 23:
            rp(f"[red]T♦[/]:{dv}",end=', ');suitlit.append('[red]T♦[/]')
        elif dv == 24:
            rp(f"[red]J♦[/]:{dv}",end=', ');suitlit.append('[red]J♦[/]')
        elif dv == 25:
            rp(f"[red]Q♦[/]:{dv}",end=', ');suitlit.append('[red]Q♦[/]')
        elif dv == 26:
            rp(f"[red]K♦[/]:{dv}",end=', ');suitlit.append('[red]K♦[/]')
        else:
            rp(f"[red]{du+1}♦[/]:{dv}",end=', ');suitlit.append('[red]'+str(du+1)+'♦[/]')
    for su,sv in enumerate(spade):
        if sv == 27:
            rp(f"[black]A♠[/]:{sv}",end=', ');suitlit.append('[black]A♠[/]')
        elif sv == 36:
            rp(f"[black]T♠[/]:{sv}",end=', ');suitlit.append('[black]T♠[/]')
        elif sv == 37:
            rp(f"[black]J♠[/]:{sv}",end=', ');suitlit.append('[black]J♠[/]')
        elif sv == 38:
            rp(f"[black]Q♠[/]:{sv}",end=', ');suitlit.append('[black]Q♠[/]')
        elif sv == 39:
            rp(f"[black]K♠[/]:{sv}",end=', ');suitlit.append('[black]K♠[/]')
        else:
            rp(f"[black]{su+1}♠[/]:{sv}",end=', ');suitlit.append('[black]'+str(su+1)+'♠[/]')
    for cu,cv in enumerate(club):
        if cv == 40:
            rp(f"[black]A♣[/]:{cv}",end=', ');suitlit.append('[black]A♣[/]')
        elif cv == 49:
            rp(f"[black]T♣[/]:{cv}",end=', ');suitlit.append('[black]T♣[/]')
        elif cv == 50:
            rp(f"[black]J♣[/]:{cv}",end=', ');suitlit.append('[black]J♣[/]')
        elif cv == 51:
            rp(f"[black]Q♣[/]:{cv}",end=', ');suitlit.append('[black]Q♣[/]')
        elif cv == 52:
            rp(f"[black]K♣[/]:{cv}",end=', ');suitlit.append('[black]K♣[/]')
        else:
            rp(f"[black]{cu+1}♣[/]:{cv}",end=', ');suitlit.append('[black]'+str(cu+1)+'♣[/]')
    #print('suitlit:')
    outa=[[0,0,0,0,0,0,0,0]]
    if not startOver:
        sdeck = [qw for qw in range(1,53)]
        print(f'{sdeck=}')
        random.shuffle(sdeck)
        print(f'{sdeck=}')
    iower=''
    try:
        if sdeck:
            iower='ok'
    except:
        rp(f'{iower} sdeck doesnt exist'    )
    running=True
   
    cdeck = []
    #   above is init    below is running
    
    for s in sdeck:
        cdeck.append(suitlit1[s])
    print(cdeck)
    ic=-1
    
    for row in range(22):
        outo=[]
        for col in range(8):
            ic += 1
            if ic < 52:
                outo.append(sdeck[ic])
            else:
                outo.append(0)
        outa.append(outo)
    #Py2Dlist = [sdeck[(ic:=ic+1)] if ic < 51 else 0 for j in range(8) for i in range(22) ]
    #rp(f'{Py2Dlist=}')
    rp(outa)
    ksdj=0
    ksdj=31
    mr=7;mc=3;dr=7;dc=0
    
    for a,b in enumerate(cdeck):        #if a%7 == 0 and a == 7:        #    print()
        if a%8 == 0:                    # and a > 8:
            print() 
        rp(b if not (b=='0') else '',end=',')
    return running, output, suitlit1, sdeck, outa, q
    #   above is init    below is running
def weWon(running, output, suitlit1, sdeck, outa, q):
    weWonr=False;putSomeUp=False;num0cols=find0columns(outa)
    if num0cols > 1:
        putSomeUp=True  
    if sum(outa[0][:4])==0 and num0cols > 2:
        weWonr=True
    fjkk=f'Check to see if game is won with freecell solver'
    return weWonr, putSomeUp, running, output, suitlit1, sdeck, outa, q

def find0columns(outa):
    colv = list(zip(*outa))   
    blankcolumns=0
    for colu in colv:
        if(sum(colu[1:]))==0:
            blankcolumns+=1
    return blankcolumns
def rpit(  running, output, suitlit1, sdeck, outa, q):
    cardc = {0:'🂠',
             1:'[red]🂱[/]',   2:'[red]🂲[/]',   3:'[red]🂳[/]',   4:'[red]🂴[/]',   5:'[red]🂵[/]',   6:'[red]🂶[/]',   7:'[red]🂷[/]',   8:'[red]🂸[/]',   9:'[red]🂹[/]',  10:'[red]🂺[/]',  11:'[red]🂻[/]',  12:'[red]🂼[/]',  13:'[red]🂽[/]',
            14:'[red]🃁[/]',  15:'[red]🃂[/]',  16:'[red]🃃[/]',  17:'[red]🃄[/]',  18:'[red]🃅[/]',  19:'[red]🃆[/]',  20:'[red]🃇[/]',  21:'[red]🃈[/]',  22:'[red]🃉[/]',  23:'[red]🃊[/]',  24:'[red]🃋[/]',  25:'[red]🃌[/]',  26:'[red]🃍[/]',
            27:'[black]🂡[/]',28:'[black]🂢[/]',29:'[black]🂣[/]',30:'[black]🂤[/]',31:'[black]🂥[/]',32:'[black]🂦[/]',33:'[black]🂧[/]',34:'[black]🂨[/]',35:'[black]🂩[/]',36:'[black]🂪[/]',37:'[black]🂫[/]',38:'[black]🂬[/]',39:'[black]🂭[/]',
            40:'[black]🃑[/]',41:'[black]🃒[/]',42:'[black]🃓[/]',43:'[black]🃔[/]',44:'[black]🃕[/]',45:'[black]🃖[/]',46:'[black]🃗[/]',47:'[black]🃘[/]',48:'[black]🃙[/]',49:'[black]🃚[/]',50:'[black]🃛[/]',51:'[black]🃜[/]',52:'[black]🃝[/]'}
    rp(f'[red]{[cardc[x] for x in range(1,27)]}[/]')
    rp(f'[black]{[cardc[x] for x in range(27,53)]}[/]')
    coly=[[outa[xu][xt] for xu in range(22)] for xt in range(8)]
    
    #col0=[outa[xs][0] for xs in range(22)]
    #col7=[outa[xs][7] for xs in range(22)]    #     colx=[]
    #colx.append(col0);colx.append(col7)    rp(colx);
    rp(f'{coly}');    ct=0
    for ex in range(22):
        for fx in range(8):
            if ct%8 == 0:                    # and a > 8:
                print() 
            rp(f'{cardc[outa[ex][fx]]}',end=', ')  #rp(b if not (b=='0') else '',end=',')
            ct+=1

    table1 = Table(title="Star Wars Movies")
    
    table1.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table1.add_column("Title", style="magenta")
    table1.add_column("Box Office", justify="right", style="green")
    
    table1.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table1.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table1.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table1.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
    rp(f'{outa=}    colh:')#\n{colh[rw] for rw in colh}')#rp(table1)
    colh = list(zip(*outa))
    for rw in colh:    
        rp(rw)
 
    #above is init     below is rpit
    gameview = Table(title='Freecell')
    #for qe in range(8):
    #   gameview.add_column('')
    for idy,row1 in enumerate(outa):
        #str4=zip(row1)        #str5=str4
        str0='';str1='';str2='';str3='';str4=''
        str5='';str6='';str7=''
        for idx,col1 in enumerate(row1):
            if idy==0:#strx=str(col1)
                gameview.add_column(suitlit1[col1])
            else:
                if idx == 0:
                    str0=f'{suitlit1[col1]}'
                elif idx == 1:
                    str1+=f'{suitlit1[col1]}'
                elif idx == 2:
                    str2+=f'{suitlit1[col1]}'
                elif idx == 3:
                    str3+=f'{suitlit1[col1]}'
                elif idx == 4:
                    str4+=f'{suitlit1[col1]}'
                elif idx == 5:
                    str5+=f'{suitlit1[col1]}'
                elif idx == 6:
                    str6+=f'{suitlit1[col1]}'
                elif idx == 7:
                    str7+=f'{suitlit1[col1]}'
        if sum(row1) > 0:
            gameview.add_row(str0,str1,str2,str3,str4,str5,str6,str7)
    consol=Console()    
    consol.print(gameview)

    return  running, output, suitlit1, sdeck, outa, q
def putSomeUp(running, output, suitlit1, sdeck, outa, q):
    colh = list(zip(*outa))
    lastnon0 = 0
    for idx,colj in enumerate(colh):#0is0
        lastnon0=0;lastidx=0        #find the last non-zero !! Does it Foundation???
        for iey,xcv in enumerate(reversed(colj)):
            if lastnon0>0:
                continue
            if xcv > 0:
                lastnon0 = int(xcv)
                lastidx  = iey
        if lastnon0 > 0 and lastidx<22:
            if lastnon0-1 in outa[0][4:]:
                #running, output, suitlit1, sdeck, outa, q = rpit(running, output, suitlit1, sdeck, outa, q)
                gidx = outa[0].index(lastnon0-1)
                outa[0][gidx]=lastnon0
                outa[22-lastidx][idx]=0
                running, output, suitlit1, sdeck, outa, q = rpit(\
                running, output, suitlit1, sdeck, outa, q)
    return running, output, suitlit1, sdeck, outa, q
def movit( running, output, suitlit1, sdeck, outa, q, minp, dinp):
    if sum(outa[0]) > 0:
        pass
    m0=minp[0];    m1=minp[1];    d0=dinp[0];    d1=dinp[1]
    if m1=='F' or m1=='G' or d1=='F' or d1=='G':
        if (d1=='F' and outa[0][d0]==0) or (d1=='G' and outa[0][d0]==0 and m0=='A'):
            piuy=[i for i, x in enumerate(outa) if x == minp]
            poi=piuy[0];roi=piuy[1]
            outa[0][d0] = outa[poi][roi]
            outa[poi][roi]=0
        #if (d1=='G' and outa[0][d0]==0 and m0=='A'):
        #    cuiy=[i for i, x in enumerate(outa) if x == minp]
        #    coi=cuiy[0];ooi=cuiy[1]
        #    outa[0][d0] = outa[coi][ooi]
        else:
            piuy=[i for i, x in enumerate(outa) if x == minp]
            poi=piuy[0];roi=piuy[1]
            outa[0][d1+1] = outa[poi][roi]
            outa[poi][roi]=0
    else:
        if outa[d0+1][d1] == 0:
            outa[d0+1][d1] = outa[m0][m1]
            outa[m0][m1]   = 0
    return  running, output, suitlit1, sdeck, outa, q, minp, dinp
def readt(  running, output, suitlit1, sdeck, outa, q, minp, dinp):
    minp = '9C';dinp = '0F'
    questions = 'Quit, Move From: (comma), GoTo Dest: '
    spliters = ',|.| '
    #minp, dinp =  input(questions).split(' ')
    answer = input(questions)
    try:
        if ',' in answer:
            minp,dinp = answer.split(',')
        elif '.' in answer:
            minp,dinp = answer.split('.')
        elif ' ' in answer:
            minp,dinp = answer.split(' ')
    except :
        rp(f'we just got an exception!')
    return  running, output, suitlit1, sdeck, outa, q, minp, dinp
def chgX2symbol(minp, dinp, mino, dino, mii, dii):
    if minp[1]=='H':
        mino =   f'{colors[0]}{minp[0]}{HDSC[0]}[/]'
    if minp[1]=='D':
        mino =   f'{colors[1]}{minp[0]}{HDSC[1]}[/]'
    if minp[1]=='S':
        mino =   f'{colors[2]}{minp[0]}{HDSC[2]}[/]'
    if minp[1]=='C':
        mino =   f'{colors[3]}{minp[0]}{HDSC[3]}[/]'
    if minp[1]=='F' or minp[1] == 'G':
        mino = f'[white]{minp}[/]'
    if dinp[1]=='H':
        dino =   f'{colors[0]}{dinp[0]}{HDSC[0]}[/]'
    if dinp[1]=='D':
        dino =   f'{colors[1]}{dinp[0]}{HDSC[1]}[/]'
    if dinp[1]=='S':
        dino =   f'{colors[2]}{dinp[0]}{HDSC[2]}[/]'
    if dinp[1]=='C':
        dino =   f'{colors[3]}{dinp[0]}{HDSC[3]}[/]'
    if dinp[1]=='F' or dinp[1] == 'G' or dinp[1]=='Z':
        dino = f'[white]{dinp}[/]'
        mii=0;dii=int(dinp[0])
    
    return minp, dinp, mino, dino, mii, dii
def multiMove( validMove, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt):
    countlenofMoving=1
    tempdou=doapt[0]+1;doo=doapt[1]
    tempmou=moapt[0]+1;moo=moapt[1]
    for tou in range(tempmou,23):#Now chk next1
        if outa[tou][moo] > 0 and outa[tou][moo] not in q:
            if outa[tou][moo] not in output[outa[tou-1][moo]]:
                return False, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt
            else:
                countlenofMoving += 1
        else:
            break
    numof0 = getNumOf0(outa)
    if outa[tempdou][doo]>0:
        validMove=False
    elif countlenofMoving<=numof0:
        #do move;0 out the move from in outa
        mmm=int(moapt[0]);ooo=int(doapt[0])
        for puss in range(mmm,mmm+countlenofMoving+1):
            outa[tempdou][doo]=outa[puss][moo];tempdou += 1 #pass
            outa[puss][moo]=0
    else:
        pass
    return False, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt

def getNumOf0(outa):
    countof0fc = 0
    for ick in range(4):
        if outa[0][ick]==0:
            countof0fc += 1
    blankcolumns = find0columns(outa)
    numof0=0
    if blankcolumns>0 and countof0fc>0:
        numof0=1+(countof0fc*blankcolumns)
    else:
        numof0=countof0fc+blankcolumns
    return numof0
def validMov(validMove, output, suitlit1, sdeck, outa, q,minp, dinp, mino, dino, mii, dii, colh, moapt, doapt):
    #SKIP m if m == "F" or "G"
    if mino in suitlit1:
        mii = suitlit1.index(mino)
    try:
        if not mii:
            mii=0
    except:
        rp(f'mii doesnt exist')
    #SKIP d if d == "F" or "G"
    if dino in suitlit1:
        dii = suitlit1.index(dino)
    if not dii:
        dii=0
    try:
        if not dii:
            dii=0
    except:
        rp(f'dii doesnt exist')
    moapt=[0,0]; doapt=[0,0]
    dou = 0; mou= 0; validMove=False
    # xinp=dinp, minp; xino=dino, mino; moapt, doapt, dou, doo, mou, moo
    #if out1/2.index(dii/mii)=0 this doesnt work 
    #doi=[out2.index(dii) if dii in out2 else 0 for out2 in outa]
    

    if dinp[1]=='F' and 0 in outa[0][:4]: 
        dou=0;doo=outa[0][:4].index(0);doapt=[dou,doo] #int(A,T,J,Q,K)??????
    elif dinp[1]=='G' or dinp in validAceMove:#C is not in list AC 7G
        dou=0; doo = 4 + validAceMove.index(minp[1]);doapt=[mou,moo]
    elif dinp[1]=='Z'and find0columns(outa) > 0:
        dou=1;doo=int(dinp[0]);doapt=[dou,doo]
    else:
        for tout,sout in enumerate(outa):
            if dii in sout and dinp[1]!= 'F' and dinp[1]!='G':
                dou = tout
                doo = sout.index(dii)
                doapt=[dou,doo]
                break
    #doo = sum(doi);

    #moi=[out1.index(mii) if mii in out1 else 0 for out1 in outa]
    if minp[1]=='F' or minp[1]=='G': #Never happen
        mou=0;moo=int(dinp[0]);moapt=[mou,moo]    # WON'T WORK
    elif  dinp in validAceMove:
        mou=0; moo = 4 + validAceMove.index(minp[1]);doapt=[mou,moo]
        
    else:
        for uout,vout in enumerate(outa):
            if mii in vout:
                mou = uout
                moo = vout.index(mii)
                moapt = [mou,moo]
                break
    #moo = sum(moi);
    #moo=1
    #for iu,qe in enumerate(moi):
    #    if qe > 0:
    #        mou=iu
    #        break
    rp(f'row{mou=},col{moo=}',end=',    ')
    #for ov,wf in enumerate(doi):
    #    if wf > 0:
    #        dou=ov
    #        break
    rp(f'row{dou=},col{doo=}')
    if dinp[1]=='Z' and int(dinp[0]) < 8:
        qqq=colh[int(dinp[0])]

    if dinp[1] == 'G':    #Foundation A-K
        dl=int(dinp[0])
        if dl in range(4,8):
            if outa[0][dl] == 0 \
            or outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
                outa[0][dl]=outa[mou][moo]
                outa[mou][moo]=0
                validMove=False #pass# valid move
            else:
                validMove=False
            #elif outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
            #    outa[0][dl]=outa[mou][moo]
            #    outa[mou][moo]=0
            #    validMove=False    
    elif dinp[1]=='Z' and sum(qqq[1:])==0:
        outa[1][int(dinp[0])]= outa[mou][moo]
        outa[mou][moo]=0
        validMove=False
    elif dinp[1] == 'F':    #Free Cell
        dk=int(dinp[0])
        if dk in range(4):
            if outa[0][dk] == 0:
                outa[0][dk]=outa[mou][moo]#pass# valid move
                outa[mou][moo]=0
                validMove=False #Done already    if not validMove:
    elif dii in q or dii==0:
        rp(f'invalid dest{dii=}')
    elif outa[mou][moo] in output[dii]:
        if outa[mou+1][moo] > 0 and mou != 0:
             validMove, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt=multiMove( validMove, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt)
        #moapt=[mou,moo];doapt=[dou,doo]
        validMove=True
        rp(f'Valid Move: {outa[mou][moo]=} in {output[dii]=}{dii=}')
    else:
        rp(f'{outa[mou][moo]=} notin{output[dii]=}{dii=}')
    #TODO:#add showing cards validation of a col of cards
          #move card(s) ADD CLASS and __init__      #1F0A1    #1F0A1
    #rp(f'[red,align(center,width({6})]🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽[/]')
    return validMove, output, suitlit1, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt

def runit(  running, output, suitlit1, sdeck, outa, q):
    '''from rich.prompt import Prompt as rin
    minp=rin.ask('move from')
    dinp=rin.ask('goto dest')'''
    running, output, suitlit1, sdeck, outa, q = rpit(running, output, suitlit1, sdeck, outa, q)
    minp = '9C';dinp = '0F'
    running, output, suitlit1, sdeck, outa, q, minp, dinp = readt(running, output, suitlit1, sdeck, outa, q, minp, dinp)
    
    colh = list(zip(*outa))
    if minp == 'q':
        return False, output, suitlit1, sdeck,outa,q
    elif minp == 's':
        global startOver
        startOver= True
        return True, output, suitlit1, sdeck,outa,q
    elif dinp in validAceMove :
        pass    # 
    elif minp[1] not in validSuits or dinp[1] not in validSuits:
        return True, output, suitlit1, sdeck,outa,q
    #functionize this    # minp, dinp, mino, dino, 
    mii = 0; dii = 0;mino='';dino=''
    minp, dinp, mino, dino, mii, dii = chgX2symbol(minp, dinp, mino, dino, mii, dii)
    moapt=[0,0]; doapt=[0,0]
    dou = 0; mou= 0; validMove=False
    validMove, output, suitlit1, sdeck, outa, q,minp, dinp, mino, dino, mii, dii, colh, moapt, doapt = validMov( \
    validMove, output, suitlit1, sdeck, outa, q,minp, dinp, mino, dino, mii, dii, colh, moapt, doapt)
    #SKIP m if m == "F" or "G"
    '''
    if mino in suitlit1:
        mii = suitlit1.index(mino)
    if not mii:
        mii=0
    #SKIP d if d == "F" or "G"
    if dino in suitlit1:
        dii = suitlit1.index(dino)
    if not dii:
        dii=0
    moapt=[0,0]; doapt=[0,0]
    dou = 0; mou= 0; validMove=False
    # xinp=dinp, minp; xino=dino, mino; moapt, doapt, dou, doo, mou, moo
    #if out1/2.index(dii/mii)=0 this doesnt work 
    #doi=[out2.index(dii) if dii in out2 else 0 for out2 in outa]
    if dinp[1]=='F' or dinp[1]=='G':
        dou=0;doo=int(dinp[0]);doapt=[dou,doo]
    elif dinp[1]=='Z':
        dou=1;doo=int(dinp[0]);doapt=[dou,doo]
    else:
        for tout,sout in enumerate(outa):
            if dii in sout and dinp[1]!= 'F' and dinp[1]!='G':
                dou = tout
                doo = sout.index(dii)
                doapt=[dou,doo]
                break
    #doo = sum(doi);

    #moi=[out1.index(mii) if mii in out1 else 0 for out1 in outa]
    if minp[1]=='F' or minp[1]=='G':
        mou=0;moo=int(dinp[0]);moapt=[mou,moo]
    else:
        for uout,vout in enumerate(outa):
            if mii in vout:
                mou = uout
                moo = vout.index(mii)
                moapt = [mou,moo]
                break
    #moo = sum(moi);
    #moo=1
    #for iu,qe in enumerate(moi):
    #    if qe > 0:
    #        mou=iu
    #        break
    rp(f'row{mou=},col{moo=}',end=',    ')
    #for ov,wf in enumerate(doi):
    #    if wf > 0:
    #        dou=ov
    #        break
    rp(f'row{dou=},col{doo=}')
    if dinp[1]=='Z':
        qqq=colh[int(dinp[0])]

    if dinp[1] == 'G':    #Foundation A-K
        dl=int(dinp[0])
        if dl in range(4,8):
            if outa[0][dl] == 0 \
            or outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
                outa[0][dl]=outa[mou][moo]
                outa[mou][moo]=0
                validMove=False #pass# valid move
            else:
                validMove=False
            #elif outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
            #    outa[0][dl]=outa[mou][moo]
            #    outa[mou][moo]=0
            #    validMove=False    
    elif dinp[1]=='Z' and sum(qqq[1:])==0:
        outa[1][int(dinp[0])]= outa[mou][moo]
        outa[mou][moo]=0
        validMove=False
    elif dinp[1] == 'F':    #Free Cell
        dk=int(dinp[0])
        if dk in range(4):
            if outa[0][dk] == 0:
                outa[0][dk]=outa[mou][moo]#pass# valid move
                outa[mou][moo]=0
                validMove=False #Done already    if not validMove:
    elif dii in q or dii==0:
        rp(f'invalid dest{dii=}')
    elif outa[mou][moo] in output[dii]:
        #moapt=[mou,moo];doapt=[dou,doo]
        validMove=True
        rp(f'Valid Move: {outa[mou][moo]=} in {output[dii]=}{dii=}')
    else:
        rp(f'{outa[mou][moo]=} notin{output[dii]=}{dii=}')
    '''
    #TODO:#add showing cards validation of a col of cards
          #move card(s) ADD CLASS and __init__      #1F0A1    #1F0A1
    #rp(f'[red,align(center,width({6})]🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽[/]')
    if validMove:
        running, output, suitlit1, sdeck, outa, q, moapt, doapt=movit(  running, output, suitlit1, sdeck, outa, q, moapt, doapt)
    weWonr, putSomeUpr, running, output, suitlit1, sdeck, outa, q = weWon(\
        running, output, suitlit1, sdeck, outa, q)
    if putSomeUpr:
        running, output, suitlit1, sdeck, outa, q=putSomeUp(running, output, suitlit1, sdeck, outa, q)
    if weWonr:
        rp(f'YOU WON!!!!!!!!!!!!!!!\n{outa=}{int('0b100',0)=}')
        '''    col0=True;col1=True;col2=True;col3=True;col4=True;col5=True;col6=True;col7=True      
        for colu in colv:  col9=False  #KH,QS,JH,TS,            
            for iw,colw in enumerate(colu): if iw  >= len(colu)-1 or iw==0:  continue
                else:    colt=int(colw);colx=int(colu[iw+1])
                    if colt==0 or colx==0:    col9=True'''     

    return running, output, suitlit1, sdeck, outa, q

running, output, suitlit1, sdeck, outa, q = pop()

while running:
    if startOver:
        running, output, suitlit1, sdeck, outa, q = pop(sdeck)
    running, output, suitlit1, sdeck, outa, q = runit(running, output, suitlit1, sdeck, outa, q)