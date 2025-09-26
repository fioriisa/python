def maiorNumero (numero1, numero2, numero3):
    if (numero1 > numero2):
        if (numero1 > numero3):
            print(f"o primeiro numero é o maior numero")

    if (numero2 > numero1):
        if (numero2 > numero3):
            print(f"o segundo numero é o maior numero")

    if (numero3 > numero1):
        if (numero3 > numero2):
            print(f"o terceiro numero é o maior numero")

numero1 = int(input("digite um numero"))
numero2 = int(input("difite um numero"))
numero3 = int(input("digite um numero"))

maiorNumero (numero1, numero2, numero3)

#da para usar o F aqui tbm , print(f"o numero {numero1} é o maior numero.")
