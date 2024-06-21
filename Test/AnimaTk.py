import time
from tkinter import *

gui = Tk()
gui.geometry("800x600")
gui.title("Tkinter Animation")
canvas = Canvas(gui,width=800,height=600,background='white')
canvas.pack()
balll = canvas.create_oval(5,5,60,60, fill='yellow')
#
#a=8
#b=3
#for x in range(0,100):
#    canvas.move(balll,a,b)
#    gui.update()
#    time.sleep(.05)    
xa = 5
yb = 10
while True:
    canvas.move(balll,xa,yb)
    pos = canvas.coords(balll)
    if pos[3] >= 600 or pos[1] <= 0:
        yb = -yb
    if pos[2] >= 800 or pos[0] <= 0:
        xa = -xa
    gui.update()
    time.sleep(.025)
#gui.mainloop()