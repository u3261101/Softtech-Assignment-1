'''
Write a turtle graphics program that draws a city skyline like the one shown in 
Figure 2. The program’s overall task is to draw an outline of some city buildings 
against a night sky. Modularize the program by writing functions that perform the 
following tasks:
 
 Draw the outline of buildings. 
 Draw some windows on the buildings. 
 Use randomly placed dots as the stars (make sure the stars appear on the 
sky, not on the buildings).
'''

import turtle
import random

def main():
	turtle.setup(600, 600)
	turtle.speed(0)
	turtle.ht()
	
	sky()
	building()
	windows()
	
	turtle.done()

def building():
	turtle.fillcolor('gray')
	turtle.pencolor('gray')
	turtle.penup()
	turtle.goto(-300,-300)
	turtle.pendown()
	turtle.begin_fill()
	turtle.left(90)
	turtle.forward(225)
	
	turtle.right(90)
	turtle.forward(75)
	turtle.left(90)
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(75)
	turtle.left(90)
	turtle.forward(225)
	turtle.right(90)
	turtle.forward(135)    
	turtle.right(90)
	turtle.forward(265)    
	turtle.left(90)
	turtle.forward(85)    
	turtle.left(90)
	turtle.forward(125)
	turtle.right(90)
	turtle.forward(85)
	turtle.right(90)
	turtle.forward(85)
	turtle.left(90)
	turtle.forward(55)
	turtle.right(90)
	turtle.forward(85)
	turtle.left(90)
	turtle.forward(85)
	turtle.right(90)
	turtle.forward(220)	    
	turtle.right(90)
	turtle.forward(595)	    
	turtle.right(90)
	turtle.forward(100)	    

	turtle.end_fill()

def windows():
	square(-220,-50)
	square(-140,120)
	square(-140,150)
	square(-60,50)
	square(-60,-150)
	square(80,50)
	
def square(x,y):
	turtle.fillcolor("white")
	turtle.pencolor('white')
	turtle.begin_fill()
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	for i in range(4):
	    turtle.forward(20)
	    turtle.right(90)
	turtle.penup()
	turtle.end_fill()

def sky():
	turtle.bgcolor('black')
	turtle.speed(10)
	for i in range(9):
		star()
    	
def star():
	x = random.randint(-280,280)
	y = random.randint(100,280)
	turtle.fillcolor("white")
	turtle.pencolor('white')
	turtle.begin_fill()
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(2)
	turtle.end_fill()
	turtle.penup()
	
	
main()