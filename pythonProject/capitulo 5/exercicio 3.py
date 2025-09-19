def imprimenumero(numero1 , numero2 , numero3):

    if (numero1 > numero2):
        if (numero1 > numero3):
            print ("esse", numero1 , "é o maior")

    if (numero2 > numero1):
        if (numero2 > numero3):
            print("esse", numero2, "é o maior")

    if (numero3 > numero1):
        if (numero3 > numero2):
            print ("esse", numero3 , "é o maior")

numero1 = int(input("digite um numero"))
numero2 = int(input("difite um numero"))
numero3 = int(input("digite um numero"))


imprimenumero(numero1 , numero2 , numero3)