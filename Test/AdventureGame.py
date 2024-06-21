from time import sleep
ah = f'>>>>>>>>>>>>>Awesome Adventure<<<<<<<<<<<<<'   #      1234567890123
a2 = f'\n\n'; name = "Brice"
ab = f'\nA long time ago, a warrior strode forth from the frozen north.'
print(f'{a2}{ah}{a2}');sleep(3)
print(f'{ab}\n Does this warrior have a name? {name}');sleep(1)
print(f'{name}, the barbarian, sword in hand and looking for adventure!');sleep(1)
print(f'However, evil is lurking nearby....');sleep(1)
print(f'A pair of bulbous eyes regards the hero...');sleep(1)
print(f'Will {name} prevail, and win great fortune...');sleep(1)
print(f'Or die by the hands of great evil...?{a2}');sleep(2)
print(f'Only time will tell...\n...\n...\n...\n...\n...{a2}{a2}{a2}');sleep(10)
print('''       You find yourself at a small inn. There is 
      little gold in your purse but your sword is sharp,
      and you are ready for adventure.
      With you are three other customers.
      A ragged looking man, and a pair of dangerous
      looking guards.''')

def start():
    print(f'\n{"-" *10}\nDo you approach the...\n\n1. Ragged looking man\n2. Dangerous looking guards')
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        ragged()
    elif cmd == '2':
        guards()

def ragged():
    print("\n" *10)
    print('''You walk up to the ragged looking man and
    greet him.
        He smiles a toothless grin and, with a strange
        accent, says
        "Buy me a cup of wine, and I will tell you of
        great treasure...''')
    sleep(2)

def guards():
    print("\n" *10)
    print('''You walk up to the dangerous looking guards
    and greet them.
        The guards look up from their drinks and
        snarl at you.
        "What do you want barbarian?" One guard reaches
        for the hilt of his sword...''')
    sleep(2)

def getcmd(cmdlist):
    cmd = input(name+'>')
    if cmd in cmdlist:
        return cmd
    elif cmd == 'help':
        print('\nEnter your choices as detailed in the game.')
        print('or enter "quit" to leave the game')
        return getcmd(cmdlist)
    elif cmd == 'quit':
        print(f'\n{'-' *10}');sleep(1)
        print(f'Sadly you return to your homeland without fame or fortune...{sleep(5)}')
        exit()

if __name__ == '__main__':
    start()


