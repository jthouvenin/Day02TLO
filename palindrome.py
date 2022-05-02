def palindrome(str):
    if str == str[::-1]:
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")

pal = str(input("Entrez vote mot ou phrase : "))
palindrome(pal)