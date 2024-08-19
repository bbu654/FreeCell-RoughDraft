from cards_msu_cse import Card as card
from cards_msu_cse import Deck as deck
from rich          import print as rp
from rich.table    import Table
from rich.console  import Console
from rich.pretty   import pprint
import sqlite3         as sql3
import tableau_mine    as Tableau
#from fc_io_New     import PrintItBBU
#from fc_io_New     import SQLiteIO

from fc_rules_mine import Rules as Rule
from fc_cons_New1  import *
rule=Rule()

class PrintItBBU(object):
    def __init__(self) -> None:
        pass
    # rp(f'{nextCard}',sep=' ',end='')rp(f'{nextCard}',sep=' ',end='')
    def printTableau(self,tablow, reason=[]):
        
        tview = Table(title='My FreeCell - BBU')
        cc =['','','','','','','','']
        for idy,row1 in enumerate(tablow):
            strRow=['','','','','','','',''] #str4=zip(row1)        #str5=str4        str0=''
            for idx,col1 in enumerate(row1):
                col2=str(col1)
                if col2 == BLANKCARD or col2=='' or col2=='0' or col2=='_' or col2=='XX' or col2=='xx':
                    stra=f'[white]{BLANKCARD}[/]'                
                else:
                    #indx0= Card.rank_list.index(str(col1)[2])
                    #indx1= Card.suit_list.index(str(col1)[7]) 
                    stra=f'{COLORS[col2[1]]}{col2[0]}{SYMBOL[col2[1]]}[/]'
                if idy==0:#strx=str(col1)    if col1 == BLANKCARD:    tview.add_column(f'[white]BLANKCARD[/]')    else:    tview.add_column(f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]')                    # tview.add_column(suitlit1[idx])
                    tview.add_column(stra)
                else:
                    strRow[idx] += stra #    if col1 == BLANKCARD:    strRow[idx] += f'[white]BLANKCARD[/]'       else:    strRow[idx] += f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'  
            if row1 != cc and row1 != EMPTYROW:
                tview.add_row(strRow[0],strRow[1],strRow[2],strRow[3],\
                              strRow[4],strRow[5],strRow[6],strRow[7])
        consol=Console()    
        consol.print(tview,justify='center')
        #return tablow
        if reason != None:
            if len(reason) > 1:
                errmsg = ''.join(str(te) for te in reason[1:])
                #rp(f'{[ti for ti in reason[1:]]}',sep='')
    def printSQLRow(self, sqlrow):
        outa=[]
        for rowa in sqlrow[3:]:
            if rowa != None:
                pass




    def printConst(self):
        self.printSuitLit()
        self.printnextCard()

    def printSuitLit(self):
        #rp(f'suitlit={suitlit[0]}')
        #rp(f"{suitlit[1:15]=}",sep=' ')
        #rp(f"{suitlit[15:28]=}",sep=' ')
        #rp(f"{suitlit[28:41]=}",sep=' ')
        #rp(f"{suitlit[41:]=}",sep=' ')
        rp(f'    {suitlit[0]=}')
        rp(f"{ suitlit[1:14]=}",sep=' ')
        rp(f"{suitlit[14:27]=}",sep=' ')
        rp(f"{suitlit[27:40]=}",sep=' ')
        rp(f"  {suitlit[40:]=}",sep=' ')
    
    def printnextCard(self):
        rp('nextCard=')
        for idxc,key in enumerate(list(nextCard.keys())):
            if idxc%4==0 and idxc>0:
                print()
            rp(f'{COLORS[key[1]]}{key}:{nextCard[key]}[/]',end=', ')
            '''if str(keys)[1] == 'C':
                rp(f'[{{keys}:{nextCard[keys]}[/]',sep=', ')
            if str(keys)[1] == 'C':
                rp(f'[blue]{keys}:{nextCard[keys]}[/]',sep=', ')
            if str(keys)[1] == 'C':
                rp(f'[blue]{keys}:{nextCard[keys]}[/]',sep=', ')
            if str(keys)[1] == 'C':
                rp(f'[blue]{keys}:{nextCard[keys]}[/]',sep=', ')'''

        #rp(f'{nextCard=}',sep=' ',end=', ')    


    def rprnt(self,tablow):
        #above is init     below is rpit
        gameview = Table(title='Freecell')
        #for qe in range(8):
        #   gameview.add_column('')
        for idy,row1 in enumerate(tablow):
            #str4=zip(row1)        #str5=str4
            str0='';str1='';str2='';str3=''
            str4='';str5='';str6='';str7='';stra=''
            for idx,col1 in enumerate(row1):
                col2=str(col1)
                if col2 == BLANKCARD:
                    stra=f'[white]BLANKCARD[/]'                
                else:
                    stra=f'{COLORS[col2[1]]}{col2[0]}{SYMBOL[col2[1]]}[/]'
                if idy==0:#strx=str(col1)
                    gameview.add_column(stra)
                        # gameview.add_column(suitlit1[idx])
                else:
                    if idx == 0:                      str0+=stra
                    elif idx == 1:                    str1+=stra
                    elif idx == 2:                    str2+=stra
                    elif idx == 3:                    str3+=stra
                    elif idx == 4:                    str4+=stra                    
                    elif idx == 5:                    str5+=stra
                    elif idx == 6:                    str6+=stra
                    elif idx == 7:                    str7+=stra
                        #if col1 == BLANKCARD:
                        #    str7+=f'[white]BLANKCARD[/]'
                        #else:
                        #    str7+= f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'
                        #str7+=f'{suitlit1[idx]}'
            if row1 !=  EMPTYROW:#[BLANKCARD for _ in range(8)]:
                gameview.add_row(str0,str1,str2,str3,str4,str5,str6,str7)
        consol=Console()    
        consol.print(gameview)
        self.printTableau(tablow)        
        return tablow

    def getAnswer(self,question = f'card, dest|FF,GG,Q: ',reason=[]):
        #answer = input(question)
        try: 
            global errmsg
            if reason != []:
                errmsg = errmsg + ''.join(str(zz) for zz in reason)
            if len(errmsg) > 1: pass
        except: errmsg=''
        validAnswer=False#; errmsg=''
        while not validAnswer:
            strquestion = f'{errmsg: ^40}{question}'
            if errmsg !='':                    #strreason= ' '.join(errmsg)
                errmsg=''
            validAnswer, answer, errmsg = rule.getValidAnswer(input(f'{strquestion}'))
            
        
        return answer
