import turtle     

from turtle import *
color('black', 'white')             

begin_fill()

turtle.home()                                       
turtle.position()

tur = turtle.Turtle()

for j in range(4):
    for i in range(4):
        tur.forward(100)
        tur.left(90)
    tur.left(90)

end_fill()
done()