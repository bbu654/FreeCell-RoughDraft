from rich import print as rp
import rich.prompt
from rich.table import Table
from rich.console import Console
def find0columns(outa):
    if type(outa)==type(''):
        pass
    return 0
def multiMove( validMove, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt):
    countlenofMoving=1
    tempdou=doapt[0]+1;doo=doapt[1]
    tempmou=moapt[0]+1;moo=moapt[1]
    for tou in range(tempmou,23):#Now chk next1
        if outa[tou][moo] > 0:
            if outa[tou][moo] not in output[outa[tou-1][moo]]:
                return False, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt
            else:
                countlenofMoving += 1
        else:
            break
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
    if outa[tempdou][doo]>0:
        validMove=False
    elif countlenofMoving<=numof0:
        #do move;0 out the move from in outa
        mmm=int(moapt[0]);ooo=int(doapt[[0]])
        for puss in range(mmm,mmm+countlenofMoving+1):
            outa[tempdou][doo]=outa[puss][doo];tempdou += 1 #pass
            outa[puss][doo]=0
        validMove=True            
    else:
        validMove=False
    return validMove, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt
def validMov(validMove, output, suitlit, sdeck, outa, q,minp, dinp, mino, dino, mii, dii, colh, moapt, doapt):
    #SKIP m if m == "F" or "G"
    if mino in suitlit:
        mii = suitlit.index(mino)
    if not mii:
        mii=0
    #SKIP d if d == "F" or "G"
    if dino in suitlit:
        dii = suitlit.index(dino)
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
        if outa[mou+1][moo] > 0:
             validMove, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt=multiMove( validMove, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt)
        #moapt=[mou,moo];doapt=[dou,doo]
        validMove=True
        rp(f'Valid Move: {outa[mou][moo]=} in {output[dii]=}{dii=}')
    else:
        rp(f'{outa[mou][moo]=} notin{output[dii]=}{dii=}')
    #TODO:#add showing cards validation of a col of cards
          #move card(s) ADD CLASS and __init__      #1F0A1    #1F0A1
    #rp(f'[red,align(center,width({6})]🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽[/]')
    return validMove, output, suitlit, sdeck, outa, q, minp, dinp, mino, dino, mii, dii, colh, moapt, doapt