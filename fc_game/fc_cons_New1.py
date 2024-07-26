from fc_card_New import Card

BLANKCARD='__'
EMPTYROW=[BLANKCARD for zce in range(8)]

SYMBOL={'C':'♣','D':'♦','H':'♥','S':'♠'}
COLORS={'C':'[blue]','D':'[bright_magenta]','H':'[red]','S':'[dark_green]'}

suitlit = [f'[white]{BLANKCARD}[/]']
for bt in SYMBOL:
    for bu in Card.rank_list[1:]:
        suitlit.append(f'{COLORS[bt]}{bu}{SYMBOL[bt]}[/]')    

output={}#nextCards not any more
for j in range(3,13+1):
    for k in range(2):
        output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
        output[j+(13*(k+2))] = [j-1, j+12]
j=0
k=0
# List to map int rank to printable character (index 0 used for no rank)
rank_list = ['x','A','2','3','4','5','6','7','8','9','T','J','Q','K']

# List to map int suit to printable character (index 0 used for no suit)
# 1 is clubs, 2 is diamonds, 3 is hearts, and 4 is spades
#suit_list = ['x','\u2663','\u2666','\u2665','\u2660']
suit_list = ['x','C','D','H','S']
SUIT_LIST = {'x': 'x', 'C': '\u2663', 'D': '\u2666', 'H': '\u2665', 'S': '\u2660'}
validsuit={'C':['D','H'],'S':['D','H'],
           'H':['C','S'],'D':['C','S']}
validrank=['A','2','3','4','5','6','7',
           '8','9','T','J','Q','K']
vsuita=['C','D','H','S']

nextCard = {}
for vsuit in validsuit:
    for idx, vrank in enumerate(validrank[2:]):
        nextCard[vrank+vsuit]=[validrank[idx+1]+validsuit[vsuit][0],validrank[idx+1]+validsuit[vsuit][1]]

validcard=[]
for s in vsuita:
    for r in validrank:
        validcard.append(f'{r}{s}')

ACES_TWOS = ('AC','2C','AS','2S','AH','2H','AD','2D')
ACESTWOS  = [vrank+vsuit for vsuit in vsuita for vrank in validrank[:2]]
#posdic={k:[-1,-1] for k in validcard}    



