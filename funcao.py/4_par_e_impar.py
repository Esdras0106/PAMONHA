import os
os.system("cls || clear")

def diferenca(numero):
    if numero % 2 == 0:
        print("= PAR =")
    else:
        print("= ÍMPAR =")

print(f"\t= PAR OU ÍMPAR =")
numero = int(input(f"\nDigite um número: "))
diferenca(numero)

