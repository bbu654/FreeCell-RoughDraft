from cards_msu_cse import Card
from cards_msu_cse import Deck
from rich          import print as rp
from rich.table    import Table
from rich.console  import Console
from rich.pretty   import pprint
import sqlite3     as sql3
import tableau_mine   as Tableau

BLANK_CARD='0'
EMPTYROW=[BLANK_CARD for _ in range(8)]
suitlit = ['[white]0[/]']
SYMBOL={'C':'♣','D':'♦','H':'♥','S':'♠'}
COLORS={'C':'[blue]','D':'[bright_magenta]','H':'[red]','S':'[dark_green]'}
#suitlitN= ['[white]0[/]']
for bt in SYMBOL:
    for bu in Card.rank_list[1:]:
        suitlit.append(f'{COLORS[bt]}{bu}{SYMBOL[bt]}[/]')    
'''for at in SYMBOL:
    for au in range(1,14):
        if au == 1:
            suitlit.append(f'{COLORS[at]}A{SYMBOL[at]}[/]')    
        elif au == 10:
            suitlit.append(f'{COLORS[at]}T{SYMBOL[at]}[/]')
        elif au == 11:
            suitlit.append(f'{COLORS[at]}J{SYMBOL[at]}[/]')
        elif au == 12:
            suitlit.append(f'{COLORS[at]}Q{SYMBOL[at]}[/]')
        elif au == 13:
            suitlit.append(f'{COLORS[at]}K{SYMBOL[at]}[/]')
        else:
            suitlit.append(f'{COLORS[at]}{str(au)}{SYMBOL[at]}[/]')'''
  
output={}#nextCards
for j in range(3,13+1):
    for k in range(2):
        output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
        output[j+(13*(k+2))] = [j-1, j+12]
        
j=0
k=0
validsuit={'C':['D','H'], 'D':['C','S'], 'H':['C','S'], 'S':['D','H'] }
nextCard = {}
for vsuit in validsuit:
    for idx, vrank in enumerate(Card.rank_list[3:]):
        nextCard[vrank+vsuit]=[Card.rank_list[idx+2]+validsuit[vsuit][0],Card.rank_list[idx+2]+validsuit[vsuit][1]]


