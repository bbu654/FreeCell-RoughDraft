import sys, string
from time import sleep
sa = [sys.argv[0],1]
lsa = len(sa)
q1 = f'Usage: [ python3 ] AlarmClock.py durationInMin'
q2 = f'Example: [ python3 ] AlarmClock.py 10'
q3 = f'Use a value of 0 test immediately.'
q4 = f'Beeps a few times after the duration is over.'
q5 = f'Press Ctrl-C to terminate the alarm clock early'
q6 = f'Invalid numeric value {sa[1]}'
q7 = f'Should be an integer >= 0'
q8 = f'Invalid value for minutes, should be >= 0'
q0 = f'Wake Up'; qA = f'Interrupted by user'
if lsa != 2:
    print(f'{q1}\n{q2}\n{q3}\n{q4}\n{q5}')
    sys.exit(1)
    #sys.exit(1)
#unitWord=''
try:
    mins = int(sa[1])
    if mins == 1:
        unitWord = 'minute'
    else:
        unitWord = 'minutes'
    q9 = f'Sleeping for {str(mins)} {unitWord}'
except ValueError:
    print(f'{q6}\n{q7}')
    sys.e(1)
secs = mins * 60
try:
    if mins > 0:
        print(f'{q9}')
        sleep(secs)
    print(f'{q0}')
    for i in range(5):
        print(),
        sleep(1)
except KeyboardInterrupt:
    print(f'{qA}')
    sys.exit(1)