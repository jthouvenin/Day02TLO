import turtle     

from turtle import *
color('black', 'white')             

begin_fill()

turtle.home()                                       
turtle.position()

for i in range(10):
    j = 100-(i*10)
    turtle.circle(j)
    turtle.circle(-j)

turtle.setheading(90)   

for k in range(10):
    l = 100-(k*10)
    turtle.circle(l)
    turtle.circle(-l)



end_fill()
done()