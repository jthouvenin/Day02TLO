import turtle     

from turtle import *
color('black', 'white')             

begin_fill()

turtle.home()                                       
turtle.position()

for i in range(10):
    j = 100-(i*10)
    turtle.circle(j)

end_fill()
done()