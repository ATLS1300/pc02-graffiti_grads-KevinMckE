#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Kevin Ecke
Sep 2, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = turtle.Turtle()

t.up()
t.goto(125,-95)
t.color("red")
t.down()
t.pensize(12)
t.right(15)
t.forward(90)

t.up()
t.goto(270,-138)
t.color("blue")
t.dot(100)
t.color("green")
t.left(145)
t.begin_fill()
t.pensize(4)
t.down()
t.fd(45)
t.right(110)
t.fd(10)
t.right(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.rt(50)
t.fd(20)
t.lt(45)
t.fd(5)
t.rt(90)
t.fd(3)
t.rt(90)
t.fd(3)
t.lt(60)
t.fd(10)
t.lt(110)
t.fd(15)
t.lt(45)
t.fd(15)
t.lt(10)
t.fd(10)
t.rt(30)
t.fd(10)
t.rt(75)
t.fd(15)
t.rt(30)
t.fd(15)
t.lt(45)
t.fd(8)
t.rt(90)
t.fd(10)
t.rt(75)
t.fd(20)
t.rt(45)
t.fd(15)
t.lt(90)
t.fd(20)
t.end_fill()

t.up()
t.goto(-25, 115)
t.color("black")
t.dot(40)
t.pensize(10)
t.rt(90)
t.down()
t.fd(88)
t.goto(-25,115)
t.lt(145)
t.fd(65)

t.up() 
t.goto(37, 50)
t.rt(180)    
t.color("brown")
t.pensize(15)
t.down()
t.fd(80)
t.color("grey")
t.dot(15)
t.lt(90)
t.pensize(1)
t.begin_fill()
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.rt(120)
t.fd(15)
t.rt(15)
t.fd(15)
t.rt(15)
t.fd(15)
t.lt(20)
t.fd(20)
t.lt(20)
t.fd(20)
t.lt(20)
t.fd(20)
t.end_fill()
t.hideturtle()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
