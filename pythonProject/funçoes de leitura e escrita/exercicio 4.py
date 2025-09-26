def verificaidade21(idade1, idade2, idade3, idade4, idade5):
    ContaIdade = 0

    if (idade1 == 21):
        ContaIdade += 1
    if (idade2 == 21):
        ContaIdade += 1
    if (idade3 == 21):
        ContaIdade += 1
    if (idade4 == 21):
        ContaIdade += 1
    if (idade5 == 21):
        ContaIdade += 1

def main():
    idade1 = int(input("digite a idade"))
    idade2 = int(input("digite a idade"))
    idade3 = int(input("digite a idade"))
    idade4 = int(input("digite a idade"))
    idade5 = int(input("digite a idade"))

    verificaidade21 (idade1,idade2, idade3, idade4, idade5)

if __name__ == "__main__":
    main()

