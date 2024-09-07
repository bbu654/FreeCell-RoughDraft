from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck
from fc_io_mine import PrintItBBU as printit
import fc_tableau_mine as tableau


class Game(object):
    tablClass=tableau.Tableau()

    def __init__(self, running=True):#, restartCurrentGameFromScratch = False, beginANewGame = True) -> None:
        self.running = running
        self.init1st = False
        #self.restartCurrentGameFromScratch = restartCurrentGameFromScratch
        #self.beginANewGame = beginANewGame
        self.testDeckls = ['8C', 'TD', 'KD', 'QD', 'TH', 'QC', '9H', '8S', 
                           '5S', '4H', '2C', 'QS', '8H', '3C', 'JS', '6H', 
                           'KH', 'JC', 'JH', '2D', '3S', '6C', '7S', '2S', 
                           'KC', '7D', '6D', '5D', '4D', 'KS', '3D', 'AC',  
                           '2H', '5C', '6S', '7C', '3H', 'QH', '9C', '9S', 
                           '5H', 'AS', '9D', 'JD', '4C', 'AD', 'AH', '8D', 
                           'TC', '7H', '4S', 'TS']
        ###########################################################
        self.testDeckls2 = ['6C', '4H', 'AS', 'JC', 'TC', '8C', '4S', '3C', 
                            '7S', '2D', '9H', '3S', 'TH', '2S', '2H', '4D', 
                            '2C', 'JS', '4C', '7H', '8H', '7C', 'KC', '8D', 
                            '5D', '5H', '3D', '9C', 'AD', 'AH', '6D', 'KH', 
                            'QH', 'KS', 'JH', '3H', '8S', 'AC', '5S', 'QC', 
                            '9D', '6S', 'TS', '9S', 'KD', 'QD', 'TD', '7D', 
                            '6H', 'JD', 'QS', '5C']
        pass
    ''''SQLiteIO' object has no attribute 'maxmoveid' '''
    '''cannot access local variable 'suitminp' where it is not associated with a value'''
    def runit(self,running,dek,tablow=None):
        if running:
            self.dek=dek
            if tablow==None or tablow == []:  #prevent abend
                running, dek, tablow = self.tablClass.handle_Re_Start(running)
            elif tablow[1] == ['0','0','0','0','0','0','0','0']:
                running, dek, tablow = self.tablClass.handle_Re_Start(running)
            if running:
                running, dek, tablow = self.tablClass.handleAnswer( \
                running, dek, tablow )
            #game.restartCurrentGameFromScratch=Game.tablClass.restartCurrentGameFromScratch
            #game.beginANewGame = Game.tablClass.beginANewGame
        return running, dek, tablow
    '''
    def checkNewGameRestartFlags(self):
        if game.beginANewGame:
            running, dek, tablow = game.tablClass.NewGame()
            game.restartCurrentGameFromScratch= True
            game.beginANewGame=False
        else:
            running, dek, tablow = game.restartCurrentGame()
            game.restartCurrentGameFromScratch= False
            game.beginANewGame=True
    def restartCurrentGame(self):
        ranklist=['K','Q','J','T','9','8','7','6','5','4','3','2','A']
        testdeck=[r+s for r in ['C','D','H','S'] for s in (ranklist)]'''
    ''' outa = [[ '0', '0', '0', '0','2C','2D','5H','5S'],       #00
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
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22'''
    ''' outb = [['QS', '0', '0', '0','AC','2D','4H','4S'],          
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
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22'''
    ''' outc = [[ '0', '0', '0', '0','2C','2D','4H','4S'],       #0  
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
                [ '0', '0', '0', '0', '0', '0', '0', '0']  ]     #22'''
    ''' outd = [[ '0', '0', '0', '0', '0', '0', '0', '0'],     #0
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
                [ '0', '0', '0', '0', '0', '0', '0', '0']]    #22   '''
    """Create a card for each strLit"""
    ''' dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list;tablow=[]
        tablow=game.tablClass.restartfromdb()    '''
    ''' for xx in outd:        
            ww=[]
            for yy in xx:
                if yy == '0':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1])))
            tablow.append(ww)'''
        
    ''' game.tablClass.game PrintTableau(tablow)        
        return True, dek, tablow        
    '''