class PrintItBBU(object):
    def __init__(self) -> None:
        pass
    # rp(f'{nextCard}',sep=' ',end='')rp(f'{nextCard}',sep=' ',end='')
    def printTableau(self,tablow):
        
        tview = Table(title='My FreeCell - BBU')
        cc =['','','','','','','','']
        for idy,row1 in enumerate(tablow):
            strRow=['','','','','','','',''] #str4=zip(row1)        #str5=str4        str0=''
            for idx,col1 in enumerate(row1):
                col2=str(col1)
                if col2 == BLANK_CARD or col2=='' or col2=='0' or col2=='_' or col2=='XX' or col2=='xx':
                    stra=f'[white]0[/]'                
                else:
                    #indx0= Card.rank_list.index(str(col1)[2])
                    #indx1= Card.suit_list.index(str(col1)[7]) 
                    stra=f'{COLORS[col2[1]]}{col2[0]}{SYMBOL[col2[1]]}[/]'
                if idy==0:#strx=str(col1)    if col1 == '0':    tview.add_column(f'[white]0[/]')    else:    tview.add_column(f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]')                    # tview.add_column(suitlit1[idx])
                    tview.add_column(stra)
                else:
                    strRow[idx] += stra #    if col1 == '0':    strRow[idx] += f'[white]0[/]'       else:    strRow[idx] += f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'  
            if row1 != cc and row1 != EMPTYROW:
                tview.add_row(strRow[0],strRow[1],strRow[2],strRow[3],\
                              strRow[4],strRow[5],strRow[6],strRow[7])
        consol=Console()    
        consol.print(tview)
        #return tablow

    def printConst(self):
        self.printSuitLit()
        self.printnextCard()

    def printSuitLit(self):
        #rp(f'suitlit={suitlit[0]}')
        #rp(f"{suitlit[1:15]=}",sep=' ')
        #rp(f"{suitlit[15:28]=}",sep=' ')
        #rp(f"{suitlit[28:41]=}",sep=' ')
        #rp(f"{suitlit[41:]=}",sep=' ')
        rp(f'{suitlit[0]=}')
        rp(f"{suitlit[1:14]=}",sep=' ')
        rp(f"{suitlit[14:27]=}",sep=' ')
        rp(f"{suitlit[27:40]=}",sep=' ')
        rp(f"{suitlit[40:]=}  ",sep=' ')
    
    def printnextCard(self):
        rp('nextCard=')
        for idxc,key in enumerate(list(nextCard.keys())):
            if idxc%10==0 and idxc<0:
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
                if col2 == '0':
                    stra=f'[white]0[/]'                
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
                        #if col1 == '0':
                        #    str7+=f'[white]0[/]'
                        #else:
                        #    str7+= f'{COLORS[col1[1]]}{col1[0]}{SYMBOL[col1[1]]}[/]'
                        #str7+=f'{suitlit1[idx]}'
            if row1 !=  EMPTYROW:#['0' for _ in range(8)]:
                gameview.add_row(str0,str1,str2,str3,str4,str5,str6,str7)
        consol=Console()    
        consol.print(gameview)
        tablow = PrintItBBU.printTableau(tablow)        
        return tablow

    def getAnswer(self,question = f'card, dest|FF,GG,Q: '):
        answer = input(question)
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
        for idxGames,field in enumerate(self.result):
            if field == ' ' or field == None or idxGames > 4:
                pass
            else:
                rp(f'{SQLiteIO.xGamesFields[idxGames]}: {field}',end='    ')#        pass
                if idxGames==4:
                    self.gameid=field
        
        #######################################
        #CREATE TABLE "Game" (       PRIMARY KEY("dbid" AUTOINCREMENT))
        #row0: ' 'idxGames)    row1: ' 'idxGames)    row2: ' 'idxGames)    row3: ' 'idxGames)    row4: ' 'idxGames)    row5: ' 'idxGames)    row6: ' 'idxGames)    row7: ' 'idxGames)    
        #######################################
        return self.gameid
    def readlastrecord(self):
        self.lastdbid=self.cursorSQL3.lastrowid
        '''(4, 2, 3, '6C0000AD00', 'AH3C9S5SQD7HKD2D', '7D9DJS5H9C5C8HAC', '3DTH8SQCAS2S2H9H', 'TS3S3H4S8DKS6STC', 'JD7CJC6HKH5DQHKC', 'QS4D4H2C6D4C08C', 'TD7SJH00000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000')'''
        sqlre=f"SELECT * FROM Game ORDER BY dbid DESC LIMIT 1;"       
        sqlfe=f"SELECT * FROM 'Game' WHERE 'dbid' IN ( SELECT max( 'dbid' ) FROM 'Game' );" 
        sqle=f"SELECT * FROM 'Game' WHERE ROWID = {self.lastdbid};"       
        self.cursorSQL3.execute(sqlre)#, ('john@example.com', 'mypassword'))
        self.mresult=self.cursorSQL3.fetchone()
        print();self.lTblRows=[]
        #self.mresult=list(bsqlt3.readlastrecord())
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

        return self.gameid,self.moveid,self.lTblRows
    def insertTablow(self,tablow,gameid,moveid)  ->  Tableau:
        """ self.fieldNames4games[:10]=['dbid', 'gameid', 'moveid', 
        'row0', 'row1', 'row2', 'row3', 'row4', 'row5', 
        'row6']||||self.row0Index=3"""
        snames=self.fieldNames4games;srowidx=self.row0Index
        self.gameid=gameid   
        self.moveid=moveid
        self.moveid+=1;self.sep=', '# Create a new record
        sqlb=[self.gameid,self.moveid]
        for sqlridx,sqlrow in enumerate(tablow):
            sqlc=''
            """ DONT SKIP THE FIRST ROW IF ITS EMPTY (skip the rest of them)"""
            if sqlridx ==0 or sqlrow != ['0' for _ in range(8)]:
                for sqlcol in sqlrow:
                    sqlcol2=str(sqlcol)
                    if sqlcol2 != '' and sqlcol2 !='0': 
                        sqlc+=sqlcol2
                    else:
                        sqlc+='xx'
                sqlb.append(sqlc)
            else:
                continue
        #
        #self.rowstring= f" VALUES ({self.gameid}, {self.moveid}, "
        #self.valuestr = f"INSERT INTO 'Game' ({snames[1]}, {snames[2]}, "
        self.rowstring= f" VALUES {tuple(sqlb[idxcv] for idxcv in range(len(sqlb)))}; "
        #numbers = [1, 2, 3, 4, 5];    squares = tuple(x**2 for x in numbers)
        #print(squares)  # Output: (1, 4, 9, 16, 25)
        self.valuestr = f"INSERT INTO 'Game' {tuple(snames[idz] for idz in range(1,len(sqlb)+1))} "
        #for idx,rowf in enumerate(sqlb):
        #    if idx == len(sqlb)-1:
        #        self.rowstring += f"'{str(rowf)}');"
        #        self.valuestr  += f"'{snames[idx+srowidx]}')"
        #    else:
        #        self.rowstring += f"'{str(rowf)}', "
        #        self.valuestr  += f"'{snames[idx+srowidx]}', "
        sqld = f"{self.valuestr}{self.rowstring}"
                    
        print(f'{sqlb=}{sqld=}',sep=',') 
        self.cursorSQL3.execute(sqld)#, ('john@example.com', 'mypassword'))
        #INSERT INTO 'game' ('gameid', 'moveid', 'subtitle`, `author`, `promocode`, `emaildate`, `picturename`, `description`, `promoline`, `forwardt`) VALUES
        # Commit changes
        self.conn.commit()

        print("Record inserted successfully")
        return tablow,self.gameid,self.moveid
    

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
        #lennodels=len(self.norowsdeleted)
        rp(f'{self.norowsdeleted[0]} Record(s) deleted successfully:')
        rp(f'{sqlf=}\n{sqlg=}') 
        
    def closeconn(self):
            self.conn.close()
        # connecting to the database
        #connection = sqlite3.connect("gfg.db")
 
# cursorcrsr = self.conn.cursor()
 
# print statement will execute if there
# are no errors    print("Connected to the database")
 
# close the connection  connection.close()    