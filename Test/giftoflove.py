import random,cardsfrommsucse as cardss
from rich import print as rp
from rich import table as Table
def IoweU():
    cardsy = cardss.Deck()
    cardsy.shuffle()
    sdeck = [qw for qw in range(1,53)]
    print(sdeck)
    random.shuffle(sdeck)
    tdeck = random.shuffle([[ws for ws in range(1,53)]])
    rp(f'{sdeck=},{tdeck=},{cardsy=}')
    ic=-1
    outa=[[0,0,0,0,0,0,0,0]]*23
    for row in range(1,23):
        outo=[]
        for col in range(8):
            ic += 1
            if ic < 52:
                outo.append(sdeck[ic])
            else:
                outo.append(0)
        outa[row] = outo
    colh = list(zip(*outa));id=-1
    Py2Dlist1 = [[0,0,0,0,0,0,0,0]]
    Py2Dlist = [[sdeck[(id:=id+1)] if id < 51 else 0 for j in range(8)] for i in range(1,23) ]
    for row in Py2Dlist:
        Py2Dlist1.append(row)
    
    from rich.table import Table
    from rich.console import Console
    table1 = Table(title="Star Wars Movies")
    
    table1.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table1.add_column("Title", style="magenta")
    table1.add_column("Box Office", justify="right", style="green")
    
    table1.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table1.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table1.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table1.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
    rp(f'{outa=}\n{Py2Dlist1=}\n{colh=}')#rp(table1)
    gameview = Table(title='Freecell')
    for qe in range(8):
        gameview.add_column('0')
    for row1 in outa:
        #str4=zip(row1)
        #str5=str4
        strz='';str1='';str2='';str3='';str4=''
        for idx,col1 in enumerate(row1):
            strx=str(col1)
            if idx == 7:
                str7=f'{col1}'
            elif idx == 6:
                str2+=f'{col1}'
        gameview.add_row(str2,str7)
    consol=Console()    
    consol.print(table1,gameview)
IoweU()