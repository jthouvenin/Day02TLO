prix = int(150000000)
b = int(31000000)

nb = 1
e = b

while (b < prix):
    c = e*0.2                               #calcul 20% semaine précedente
    #print(c)
    d = e - c     
    #print(d)                               #calcul benefice semaine en cours
    b = b + d                               #calcul bénéfice total

    e = d                                   #affecttion à une variable des benefices de la semaine en cours

    nb = nb +1                              #incrémentation du nombre de semaine
    #print(b)

print("Nb de semaines : ",nb)