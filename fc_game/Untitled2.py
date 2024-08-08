from typing import Any, Generic, List, Optional, TextIO, TypeVar, Union, overload

#from random import choice
#from re import T
from rich import prompt
from rich import print as rp
errmsg = '!'
#POIU= List('0',1,"2",3.0)
def getAnswer(question = f'{errmsg: ^40}card, dest|FF,GG,Q: ',schoics=False,sdefauls=False,choicest=[],defaultt=''):
    #choicet=False;       fefault=False    
    answer = prompt.Prompt.ask(question,choices=choicest,default=defaultt,show_choices=schoics,show_default=sdefauls)
    return answer

if __name__ == '__main__':
    question = f'{'tough' : >10}' 
    rp(getAnswer())
    choicet=True;       fefault=True
    rp(getAnswer(f'{question} lots',choicet,fefault))
    choicet=False;       fefault=True
    rp(getAnswer(f'{question} lots',choicet,fefault))
    choicet=True;       fefault=False
    rp(getAnswer(f'{question} lots',choicet,fefault))
