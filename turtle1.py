import turtle                                       #importation de les fonctionnalités de la tortue


from turtle import *                                #
color('black', 'white')                             #trait en noirn remplissage en blanc

begin_fill()                                        #on commence le dessin

turtle.home()                                       
turtle.position()
turtle.circle(100)                                  #on trace le premier cercle
turtle.circle(-100)                                 #on trace le 2e cercle (opposé au 1er)

turtle.setheading(90)                               #on tourne à 90 la tete de la tortue

turtle.circle(100)                                  #on trace les 2 derniers cercles
turtle.circle(-100)


end_fill()
done()

