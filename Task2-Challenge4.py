'''
Use the turtle graphics library to write program that reproduce the design shown in Figure 
below:
 / \  / \
/   \/   \
\   /\   /
 \ /  \ /
'''

import turtle
turtle.setup(640, 480)
turtle.bgcolor("lightblue")
turtle.hideturtle()
turtle.fillcolor("white")
turtle.pensize(5)
turtle.begin_fill()
turtle.goto(0,0)
turtle.left(45)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

turtle.done()