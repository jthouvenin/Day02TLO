import turtle     

from turtle import *
color('black', 'white')             

#begin_fill()

turtle.home()                                       
turtle.position()

for i in range(0,72):
    turtle.forward(100)
    turtle.forward(-100)
    turtle.left(5)

for i in range(0,18):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(-100)
    turtle.left(5)

#end_fill()

done()