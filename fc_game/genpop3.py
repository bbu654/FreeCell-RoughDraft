from fc_cons_New1    import *
from fc_card_New1    import Card
from fc_card_New1    import Deck    
from rich            import print as rp
from fc_tableau_mine import StateFlags
from fc_tableau_mine import Tableau_dataclass
from fc_rules_mine   import Rules
from fc_tableau_mine import  findNoOf0FC, findNoOf0Cols, posdictNEtablo
from copy            import deepcopy as dpcopy
CardA = Card();      rules = Rules() 
class Tableau(Tableau_dataclass):   
    def GGCard(self, minp):
        #self.validGG=False                nofoundation just done
        listsuit=list(SYMBOL.keys())
        if minp[1] in listsuit:
        #if minp[1] in list(SYMBOL.keys()):    rank=A t[0][f]=BLANKCARD
            foundation =  listsuit.index(minp[1]) + 4     #-1 for the x in listsuit
            if self.verbose and not self.winning:
                rp(f'{foundation=} = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit')
            moveCard   = validrank.index(minp[0])
            if (moveCard == 0 and self.tablown[0][foundation]==BLANKCARD) or \
                str(self.tablown[0][foundation])[0] == validrank[moveCard -1]:
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
                
                #tempCard=CardA.stringToCard(minp)
#                if foundation not in range(4,8):
#                    raise Exception(f'{foundation=} Out of range(s/b 4-7)')
                
                self.tablown[0][foundation] = minp
                self.tablown[0][foundation] = Card(Card.rank_list.index(minp[0]),Card.suit_list.index(minp[1]),0,foundation)
                self.posdict.update({minp:[0,foundation]})#self.validGG=True
        
    def FFCard(self, minp):
        moapt=0,0;doapt=0,0
        if minp[1] in list(SYMBOL.keys()):
            numOf0InFC, first0InFC = self.findNoOf0FC()
            if first0InFC > -1:
                doapt=0,first0InFC; mou=0; moo=0
                mou,moo=Card(Card.rank_list.index(minp[0]),Card.suit_list.index(minp[1])).get_position()
                newCard=Card(mou,moo).set_position(0,first0InFC)
                self.tablown[0][first0InFC]=newCard
                for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        self.posdictNEtablo(minp, mou, moo, moapt)
                        self.tablown[doapt[0]][doapt[1]]=self.tablown[mou][moo]
                        self.tablown[mou][moo]=BLANKCARD
                        self.posdict.update({minp:[0,first0InFC]})
                        break
            else:
                self.moveing = False
        else:
            self.moveing = False

           # moapt,doapt
      
    def getCardLocation(self, minp, dinp):
        mou=-1;moo=0;dou=-1;doo=0;moapt=mou,moo;doapt=dou,doo
        for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
            rr=[str(ss) for ss in qq]
            if minp in rr: 
                mou=ii; moo=rr.index(minp);moapt=mou,moo
                #sliceddict = { key: self.posdict[key] for key in self.posdict.keys() if key in ['AC', '2C', '3C', '4C', '5C', '6C', '7C']}
                #self.posdictNEtablo(minp, mou, moo, moapt)
                if dinp == 'dinp':     break    
            if dinp in rr and dinp != 'dinp': 
                dou=ii; doo=rr.index(dinp);doapt=dou,doo
                #     self.posdictNEtablo(dinp, dou, doo, doapt)            #if dou > -1 and mou > -1:
            #    self.tablown[doapt[0]+1][doapt[1]]=self.tablown[mou][moo]
            #    self.tablown[mou][moo]=BLANKCARD
            #    break  # moapt,doapt
        return moapt, doapt
    
    def moveCCCard(self, moapt, doapt):
        mou,moo=moapt;dou,doo=doapt
        if dou > -1 and mou > -1: '''fix'''
            self.tablown[dou+1][doo]=self.tablown[mou][moo]
            self.posdict.update({str(self.tablown[mou][moo]):[doapt[0]+1,doapt[1]]})
            self.tablown[mou][moo]=BLANKCARD    #break  # moapt,doapt


    def ZZCard(self, minp):
        moapt=0,0;doapt=0,0
        if minp[1] in list(SYMBOL.keys()):
            self.copytavl = dpcopy(self.tablown[1:])
            blankcolumns, first0Col = self.findNoOf0Cols(self.copytavl)
            if first0Col > -1:
                doapt=1,first0Col; mou=0; moo=0
                for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        self.posdictNEtablo(minp, mou, moo, moapt)
                        self.tablown[doapt[0]][doapt[1]]=self.tablown[mou][moo]
                        self.tablown[mou][moo]=BLANKCARD
                        self.posdict.update({minp:[0,first0Col]})
                        break
            else:
                self.moveing = False
        else:
            self.moveing = False

    def getFGZ_Dest(self, minp, dinp):
        doapt=[0,0]; self.moveing = False
        if dinp[1] == "F":
            FFnumOf0InFC, first0InFC = self.findNoOf0FC()
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
 
 
 
 
    def FGZCard(self, minp, dinp):
        if minp in validcard:
            moapt=0,0;doapt=0,0
            self.copytavl= dpcopy(self.tablown)
            doapt = self.getFGZ_Dest(dinp)
            FFnumOf0InFC, first0InFC = self.findNoOf0FC()
            if first0InFC > -1 and dinp[1]:
                doapt = [0,first0InFC]; mou=0; moo=0
                mou,moo=Card(rank_list.index(minp[0]), suit_list.index(minp[1])).get_position()
                newCard=Card(mou,moo).set_position(0,first0InFC)
                self.tablown[0][first0InFC]=newCard
                for ii,qq in enumerate(self.tablown):# if minp in qq else 0]
                    rr=[str(ss) for ss in qq]
                    if minp in rr: 
                        mou=ii; moo=rr.index(minp);moapt=mou,moo
                        self.posdictNEtablo(minp, mou, moo, moapt)
                        self.tablown[doapt[0]][doapt[1]]=self.tablown[mou][moo]
                        self.tablown[mou][moo]=BLANKCARD
                        self.posdict.update({minp:[0,first0InFC]})
                        break
            else:
                self.moveing = False
        else:
            self.moveing = False

           # moapt,doapt
    
