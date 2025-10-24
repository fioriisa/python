#Elaborar um programa que imprima todos os números inteiros ÍMPARES entre 1 e 30, utilizando o FOR.
def main():
    for i in range (0, 30):
        if i % 2 == 0:
            continue
        print(i)

tecla = input("aperte a tecla enter")


if __name__ == "__main__":
    main()