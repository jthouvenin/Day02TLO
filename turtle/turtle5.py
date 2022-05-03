import turtle     

from turtle import *
color('black', 'white')             

begin_fill()

turtle.home()                                       
turtle.position()

turtle.circle(100)

turtle.left(90)
turtle.forward(100)

for i in range(0,72):
    turtle.forward(100)
    turtle.position()
    turtle.forward(-100)
    turtle.position()
    turtle.left(5)

turtle.setpos(0,150)

for i in range(0,72):
    turtle.left(-135)
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)

end_fill()
done()