import turtle
import random

#bas
turtle.setup(600, 600)
turtle.bgcolor("snow")
stift = turtle.Turtle()
stift.hideturtle()
stift.speed(-1)

def zeichne_baum(x, y, scale):

    stift.penup()
    stift.goto(x, y)
    stift.pendown()

    
    base_x = x
    base_y = y

    
    stift.color("green", "green")

    
    stift.penup()
    stift.goto(base_x - 100*scale, base_y)
    stift.pendown()
    stift.begin_fill()
    stift.goto(base_x + 100*scale, base_y)
    stift.goto(base_x, base_y + 100*scale)
    stift.goto(base_x - 100*scale, base_y)
    stift.end_fill()

    
    stift.penup()
    stift.goto(base_x - 80*scale, base_y + 50*scale)
    stift.pendown()
    stift.begin_fill()
    stift.goto(base_x + 80*scale, base_y + 50*scale)
    stift.goto(base_x, base_y + 150*scale)
    stift.goto(base_x - 80*scale, base_y + 50*scale)
    stift.end_fill()

    
    stift.penup()
    stift.goto(base_x - 60*scale, base_y + 100*scale)
    stift.pendown()
    stift.begin_fill()
    stift.goto(base_x + 60*scale, base_y + 100*scale)
    stift.goto(base_x, base_y + 200*scale)
    stift.goto(base_x - 60*scale, base_y + 100*scale)
    stift.end_fill()

    
    stift.color("sienna", "sienna")
    stift.penup()
    stift.goto(base_x - 25*scale, base_y)
    stift.pendown()
    stift.begin_fill()
    stift.goto(base_x + 25*scale, base_y)
    stift.goto(base_x + 25*scale, base_y - 60*scale)
    stift.goto(base_x - 25*scale, base_y - 60*scale)
    stift.goto(base_x - 25*scale, base_y)
    stift.end_fill()

    stift.penup()


def baum_bei_maus():

    
    x = turtle.getcanvas().winfo_pointerx() - turtle.getcanvas().winfo_rootx() - 750
    y = 300 - (turtle.getcanvas().winfo_pointery() - turtle.getcanvas().winfo_rooty())

    
    scale = random.uniform(0.3, 1.5)

    zeichne_baum(x, y, scale)



turtle.listen()
turtle.onkeypress(baum_bei_maus, "b")
#turtle.onkeypress(sman_bei_maus, "s")
#turtle.onkeypress(haus_bei_maus, "h")

turtle.done()
