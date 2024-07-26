from dataclasses import dataclass
import sqlite3   as sql3 

bsqlt3=sql3()

@dataclass

class OldShatMFCode(object):

    BLANKCARD='0'
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
                lastnon0=self.BLANKCARD;lastidx=-1        #find the last non-zero !! Does it Foundation???
                #check if FCs will go up       #object of type 'reversed' has no len()
                reversedcolj = []
                for xx in reversed(colj):
                    reversedcolj.append(str(xx))            
                if reversedcolj == [self.BLANKCARD for poiu in range(len(reversedcolj))]:
                    pass
                else:
                    for iey,xcv in enumerate(reversedcolj):
                        xxx=str(xcv)
                        lln0=len(lastnon0)
                        if lastidx == -1 and xxx != self.BLANKCARD:
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
                            bsqlt3.gamePrintTableau(yackuptbj, self.reason)

        return    running,tablow
