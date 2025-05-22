import os
os.system("cls || clear")


def valores():
    print(f"\t:)")
for i in range (1,3):
    valores()
    primeiro_valor = float(input(f"\nDigite o 1º valor: "))
    segundo_valor = float(input(f"\nDigite o 2º valor: "))
    break

def subtrair (valor1, valor2):
    return valor1 - valor2

def somar(valor1, valor2):
    return valor1 + valor2

def produtos(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    return valor1 / valor2


valores()
subtracao = subtrair(primeiro_valor, segundo_valor)
soma = somar(primeiro_valor, segundo_valor)
produto = produtos(primeiro_valor, segundo_valor)
media = divisao(primeiro_valor, segundo_valor)

print(f"Primeiro Número: {primeiro_valor}")
print(f"Segundo Número: {segundo_valor}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Produto: {produto}")
print(f"Média: {media: .2f}")