class SQLiteIO(object):
    xGamesFields=[	"dbid",	 "gameid", "solved", "test", "currentgameid",
                    "row0",  "row1",   "row2",	 "row3",	 "row4",  "row5",  "row6",
                    "row7",	 "row8",   "row9",	 "row10", "rpw11", "row12", "row13", 
                    "row14", "row15",  "row16",  "row17", "row18", "row19", "row20", 
                    "row21", "row22" ] 

    gameFields=[ "dbid",  "gameid", "moveid", "row0",  "row1",  "row2", 
                 "row3",  "row4",   "row5",   "row6",  "row7",  "row8", 
                 "row9",  "row10",  "row11",  "row12", "row13", "row14", 
                 "row15", "row16",  "row17",  "row18", "row19", "row20", 
                 "row21", "row22" ] 

    def __init__(self) -> None:
                # connecting to the database
        self.conn = sql3.connect("fc_SQLite3_FC.sqlite3")
        self.cursorSQL3=self.conn.cursor()
        self.getFieldNamesfromPRAGMAtable_info()
        self.allMoveSQLFwdBack = []
        self.brichp1=PrintItBBU()
        self.maxmoveid=1
    def getFieldNamesfromPRAGMAtable_info(self):
        """This script will print out each column's name from the users table. The PRAGMA statement returns a list of tuples, where each tuple represents a column. The second element in each tuple (index 1) is the column name.
        While this method is more verbose than the basic example, it also provides additional details about each column, such as data type, whether the column can hold NULL values, and the default value for the column, among others.
        Exploring Metadata with PRAGMA
        If you're interested in fetching more than just the column names, like the data type or whether the column is a primary key, you can adjust the aforementioned code to suit your needs. Here is how you can do it:"""
        self.cursorSQL3.execute('PRAGMA table_info(Game)')
        table_info4Games=[];ti4gRow=[];litlist=['','Name:','Type:','NULL:','Dfalt:','IsPK:']
        for idx,row in enumerate(self.cursorSQL3.fetchall()):
            ti4gRow=[]
            for idy in range(1,6):
                ti4gRow.append(row[idy])#;ti4gRow.append(litlist[idy])
            table_info4Games.append(ti4gRow)
        self.fieldNames4games=[table_info4Games[idz][0] for idz in range(len(table_info4Games))]
        self.row0Index=self.fieldNames4games.index('row0')
        rp(f'{self.fieldNames4games[:11]=}||||{self.row0Index=}',sep=', ')
    
    def readFirstGamesRec(self):
        sqlf=f"SELECT * FROM 'xGames'"# WHERE 'gameid' = 1"        
        self.cursorSQL3.execute(sqlf)
        self.result=self.cursorSQL3.fetchone()
        #CREATE TABLE "xGamesFields" (	/*"moveid"	INTEGER NOT NULL,*/	PRIMARY KEY("dbid" AUTOINCREMENT))
        for idxGames,rfield in enumerate(self.result):
            if rfield == ' ' or rfield == None or idxGames > 4:
                pass
            else:
                rp(f'{SQLiteIO.xGamesFields[idxGames]}: {rfield}',end='    ')#        pass
                if idxGames==4:
                    self.gameid=rfield
        
        #######################################
        #CREATE TABLE "Game" (       PRIMARY KEY("dbid" AUTOINCREMENT))
        #row0: ' 'idxGames)    row1: ' 'idxGames)    row2: ' 'idxGames)    row3: ' 'idxGames)    row4: ' 'idxGames)    row5: ' 'idxGames)    row6: ' 'idxGames)    row7: ' 'idxGames)    
        #######################################
        return self.gameid
    def readlastrecord(self):
        self.lastdbid=self.cursorSQL3.lastrowid
        '''(4, 2, 3, '6C0000AD00', 'AH3C9S5SQD7HKD2D', '7D9DJS5H9C5C8HAC', '3DTH8SQCAS2S2H9H', 'TS3S3H4S8DKS6STC', 'JD7CJC6HKH5DQHKC', 'QS4D4H2C6D4C08C', 'TD7SJH00000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000')'''
        sqlre=f"SELECT * FROM Game ORDER BY dbid DESC LIMIT 1;"       
        self.cursorSQL3.execute(sqlre)#, ('john@example.com', 'mypassword'))
        self.sqlcreateslTblRows()

        return self.gameid,self.moveid,self.lTblRows

    def sqlcreateslTblRows(self):
        self.mresult=self.cursorSQL3.fetchone()
        print();self.lTblRows=[]
        #self.mresult=list(bsqlt3.readlast record())
        for idxGamem,mfield in enumerate(self.mresult):
            if mfield == ' ' or mfield == None :
                pass
            else:
                rp(f'{SQLiteIO.gameFields[idxGamem]}: {mfield}',end='    ')#
                if idxGamem==1:
                    self.gameid=mfield
                elif idxGamem==2:
                    self.moveid=mfield
                elif idxGamem>2:
                    self.lTblRows.append(mfield)

    def insertTablow(self,tablow,gameid,moveid,dontchgmoveid=False):
        """ self.fieldNames4games[:10]=['dbid', 'gameid', 'moveid', 
        'row0', 'row1', 'row2', 'row3', 'row4', 'row5', 
        'row6']||||self.row0Index=3"""
        #self.newGameFlag = newGameFlag
        self.dontchgmoveid = dontchgmoveid
        if        self.dontchgmoveid == True:
            self.savedmoveid=moveid
            moveid = self.tempmoveid
        sqld, tablow = self.convertTablo2SQL(tablow, gameid, moveid) 
        self.cursorSQL3.execute(sqld)#, ('john@example.com', 'mypassword'))
        #INSERT INTO 'game' ('gameid', 'moveid', 'subtitle`, `author`, `promocode`, `emaildate`, `picturename`, `description`, `promoline`, `forwardt`) VALUES
        # Commit changes
        if        self.dontchgmoveid == True:
            moveid = self.savedmoveid
            self.dontchgmoveid = False

        if self.moveid % 5 == 0 or self.moveid == 1 or self.moveid == 2 or self.moveid == 3: #unfotunately i abend all the time while 
            self.conn.commit()

        print("Record inserted successfully")
        return tablow,self.gameid,self.moveid
    
    def handlebackfwd(self, running, tablow, answer, reason):
        """running,self.moveing, tablow, self.reason = bsqlt3.handlebackfwd(running,tablow, answer,self.reason)"""
        answer=answer[0].upper()+answer[1:]  if str(answer)[0].isalpha() else answer
        self.currentMoveId = self.moveid;self.reason = reason
        self.noOfRows2Move=0; self.needAnswer=True
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
            if self.currentMoveId + self.noOfRows2Move >= self.maxmoveid:
                self.needAnswer=False
            else:
                self.currentMoveId += self.noOfRows2Move 
        running = True
        if self.needAnswer:
            #running, tablow, self.lTblRows = 
            self.getSpecificTablowDisplay( running, tablow,  self.currentMoveId)
            #if not self.reason: self.reason=[]
            #self.gamePrintTableau(tablow, self.reason)
        return running,self.needAnswer, tablow, self.reason, self.lTblRows
    #running,self.moveing, tablow, self.reason

    def convertTablo2SQL(self, tablow, gameid, moveid):
        snames=self.fieldNames4games;srowidx=self.row0Index
        self.gameid=gameid   
        self.moveid=moveid
        self.moveid+=1
        if self.newGameFlag:
            self.gameid += 1;self.moveid = 1;self.maxmoveid=1
        self.sep=', '# Create a new record
        testtablow = [True if len(rol1) == 8 else False for rol1 in tablow]
        if False in testtablow:
            self.closeconn()
            raise Exception()
        sqlb=[self.gameid,self.moveid]
        for sqlridx,sqlrow in enumerate(tablow):
            sqlc=''

            """ DONT SKIP THE FIRST ROW IF ITS EMPTY (skip the rest of them)"""
            if sqlridx ==0 or sqlrow != [BLANKCARD for _ in range(8)]:
                for sqlcol in sqlrow:
                    sqlcol2=str(sqlcol)
                    if sqlcol2 != '' and sqlcol2 !=BLANKCARD: 
                        sqlc+=sqlcol2
                    else:
                        sqlc+='__'
                sqlb.append(sqlc)
            else:
                continue
        
        #self.rowstring= f" VALUES ({self.gameid}, {self.moveid}, "
        #self.valuestr = f"INSERT INTO 'Game' ({snames[1]}, {snames[2]}, "
        self.SQLvalues = f"{tuple(sqlb[idxcv] for idxcv in range(len(sqlb)))}; " 
        #self.rowstring = f" VALUES {self.SQLvalues}; "
        #numbers = [1, 2, 3, 4, 5];    squares = tuple(x**2 for x in numbers)
        #print(squares)  # Output: (1, 4, 9, 16, 25)
        self.valuestr = f"INSERT INTO 'Game' {tuple(snames[idz] for idz in range(1,len(sqlb)+1))} "
        '''for idx,rowf in enumerate(sqlb):
            if idx == len(sqlb)-1:
                self.rowstring += f"'{str(rowf)}');"
                self.valuestr  += f"'{snames[idx+srowidx]}')"
            else:
                self.rowstring += f"'{str(rowf)}', "
                self.valuestr  += f"'{snames[idx+srowidx]}', "    '''
        sqld = f"{self.valuestr} VALUES {self.SQLvalues}"
        self.allMoveSQLFwdBack.append(self.SQLvalues)  
        if self.dontchgmoveid:  rp(f'{sqld=}',sep=',')
        else:                print(f'{sqld=}',sep=',')
        return sqld, tablow
    

    def deleteMostOfDbRowsAfterWin(self,gameid,norow2leave=3):
        sqlf=f'SELECT COUNT(*) FROM Game WHERE gameid = {gameid} and moveid > {norow2leave};'
        self.cursorSQL3.execute(sqlf)
        #self.norowsdeleted = []
        self.norowsdeleted = self.cursorSQL3.fetchone()         
        
        sqlg=f'DELETE FROM Game WHERE gameid = {gameid} and moveid > {norow2leave};'
        self.cursorSQL3.execute(sqlg)
        #, ('john@example.com', 'mypassword'))
        #INSERT INTO 'game' ('gameid', 'moveid', 'subtitle`, `author`, `promocode`, `emaildate`, `picturename`, `description`, `promoline`, `forwardt`) VALUES
        # Commit changes
        self.conn.commit()
        self.allMoveSQLFwdBack=[]#if u move this up 
        #we will lose the ability to restart this app
        #lennodels=len(self.norowsdeleted)
        rp(f'{self.norowsdeleted[0]} Record(s) deleted successfully:')
        rp(f'{sqlf=}\n{sqlg=}') 

    #def convertSQL2Tablo(self):#update to tableau must be done in tableau_dataclass        
    '''    
    def convertSQL2Tablo(self):
        #dek=deck();#deckA,deckB=dek.turnTestdeckIntoDeck(testdeck)
        suit1=card.suit_list; rank1=card.rank_list
        tablow=[]
        #with closing(sql3class.cursorSQL3) as cursor3:
        #gamer=game()
        self.tablow=[]
        qq=[BLANKCARD for zz in range(8)]
        self.tablow.append(qq)
        running=True#self.lTblRows=sql3class.readlast record()
        cardi=[]
        if self.lTblRows !=None and len(self.lTblRows) < 2:
            self.gameid,self.moveid,self.lTblRows = self.readlastrecord()
        #self.gameid+=1     #self.moveid+=1    #tablow = fromsql2tablo
        for listoflists in self.lTblRows:
            if len(listoflists) != 16: 
                self.invalidTabloLen = True
                self.closeconn()
                raise Exception()#            else:
            lof2char= [listoflists[i:i+2] for i in range(0, len(listoflists), 2)]
            cardi.append(lof2char)
        suit1=card.suit_list; rank1=card.rank_list
        tablow=[];self.rowx=-1;self.coly=-1
        for ir,xx in enumerate(cardi):
            ww=[];self.rowx += 1
            if self.rowx > 22: raise Exception(f"rowx Index[[{self.rowx}] out of range")
            for ic,yy in enumerate(xx):
                self.coly += 1                        #if self.coly > 7: raise Exception(f"coly Index[[{self.coly}] out of range") 
                if yy == 'xx':
                    ww.append(yy)
                else:
                    ww.append(card(rank1.index(yy[0]),suit1.index(yy[1]),ir,ic))
                    rule.posdic.update({yy:[ir,ic]})
            tablow.append(ww)
        while len(tablow)<23:
            tablow.append([BLANKCARD for w in range(8)])
        for idxm,rown in enumerate(tablow):
            for idxn, itemn in enumerate(rown):
                if str(itemn) == 'xx':
                    tablow[idxm][idxn] = BLANKCARD    #Tableau.gamePrintTableau(tablow)
        
        return running, tablow
        '''
        

    def readAllRowsOnRestart(self):
        sqlk=f'SELECT * FROM Game WHERE gameid = {self.gameid};'
        self.cursorSQL3.execute(sqlk)#, ('john@example.com', 'mypassword'))
        self.lTblRowsOR=self.cursorSQL3.fetchmany()
        self.allMoveSQLFwdBack=[]
        print()
        for row in self.lTblRowsOR:  
            self.allMoveSQLFwdBack.append(row)

    def  getSpecificTablowDisplay(self, running, tablow, currentMoveId):   
        self.currentMoveId = currentMoveId
        sqll=f'SELECT * FROM Game WHERE gameid = {self.gameid} AND moveid = {self.currentMoveId};'
        #try:
        self.cursorSQL3.execute(sqll)#, ('john@example.com', 'mypassword'))
        self.sqlcreateslTblRows()
        #running, tablow = self.convertSQL2Tablo()
    
        
    def gamePrintTableau(self, tablow,reason,newGameFlag=False):
        self.newGameFlag = newGameFlag
        tablow,self.gameid,self.moveid = self.insertTablow(tablow,self.gameid,self.moveid)
        if self.moveid == self.maxmoveid+1: 
            self.maxmoveid += 1
        self.brichp1.printTableau(tablow,reason)                    
        self.newGameFlag=False

    def insertCurrentTablownAsMoveid2(self, tablow,tempmoveid=1):
        self.newGameFlag   = False
        self.dontchgmoveid = True
        self.tempmoveid    = tempmoveid
        self.rmpmid        = self.moveid
        tablow, self.gameid, self.moveid = self.insertTablow(tablow,self.gameid,tempmoveid,self.dontchgmoveid)
        self.moveid        = self.rmpmid
        self.dontchgmoveid = False


    def closeconn(self):
            self.conn.close()
        # connecting to the database
        #connection = sqlite3.connect("gfg.db")
 
# cursorcrsr = self.conn.cursor()
 
# print statement will execute if there
# are no errors    print("Connected to the database")
 
# close the connection  connection.close()    