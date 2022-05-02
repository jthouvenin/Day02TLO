def fizzbuzz(n):
    if (n%3 == 0 and n%5 == 0):                         #si le nombre esrt divisible par 3 et par 5
        print("Fizzbuzz")
    else:
        if n%3 == 0:                                    #sinon si le nombre est uniquement divisible par 3
            print("Fizz")
        else:
            if n%5 == 0:                                #sinon si le nombre est uniquement divisible par 5
                print("Buzz")
            else:
                print("Pas de Fizz, pas de Buzz, pas de Fizzbuzz")



nombre = int(input("Quel est votre nombre ? : "))       #On demande à l'utilisateur de choisir un nombre
fizzbuzz(nombre)