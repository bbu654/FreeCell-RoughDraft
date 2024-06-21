from turtle import Screen as ScreenA, Turtle as turtleA
screen = ScreenA()
yertle = turtleA()

def k101():
    screen.onscreenclick(clickHandler)

def clickHandler(x,y):
    screen.onscreenclick(None)    #disable event inside event handler
    yertle.setheading(yertle.towards(x,y))
    yertle.goto(x,y)
    screen.onscreenclick(clickHandler)    #reenable event on event handler exit

screen.onkey(k101, " ")    #space turns on mouse drawing
screen.bgcolor("yellow")
screen.title("Hit space key and Draw")
screen.listen()
screen.mainloop()
"""
from turtle import *
shape("circle")
pencolor("red")
width(6)
ondrag(goto)
listen()"""