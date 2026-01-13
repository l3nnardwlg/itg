import turtle
from turtle import *
turt = turtle.Turtle()
turt.shape(“blank”)
wn = turtle.Screen()
wn.screensize(400,400)
wn.title(“Drawing Adventure”)
while True:
   figure_list = [“circle”, “square” ,”rectangular”, “triangle”, “star” ]
   input= turtle.textinput(“Type a Figure: “,”What do you want to draw?: “)
   if input in figure_list:
      if input == figure_list[0]:
         color = turtle.textinput(“Color”, “Type a color:”)
         x_axis = float(turtle.textinput(“Location”, “x = ?”))
         y_axis = float(turtle.textinput(“Location”, “y = ?”))
         size_of_figure = int(turtle.textinput(“Size”, “Define the size”))
         turt.penup() #turt was our turtle’s name
         turt.goto(x_axis,y_axis) #specific location we asked for
         turt.pendown()
         turt.color(color) #specific color we asked for
         turt.begin_fill()
         turt.circle(size_of_figure) #specific size we asked for
         turt.end_fill
      if input== figure_list[1] and figure_list[2]:
         color = turtle.textinput(“Define the color”, “Type a color”)
         x_axis = float(turtle.textinput(“x location”, “x = ?”))
         y_axis = float(turtle.textinput(“y location”, “y = ?”))
         size_short= int(turtle.textinput(“size”, “short edge”))
         size_long= int(turtle.textinput(“size”, “long edge”))
         turt.penup()
         turt.goto(x_axis,y_axis)
         turt.pendown()
         turt.color(color)
         turt.begin_fill()
         for _ in range(2):
            turt.forward(size_short)
            turt.left(90)
            turt.forward(size_long)
            turt.left(90)
         turt.end_fill()
      if input == figure_list[3]:
         color = turtle.textinput(“Define the color”, “Type a color”)
         x_axis = float(turtle.textinput(“x location”, “x = ?”))
         y_axis = float(turtle.textinput(“y location”, “y = ?”))
         size_of_tri = int(turtle.textinput(“size”,”lenght of edges”))
         turt.penup()
         turt.goto(x_axis,y_axis)
         turt.pendown()
         turt.color(color)
         turt.begin_fill()
         for _ in range(3):
            turt.forward(size_of_tri)
            turt.left(120)
         turt.end_fill()
      if input == figure_list[4]:
         color = turtle.textinput(“Define the color”, “Type a color”)
         x_axis = float(turtle.textinput(“x location”, “x = ?”))
         y_axis = float(turtle.textinput(“y location”, “y = ?”))
         size_of_star = int(turtle.textinput(“size”,”lenght of edges”))
         turt.penup()
         turt.goto(x_axis,y_axis)
         turt.pendown()
         turt.color(color)
         turt.begin_fill()
         for _ in range(5):
            turt.forward(size_of_star)
            turt.right(144)
         turt.end_fill()
      wn.exitonclick()
      break