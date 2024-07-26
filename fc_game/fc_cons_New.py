from dataclasses import dataclass

@dataclass
class Constants(object):
    
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