if __name__ == '__main__':
        '''TEST i,i22,iiii,iiiiii,,b11,f2
           add tkinter option, autoRun
           remove insertTablow(Moveid2'''
        running=True    #Need moves; help
        game=Game(running)#,restartCurrentGameFromScratch=True,beginANewGame = False)
        running, dek, tablow = game.tablClass.handle_Re_Start(running, game.init1st, ' R|estartLastGameFromDB')
        #game.checkNewGameRestartFlags()
        while game.running:    #f bsqlt3(tableau)***inse(io)
            running, dek, tablow = game.runit(running, dek, tablow)
            #if running:            #    game.checkNewGameRestartFlags()
            game.running=running
        """Need to update posdic everywhere"""
        #['undermove!blank']
        """
            Test SQLite3-table the test answers/tablow
        
        
        Need 2 add multi_Card_Move   Turn test to PROD"""
'''foundation=5 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=5 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=7 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=7 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=7 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
(1, 4, 9, 16, 25)
sqlb=[2, 120, 'xxxxxxxxJCQDJHQS', 'xxKHKCQHxxKSKDxx', 'xxQCxxxxxxxxxxxx']sqld="INSERT INTO 'Game' ('gameid', 'moveid', 'row0', 'row1', 'row2')  VALUES (2, 120, 'xxxxxxxxJCQDJHQS', 'xxKHKCQHxxKSKDxx', 'xxQCxxxxxxxxxxxx'); "
fgrewwsdgh='RESTART!    ' +'RESTART!    ' +'RESTART!    ' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!' +'RESTART!'    
Record inserted successfully
           My FreeCell - BBU
┏━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┓
┃ 0 ┃ 0  ┃ 0  ┃ 0  ┃ J♣ ┃ Q♦ ┃ J♥ ┃ Q♠ ┃
┡━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━╇━━━━┩
│   │    │    │    │    │    │    │    │
│ 0 │ K♥ │ K♣ │ Q♥ │ 0  │ K♠ │ K♦ │ 0  │
│ 0 │ Q♣ │ 0  │ 0  │ 0  │ 0  │ 0  │ 0  │
└───┴────┴────┴────┴────┴────┴────┴────┘
foundation=4 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=4 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=6 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=7 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
foundation=5 = list(SYMBOL.keys()).index(minp[1]) + 4 - 1)    #-1 for the x in listsuit
           f'DELETE FROM Game WHERE gameid = {currentgameid} and moveid > 3;'
           2.fixfc_rules_mine mover not diff color/-1  dinp='6H' cant be dinp[1]='H': True"
           2. Add flags field 2 zgames DB to           
           4. Add z in front of DB table.name
           6. FORGOT 1?¿???????'''
'''        1. Need update xGames gameid & new row to insert the current_games_original_tablow b4 exit
           1. need solved,test,???other Flags
           1A.need goback,forward started & working
           1B.needfooter for errmsg,,erase Won until it happens
           2. need 2 !screw it up
           2. fix'''

           #    DONE    DONE    DONE    DONE    DONE    DONE    DONE    
           #    5. String the 'tablow' before move to minp
           #    1. Test gg  4 invalid code
           #    3. Test each last card not the row
        



nonlocalsqlr="INSERT INTO Game  (gameid, moveid, row0, row1, row2, row3, row4, row5, row6, row7) VALUES (21, 1, 'xxxxxxxxxxxxxxxx', '4DAS5D6HKC8S7DQD', '7S3C6DKHAH2H4SKD', '3D2DAC9CQH5C9D8H', 'JSTC3H7CKSJCTD2S', '8DQS8C9HJD5SQC7H', 'TS6S3S2C4C5H9S6C', 'ADTHJH4Hxxxxxxxx');"


# Rules.noFoundationAsMover() missing 1 required 
# positional argument: 'minp'
productionize= f'https://developer.android.com/studio/publish/preparing#:~:text=Configure%20your%20app%20for%20release%201%20Choose%20a,URLs%20for%20servers%20and%20services%20...%20More%20items'
'''Break down the code Always limit tasks to their specific functions. ...
Start Using a Proper IDE ...
Group Files on the Basis of Tasks/Steps ...
Use config.Py for All Your Directories ...
Use Blueprints for Flask ...
Try to Optimize Your Code As Much As Possible ...
Logging Critical Failures and Intermediate Results ...
Handle Possible Errors in the Code ...'''



                             #
                             # 
                             # 
                             # 1└────┴────┴────┴────┴────┴────┴────┴────
'''card, dest|FF,GG,Q: z
               Z !in NRWQ               card, dest|FF,GG,Q: 
                                        card, dest|FF,GG,Q: 
                                        card, dest|FF,GG,Q: z
               Z !in NRWQ               card, dest|FF,GG,Q: 44444
                                        card, dest|FF,GG,Q: z
               Z !in NRWQ               card, dest|FF,GG,Q: '''